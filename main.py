
# Øvelser del 3 - tekstsrenge

def opg1():
    n = input("Enter the word and see if it is palindrome: ")

    if n == n[::-1]:
        print("This word is palindrome")
    else:
        print("This word is not palindrome")


def opg2():
    n = input("Enter the word / sætinger and see if it is palindrome: ").replace(" ", "").replace(".", "").replace(",", "")
    if n == n[::-1]:
        print("This word is palindrome")
    else:

        print("This word is not palindrome")


def opg3_del1():
    streng = input("Enter an string: ")

    streng_baglæns = streng[::-1]
    print(streng_baglæns)


def opg3_del2():
    words = ["devil", "wolf", "lamina", "flow", "peek", "retool",
             "lived", "keep", "panel", "animal", "looter", "lizard"]

    for word in words:
        for w in words:
            word_baglæns = word[::-1]
            if w == word_baglæns:
                print(word_baglæns, " -- ", word)


def opg4():
    import re
    linjer = ["Hvad hedder du?", "Sikke et vejr vi har!", "Hvad har du nu gjort?",
              "Pyt med det.", "Tror du, det er rigtigt?"]

    print("Antallet af ord i hver sætning")
    for sæt in linjer:
        count_all_words = len(sæt.split())
        print(count_all_words)

    print("\nAntallet af bogstaver (uden tegn og mellemrum) i hver sætning.")
    for sæt in linjer:
        sæt2 = re.sub('[^A-Za-z0-9]+', '', sæt)
        count_all_chars = len(sæt2)
        print(count_all_chars)

    print("\nUdskriver det sidste ord i hver sætning (uden tegn)")
    for sæt in linjer:
        sæt2 = re.sub('[^A-Za-z0-9]+', ' ', sæt)
        last_word = sæt2.split()[-1]

        print(last_word)

opg4()

print("\n\nDone!!")
