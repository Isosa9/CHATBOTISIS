from db import fetch_products

def main():
    palabra_busqueda = "ganado"   # Cambia por lo que quieras buscar
    productos = fetch_products(palabra_busqueda)

    if productos:
        print(f"Productos encontrados para '{palabra_busqueda}':\n")
        for p in productos:
            nombre, categoria, descripcion, precio = p
            print(f"- {nombre} ({categoria})")
            print(f"  Descripción: {descripcion}")
            print(f"  Precio: L {precio:.2f}\n")
    else:
        print("No se encontraron productos con esa descripción.")

if __name__ == "__main__":
    main()
