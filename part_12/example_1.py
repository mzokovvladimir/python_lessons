import sqlite3

DB_NAME = 'store.db'


def add_products(db_name: str, some_values: list[tuple]):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.executemany("""INSERT INTO Products (name, price, stock) VALUES (?, ?, ?)""", some_values)
    print("products added")
    conn.commit()
    conn.close()


def add_order(db_name: str, product_id: int, quantity: int):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Перевірка наявності товару
    cursor.execute("""SELECT price, stock FROM Products WHERE id = ?""", (product_id,))
    product = cursor.fetchone()

    if product is None:
        print("Товар не знайдено")
        conn.close()
        return

    price, stock = product

    if quantity > stock:
        print("Недостатньо товару на складі")
        conn.close()
        return

    total_price = price * quantity

    # Використання транзакції
    try:
        cursor.execute("BEGIN TRANSACTION")

        # Додаємо замовлення
        cursor.execute("INSERT INTO Orders (product_id, quantity, total_price) VALUES (?, ?, ?)",
                       (product_id, quantity, total_price))

        # Оновлюємо залишок товару
        cursor.execute("UPDATE Products SET stock = stock - ? WHERE id = ?", (quantity, product_id))

        conn.commit()
        print("Замовлення успішно оформлено")

    except Exception as e:
        conn.rollback()
        print("Помилка при оформленні замовлення:", e)

    conn.close()


def update_price(db_name: str, product_id: int, new_price: float):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""UPDATE Products SET price = ? WHERE id = ?""", (new_price, product_id))
    conn.commit()
    print(f"Ціна товару {product_id} оновлена!")
    conn.close()


def get_all_products(db_name: str=DB_NAME):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products ORDER BY price DESC")
    products = cursor.fetchall()

    conn.close()

    print("ID | Назва | Ціна | Кількість")
    for p in products:
        print(f"{p[0]} | {p[1]} | ${p[2]:.2f} | {p[3]} шт.")


def get_order_statistics(db_name: str):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(quantity) AS total_items_sold, SUM(total_price) AS total_revenue FROM Orders")
    stats = cursor.fetchone()

    conn.close()

    print(f"Загальна кількість проданих товарів: {stats[0]}")
    print(f"Сумарна виручка: ${stats[1]:.2f}")


class TotalRevenueAggregator:
    """Агрегатна функція для підрахунку загального прибутку від продажу товару."""

    def __init__(self):
        self.total_revenue = 0  # Ініціалізуємо накопичувач доходу

    def step(self, price, quantity):
        """Додає значення до накопичувача."""
        self.total_revenue += price * quantity

    def finalize(self):
        """Повертає остаточний підсумок."""
        return self.total_revenue


def calculate_total_revenue(db_name: str):
    """Функція для підключення до бази даних, реєстрації агрегатної функції та виконання запиту."""
    conn = sqlite3.connect(db_name)

    # Реєструємо агрегатну функцію в SQLite
    conn.create_aggregate("total_revenue_per_product", 2, TotalRevenueAggregator)

    # Використання агрегатної функції
    cursor = conn.cursor()
    cursor.execute("""
        SELECT product_id, total_revenue_per_product(price, quantity) 
        FROM Orders 
        JOIN Products ON Orders.product_id = Products.id 
        GROUP BY product_id
    """)
    results = cursor.fetchall()

    # Виводимо результати
    print("Доходи від продажу кожного товару:")
    for row in results:
        print(f"Товар ID {row[0]}: ${row[1]:.2f}")

    conn.close()
