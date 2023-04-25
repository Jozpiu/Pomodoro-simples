import time

def pomodoro_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Pomodoro completed!\n")

def main():
    pomodoro_count = 0
    while True:
        print("Pomodoro Timer")
        print("1. Start Pomodoro")
        print("2. Exit")
        option = input("Enter your choice: ")
        if option == "1":
            pomodoro_count += 1
            print(f"\nStarting Pomodoro {pomodoro_count}")
            pomodoro_timer(25)
            print("Pomodoro finished. Take a break!")
            break_time = input("Press Enter to start a 5 minute break: ")
            pomodoro_timer(5)
            print("Break finished. Get back to work!\n")
        elif option == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
