import re
import requests

# Tu clave de API de DeepL
DEEPL_API_KEY = 'tu_clave_api_deepl_aqui'  # ← Reemplázala

# Archivos
input_file = "messages_en.properties"
output_file = "messages_es.properties"

# URL de la API
DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"

# Regex para separar claves y valores
line_pattern = re.compile(r"^([^=]+)=(.*)$")

# Elimina etiquetas MiniMessage para traducir solo el texto plano
def extract_plain_text(message):
    return re.sub(r"<[^>]+>", "", message).strip()

# Sustituye los textos traducidos respetando el formato original
def replace_with_translation(original, translated):
    parts = re.split(r"(<[^>]+>)", original)
    result = ""
    trans_index = 0
    for part in parts:
        if part.startswith("<") and part.endswith(">"):
            result += part
        else:
            if part.strip():
                result += translated[trans_index]
                trans_index += 1
            else:
                result += part
    return result

# Traduce con DeepL
def translate_deepl(text, target_lang="ES"):
    response = requests.post(
        DEEPL_API_URL,
        data={
            "auth_key": DEEPL_API_KEY,
            "text": text,
            "target_lang": target_lang
        }
    )
    response.raise_for_status()
    return response.json()["translations"][0]["text"]

# Proceso principal
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        match = line_pattern.match(line)
        if match:
            key, value = match.groups()
            plain_text = extract_plain_text(value)
            try:
                translation = translate_deepl(plain_text)
                final_value = replace_with_translation(value, [translation])
                outfile.write(f"{key}={final_value}\n")
            except Exception as e:
                print(f"Error en línea: {key} - {e}")
                outfile.write(f"{key}={value}\n")
        else:
            outfile.write(line)
