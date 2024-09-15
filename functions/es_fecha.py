import re #comprueba si el texto contiene un patron

def es_fecha(texto):
    # define the patron of regular expresion for a dd/mm/yyyy format
    # Definir el patrón de la expresión regular para el formato dd/mm/yyyy
    patron1 = r'^\d{2}/\d{2}/\d{4}$' # dia con 2 digitos, mes con 2 digitos
    patron2 = r'^\d{1}/\d{2}/\d{4}$' # dia con 1 digitos, mes con 2 digitos
    
    patron3 = r'^\d{1}/\d{1}/\d{4}$' # dia con 1 digitos, mes con 1 digitos
    patron4 = r'^\d{2}/\d{1}/\d{4}$' # dia con 2 digitos, mes con 1 digitos
    
    # Comprobar si el texto coincide todas las convianciones de patrones
    if re.match(patron1, texto) or re.match(patron2, texto) or re.match(patron3, texto) or re.match(patron4, texto) :
        return True
    else:
        return False
