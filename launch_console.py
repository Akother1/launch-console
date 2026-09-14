print("Welcome to the Launch Console!")

name = input("What is your name? ")
print(f"Hi, {name}! Welcome to my Launch Console.")

running = True

while running:
    print("\nMenu")
    print("1. About me")
    print("2. My goals")
    print("3. Favorite project")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print(f"My name is Aryav. I enjoy computer science, robotics, and learning about new technology.")

    elif choice == "2":
        print("My goals are to improve my programming skills, study computer science, and build useful technology.")

    elif choice == "3":
        print("One of my favorite projects is working on robots for FIRST Robotics Competition.")

    elif choice == "4":
        print(f"Goodbye, {name}! Thanks for using the Launch Console.")
        running = False

    else:
        print("Please enter 1, 2, 3, or 4.")