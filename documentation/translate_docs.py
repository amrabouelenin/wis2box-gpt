import os
import openai
import markdown
import time

# Set your OpenAI API key
openai.api_key = ""

# Function to translate text using OpenAI
def translate_text(text, target_language):
    prompt = f"Translate the following Markdown content into {target_language}:\n\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "You are a Markdown-aware translator."},
                  {"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response['choices'][0]['message']['content']

# Function to process and translate Markdown files
def process_markdown_files(input_folder, output_folder, languages):
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path}")
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                for lang in languages:
                    translated_text = translate_text(content, lang)

                    # Save translated file in a corresponding language folder
                    lang_path = 'ru' if lang == 'Russian' else 'es'
                    relative_path = os.path.relpath(root, input_folder)
                    print(f"relative path: {relative_path}")
                    # remove en/ from relative path
                    relative_path = relative_path[3:]
                    target_dir = os.path.join(output_folder, lang_path, relative_path)
                    os.makedirs(target_dir, exist_ok=True)

                    target_file_path = os.path.join(target_dir, file)
                    print(f"target file path: {target_file_path}")
                    with open(target_file_path, "w", encoding="utf-8") as f:
                        f.write(translated_text)

                    print(f"Translated {file} to {lang}")

                time.sleep(1)  # Avoid rate limits

# Set paths
input_folder = "docs"  # Change this to your Markdown folder
output_folder = "docs"
languages = ["Spanish", "Russian"]

# Run translation
process_markdown_files(input_folder, output_folder, languages)
