import random
import time
from datetime import datetime

PLAYERS_FILE = "players.txt"
HISTORY_FILE = "history.txt"


# ---------------- LOAD / SAVE PLAYERS ----------------
def load_players():
    try:
        with open(PLAYERS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except:
        return []


def save_player(name):
    players = load_players()

    if name not in players:
        with open(PLAYERS_FILE, "a") as file:
            file.write(name + "\n")


# ---------------- LOGIN SYSTEM ----------------
def login():
    while True:
        name = input("Enter your name: ").strip()

        if name == "":
            print("Name cannot be empty!")
            continue

        players = load_players()

        if name in players:
            print(f"\nWelcome back, {name}! 🎮")
        else:
            print(f"\nNew Player Registered: {name} 🎉")
            save_player(name)

        return name


# ---------------- GAME ----------------
def play_game(name):
    print("\nSelect Difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")

    while True:
        choice = input("Enter choice: ")

        if choice == "1":
            max_num = 50
            level = "Easy"
            break
        elif choice == "2":
            max_num = 100
            level = "Medium"
            break
        elif choice == "3":
            max_num = 500
            level = "Hard"
            break
        else:
            print("Invalid choice!")

    secret = random.randint(1, max_num)
    attempts = 0
    start_time = time.time()

    print(f"\nGuess the number between 1 and {max_num}")

    while True:
        try:
            guess = int(input("Enter guess: "))

            if guess < 1 or guess > max_num:
                print("Out of range!")
                continue

        except:
            print("Invalid input!")
            continue

        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            end_time = time.time()
            total_time = round(end_time - start_time, 2)

            print("\n🎉 YOU WON!")
            print(f"Attempts: {attempts}")
            print(f"Time: {total_time} sec")

            save_history(name, level, attempts, total_time)
            break


# ---------------- SAVE HISTORY ----------------
def save_history(name, level, attempts, time_taken):
    date = datetime.now().strftime("%Y-%m-%d")

    with open(HISTORY_FILE, "a") as file:
        file.write(f"{name},{level},{attempts},{time_taken},{date}\n")


# ---------------- VIEW HISTORY ----------------
def view_history(name):
    print("\n===== YOUR HISTORY =====")

    try:
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()

        found = False

        for line in lines:
            data = line.strip().split(",")

            if data[0] == name:
                print(f"Level: {data[1]} | Attempts: {data[2]} | Time: {data[3]} sec | Date: {data[4]}")
                found = True

        if not found:
            print("No history found!")

    except:
        print("No history file found!")


# ---------------- LEADERBOARD ----------------
def leaderboard():
    print("\n===== LEADERBOARD =====")

    try:
        with open(HISTORY_FILE, "r") as file:
            data = file.readlines()

        records = []

        for line in data:
            name, level, attempts, time_taken, date = line.strip().split(",")

            records.append((name, int(attempts), float(time_taken)))

        records.sort(key=lambda x: (x[1], x[2]))

        rank = 1
        for r in records[:10]:
            print(f"{rank}. {r[0]} | Attempts: {r[1]} | Time: {r[2]}")
            rank += 1

    except:
        print("No data available!")


# ---------------- MENU ----------------
def menu(name):
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Play Game")
        print("2. View My History")
        print("3. Leaderboard")
        print("4. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            play_game(name)
        elif choice == "2":
            view_history(name)
        elif choice == "3":
            leaderboard()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


# ---------------- MAIN ----------------
def main():
    print("====================================")
    print("    NUMBER GUESSING GAME PROJECT    ")
    print("====================================")

    name = login()
    menu(name)


main()