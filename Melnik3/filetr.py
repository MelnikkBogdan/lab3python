import os
from deep_translator import GoogleTranslator
import re
import sys


def read_config(config_file):
    """Читає конфігураційний файл та повертає параметри."""
    try:
        with open(config_file, 'r') as file:
            lines = file.readlines()
            text_file = lines[0].strip()
            target_lang = lines[1].strip()
            output_mode = lines[2].strip().lower()
            char_limit = int(lines[3].strip())
            word_limit = int(lines[4].strip())
            sentence_limit = int(lines[5].strip())
            return text_file, target_lang, output_mode, char_limit, word_limit, sentence_limit
    except Exception as e:
        print(f"Помилка при читанні конфігураційного файлу: {e}")
        sys.exit(1)


def file_statistics(text):
    """Обчислює статистику тексту."""
    num_chars = len(text)
    num_words = len(re.findall(r'\w+', text))
    num_sentences = len(re.split(r'[.!?]', text)) - 1
    return num_chars, num_words, num_sentences


def read_text_file(file_name, char_limit, word_limit, sentence_limit):
    """Зчитує текстовий файл до виконання однієї з умов."""
    try:
        text = ""
        with open(file_name, 'r',encoding='utf-8') as file:
            for line in file:
                if (len(text) + len(line) > char_limit) or (file_statistics(text)[1] > word_limit) or (
                        file_statistics(text)[2] > sentence_limit):
                    break
                text += line
        num_chars, num_words, num_sentences = file_statistics(text)
        return text, num_chars, num_words, num_sentences
    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні текстового файлу: {e}")
        sys.exit(1)


def translate_text(text, target_lang):
    """Перекладає текст на вказану мову."""
    try:
        translator = GoogleTranslator(target=target_lang)
        translated_text = translator.translate(text)
        return translated_text
    except Exception as e:
        return f"Помилка при перекладі: {e}"


def write_output(file_name, output_mode, target_lang, translated_text):
    """Записує перекладений текст на екран або в файл."""
    try:
        if output_mode == 'screen':
            print(f"Мова перекладу: {target_lang}")
            print(f"Перекладений текст:\n{translated_text}")
        elif output_mode == 'file':
            output_file = f"{os.path.splitext(file_name)[0]}_{target_lang}.txt"
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(translated_text)
            print("Ok")
        else:
            print("Невірний параметр 'output_mode'. Використовуйте 'screen' або 'file'.")
    except Exception as e:
        print(f"Помилка при запису результату: {e}")


def main():
    config_file = 'C:/Users/Lenovo/PycharmProjects/Melnik3/config.txt'
    text_file, target_lang, output_mode, char_limit, word_limit, sentence_limit = read_config(config_file)

    print(f"Назва файлу: {text_file}")

    text, num_chars, num_words, num_sentences = read_text_file(text_file, char_limit, word_limit, sentence_limit)

    print(f"Розмір файлу: {num_chars} символів")
    print(f"Кількість символів: {num_chars}")
    print(f"Кількість слів: {num_words}")
    print(f"Кількість речень: {num_sentences}")

    translated_text = translate_text(text, target_lang)
    if "Помилка" in translated_text:
        print(translated_text)
    else:
        write_output(text_file, output_mode, target_lang, translated_text)


if __name__ == "__main__":
    main()
