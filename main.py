
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

    phone_book = []

    def __init__(self, name):
        self.name = name

    def add_contact(self, name, surname, phone_number, **kwargs):
        contact = Contact(name, surname, phone_number, **kwargs)
        self.phone_book.append(contact)
        return self.phone_book

    def display_contacts(self):
        for contact in self.phone_book:
            print(contact)

    def delete_contact(self, phone_number):
        for person in self.phone_book:
            if person.phone_number == phone_number:
                self.phone_book.remove(person)
        return self.phone_book

    def chosen_contact_search(self):
        chosen_contact_list = list()
        for person in self.phone_book:
            chosen_contact_list.append(person.chosen_contact)
        for contact in chosen_contact_list:
            print(contact)

    def find_contact_by_name_surname(self, name, surname):
        find_contact_by_name_surname_list = list()
        for person in self.phone_book:
            if person.name == name and person.surname == surname:
                find_contact_by_name_surname_list.append(person)
        for contact in find_contact_by_name_surname_list:
            print(contact)



person_1 = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
person_2 = Contact('Иван', 'Федоров', '+71234561015', telegram='@ivan', email='ivan@fedorov.com')

phonebook = PhoneBook("Коллеги")
phonebook.add_contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
phonebook.add_contact('Иван', 'Федоров', '+71234561015', telegram='@ivan', email='ivan@fedorov.com')
phonebook.display_contacts()
phonebook.delete_contact('+71234567809')
phonebook.display_contacts()
phonebook.chosen_contact_search()
phonebook.find_contact_by_name_surname('Иван', 'Федоров')
