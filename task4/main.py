def parse_input(user_input):
    # Розділяємо введений рядок на команду та аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()  # Приводимо команду до нижнього регістру
    return cmd, *args

def add_contact(args, contacts):
    # Додаємо новий контакт
    if len(args) != 2:
        return "Invalid command. Please provide both name and phone number."
    name, phone = args       # список args із 2 рядкових значень розпаковується в 2 змінні: name (ім'я) і phone (номер телефону).
    contacts[name] = phone   # додаємо пару ключ значення  ключ(name): значення(phone)
    return "Contact added."

def change_contact(args, contacts):
    # Змінюємо номер телефону існуючого контакту
    if len(args) != 2:
        return "Invalid command. Please provide both name and new phone number."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return f"Contact with name {name} not found."

def show_phone(args, contacts):
    # Показуємо номер телефону для конкретного контакту
    if len(args) != 1:
        return "Invalid command. Please provide a name."
    name = args[0]
    if name in contacts:
        return contacts[name]
    return f"Contact with name {name} not found."

def show_all(contacts):
    # Виводимо всі контакти
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return "No contacts found."

def main():
    contacts = {}  # Зберігаємо контакти в словнику
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

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
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
