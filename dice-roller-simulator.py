import random

def dice_faces(face):
    switch={
        1:"⌈━━━━━━━━━⌉\n|         |\n|    ●    |\n|         |\n⌊━━━━━━━━━⌋",
        2:"⌈━━━━━━━━━⌉\n| ●       |\n|         |\n|       ● |\n⌊━━━━━━━━━⌋",
        3:"⌈━━━━━━━━━⌉\n| ●       |\n|    ●    |\n|       ● |\n⌊━━━━━━━━━⌋",
        4:"⌈━━━━━━━━━⌉\n| ●     ● |\n|         |\n| ●     ● |\n⌊━━━━━━━━━⌋",
        5:"⌈━━━━━━━━━⌉\n| ●     ● |\n|    ●    |\n| ●     ● |\n⌊━━━━━━━━━⌋",
        6:"⌈━━━━━━━━━⌉\n| ●     ● |\n| ●     ● |\n| ●     ● |\n⌊━━━━━━━━━⌋"
    }
    return switch.get(face, "Invalid input")

def dice_game():
    throw_dice = input("Digita 'GO' per lanciare il dado! -> ").lower()
    error = ("SCELTA NON VALIDA! Riavvio gioco...\n\n")

    if throw_dice == "go":
        p2_dice = (random.randint(1, 6))
        p1_dice = (random.randint(1, 6))

        print(f"\nIl dado del giocatore 1 è \n⬇️ \n{dice_faces(p1_dice)}\n")
        move_on = input("Digita 'VAI' per proseguire -> ").lower()

        if move_on == "vai":
            print(f"\nIl giocatore 2 sta lanciando il suo dado...")
            if p1_dice == p2_dice:
                print("Pareggio")
                print(f"Dado giocatore 1 \n⬇️ \n{dice_faces(p1_dice)}\n")
                print(f"Dado giocatore 2 \n⬇️ \n{dice_faces(p2_dice)}\n")
            elif p1_dice > p2_dice:
                print("Giocatore 1 HA VINTO!")
                print(f"Dado giocatore 1 \n⬇️ \n{dice_faces(p1_dice)}\n")
                print(f"Dado giocatore 2 \n⬇️ \n{dice_faces(p2_dice)}\n")
            else:
                print("Giocatore 2 HA VINTO!")
                print(f"Dado giocatore 1 \n⬇️ \n{dice_faces(p1_dice)}\n")
                print(f"Dado giocatore 2 \n⬇️ \n{dice_faces(p2_dice)}\n")
    else:
        print(error)


def dice_roll():
    game = False
    while True:

        if game == False:
            print(" 🎲🎲🎲 BENVENUTO/A AL GIOCO DEL LANCIO DEI DADI 🎲🎲🎲")
            dice_game()
            game = True

        else:
            again = input("\nVuoi giocare (play) o uscire (quit)? -> ").lower()
            match again:
                case "play":
                    game = True
                    dice_game()
                case "quit":
                    return
                case _:
                    print("Scelta non valida, cosa vuoi fare?")
                    input("PLAY o QUIT? -> ")

dice_roll()