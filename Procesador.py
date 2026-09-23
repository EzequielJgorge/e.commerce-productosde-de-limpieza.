# 1. Creamos un diccionario vacío para acumular los totales por producto
totales_por_producto = {}

# 2. Abrimos y leemos el archivo local de forma segura usando 'with'
with open("datos_sucios.txt", "r", encoding="utf-8") as archivo:
    # Leemos la primera línea (encabezados) para saltarla
    encabezados = archivo.readline()
    
    # Recorremos el archivo línea por línea
    for linea in archivo:
        # Eliminamos espacios invisibles y dividimos los datos por la coma
        datos = linea.strip().split(",")
        
        # Si la línea está vacía, la salteamos
        if len(datos) < 3:
            continue
            
        # Limpiamos el texto: quitamos espacios extras y pasamos todo a mayúsculas
        # Esto unifica "Lavandina concentrada" y "lavandina concentrada" como un solo producto
        nombre_producto = datos[0].strip().upper()
        cantidad = int(datos[1].strip())
        precio_unidad = float(datos[2].strip())
        
        # Calculamos el total de esa venta específica
        total_venta = cantidad * precio_unidad
        
        # 3. Guardamos o sumamos el resultado en nuestro diccionario
        if nombre_producto in totales_por_producto:
            totales_por_producto[nombre_producto] += total_venta
        else:
            totales_por_producto[nombre_producto] = total_venta

# 4. Creamos un nuevo archivo local para escribir el reporte limpio
with open("reporte_limpio.txt", "w", encoding="utf-8") as archivo_salida:
    # Escribimos los nuevos encabezados
    archivo_salida.write("PRODUCTO,TOTAL_RECAUDADO\n")
    
    # Volcamos los resultados acumulados
    for producto, total in totales_por_producto.items():
        archivo_salida.write(f"{producto},${total:.2f}\n")

print("¡Procesamiento completado con éxito! Se ha generado 'reporte_limpio.txt'.")
