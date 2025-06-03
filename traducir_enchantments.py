#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
traducir_enchantments.py

Este script abre tu archivo original de encantamientos (p. ej. "enchantments.yml"),
elimina los comentarios (líneas que empiezan con "#"), detecta cada campo
description: (inline o multilinea), traduce su contenido al español usando googletrans,
y escribe un archivo nuevo con las descripciones traducidas, manteniendo intactos
los nombres de los encantamientos y el resto de la estructura YAML.
"""

import re
import sys
from googletrans import Translator

def traducir_bloque(lines, start_idx, traductor):
    """
    A partir de la línea 'start_idx' (donde aparece 'description: |-'),
    recorre todas las líneas indentadas que forman el bloque de descripción.
    Traduce cada línea, preservando la indentación original.
    Devuelve una tupla (bloque_traducido, índice_siguiente_a_procesar).
    """
    base_indent = len(lines[start_idx]) - len(lines[start_idx].lstrip())
    bloque_traducido = [lines[start_idx]]
    i = start_idx + 1
    textos_a_traducir = []
    indices = []

    while i < len(lines):
        linea = lines[i]
        if linea.strip() == "":
            bloque_traducido.append(linea)
            i += 1
            continue
        indent = len(linea) - len(linea.lstrip())
        if indent <= base_indent:
            break
        texto = linea[indent:].rstrip("\n")
        textos_a_traducir.append(texto)
        indices.append(i)
        i += 1

    if textos_a_traducir:
        traducciones = traductor.translate(textos_a_traducir, dest="es")
        for idx_original, trad in zip(indices, traducciones):
            indent = len(lines[idx_original]) - len(lines[idx_original].lstrip())
            bloque_traducido.append(" " * indent + trad.text + "\n")

    return bloque_traducido, i

def traducir_inline(line, traductor):
    """
    Traduce una línea de tipo:
        description: 'Texto a traducir'
        o
        description: "Otro texto a traducir"
    Si no coincide, devuelve la línea original.
    """
    patron = r'^(\\s*description:\\s*)([\\'"])(.*)([\\'"])\\s*$'
    m = re.match(patron, line)
    if not m:
        return line
    prefix, quote, contenido, _ = m.groups()
    traducido = traductor.translate(contenido, dest="es").text
    return f"{prefix}{quote}{traducido}{quote}\\n"

def procesar_archivo(ruta_entrada, ruta_salida):
    traductor = Translator()
    with open(ruta_entrada, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    resultado = []
    i = 0
    while i < len(lineas):
        linea = lineas[i]
        if linea.lstrip().startswith("#"):
            i += 1
            continue
        if re.match(r'^\\s*description:\\s*\\|-\\s*$', linea):
            bloque_trad, siguiente_idx = traducir_bloque(lineas, i, traductor)
            resultado.extend(bloque_trad)
            i = siguiente_idx
            continue
        if re.match(r'^\\s*description:\\s*[\\'"].+[\\'"]\\s*$', linea):
            resultado.append(traducir_inline(linea, traductor))
            i += 1
            continue
        resultado.append(linea)
        i += 1

    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.writelines(resultado)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python traducir_enchantments.py <entrada.yml> <salida_traducida.yml>")
        sys.exit(1)

    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    procesar_archivo(archivo_entrada, archivo_salida)
    print(f"✅ Traducción final guardada en: {archivo_salida}")
