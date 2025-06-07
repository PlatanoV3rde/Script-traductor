#!/usr/bin/env python3
import os
import re
import time
import argparse
import sys
from googletrans import Translator
from googletrans.exceptions import JSONDecodeError, TranslateError

# ——————————————————————————————
# Configuración del traductor de Google (librería googletrans)
# ——————————————————————————————
translator = Translator()

# ——————————————————————————————
# Expresiones regulares
# ——————————————————————————————
LINE_PATTERN = re.compile(r"^([^=]+)=(.*)$")
TAG_SPLIT    = re.compile(r"(<[^>]+>)")

# ——————————————————————————————
# Funciones auxiliares
# ——————————————————————————————
def extract_plain_text(msg: str) -> str:
    """Quita etiquetas MiniMessage para enviar solo texto plano a Google."""
    return re.sub(r"<[^>]+>", "", msg).strip()

def replace_with_translation(original: str, translated: str) -> str:
    """
    Reconstruye el valor original, sustituyendo solo el texto plano
    por su traducción, y dejando intactas todas las etiquetas.
    """
    parts  = TAG_SPLIT.split(original)
    result = []
    for part in parts:
        if TAG_SPLIT.fullmatch(part):
            result.append(part)
        else:
            # Si hay texto (no solo espacios), usa la traducción
            result.append(translated if part.strip() else part)
    return "".join(result)

def translate_google(text: str, target_lang="es", max_retries=3) -> str:
    """
    Traduce 'text' usando googletrans con reintentos ante errores.
    """
    for attempt in range(1, max_retries+1):
        try:
            res = translator.translate(text, dest=target_lang)
            return res.text
        except (JSONDecodeError, TranslateError) as e:
            wait = attempt * 1.5
            print(f"[Googletrans error] intento {attempt}/{max_retries}, esperando {wait}s…", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError("No se pudo traducir tras varios intentos.")

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

    try:
        with open(args.input, "r", encoding="utf-8") as infile, \
             open(args.output, "w", encoding="utf-8") as outfile:

            for line in infile:
                m = LINE_PATTERN.match(line)
                if m:
                    key, value = m.groups()
                    plain = extract_plain_text(value)
                    if plain:
                        try:
                            trans = translate_google(plain)
                            new_val = replace_with_translation(value, trans)
                            outfile.write(f"{key}={new_val}\n")
                        except Exception as e:
                            print(f"[ERROR] {key}: {e}", file=sys.stderr)
                            outfile.write(line)
                    else:
                        outfile.write(line)
                else:
                    # Comentarios, líneas vacías, etc.
                    outfile.write(line)

        print(f"✔ Traducción completada: {args.output}")
    except FileNotFoundError as e:
        print(f"❌ Archivo no encontrado: {e.filename}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
