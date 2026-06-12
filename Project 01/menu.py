# I have to make an Menu of the Project 
# 1. Number Guessing Game
# 2. View History
# 3. Leaderboard
# 4. Exit
name = input("Enter your name: ")
number_guessing_game(name) # type: ignore
def menu(name):
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Play Game")
        print("2. View My History")
        print("3. Leaderboard")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            play_game(name)     # type: ignore
        elif choice == "2":
            view_history(name) # type: ignore
        elif choice == "3":
            leaderboard()      # type: ignore
        elif choice == "4":
            print("Goodbye!")
            break