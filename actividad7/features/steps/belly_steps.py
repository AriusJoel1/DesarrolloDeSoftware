from behave import given, when, then
import re
import random

# Función para convertir palabras o dígitos a número (mantiene tu lógica original)
def convertir_palabra_a_numero(palabra):
    palabra = palabra.lower()
    # 1) Si viene en dígitos (p. ej. "90" o "2.5")
    if re.fullmatch(r"\d+(?:\.\d+)?", palabra):
        return float(palabra)

    # 2) Diccionarios originales
    palabras_a_numeros_es = {
        "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
        "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
        "once": 11, "doce": 12, "trece": 13, "catorce": 14, "quince": 15,
        "veinte": 20, "veinti": 20, "treinta": 30, "cuarenta": 40, "cincuenta": 50,
        "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90, "cien": 100
    }
    palabras_a_numeros_en = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100
    }

    if palabra in palabras_a_numeros_es:
        return palabras_a_numeros_es[palabra]
    elif palabra in palabras_a_numeros_en:
        return palabras_a_numeros_en[palabra]
    else:
        return 0  # casos no esperados

# Steps de Behave
@given('que he comido {cukes:d} pepinos')
def step_given_eaten_cukes(context, cukes):
    context.belly.comer(cukes)

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    # Limpieza básica
    time_description = time_description.strip('"').lower().strip()
    # Elimina separadores como comas
    time_description = time_description.replace(',', '')

    # Caso especial: tiempo aleatorio
    match_random = re.search(
        r'un\s+tiempo\s+aleatorio\s+entre\s+(\d+(?:\.\d+)?)\s+y\s+(\d+(?:\.\d+)?)\s+horas?',
        time_description
    )
    if match_random:
        low = float(match_random.group(1))
        high = float(match_random.group(2))
        total_time_in_hours = random.uniform(low, high)
        print(f"🕒 Tiempo aleatorio generado: {total_time_in_hours:.2f} horas")
        context.belly.esperar(total_time_in_hours)
        return

    # Normalizar "y" y "and"
    time_description = time_description.replace(' y ', ' ').replace(' and ', ' ')

    # Regex que captura horas, minutos y segundos (número o palabra)
    pattern = re.compile(
        r'(?:(\d+(?:\.\d+)?|\w+)\s*(horas?|hours?))?'      # grupo 1: horas
        r'\s*(?:(\d+(?:\.\d+)?|\w+)\s*(minutos?|minutes?))?'# grupo 3: minutos
        r'\s*(?:(\d+(?:\.\d+)?|\w+)\s*(segundos?|seconds?))?'# grupo 5: segundos
    )
    match = pattern.match(time_description)

    if match:
        raw_hours = match.group(1) or "0"
        raw_minutes = match.group(3) or "0"
        raw_seconds = match.group(5) or "0"

        hours = convertir_palabra_a_numero(raw_hours)
        minutes = convertir_palabra_a_numero(raw_minutes)
        seconds = convertir_palabra_a_numero(raw_seconds)

        total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)
        print(f"⏳ Tiempo calculado: {total_time_in_hours:.4f} horas")
        context.belly.esperar(total_time_in_hours)
    else:
        raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

@when('pregunto cuántos pepinos más puedo comer')
def step_when_ask_how_many_more(context):
    max_without_grumble = 10
    eaten = context.belly.pepinos_comidos
    context.remaining_cukes = max(0, max_without_grumble - eaten)

@then('debería decirme que puedo comer {expected:d} pepinos más')
def step_then_should_say_can_eat_more(context, expected):
    actual = context.remaining_cukes
    assert actual == expected, f"Se esperaban {expected} pepinos más, pero se obtuvieron {actual}."

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."

@then('debería haber comido {expected:d} pepinos')
def step_then_should_have_eaten_cukes(context, expected):
    eaten = context.belly.pepinos_comidos
    assert eaten == expected, f"Se esperaban {expected} pepinos comidos, pero se encontraron {eaten}."
