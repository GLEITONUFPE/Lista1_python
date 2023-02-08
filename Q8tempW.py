resp = "s"


while resp == "s":
    f = float(input("Digite a temperatura em F: "))

    celsius = (f-32)*5/9
    print("a temperatura em celsius é:", celsius)

    resp = input("Digite s para continuar: ")
