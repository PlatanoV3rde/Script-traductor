#!/usr/bin/env python3
import os
import re
import time
import requests
import argparse
import sys

# ——————————————————————————————
# Configuración de la API de DeepL (FREE)
# ——————————————————————————————
DEEPL_AUTH_KEY = os.getenv("DEEPL_AUTH_KEY")
if not DEEPL_AUTH_KEY:
    print("❌ Error: define la variable de entorno DEEPL_AUTH_KEY con tu API key free de DeepL", file=sys.stderr)
    sys.exit(1)

DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"

# ——————————————————————————————
# Expresiones regulares
# ——————————————————————————————
LINE_PATTERN = re.compile(r"^([^=]+)=(.*)$")
TAG_SPLIT    = re.compile(r"(<[^>]+>)")

# ——————————————————————————————
# Funciones auxiliares
# ——————————————————————————————
def extract_plain_text(msg: str) -> str:
    return re.sub(r"<[^>]+>", "", msg).strip()

def replace_with_translation(original: str, translated: str) -> str:
    parts  = TAG_SPLIT.split(original)
    result = []
    for part in parts:
        if TAG_SPLIT.fullmatch(part):
            result.append(part)
        else:
            result.append(translated if part.strip() else part)
    return "".join(result)

def translate_deepl(text: str, target_lang="ES", max_retries=5) -> str:
    for attempt in range(max_retries):
        resp = requests.post(
            DEEPL_API_URL,
            data={
                "auth_key": DEEPL_AUTH_KEY,
                "text":      text,
                "target_lang": target_lang
            }
        )
        if resp.status_code == 429:
            wait = 2 ** attempt
            print(f"[DeepL 429] reintentando en {wait}s… ({attempt+1}/{max_retries})", file=sys.stderr)
            time.sleep(wait)
            continue
        resp.raise_for_status()
        return resp.json()["translations"][0]["text"]
    raise RuntimeError("Demasiados 429 consecutivos; abortando traducción.")

# ——————————————————————————————
# Lógica principal
# ——————————————————————————————
def main():
    p = argparse.ArgumentParser(
        description="Traduce un .properties (messages_en.properties) a español manteniendo tipografía y etiquetas"
    )
    p.add_argument("-i", "--input",  required=True, help="Ruta al archivo .properties original")
    p.add_argument("-o", "--output", required=True, help="Ruta al archivo .properties traducido")
    args = p.parse_args()

    with open(args.input, "r", encoding="utf-8") as infile, \
         open(args.output, "w", encoding="utf-8") as outfile:

        for line in infile:
            m = LINE_PATTERN.match(line)
            if m:
                key, value = m.groups()
                plain = extract_plain_text(value)
                if plain:
                    try:
                        trans = translate_deepl(plain)
                        new_val = replace_with_translation(value, trans)
                        outfile.write(f"{key}={new_val}\n")
                    except Exception as e:
                        print(f"[ERROR] {key}: {e}", file=sys.stderr)
                        outfile.write(line)
                else:
                    outfile.write(line)
            else:
                outfile.write(line)

    print(f"✔ Traducción completada: {args.output}")

if __name__ == "__main__":
    main()
