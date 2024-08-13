def celcius_a_fahrenheit(valor):
    return (valor * 9/5) + 32

def fahrenheit_a_celcius(valor):
    return (valor - 32) * 5/9

if __name__ == "__main__":
    temperatura = float(input("Ingrese temperatura: "))
    escala = input("Ingrese escala (C para celcius, F para Faharenheit): ").strip().upper()
    #strip(): Elimina los espacios en blanco (u otros caracteres específicos).
    #upper(): Convierte todos los caracteres en la cadena a mayúsculas.
    if (escala == "C"):
        temperatura_convertida = celcius_a_fahrenheit(temperatura)
        print(f"{temperatura}°C es igual a {temperatura_convertida:.2f}°F")
        #La temperatura convertida se imprime con dos decimales usando :.2f para el formato.
    elif (escala == "F"):
        temperatura_convertida = fahrenheit_a_celcius(temperatura)
        print(f"{temperatura}°F es igual a {temperatura_convertida:.2f}°C")
    else:
        print("Escala no reconocida. Por favor, ingrese 'C' para Celsius o 'F' para Fahrenheit.")