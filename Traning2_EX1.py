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