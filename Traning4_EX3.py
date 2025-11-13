negatiu = False

for i in range(10):
    num = float(input(f"Introdueix el nombre {i+1}: "))
    
    if num < 0:
        negatiu = True

if negatiu:
    print("Hi havia almenys un nombre negatiu.")
else:
    print("No hi ha cap nombre negatiu.")