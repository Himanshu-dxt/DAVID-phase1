from david_memory import add_to_memory, get_from_memory

def main():
    print("Hello, I am DAVID - your AI buddy!💡")


    while True:
        user_input = input("\nYou: ").strip().lower()

        if user_input == "exit":
            print("DAVID: GoodBye! Stay Smart Sir!")
            break

        elif user_input.startswith("remember"):
            try:

                _, key, value = user_input.split(" ", 2)
                add_to_memory(key, value)
                print(f"DAVID: Got it! I'll remember that {key} is {value}.")
            except ValueError:
                print("DAVID: Use this format - remember [key] [value]")

        elif user_input.startswith("recall"):
            try:

                _, key = user_input.split(" ", 1)
                value = get_from_memory(key)
                print(f"DAVID: You told me {key} is {value}.")
            except ValueError:
                print("DAVID: Use this formal - recall [key]")

        else:
            print("DAVID: I'm still learning how to respond to that!!")


if __name__ == "__main__":
    main()