from googletrans import Translator, LANGUAGES

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translator = Translator()
        translation = translator.translate(text, src=scr, dest=dest)
        return translation.text
    except Exception as e:
        return f"Помилка при перекладі: {e}"

def CodeLang(lang : str) -> str:
    lang = lang.lower()

    if lang in LANGUAGES.keys():
        # Якщо введено код мови, повернути назву
        return LANGUAGES[lang]
    elif lang in LANGUAGES.values():
        # Якщо введено назву мови, повернути код
        for code, name in LANGUAGES.items():
            if name == lang:
                return code
    else:
        return None  # Якщо мова не знайдена

def LangDetect(text : str, set : str) -> str:
    try:
        translator = Translator()
        detection = translator.detect(text)

        if detection.confidence is None:
            confidence = 0.0
        else:
            confidence = detection.confidence

        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return str(confidence)
        elif set == "all":
            return f"Мова: {detection.lang}, Коефіцієнт довіри: {confidence}"
        else:
            return "Невірне значення параметра 'set'. Використовуйте 'lang', 'confidence' або 'all'."
    except Exception as e:
        return f"Помилка при визначенні мови: {e}"

def LanguageList(out : str, text : str) -> str:
    try:
        translator = Translator()
        languages = LANGUAGES
        table_data = []

        for idx, (lang_code, lang_name) in enumerate(languages.items(), start=1):
            if text:
                translated = translator.translate(text, dest=lang_code).text
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
        table_str = "\n".join(" ".join(f"{item.ljust(width)}" for item, width in zip(row, col_widths)) for row in table)
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

