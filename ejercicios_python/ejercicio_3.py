def suma (a,b):
    return a + b

def resta (a,b):
    return a - b

def multiplicacion (a,b):
    return a * b

def division (a,b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."

if __name__ == "__main__":
    num1 = float(input("Ingrese primer numero: "))
    num2 = float(input("Ingrese segundo numero: "))
    
    print(f"Suma: {num1} + {num2} = {suma(num1,num2)}")
    print(f"Resta: {num1} - {num2} = {resta(num1,num2)}")
    print(f"Multiplicacion: {num1} * {num2} = {multiplicacion(num1,num2)}")
    print(f"Division: {num1} / {num2} = {division(num1,num2)}")