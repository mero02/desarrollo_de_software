import sys #Esto te permite acceder a los argumentos de la línea de comandos

def saludo(name):
    print(f"Hola {name.capitalize()}!")
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
        saludo(name)
    else:
        print("Por favor, proporciona un nombre como argumento.")