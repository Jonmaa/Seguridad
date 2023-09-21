#Cifrado
texto= "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE"

def contar_letras_ordenadas(texto):
    resultado = {}
    #texto = texto.lower()U
    for letra in texto:   
        if letra.isalpha() : #Solo cuenta las letras, skipea números y espacios
            if letra in resultado:
                resultado[letra] += 1
            else:
                resultado[letra] = 1
    ordenados = sorted(resultado.keys(), key=lambda letra: resultado[letra], reverse=True)
    return ordenados  

texto_ordenado = contar_letras_ordenadas(texto)
print(texto_ordenado)

primer_caracter = texto_ordenado[0]
segundo_caracter = texto_ordenado[1]

frecuencia_espanol = [
    'e', 'a', 'O', 'L', 'S', 'N', 'D', 'R',
    'U', 'I', 'T', 'C', 'P', 'M', 'Y', 'Q',
    'B', 'H', 'G', 'F', 'V', 'J', 'Ñ', 'Z',
    'X','K', 'W'
]

texto = texto.replace(primer_caracter, frecuencia_espanol[0])
texto = texto.replace(segundo_caracter, frecuencia_espanol[1])

#frecuencia_espanol = {
#    'E': 16.78, 'A': 11.96, 'O': 8.69, 'L': 8.37, 'S': 7.88, 'N': 7.01, 'D': 6.87, 'R': 4.94,
#    'U': 4.80, 'I': 4.15, 'T': 3.31, 'C': 2.92, 'P': 2.776, 'M': 2.12, 'Y': 1.54, 'Q': 1.53,
#    'B': 0.92, 'H': 0.89, 'G': 0.73, 'F': 0.52, 'V': 0.39, 'J': 0.30, 'Ñ': 0.29, 'Z': 0.15,
#    'X': 0.06,'K': 0.00, 'W': 0.00
#}



print(primer_caracter)
print(frecuencia_espanol[0])
print(texto)

palabra= ""
palabra2= ""

while palabra != "exit":
    palabra=input("Escribe una letra o exit para salir  ")
    if palabra != "exit" :
        palabra2=input("Escribe una letra o exit para salir  ")
        if palabra2 != "exit" and  palabra.isalpha() and  palabra2.isalpha():
            texto = texto.replace(palabra,palabra2)
            print(texto)
    


   