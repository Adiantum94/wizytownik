from faker import Faker
fake = Faker()


class Contact:
   def __init__(self, name, last_name, email):
       self.name = name
       self.last_name = last_name
       self.email = email

       self._label_lenght = len(self.name) + len(self.last_name) +1

   def __str__(self):
    return f'{self.name} {self.last_name} {self.email}'

   def contact(self):
       print(f"Kontaktuję się z {self.name} {self.last_name} {self.email}")

   @property
   def label_lenght(self):
      print(self._label_lenght)
   @label_lenght.setter
   def label_lenght(self, value):
    if value >= len(self.name) + len(self.last_name) +1:
        self._label_lenght = value
    else:
        raise ValueError(f"Value: {value} is less than the length of the first and last names: {len(self.name) + len(self.last_name) +1}")

class BaseContact(Contact):
   def __init__(self, phone, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.phone = phone
   def __str__(self):
    return f'{self.name} {self.last_name} {self.email} {self.phone}'   

   def contact(self):
       print(f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.last_name}")

class BusinessContact(Contact):
   def __init__(self, company, occupation, business_phone, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.business_phone = business_phone
       self.company = company
       self.occupation = occupation
   def __str__(self):
    return f'{self.name} {self.last_name} {self.email} {self.company} {self.occupation} {self.business_phone}'    

   def contact(self):
       print(f"Wybieram numer {self.business_phone} i dzwonię do {self.name} {self.last_name}")

def create_contacts(card_type, amount):
   for person in range(amount):
       if card_type == 'business':
           person= BusinessContact(name=fake.first_name(), last_name=fake.last_name(), email= fake.free_email(), company= fake.company(), occupation = fake.job(), business_phone = fake.phone_number())
           print(person)
           person.contact()
           person.label_lenght
       elif card_type == 'base':
           person= BaseContact(name=fake.first_name(), last_name=fake.last_name(), email= fake.free_email(), phone = fake.phone_number())
           print(person)
           person.contact()
           person.label_lenght



