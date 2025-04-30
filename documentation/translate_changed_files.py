import subprocess
import os
import sys
from pathlib import Path
import openai
lang_dict = {
    "Arabic": "ar",
    "Chinese": "zh",
    "French": "fr",
    "Russian": "ru",
    "Spanish": "es",
    "Portuguese": "pt",
    "Italian": "it",
    "German": "de",
}

OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY
TARGET_LANGS = ['ru']  # Update as needed
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
    prompt = f"""
    You are an expert Markdown-aware translator with deep knowledge of technical, legal, and business terminology. 
    Translate the following Markdown document into {target_language}, ensuring that:
    
    - The translation accurately conveys the meaning of technical terms rather than translating them literally.
    - The document retains its original structure, including headings, bullet points, and code blocks.
    - The tone and style remain appropriate for the intended audience.
    - Common industry-specific terminology is translated correctly based on its meaning in the given context.

    Here is the Markdown content to translate:
    
    {text}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are an expert Markdown translator with domain-specific knowledge."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    return response['choices'][0]['message']['content']


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
