"""
Додати enum gender: FEMALE, MALE, NON_BINARY, …. 
Створити клас Guest( id, name, age, city, phone number). 
Додати клас Party (day, reason), на яку прийде певна кількість гостей guests. 
Додати функцію findAverageAge( Guest*, gender) - знайти середній вік гостей за статтю. Додати метод визначення, чи номер телефону є щасливий isLuckyPhoneNumber (якщо більше, ніж три сімки - True).  
Посортуйте гостей за номером id.
"""

from enum import Enum

class Gender(Enum):
    FEMALE = "Female"
    MALE = "Male"
    NON_BINARY = "Non-binary"
    OTHER = "Other"

class Guest:
    def __init__(self, id: int, fullName: str, age: int, city: str, phone: str, gender: Gender):
        self.id = id
        self.fullName = fullName
        self.age = age
        self.city = city
        self.phone = phone
        self.gender = gender

    def check_phone_num(self):
        return self.phone.count('7') > 3 

class Party:
    def __init__(self, day: str, reason: str, guests: list[Guest]):
        self.day = day
        self.reason = reason
        self.guests = guests

def findAvgAgeByGender(party: Party, gender: Gender) -> float:
    guests = party.guests
    matching_ages = [guest.age for guest in guests if guest.gender == gender]
    
    if not matching_ages:
        return 0.0
    
    return round(sum(matching_ages) / len(matching_ages), 1)

# AI test data
guests = [
    Guest(8, "Kateryna Melnyk", 27, "Ternopil", "+380681234567", Gender.FEMALE),
    Guest(4, "Anna Tkachuk", 29, "Kharkiv", "+380677712345", Gender.FEMALE),
    Guest(7, "Maksym Shevchenko", 31, "Zaporizhzhia", "+380997777777", Gender.MALE), 
    Guest(1, "Oleksandr Ivanov", 28, "Kyiv", "+380671234567", Gender.MALE),
    Guest(2, "Mariia Kovalenko", 34, "Lviv", "+380777771234", Gender.FEMALE),    
    Guest(9, "Andrii Lysenko", 35, "Ivano-Frankivsk", "+380931234567", Gender.MALE),
    Guest(3, "Ivan Petrenko", 22, "Odesa", "+380509876543", Gender.MALE),
    Guest(10, "Viktoriia Kravchenko", 30, "Zhytomyr", "+380977234567", Gender.FEMALE),
    Guest(5, "Dmytro Sydorenko", 41, "Dnipro", "+380971234777", Gender.MALE),    
    Guest(6, "Olena Boiko", 25, "Vinnytsia", "+380631112233", Gender.FEMALE),
]


guests.sort(key = lambda guest: guest.id )

print('Checking for lucky phone number')
for guest in guests:
    print(f'{guest.id:<3}\t{guest.fullName:<20}\t{str(guest.check_phone_num()):<5}')

party_1 = Party(1, 'test1', guests[:5])
party_2 = Party(2, 'test2', guests[-5:])

print('\nAvg age for males in party_1:', findAvgAgeByGender(party_1, Gender.MALE))
print('Avg age for females in party_2:', findAvgAgeByGender(party_2, Gender.FEMALE))