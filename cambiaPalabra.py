import sys

argumentos = sys.argv

if len(argumentos) < 2:
    f = input("Nombre de ficheros: ")
    argumentos.append(f)

if len(argumentos) < 3:
    argumentos.append(input("palabra original:"))
    
if len(argumentos) < 4:
    argumentos.append(input("nueva palabra: "))

nombreF = argumentos[1]
original = argumentos[2]
nueva = argumentos[3]

f = open(nombreF, "r")

texto_original = f.read()
f.close()

texto_sustituido = texto_original.replace(original, nueva)

f = open(nombreF, "w")
f.write(texto_sustituido)
f.close()