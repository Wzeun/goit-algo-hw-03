import random

def get_numbers_ticket(min, max, quantity):
        if min < 1 or max >  1000 or quantity > max - min + 1:
            print("несправнi параметри!")
            return []
        numbers = set()
        while len(numbers) < quantity:
            num = random.randint(min, max)
            numbers.add(num)
        return sorted(numbers)


print(get_numbers_ticket(3, 100, 5))