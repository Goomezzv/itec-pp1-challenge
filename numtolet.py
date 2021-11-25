unidades = ('cero','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve')

decenas = ('diez','once','doce','trece','catorce','quince','dieciseis','diecisiete','dieciocho','diecinueve')

decenas_diez = ('cero','diez','veinte','treinta','cuarenta','cincuenta','sesenta','setenta','ochenta','noventa')

Cien = ('_','ciento','doscientos','trescientos','cuatroscientos', 'quinientos','seiscientos','setecientos','ochocientos','novecientos')

maxNum= 9999999999

def numtolet(numero):
    numero_entero = int(numero)
    if numero_entero > maxNum:
        raise OverflowError('Número excede el limite')
    if numero_entero < 0:
        return 'menos %s' % numero_a_letras(abs(numero))
    letras_decimal = ''
    decimal = int(round((abs(numero) - abs(numero_entero)) * 100))
    if decimal > 9:
        letras_decimal = 'punto %s' % numero_a_letras(decimal)
    elif decimal > 0:
        letras_decimal = 'punto cero %s' % numero_a_letras(decimal)
    if (numero_entero <= 99):
        resultado = leer_decenas(numero_entero)
    elif (numero_entero <= 999):
        resultado = read_centenas(numero_entero)
    elif (numero_entero <= 999999):
        resultado = read_miles(numero_entero)
    elif (numero_entero <= 999999999):
        resultado = read_millones(numero_entero)
    else:
        resultado = read_millar(numero_entero)
    resultado = resultado.replace('uno mil', 'un mil')
    resultado = resultado.strip()
    resultado = resultado.replace(' _ ', ' ')
    resultado = resultado.replace('  ', ' ')
    if decimal > 0:
        resultado = '%s %s' % (resultado, letras_decimal)
    return resultado

def leer_decenas(numero):
    if numero < 10:
        return unidades[numero]
    decena, unidad = divmod(numero, 10)
    if numero <= 19:
        resultado = decenas[unidad]
    elif numero <= 29:
        resultado = 'veinti%s' % unidades[unidad]
    else:
        resultado = decenas_diez[decena]
        if unidad > 0:
            resultado = '%s y %s' % (resultado, unidades[unidad])
    return resultado

def read_centenas(numero):
    centena, decena = divmod(numero, 100)
    if decena == 0:
        resultado = 'cien'
    else:
        resultado = Cien[centena]
        if decena > 0:
            resultado = '%s %s' % (resultado, leer_decenas(decena))
    return resultado

def read_miles(numero):
    millar, centena = divmod(numero, 1000)
    resultado = ''
    if (millar == 1):
        resultado = ''
    if (millar >= 2) and (millar <= 9):
        resultado = unidades[millar]
    elif (millar >= 10) and (millar <= 99):
        resultado = leer_decenas(millar)
    elif (millar >= 100) and (millar <= 999):
        resultado = read_centenas(millar)
    resultado = '%s mil' % resultado
    if centena > 0:
        resultado = '%s %s' % (resultado, read_centenas(centena))
    return resultado

def read_millones(numero):
    millon, millar = divmod(numero, 1000000)
    resultado = ''
    if (millon == 1):
        resultado = ' un millon '
    if (millon >= 2) and (millon <= 9):
        resultado = unidades[millon]
    elif (millon >= 10) and (millon <= 99):
        resultado = leer_decenas(millon)
    elif (millon >= 100) and (millon <= 999):
        resultado = read_centenas(millon)
    if millon > 1:
        resultado = '%s millones' % resultado
    if (millar > 0) and (millar <= 999):
        resultado = '%s %s' % (resultado, read_centenas(millar))
    elif (millar >= 1000) and (millar <= 999999):
        resultado = '%s %s' % (resultado, read_miles(millar))
    return resultado

def read_millar(numero):
    millar, millon = divmod(numero, 1000000)
    return '%s millones %s' % (read_miles(millar), read_millones(millon))

print(numtolet(1973))