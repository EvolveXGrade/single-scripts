import hashlib

hash_objetivo = "c967d488512ab5559b446f97843de1be0d615088"

wordlist = []

with open("wordlist.lst", "r") as f:
    for linea in f:
        wordlist.append(linea.strip())

encontrada = False

for palabra1 in wordlist:
    for palabra2 in wordlist:
        palabra = palabra1 + palabra2
        hash_palabra = hashlib.sha1(palabra.encode()).hexdigest()
        if hash_palabra == hash_objetivo:
            print("Contraseña encontrada: ", palabra)
            encontrada = True
            break

    if encontrada:
        break

if not encontrada:
    print("No hay ninguna combinación de dos cadenas que sea la contraseña")