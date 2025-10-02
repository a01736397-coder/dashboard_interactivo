print("hola de nuevo")
print("lp")

def suma(a,b):
    return a+b

print(suma(4,6))


import matplotlib.pyplot as plt

def graficar_ventas(dias, ventas):
    plt.figure(figsize=(8,4))
    plt.plot(dias, ventas, marker = "o", linestyle ="-", color ="red")
    plt.title("Ventas diarias")
    plt.xlabel("Día")
    plt.ylabel("Ventas")
    plt.grid(True)
    plt.show()

def main_frontend(): 
    dias = ["Lun", "Mar", "Mie", "Jue", "Vie"]
    ventas = [120, 500, 230, 289, 310]
    graficar_ventas(dias,ventas)

main_frontend()