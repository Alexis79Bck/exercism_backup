"""Verifier ISBN-10 code"""

ISBN_LENGTH = 10

def is_valid(isbn: str) -> bool:
    """Verify is a code is a ISBN-10 format code valid"""
    
    cleaned_isbn = ""
    for char in isbn:
        if char != "-":
            cleaned_isbn += char

    # 2. Validación de longitud estricta
    if len(cleaned_isbn) != 10:
        return False

    # 3. Inicialización de acumuladores
    total = 0
    length = len(cleaned_isbn)

    # 4. Bucle explícito indexado (estilo C / PHP clásico)
    for index in range(length):
        current_char = cleaned_isbn[index]
        multiplier = length - index

        # Determinar el valor numérico del carácter de forma explícita
        if current_char.isdigit():
            numeric_value = int(current_char)
        elif current_char == "X" and index == 9:
            numeric_value = 10
        else:
            # Si hay un caracter inválido o una 'X' mal ubicada, se rechaza de inmediato
            return False

        # Acumular el resultado paso a paso
        total += numeric_value * multiplier

    # 5. Comprobación matemática final
    
    return  total % 11 == 0 
    
