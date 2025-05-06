def tasks_list(tasks):
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def todo_list_app():
    print("\n ⭐⭐⭐ Benvenuto/a nella ToDo List ⭐⭐⭐")
    tasks = []

    while True:
        print("\n ----> Menù Principale <----")
        print("\n1. ➕ Aggiungi una Nuova Task")
        print("2. ❌ Rimuovi una Task")
        print("3. 🏃🏻 Esci")

        choice = input("Cosa vuoi fare? Scegli tra (1/2/3): ")

        if choice == "1":
            while True:
                print("🖋️ Digita la tua task")
                print("Oppure digita 'MENU' per tornare al 🏠 menu principale o 'ESCI' per uscire dall'app")
                task = input()
                if task.lower() == "menu":
                    break
                elif task.lower() == "esci":
                    return
                else:
                    tasks.append(task)
                    print("Task Aggiunta ✅")

        elif choice == "2":
            while True:
                if tasks:
                    print("\n 📝 Sotto la lista delle tue tasks aggiornata:")
                    tasks_list(tasks)
                else:
                    print("\n 🤷🏻 La lista è vuota digita 1 per inserire una nuova task")
                    break
                task = input("\n 🤔 Quale task vuoi rimuovere? - Se vuoi tornare al menu principale digita 'MENU' -> ")
                if task.lower() == "menu":
                    break
                tasks.pop()
                print("Task Rimossa ❌")

        elif choice == "3":
            print(" 🫂 Grazie per aver utilizzato TODO List!")
            break

        else:
            print("🚫 Scelta non valida")

        if tasks:
            print("\n\n 📝 Lista delle tue tasks:")
            tasks_list(tasks)

todo_list_app()