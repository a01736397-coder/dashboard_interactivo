print("")
print("Hola de nuevo")

a = 40
b = 30
c = 8

<<<<<<< HEAD
def suma():
    print("Suma total: ", a + b + c)

suma()
=======
print(suma(4,6))
>>>>>>> 998460a46d4ad2d8d81ccb1272a9aa00b8a8c1d7


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
<<<<<<< HEAD
    graficar_ventas(dias, ventas)

main_frontend()

print("Despliegue de datos")

def generar_datos_ventas():
    dias = ["Lun", "Mar", "Mie", "Jue", "Vie"]
    ventas = [120, 500, 230, 289, 310]
    return dias, ventas

def resumen_analitica():
    dias, ventas = generar_datos_ventas()
    total = sum(ventas)
    promedio = total / len(ventas)
    return {
        "dias": dias, 
        "ventas": ventas,
        "total": total, 
        "promedio": promedio
    }
datos = resumen_analitica()
print("Total de ventas :", datos["total"])
print("Promedio diario:", datos["promedio"])
=======
    graficar_ventas(dias,ventas)

main_frontend()

print("lp")
>>>>>>> 998460a46d4ad2d8d81ccb1272a9aa00b8a8c1d7
