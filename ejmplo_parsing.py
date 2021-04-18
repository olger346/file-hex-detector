import argparse
# parser con argparse
# instanciamos el objeto de argparse

parser = argparse.ArgumentParser()

# anadimos argumentos, estos argumentos estan declarados como argumentos posicionales, es decir que son obligatorios
# los argumentos opcionales se marcan con --nombre_argumento y se escribe de la misma manera en la cli.
parser.add_argument("numero1", help="primer numero")
parser.add_argument("numero2", help="segundo numero")
parser.add_argument("operacion", help="realiza una operacion matematica")
parser.add_argument("--optional", help="argumento opcional, no hace nada xD")

# guardamos los argumentos como objetos y los instanciamos en la variable args
args = parser.parse_args()

print("imprimiendo argumentos")

# se hace el llamado de las propiedades dentro de la case, estas son almacenadas en ste

print("Priner argumento {0}".format(args.numero1))
print("Segundo Argumento {0}".format(args.numero2))
print('Operacion a realizar "{0}"'.format(args.operacion))
print("Argumento opcional {0}".format(args.optional))