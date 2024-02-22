class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, first_name, last_name, phone, address):
        self.contacts[(first_name, last_name)] = {'phone': phone, 'address': address}

    def search_contact(self, first_name, last_name):
        return self.contacts.get((first_name, last_name), "Контакт не найден")

    def update_contact_by_name(self, name, new_phone=None, new_address=None):
        for key, value in self.contacts.items():
            if key[0] == name or key[1] == name:
                if new_phone:
                    value['phone'] = new_phone
                if new_address:
                    value['address'] = new_address
                print("Контакт успешно обновлен!")
                return
        print("Контакт не найден")

    def delete_contact_by_name(self, name):
        for key in list(self.contacts.keys()):
            if key[0] == name or key[1] == name:
                del self.contacts[key]
                print("Контакт успешно удален!")
                return
        print("Контакт не найден")


def update_data_by_name(phone_book):
    name = input("Введите имя или фамилию для обновления: ")
    new_phone = input("Введите новый номер телефона (нажмите Enter, если не хотите менять): ")
    new_address = input("Введите новый адрес (нажмите Enter, если не хотите менять): ")
    phone_book.update_contact_by_name(name, new_phone, new_address)


def delete_data_by_name(phone_book):
    name = input("Введите имя или фамилию для удаления: ")
    phone_book.delete_contact_by_name(name)


def main():
    phone_book = PhoneBook()

    while True:
        print("\n1. Добавить контакт")
        print("2. Поиск контакта")
        print("3. Обновить контакт")
        print("4. Удалить контакт")
        print("5. Вывести все контакты")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            first_name = input("Введите имя: ")
            last_name = input("Введите фамилию: ")
            phone = input("Введите номер телефона: ")
            address = input("Введите адрес: ")
            phone_book.add_contact(first_name, last_name, phone, address)
            print("Контакт успешно добавлен!")
        elif choice == "2":
            first_name = input("Введите имя для поиска: ")
            last_name = input("Введите фамилию для поиска: ")
            result = phone_book.search_contact(first_name, last_name)
            if result != "Контакт не найден":
                print(f"Телефон: {result['phone']}, Адрес: {result['address']}")
            else:
                print(result)
        elif choice == "3":
            update_data_by_name(phone_book)
        elif choice == "4":
            delete_data_by_name(phone_book)
        elif choice == "5":
            if phone_book.contacts:
                print("Телефонный справочник:")
                for name, info in phone_book.contacts.items():
                    print(f"Имя: {name[0]}, Фамилия: {name[1]}, Телефон: {info['phone']}, Адрес: {info['address']}")
            else:
                print("Справочник пуст")
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main()


    


