from datetime import datetime, timedelta, date
import random

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date):
    return date.strftime("%Y.%m.%d")

def prepare_user_list(user_data):
    user_data_new = user_data.copy()
    for user in user_data_new:
        user.update({"birthday": string_to_date(user['birthday'])})
    return user_data_new

def find_next_weekday(start_date, weekday=0):
    start_weekday = start_date.weekday()
    days_ahead = weekday - start_weekday
    if days_ahead <= 0:
        days_ahead = days_ahead + 7
    future = start_date + timedelta(days=days_ahead)
    return future


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = user["birthday"].replace(year=today.year + 1)
        dif = (birthday_this_year - today).days
        if dif >= 0 and dif <= 7:
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": date_to_string(adjust_for_weekend(birthday_this_year))})

    return upcoming_birthdays


def adjust_for_weekend(birthday):
    if birthday.weekday() == 5 or birthday.weekday() == 6:
        return find_next_weekday(birthday)
    return birthday

users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

'''print(get_upcoming_birthdays(prepare_user_list(users)))'''

def get_days_from_today(date: str) -> int | str:
    """
        Функція обчислює кількість днів між заданою датою та поточною датою.

        :param date: рядок у форматі 'YYYY-MM-DD'
        :return: ціле число (може бути від'ємним), що вказує різницю у днях
        """
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        return given_date.toordinal() - today.toordinal()
    except ValueError:
        return f"Помилка: '{date}' не відповідає формату 'YYYY-MM-DD'."

print(get_days_from_today("2025-094-18"))

def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list[int]:
    """
    Функція повертає випадковий набір чисел у межах заданих параметрів.

    :param min_value: мінімальне можливе число у наборі (не менше 1)
    :param max_value: максимальне можливе число у наборі (не більше 1000)
    :param quantity: кількість чисел, які потрібно вибрати (значення між min і max)
    :return: список цілих чисел, відсортований без повторів, або порожній список при некоректних параметрах
    """

    if min_value < 1:
        return []
    if max_value > 1000:
        return []
    if quantity > (max_value - min_value + 1):
        return []

    res = random.sample(range(min_value, max_value + 1), quantity)
    res.sort()
    return res

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
''