print("hola de nuevo")
print("lp")

def suma(a,b):
    return a+b

print(suma(4,6))

def generar_datos_ventas():
    dias = ["Lun", "Mar", "Mie", "Jue", "Vie"]
    ventas = [120, 500, 230, 289, 310]
    return dias, ventas

def resumen_analitica():
    dias, ventas = generar_datos_ventas()
    total = sum(ventas)
    promedio = total/len(ventas)
    return {
        "dias": dias,
        "ventas": ventas,
        "total": total,
        "promedio": promedio
    }
datos = resumen_analitica()
print("Total de ventas :", datos["total"])
print("promedio diario : ", datos["promedio"])