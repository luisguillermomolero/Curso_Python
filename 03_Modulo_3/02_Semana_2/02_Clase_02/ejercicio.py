from datasets import load_dataset

def cargar_resenas_amazon(cantidad=5):
    dataset = load_dataset("amazon_polarity", split=f"train[:{cantidad}]")
    resenas = {}
    for i, entrada in enumerate(dataset, start=1):
        resenas[f"r{i:03}"] ={
            "título": entrada["title"],
            "contenido": entrada["content"],
            "Sentimiento": "positivo" if entrada["label"] == 1 else "Negativo"
        }
    return resenas

def mostrar_resenas(resenas_dict):
    for id_resenas, datos in resenas_dict.items():
        print(f"ID: {id_resenas}")
        
        for clave, valor in datos.items():
            print(f" {clave.capitalize()}: {valor}")
        print()

def main():
    cantidad = 5
    resenas_estructuradas = cargar_resenas_amazon(cantidad)
    mostrar_resenas(resenas_estructuradas)

if __name__ == "__main__":
    main()
