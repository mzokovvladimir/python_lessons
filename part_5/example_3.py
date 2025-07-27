class InsufficientFundsError(Exception):
    """
    Кастомний клас-вийняток для обробки помилок недостатнього балансу.
    """

    def __init__(self, balance, amount):
        super().__init__(f"Недостатньо коштів: ваш баланс {balance}, а ви намагаєтеся зняти {amount}.")
        self.balance = balance
        self.amount = amount


class BankAccount:
    """
    Клас для моделювання банківського рахунку.
    """

    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount: float):
        """
        Додає кошти на рахунок.
        """
        if amount <= 0:
            raise ValueError("Сума поповнення має бути більше нуля.")
        self.balance += amount
        print(f"Поповнення: ваш новий баланс {self.balance:.2f} грн.")

    def withdraw(self, amount: float):
        """
        Знімає кошти з рахунку, якщо баланс достатній.
        """
        if amount <= 0:
            raise ValueError("Сума зняття має бути більше нуля.")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Зняття: ваш новий баланс {self.balance:.2f} грн.")

    def __str__(self):
        return f"Рахунок власника {self.owner}: баланс {self.balance:.2f} грн."


try:
    account = BankAccount("Олександр", 1000.0)
    print(account)

    account.deposit(500.0)
    account.withdraw(2000.0)

except InsufficientFundsError as e:
    print(f"Помилка: {e}")
except ValueError as e:
    print(f"Помилка: {e}")
else:
    print("Усі операції виконані успішно.")
finally:
    print("Дякуємо за використання нашого банківського сервісу.")
