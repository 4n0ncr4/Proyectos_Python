while True:
    x = int(input("Numero: "))
    if x == 0:
        break
    if x < 0:
        print("Solo numeros positivos")
    print("Recibí", x)

for i in range(1, 21):
    if i == 13:
        continue
    if i > 15:
        break
    print(i)

sentimiento = int(input("Del 1 al 10, cómo te sientes hoy?: "))
while True:
    if sentimiento < 0:
        sentimiento = int(input("Del 1 al 10, cómo te sientes hoy? (Mayor a 0): "))
    else:
        if sentimiento >= 0 and sentimiento <= 3:
            print("Te sientes mal")
            break
        elif sentimiento >= 4 and sentimiento <= 7:
            print("Te sientes regular")    
            break
        else:
            print("Estás excelente")
            break

horas = int(input("Cuantas horas dormiste?: "))
while True:
    if horas < 0:
        horas = int(input("Cuantas horas dormiste? (Mayor a 0): "))
    else:
        if horas < 3:
            print("No dormiste nada")
            break
        elif horas >= 3 and horas <= 8:
            print("Dormiste regular")
            break
        else:
            print("Dormiste muy bien")    
            break

for i in range(0, 10, 2):
    print("Tengo hambre")

