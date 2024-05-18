my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list.append(11)
my_list.insert(1, 1.4)

# print(my_list)

for i in my_list:
    print(i)
    print(my_list.pop(0))


# extra 1


web1 = "Pàgina 1"

url = [web1]
pag = 1 

def navegador (url):
    if len(url) == 5:
        print("Has arribat al final.")
        url = []
    elif len(url) == 0:
        print("No es pot retrocedir més")
        url = []
    else:
        pag = len(url)
        print((f"Estàs a la pàgina {pag}"))
        accio = input("Que vols fer? avançar o retrocedir? ")
        if accio == "avançar":
            pag = pag + 1
            url.append(f"Pàgina {pag}")
            navegador(url)
        elif accio == "retrocedir":
            pag = pag - 1
            url.pop()
            navegador(url)
        else:
            print("Esta no és una resposta correcta")
    
navegador(url)


# Extra 2

documents = ["TFM", "TFG", "Llibre Python", "Llibre Fantasia"]

def accio_imprimir(documents: list):
    if documents == []:
        print("No hi ha res per a imprimir")
    else:
        resposta = input(str("Què vols imprimir? "))
        if resposta == "imprimir":
            print(f"S'imprimirà el document {documents.pop()}")
            accio_imprimir(documents)
        elif resposta == "fi":
            pass
        else:
            documents.append(resposta)
            print(f"El document {resposta} s'afegirà a la cola")
            print(documents)
            accio_imprimir(documents)

accio_imprimir(documents)
