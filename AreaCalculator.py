import math

print("==================")
print("Area Calculator 📐")
print("==================")
print("")
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

while True:
    opcion = int(input("\n(1-4)Select your shape, (5) Quit: "))

    if opcion == 1:
        height = float(input("Height: "))
        base = float(input("Base: "))
        area = (height * base) / 2
        print("\nThe area of the Triangle is ", area)

    elif opcion == 2:
        lenght = float(input("Length: "))
        width = float(input("Width: "))
        area = (lenght * base) / 2
        print("\nThe area of the Rectangle is ", area)

    elif opcion == 3:
        side = float(input("Side: "))
        area = side ** 2
        print("\nThe area of the Square is is ", area)
        
    elif opcion == 4:
        radius = float(input("Radius: "))
        area = math.pi * radius ** 2
        print("\nThe area of the Circle is ", area)
        
    elif opcion == 5:
        print("\nSaliendo del programa...")
        break
    else:
        print("\nOpción inválida. Ingrese otro número.")
2