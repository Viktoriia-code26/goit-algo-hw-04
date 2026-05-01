def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    save_contacts(contacts)
    return "Contact added."


def change_contact(args, contacts):
    name, new_phone = args

    if name not in contacts:
        return "Contact not found."

    contacts[name] = new_phone
    save_contacts(contacts)

    return "Contact updated."


def show_phone(args, contacts):
    name = args[0]

    if name in contacts:
        return contacts[name]

    return "Contact not found."


def show_all(args, contacts):
    if not contacts:
        return "No contacts found."

    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")


def get_contacts():
    contacts = {}

    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except FileNotFoundError:
        pass

    return contacts


def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.lower(), args


def main():
    print("Welcome to the assistant bot!")

    contacts = get_contacts()

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(args, contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()