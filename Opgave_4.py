
# Øvelser del 4 list og dictionary

def opg1():
    usr_num = int(input("how manyt numbers do like add together : "))

    values = []
    for index in range(usr_num):
        values.append(int(input("Please enter a value : ")))

    usr_operator = input("Please pick an operator: ")
    resultat = 0
    for num in values:
        if usr_operator == "+":
            resultat += num
        elif usr_operator == "-":
            if resultat > 0:
                resultat -= num
            else:
                resultat = num
        elif usr_operator == "*":
            if resultat > 0:
                resultat *= num
            else:
                resultat = num
        elif usr_operator == "/":
            if resultat > 0:
                resultat /= num
            else:
                resultat = num

    if resultat == 0:
        print("du her ikke indtastede et validt operator ")
    else:
        print(resultat)


def opg2():
    ord = ['hej', 'test', 'bla', 'python', 'bla', 'hej', 'bla']

    antal = {}
    for o in ord:
        if o not in antal:
            antal[o] = 0
        antal[o] += 1

    print(antal)


opg2()