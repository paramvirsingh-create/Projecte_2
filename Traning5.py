from time import sleep
def Traning1_EX1():
    print ("Hola món!")
def Traning2_EX1():
    side = float(input("Introdueix la mida del lateral del quadrat: "))

    if side >= 0:
        print("No es pot calcular l'àrea si el costat és zero o negatiu.")
    else:
        area = side * side
        print(f"L'àrea del quadrat és: {area}")
    if side <= 0:
        side = float(input("Introdueix la mida del lateral del quadrat: "))
        if side > 0:
            area = side * side
            print(f"L'àrea del quadrat és: {area}")

def Traning2_EX2():
    num1 = int(input("Introdueix el primer nombre enter: "))
    num2 = int(input("Introdueix el segon nombre enter: "))

    suma = num1 + num2
    resta = num1 - num2
    multiplicacio = num1 * num2
    divisio = num1 / num2 

    print("Suma:", suma)
    print("Resta:", resta)
    print("Multiplicació:", multiplicacio)
    print("Divisió:", divisio)

def Traning2_EX3():
    paraula1 = input("Introdueix la primera paraula: ")
    paraula2 = input("Introdueix la segona paraula: ")
    paraula3 = input("Introdueix la tercera paraula: ")

    frase = paraula1 + " " + paraula2 + " " + paraula3

    print("La frase formada és:", frase)

def Traning2_EX4():
    num1 = float(input("Introdueix el primer nombre decimal: "))
    num2 = float(input("Introdueix el segon nombre decimal: "))

    resultat_enter = int(num1 + num2)

    print("El resultat en enter és:", resultat_enter)

def Traning3_EX1():
    edat = int(input("Introdueix la teva edat: "))

    if edat >= 18:
        print("Ets major d'edat")
    else:
        print("Ets menor d'edat")

def Traning3_EX2():
    num1 = float(input("Introdueix el primer nombre: "))
    num2 = float(input("Introdueix el segon nombre: "))
    num3 = float(input("Introdueix el tercer nombre: "))

    if num1 > num2 and num1 > num3:
        print("El nombre més gran és:", num1)
    elif num2 > num1 and num2 > num3:
        print("El nombre més gran és:", num2)
    else:
        print("El nombre més gran és:", num3)
def Traning3_EX3():
    num = float(input("Introdueix un nombre: "))

    if num >= 0:
        print("El nombre és positiu.")
    else:
        print("El nombre és negatiu.")
def Traning4_EX1():
    for num in range(1, 201):
        if num % 2 == 0:
            print(num) 
def Traning4_EX2():
    while True:
        nota = float(input("Introdueix una nota (0-10) o -1 per acabar: "))
    
        if nota == -1:
            break
    
        if nota == 10:
            Nota = True

    if Nota:
        print("Hi ha hagut alguna nota que té un 10.")
    else:
        print("No hi ha cap 10.")
def Traning4_EX3():
    for i in range(10):
        num = float(input(f"Introdueix el nombre {i+1}: "))
    
        if num < 0:
            negatiu = True
        if num >= 0:
            negatiu = False
    if negatiu:
        print("Hi havia almenys un nombre negatiu.")
    else:
        print("No hi ha cap nombre negatiu.")

#Ara es comensa la Activitat 5:

def menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Traning1_EX1 → Hola món")
    print("2. Traning2_EX1 → Càlcul de l'àrea d'un quadrat")
    print("3. Traning2_EX2 → Operacions amb dos enters")
    print("4. Traning2_EX3 → Crear una frase amb tres paraules")
    print("5. Traning2_EX4 → Suma de decimals (resultat enter)")
    print("6. Traning3_EX1 → Major o menor d'edat")
    print("7. Traning3_EX2 → Trobar el nombre més gran")
    print("8. Traning3_EX3 → Positiu o negatiu")
    print("9. Traning4_EX1 → Mostrar nombres parells fins a 200")
    print("10. Traning4_EX2 → Comprovar si hi ha alguna nota 10")
    print("11. Traning4_EX3 → Comprovar si hi ha algun nombre negatiu")
    print("S. Sortir")

while (True):
    menu() 
    opcio = input("Tria una opció: ")
    match opcio:
        case "1":
            Traning1_EX1()
        case "2":
            Traning2_EX1()
        case "3":
            Traning2_EX2()
        case "4":
            Traning2_EX3()
        case "5":
            Traning2_EX4()
        case "6":
            Traning3_EX1()
        case "7":
            Traning3_EX2()
        case "8":
            Traning3_EX3()
        case "9":
            Traning4_EX1()
        case "10":
            Traning4_EX2()
        case "11":
            Traning4_EX3()
        case "S":
            print("Sortint del programa... Adeu!")
            break
        case _:
            print("Opció no vàlida. Torna-ho a intentar.")
    sleep(2)