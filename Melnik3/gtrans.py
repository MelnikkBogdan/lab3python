from pack.file1 import TransLate, CodeLang, LangDetect, LanguageList  # Імпортуємо функції з першого модуля


def main():
    print("=== Демонстрація функцій перекладу та визначення мови ===\n")

    # Демонстрація перекладу
    text = "Hello, how are you?"
    scr = "en"  # Початкова мова: англійська
    dest = "uk"  # Цільова мова: українська
    print(f"Переклад тексту '{text}' з {scr} на {dest}:")
    translation = TransLate(text, scr, dest)
    print(f"Переклад: {translation}\n")

    # Демонстрація визначення мови
    text_to_detect = "Bonjour tout le monde"
    print(f"Визначення мови тексту: '{text_to_detect}'")
    detected_lang = LangDetect(text_to_detect, "all")
    print(f"Результат: {detected_lang}\n")

    # Демонстрація отримання коду мови
    lang_name = "french"
    print(f"Отримання коду для мови '{lang_name}':")
    lang_code = CodeLang(lang_name)
    print(f"Код мови: {lang_code}\n")

    # Демонстрація виведення списку мов
    print("Виведення списку мов на екран:")
    LanguageList("screen", "Hello!")  # Текст для перекладу всім мовам


if __name__ == "__main__":
    main()
