def StringComLetraA(StringComA):
    stringComA = StringComA
    b = 0
    for i in stringComA:
        if i == "a" or i == "A":
            b += 1 

    print(f"Encontrou A letra a {b} vezes")

StringComLetraA("Agora eu vou contar quantas letras a tem nessa string")