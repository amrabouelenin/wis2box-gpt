import subprocess
import os
import sys
from pathlib import Path
import openai
import anthropic

lang_dict = {
    "ar": "Arabic",
    "zh": "Chinese",
    "fr": "French",
    "ru": "Russian",
    "es": "Spanish",
    "pt": "Portuguese",
    "it": "Italian",
    "de": "German",
}

OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

openai.api_key = OPENAI_API_KEY
TARGET_LANGS = ['it']  # Update as needed
# TARGET_LANGS = ['ru', 'es', 'it', 'fr', 'ar', 'zh', 'pt', 'de']  # Update as needed

EN_DIR = Path('documentation/docs/en')
BASE_DIR = Path('documentation/docs')


def get_changed_files():
    result = subprocess.run(
        ['git', 'diff', '--name-only', 'HEAD~1'],
        stdout=subprocess.PIPE,
        text=True,
        check=True
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip().endswith('.md')]

def translate_text(text, target_language):

    # Use OpenAI API for translation
    translated_text = translate_text_gpt(text, target_language)

    # Uncomment the following line to use Anthropic API instead - for now it requires a paid plan
    # translated_text = translate_text_claude(text, target_language)

    return translated_text

def translate_text_gpt(text, target_language):
    prompt = f"""
        You are a professional translator specializing in technical Markdown documentation.

        Translate the following content **into {lang_dict[target_language]} only**. Do not use or mix in other languages.

        Ensure that:
        - All headings, code blocks, links, and formatting are preserved exactly.
        - Technical and domain-specific terms are translated with care, not literally.
        - Sentences and paragraphs remain semantically equivalent to the original English.

        Here is the Markdown content to translate:

        {text}
    """

    print(f"Translating to {lang_dict[target_language]} using OpenAI API")
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are an expert Markdown translator with domain-specific knowledge."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    return response['choices'][0]['message']['content']


client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def translate_text_claude(text, target_language):
    prompt = f"""
        You are a professional translator specializing in technical Markdown documentation.

        Translate the following content **into {lang_dict[target_language]} only**. Do not use or mix in other languages.

        Ensure that:
        - All headings, code blocks, links, and formatting are preserved exactly.
        - Technical and domain-specific terms are translated with care, not literally.
        - Sentences and paragraphs remain semantically equivalent to the original English.

        Here is the Markdown content to translate:

        {text}
    """
    print(f"Translating to {target_language} using Anthropic API")
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=4000,
        system="You are an expert Markdown translator with domain-specific knowledge.",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    # Extract the translated text from the response
    translated_text = response.content[0].text
    return translated_text



def translate_file(source_path: Path, lang: str):
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"Translating {source_path} to {lang}")
    translated = translate_text(content, lang)
    dest_path = BASE_DIR / lang / source_path.relative_to(EN_DIR)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(translated)
    print(f"Translated {source_path} → {dest_path}")


def main():
    if '--changed-only' in sys.argv:
        changed = get_changed_files()
        md_files = [Path(f) for f in changed if f.startswith(str(EN_DIR))]

    print(f"Found {len(md_files)} Markdown files to translate.")
    # print filse names/paths
    for md_file in md_files:
        print(md_file)
    if not md_files:
        print("No Markdown files found.")
        return

    for md_file in md_files:
        for lang in TARGET_LANGS:
            translate_file(md_file, lang)


if __name__ == '__main__':
    main()
