
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