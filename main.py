def main():
    vertices = []
    caras = []
    
    while True:
        print("\nMenú:")
        print("1. Agregar vértice")
        print("2. Agregar cara")
        print("3. Mostrar figura")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            x = input("Ingrese X: ")
            y = input("Ingrese Y: ")
            z = input("Ingrese Z: ")
            vertices.append((x, y, z))
            print("Vértice agregado.")
        elif opcion == "2":
            if not vertices:
                print("No hay vértices registrados.")
                continue
            indices = input("Ingrese los índices de los vértices separados por espacios: ").split()
            caras.append([int(i) for i in indices])
            print("Cara agregada.")
        elif opcion == "3":
            print("\nVértices:")
            for i, v in enumerate(vertices):
                print(f"{i}: {v}")
            print("Caras:")
            for i, c in enumerate(caras):
                print(f"{i}: {c}")
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()

