from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

def TransLate(text: str, scr: str, dest: str) -> str:

    try:
        translated_text = GoogleTranslator(source=scr, target=dest).translate(text)
        return translated_text
    except Exception as e:
        return f"Помилка при перекладі: {e}"


# Для стабільності результатів детектування мови
DetectorFactory.seed = 0


def LangDetect(text: str, set: str = "all") -> str:
    try:
        detected_lang = detect(text)
        # Пакет langdetect не повертає коефіцієнт довіри, тому значення буде фіксованим
        confidence = 1.0

        if set == "lang":
            return detected_lang
        elif set == "confidence":
            return str(confidence)
        elif set == "all":
            return f"Мова: {detected_lang}, Коефіцієнт довіри: {confidence}"
        else:
            return "Невірне значення параметра 'set'. Використовуйте 'lang', 'confidence' або 'all'."
    except LangDetectException as e:
        return f"Помилка при визначенні мови: {e}"


def LanguageList(out: str = "screen", text: str = None) -> str:

    try:
        languages = GoogleTranslator.get_supported_languages(as_dict=True)
        table_data = []

        for idx, (lang_name, lang_code) in enumerate(languages.items(), start=1):
            if text:
                translated = GoogleTranslator(source='auto', target=lang_code).translate(text)
                table_data.append((idx, lang_name.capitalize(), lang_code, translated))
            else:
                table_data.append((idx, lang_name.capitalize(), lang_code))

        # Форматування таблиці
        header = ["N", "Language", "ISO-639 code"]
        if text:
            header.append("Text")

        table = [header]
        for row in table_data:
            table.append([str(item) for item in row])

        # Форматування виводу
        col_widths = [max(len(str(item)) for item in col) for col in zip(*table)]
        table_str = "\n".join(
            " ".join(f"{item.ljust(width)}" for item, width in zip(row, col_widths))
            for row in table
        )
        table_str = f"{'-' * sum(col_widths)}\n{table_str}\n{'-' * sum(col_widths)}"

        if out == "screen":
            print(table_str)
        elif out == "file":
            with open("language_list.txt", "w", encoding="utf-8") as file:
                file.write(table_str)
        else:
            return "Невірне значення параметра 'out'. Використовуйте 'screen' або 'file'."

        return "Ok"
    except Exception as e:
        return f"Помилка при виконанні операції: {e}"


def CodeLang(lang: str) -> str:
    try:
        # Створюємо екземпляр GoogleTranslator
        translator = GoogleTranslator()

        # Отримуємо словник мов та їх кодів
        languages = translator.get_supported_languages(as_dict=True)

        # Приводимо введену мову до нижнього регістру, щоб уникнути помилок у регістрі
        lang_lower = lang.lower()

        # Пошук коду мови
        if lang_lower in languages:
            return languages[lang_lower]
        else:
            return f"Мова '{lang}' не знайдена. Перевірте правильність введення."
    except Exception as e:
        return f"Помилка при пошуку коду мови: {e}"


def LanguageList(out: str = "screen", text: str = None) -> str:

    try:
        # Отримуємо список мов та їх кодів
        languages = GoogleTranslator().get_supported_languages(as_dict=True)
        table_data = []

        # Створюємо заголовки для таблиці
        header = ["N", "Language", "ISO-639 code"]
        if text:
            header.append("Text")

        table_data.append(header)

        # Формуємо дані таблиці
        for idx, (lang_code, lang_name) in enumerate(languages.items(), start=1):
            row = [str(idx), lang_name.capitalize(), lang_code]
            if text:
                translated_text = GoogleTranslator(source="auto", target=lang_code).translate(text)
                row.append(translated_text)
            table_data.append(row)

        # Форматування таблиці
        col_widths = [max(len(str(item)) for item in col) for col in zip(*table_data)]
        table_str = "\n".join(
            " ".join(f"{item.ljust(width)}" for item, width in zip(row, col_widths))
            for row in table_data
        )

        # Виведення на екран або в файл
        if out == "screen":
            print(table_str)
        elif out == "file":
            with open("language_list.txt", "w", encoding="utf-8") as file:
                file.write(table_str)
        else:
            return "Невірне значення параметра 'out'. Використовуйте 'screen' або 'file'."

        return "Ok"
    except Exception as e:
        return f"Помилка при виконанні операції: {e}"