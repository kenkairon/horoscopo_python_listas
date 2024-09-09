def obtener_signo_zodiacal(mes, dia):
    signos = [
        {"nombre": "Capricornio", "inicio": (12, 22), "fin": (1, 19),
         "descripcion": "Los capricornio son personas ambiciosas y determinadas, con una gran capacidad para el trabajo duro."},
        {"nombre": "Acuario", "inicio": (1, 20), "fin": (2, 18),
         "descripcion": "Los acuario son personas amables, inteligentes y llenas de curiosidad por el mundo."},
        {"nombre": "Piscis", "inicio": (2, 19), "fin": (3, 20),
         "descripcion": "Los piscis son personas sensibles y emocionales, con una gran capacidad de empatía."},
        {"nombre": "Aries", "inicio": (3, 21), "fin": (4, 19),
         "descripcion": "Los aries son personas valientes, enérgicas y llenas de pasión."},
        {"nombre": "Tauro", "inicio": (4, 20), "fin": (5, 20),
         "descripcion": "Los tauro son personas prácticas y realistas, con un fuerte sentido de la determinación."},
        {"nombre": "Géminis", "inicio": (5, 21), "fin": (6, 20),
         "descripcion": "Los géminis son personas curiosas y sociables, con una mente abierta y adaptable."},
        {"nombre": "Cáncer", "inicio": (6, 21), "fin": (7, 22),
         "descripcion": "Los cáncer son personas emocionales y sensibles, con una gran capacidad de empatía."},
        {"nombre": "Leo", "inicio": (7, 23), "fin": (8, 22),
         "descripcion": "Los leo son personas valientes y apasionadas, con una gran autoconfianza."},
        {"nombre": "Virgo", "inicio": (8, 23), "fin": (9, 22),
         "descripcion": "Los virgo son personas meticulosas y perfeccionistas, con una gran atención al detalle."},
        {"nombre": "Libra", "inicio": (9, 23), "fin": (10, 22),
         "descripcion": "Los libra son personas equilibradas y justas, con una gran habilidad para encontrar la armonía."},
        {"nombre": "Escorpión", "inicio": (10, 23), "fin": (11, 21),
         "descripcion": "Los escorpio son personas intensas y apasionadas, con una gran profundidad emocional."},
        {"nombre": "Sagitario", "inicio": (11, 22), "fin": (12, 21),
         "descripcion": "Los sagitario son personas aventureras y optimistas, con una gran pasión por la exploración."}
    ]

    for signo in signos:
        if (mes == signo["inicio"][0] and dia >= signo["inicio"][1]) or (mes == signo["fin"][0] and dia <= signo["fin"][1]):
            return signo["nombre"], signo["descripcion"]

    return 'Desconocido', 'Fecha fuera del rango de signos zodiacales.'

# Ejemplo de uso:
mes = int(input("Ingresa el mes (1-12): "))
dia = int(input("Ingresa el día (1-31): "))
signo, descripcion = obtener_signo_zodiacal(mes, dia)
print(f"Signo: {signo}")
print(f"Descripción: {descripcion}")
