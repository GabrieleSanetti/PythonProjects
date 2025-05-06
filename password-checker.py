#----PASSWORD CHECKER----#

#---Function Score Numeri---#
def score_numeri(password):
    count_numbs = 0
    score = 0
    for charNumbs in password:
        if charNumbs in "1234567890":
            count_numbs += 1
        # print(countNumbs, charNumbs) #--> TEMPORANEO

    if count_numbs == 1:
        score += 12.5
    else:
        score += 25
# --->END Score per Numeri <---#
print("<---- ISTRUZONI TEST ---->")
print("Il password checker funziona tramite un sistema di punteggio.")
print("Il sistema valuta la password e rispondendoti con una valutazione tra, DEBOLE, BUONA e MOLTO FORTE.")
print("Per la valutazione il sistema assegna dei punti in base a: numero caratteri, caratteri speciali, maiuscole e minuscole ed infine numeri.")

print("\n<---- NUMERO CARATTERI ---->")
print("Numero caratteri UGUALI 8 -> 8 punti\nNumero caratteri TRA 9 E 15 -> 12.5 punti\nNumero caratteri MAGGIORI di 15 -> 25 punti.")

print("\n<---- CARATTERI SPECIALI ---->")
print("Caratteri speciali UGUALI a 1 -> 12.5 punti\nCaratteri speciali MAGGIORI di 1 -> 25 punti")

print("\n<---- MAIUSCOLE E MINUSCOLE ---->")
print("Maiuscole e Minuscole UGUALI a 1 -> 12.5 punti\nMaiuscole e Minuscole MAGGIORI di 1 -> 25 punti")

print("\n<---- NUMERI ---->")
print("Numeri UGUALI a 1 -> 12.5 punti\nNumeri MAGGIORI di 1 -> 25 punti")

print("Password DEBOLE, punti minori o uguali a 50.\nPassword BUONA, punti tra 51 e 75.\nPassword MOLTO FORTE, punti tra 76 e 100.")

def pass_check():
    while True:
        password = input("\nInserire la password: \n")


        #---Score System Variables---#
        count_length = len(password)
        score = 0
        count_spec = 0
        count_alpha = 0
        #--- END Score System Variables---#

        length = False
        special_char = False
        upper = False
        lower = False
        numbers = False

        count = len(password)


        if count < 8:
            print("❌ Passord invalida, digita almeno 8 caratteri")
        else:
            length = True
            print("✅ Lunghezza minima raggiunta")

        # --->Score per Lunghezza <---#
        if count_length == 8:
            score += 8
        elif 9 <= count_length <= 15:
            score += 12.5
        else:
            score += 25
        # --->END Score per Lunghezza <---#



        if password.isalnum():
            print("❌ Nessun carattere speciale, digitane almeno uno tra '!#$%&()*+,-./:;<=>?@[\\]_'{|}'")
        else:
            special_char = True
            # --->Score per Caratteri Speciali <---#
            for char in password:
                if char in "!#$%&()*+,-./:;<=>?@[\\]_'{|}":
                    count_spec += 1
                # print(countSpec, char) #--> TEMPORANEO

        if count_spec == 1:
            score += 12.5
        else:
            score += 25
        # --->END Score per Caratteri Speciali <---#
        print("✅ Almeno un carattere speciale è presente")
        print(special_char)

        for char in password:
            if char.isupper():
                upper = True

            if char.islower():
                lower = True

        if upper and lower:
            # --->Score per Maiuscole Minuscole <---#
            for charAlpha in password:
                if charAlpha in "QWERTYUIOPASDFGHJKLZXCVBNM":
                    count_alpha += 1
                # print(countAlpha, charAlpha) #--> TEMPORANEO

            if count_alpha == 1:
                score += 12.5
            else:
                score += 25
            # --->END Score per Maiuscole Minuscole <---#
            print("✅ È presente almeno un carattere maiuscolo e minuscolo")
        else:
            print("❌ Non è presente almeno un carattere maiuscolo o minuscolo")



        for char in password:
            if char.isdigit():
                numbers = True

        if numbers:
            score_numeri(password)
            print("✅ È presente almeno un numero")
        else:
            print("❌ Non è presente un numero")

        if length and special_char and upper and lower and numbers:
            if score <= 50:
                print(" 😟 La Password è DEBOLE riprova")
            elif 51 < score <= 75:
                print(" 👍🏻 La Password è BUONA")
            elif 75 < score <= 100:
                print(" 💪🏻 WOW! La Password è MOLTO FORTE")
            else:
                print("Password invalida")

        print(score)


pass_check()