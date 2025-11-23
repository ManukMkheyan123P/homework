import random
import smtplib
import string
from datetime import datetime, timedelta
from typing import Optional


class BankUser:
    def __init__(self, name, surname, age, salary, money, pin):

        if not (name.isalpha() and surname.isalpha()
                and age.isdigit() and salary.isdigit()
                and money.isdigit() and pin.isdigit()):
            raise ValueError("Incorrect user data")

        self.name = name
        self.surname = surname
        self.age = int(age)
        self.salary = int(salary)
        self.money = int(money)
        self.pin = int(pin)

    def gmail_name(self, gmail):
        if "@" in gmail and "." in gmail and gmail.index("@") < gmail.rindex("."):
            self.gmail = gmail
        else:
            raise ValueError("Invalid gmail address")

    def set_card_number(self, card_number: str):
        if not isinstance(card_number, str):
            raise ValueError("Invalid card number")

        cleaned = card_number.replace(" ", "").replace("-", "")

        if not (cleaned.isdigit() and len(cleaned) == 16):
            raise ValueError("Invalid card number, card number must be 16 digits")

        if not self._luhn_check(cleaned):
            raise ValueError("Invalid card number, card number must be 16 digits")
        self.card_number = cleaned
        return True

    def _luhn_check(digits: str) -> bool:
        total = 0

        reversed_digits = digits[::-1]
        for i, ch in enumerate(reversed_digits):
            d = int(ch)
            if i % 2 == 1:
                d = d * 2
                if d > 9:
                    d -= 9
            total += d
        return total % 10 == 0

    def _check_access(self):
        if self.__blocked:
            raise PermissionError("Account is blocked due to 3 incorrect PIN attempts.")

    def check_pin(self, pin):
        if self.__blocked:
            raise PermissionError("Account is blocked due to 3 incorrect PIN attempts.")

        if pin != self.__pin:
            self.__attempts += 1
            if self.__attempts >= 3:
                self.__blocked = True
                raise PermissionError("PIN incorrect 3 times. Account blocked.")
            raise ValueError("Incorrect PIN")
        else:
            self.__attempts = 0
            return True

CHATGPTcode
# class BankUser:
#     def __init__(self, name, surname, age, salary, money, pin):
#
#         if not (name.isalpha() and surname.isalpha()
#                 and age.isdigit() and salary.isdigit()
#                 and money.isdigit() and pin.isdigit()):
#             raise ValueError("Incorrect user data")
#
#         # защищённые данные
#         self._name = name
#         self._surname = surname
#         self._age = int(age)
#         self._salary = int(salary)
#
#         # скрытые данные
#         self.__money = int(money)
#         self.__pin = pin
#         self.__card_number = None
#
#         # доп. параметры
#         self.__blocked = False
#         self.__attempts = 0
#         self.__email = None
#
#     def gmail_name(self, gmail):
#         if "@" in gmail and "." in gmail and gmail.index("@") < gmail.rindex("."):
#             self.__email = gmail
#         else:
#             raise ValueError("Invalid gmail address")
#
#     def set_card_number(self, card_number: str):
#         if not isinstance(card_number, str):
#             raise ValueError("Invalid card number")
#
#         cleaned = card_number.replace(" ", "").replace("-", "")
#
#         if not (cleaned.isdigit() and len(cleaned) == 16):
#             raise ValueError("Invalid card number, card number must be 16 digits")
#
#         if not self._luhn_check(cleaned):
#             raise ValueError("Invalid card number (failed Luhn check)")
#
#         self.__card_number = cleaned
#         return True
#
#     def _luhn_check(self, digits: str) -> bool:   # ← добавил self
#         total = 0
#         reversed_digits = digits[::-1]
#
#         for i, ch in enumerate(reversed_digits):
#             d = int(ch)
#             if i % 2 == 1:
#                 d *= 2
#                 if d > 9:
#                     d -= 9
#             total += d
#
#         return total % 10 == 0
#
#     # ---------- НИЖЕ ПРОДОЛЖЕНИЕ ТВОЕГО КОДА ----------
#
#     def _check_access(self):
#         """ Запрещает доступ, если аккаунт заблокирован """
#         if self.__blocked:
#             raise PermissionError("Account is blocked due to 3 incorrect PIN attempts.")
#
#     def _check_pin(self, pin):
#         """ Проверка PIN """
#         if self.__blocked:
#             raise PermissionError("Account blocked. Restore access first.")
#
#         if pin != self.__pin:
#             self.__attempts += 1
#             if self.__attempts >= 3:
#                 self.__blocked = True
#                 raise PermissionError("PIN incorrect 3 times. Account blocked.")
#             raise ValueError("Incorrect PIN")
#         else:
#             self.__attempts = 0
#             return True
#
#     def get_full_name(self):
#         """ Возвращает имя и фамилию """
#         self._check_access()
#         return f"{self._name} {self._surname}"
#
#     def get_card_info(self, pin):
#         """ Возвращает номер карты и деньги """
#         self._check_access()
#         self._check_pin(pin)
#
#         hidden = self.__card_number[:4] + " **** **** " + self.__card_number[-4:]
#         return hidden, self.__money
#
#     def deposit(self, amount, pin):
#         """ Добавить деньги """
#         self._check_access()
#         self._check_pin(pin)
#
#         if amount <= 0:
#             raise ValueError("Amount must be positive")
#
#         self.__money += amount
#         return self.__money
#
#     def withdraw(self, amount, pin):
#         """ Снять деньги """
#         self._check_access()
#         self._check_pin(pin)
#
#         if amount <= 0:
#             raise ValueError("Amount must be positive")
#         if amount > self.__money:
#             raise ValueError("Not enough money")
#
#         self.__money -= amount
#         return self.__money
#
#     def restore_access(self, code, sent_code):
#         """ Восстановление через e-mail """
#         if code == sent_code:
#             self.__blocked = False
#             self.__attempts = 0
#             return True
#         else:
#             raise ValueError("Incorrect restore code")



















