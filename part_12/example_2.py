import sqlite3
from example_1 import DB_NAME, add_products, add_order, update_price, get_all_products, get_order_statistics, calculate_total_revenue


products = [
    ('Ноутбук', 1500.00, 10),
    ('Смартфон', 800.00, 15),
    ('Планшет', 600.00, 8),
    ('Монітор', 300.00, 12),
    ('Миша', 50.00, 30)
]
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Створення таблиці товарів
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
);
""")

# Створення таблиці замовлень
cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    total_price REAL NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products (id)
);
""")

conn.commit()

add_products(DB_NAME, products)
add_order(DB_NAME, 1, 2)
add_order(DB_NAME, 2, 3)
update_price(DB_NAME, 2, 750.00)

get_all_products(DB_NAME)
get_order_statistics(DB_NAME)
calculate_total_revenue(DB_NAME)
conn.close()
