# Simple To-Do App - Made by Mahek

tasks = []

while True:
    print("\n--- My To-Do App ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Choose karo (1-4): ")

    if choice == "1":
        task = input("Task likho: ")
        tasks.append(task)
        print("Task add ho gaya!")

    elif choice == "2":
        if len(tasks) == 0:
            print("Abhi koi task nahi hai")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "3":
        num = int(input("Konsa number delete karna hai? "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            print("Delete ho gaya!")
        else:
            print("Ghalat number hai")

    elif choice == "4":
        print("Allah Hafiz! App band ho raha hai")
        break
    else:
        print("Sahi number likho 1-4 tak")
