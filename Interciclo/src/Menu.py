import Cuadrado
def menu():
    print("Reconocimiento de figuras")
    print("1. Reconocimiento de Circulos")
    print("2. Reconocimiento de Cuadrados")
    print("3. Reconocimiento de Rectangulos")
    print("4. Reconocimiento de Triangulos")
    print("5. Reconocimiento de Varias figuras")
    print("Esc. Salir")

if __name__ == "__main__":
    Ejec=1
    Cuadrado.reconocimiento()
    while(Ejec == 1):
        menu()
        Ejec = 0
        
