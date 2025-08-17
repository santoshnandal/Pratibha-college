import requests

def translate_text(from_lang: str, to_lang: str, text: str) -> str:
    # API documentation https://mymemory.translated.net/doc/spec.php
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"{from_lang}|{to_lang}"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Translation failed: {response.text}")

    data = response.json()
    return data["responseData"]["translatedText"]

#  Example usage
if __name__ == "__main__":
    print("🌐 Language Translator using MyMemory API")
    print("Supported codes: en, hi, es, fr, de, zh, ar, ru, ja, ta")

    from_lang = input("From language code: ").strip()
    to_lang = input("To language code: ").strip()
    text = input("Text to translate: ").strip()

    try:
        translated = translate_text(from_lang, to_lang, text)
        print(f"\n📝 Translated Text ({from_lang} → {to_lang}):\n{translated}")
    except Exception as e:
        print("❌ Error:", e)
