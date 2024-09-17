# Імпорт функцій з другого модуля
from pack.file2 import TransLate, LangDetect, LanguageList, CodeLang


def main():
    print("=== Демонстрація функцій з deep_translator та langdetect ===\n")

    # 1. Переклад тексту
    text = "Hello, how are you?"
    src_lang = "en"
    dest_lang = "uk"
    print(f"Переклад тексту '{text}' з {src_lang} на {dest_lang}:")
    translation = TransLate(text, src_lang, dest_lang)
    print(f"Переклад: {translation}\n")

    # 2. Визначення мови
    text_to_detect = "Bonjour tout le monde"
    print(f"Визначення мови тексту: '{text_to_detect}'")
    detected_lang = LangDetect(text_to_detect, "all")
    print(f"Результат: {detected_lang}\n")

    # 3. Виведення списку мов
    lang_name = "arabic"
    print(f"Пошук коду для мови '{lang_name}':")
    lang_code = CodeLang(lang_name)
    print(f"Код мови: {lang_code}")

    # 4. Пошук коду мови
    print("Виведення списку мов на екран:")
    LanguageList("screen", "Hello!")

if __name__ == "__main__":
    main()
