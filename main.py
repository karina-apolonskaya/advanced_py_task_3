
class Contact:

    def __init__(self, name, surname, phone_number, **info_additional):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.chosen_contact = False
        self.info_additional = info_additional

    def get_modified_contact(self):
        add_info = list()
        str_out = '\nДополнительная информация:'
        info = f"Имя: {self.name} " \
               f"\nФамилия: {self.surname} " \
               f"\nТелефонный номер: {self.phone_number}" \
               f"\nВ избранных: {self.chosen_contact}"
        for add_info_name, add_info_value in self.info_additional.items():
            add_info.append(f"{add_info_name} : {add_info_value}")
        for item in add_info:
            str_out += '\n\t\t\t' + item
        final_info = info + str_out
        return final_info

    def __str__(self):
        return self.get_modified_contact()


class PhoneBook:

    phone_book = list()

    def __init__(self, name):
        self.name = name

    def add_contact(self, contact):
        contact_added = {"Имя": contact.name, "Фамилия": contact.surname,
                         "Телефонный номер": contact.phone_number,
                         "Избранный контакт": contact.chosen_contact,
                         "Дополнительная информация": contact.info_additional}
        self.phone_book.append(contact_added)
        return self.phone_book

    def display_contacts(self):
        return self.phone_book

    def delete_contact(self, phone_number):
        for item in self.phone_book:
            if item["Телефонный номер"] == phone_number:
                self.phone_book.remove(item)
        return self.phone_book

    def chosen_contact_search(self):
        chosen_contact_list = list()
        for item in self.phone_book:
            chosen_contact_list.append(item["Избранный контакт"])
        return chosen_contact_list

    def find_contact_by_name_surname(self, name, surname):
        find_contact_by_name_surname_list = list()
        for item in self.phone_book:
            if item["Имя"] == name and item["Фамилия"] == surname:
                find_contact_by_name_surname_list.append(item)
        return find_contact_by_name_surname_list


person_1 = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
person_2 = Contact('Иван', 'Федоров', '+71234561015', telegram='@ivan', email='ivan@fedorov.com')
print(person_1)
print(person_2)
phonebook = PhoneBook("Коллеги")
print(phonebook.add_contact(person_1))
print(phonebook.add_contact(person_2))
print(phonebook.display_contacts())
print(phonebook.delete_contact('+71234567809'))
print(phonebook.chosen_contact_search())
print(phonebook.find_contact_by_name_surname("Иван", "Федоров"))



