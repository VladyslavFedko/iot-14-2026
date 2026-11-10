class Guest:
    def __init__(self, id: int, fullName: str, age: int, city: str, phone: str, gender: str):
        self.id = id
        self.fullName = fullName
        self.age = age
        self.city = city
        self.phone = phone
        self.gender = gender

    def check_phone_num(self):
        return self.phone.count('7') > 3 

class Party:
    def __init__(self, day: str, reason: str, guests: list):
        self.day = day
        self.reason = reason
        self.guests = guests

def findAvgAgeByGender(party: Party, gender: str):
    guests = party.guests
    count = 0
    sum = 0
    
    for guest in guests:
        if guest.gender == gender:
            count += 1
            sum += guest.age

    return round(sum / count, 1)

# AI test data
guests = [
    Guest(8, "Kateryna Melnyk", 27, "Ternopil", "+380681234567", "female"),
    Guest(4, "Anna Tkachuk", 29, "Kharkiv", "+380677712345", "female"),
    Guest(7, "Maksym Shevchenko", 31, "Zaporizhzhia", "+380997777777", "male"), 
    Guest(1, "Oleksandr Ivanov", 28, "Kyiv", "+380671234567", "male"),
    Guest(2, "Mariia Kovalenko", 34, "Lviv", "+380777771234", "female"),    
    Guest(9, "Andrii Lysenko", 35, "Ivano-Frankivsk", "+380931234567", "male"),
    Guest(3, "Ivan Petrenko", 22, "Odesa", "+380509876543", "male"),
    Guest(10, "Viktoriia Kravchenko", 30, "Zhytomyr", "+380977234567", "female"),
    Guest(5, "Dmytro Sydorenko", 41, "Dnipro", "+380971234777", "male"),    
    Guest(6, "Olena Boiko", 25, "Vinnytsia", "+380631112233", "female"),
]

guests.sort(key=lambda guest: guest.id )


print('Checking for lucky phone number')
for guest in guests:
    print(f'{guest.id:<3}\t{guest.fullName:<20}\t{str(guest.check_phone_num()):<5}')

party_1 = Party(1, 'test1', guests[:5])
party_2 = Party(2, 'test2', guests[-5:])

print('\nAvg age for males in party_1:', findAvgAgeByGender(party_1, 'male'))
print('Avg age for females in party_2:', findAvgAgeByGender(party_2, 'female'))
