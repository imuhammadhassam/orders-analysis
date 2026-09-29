import sqlite3

# Create database connection
conn = sqlite3.connect("orders.db")

cursor = conn.cursor()

# Create customers table
cursor.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

# Create orders table
cursor.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount INTEGER,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
)
""")

# Insert customers data
customers = [
    (1, "Ali", "Islamabad"),
    (2, "Sara", "Lahore"),
    (3, "Bilal", "Karachi"),
    (4, "Ayesha", "Islamabad"),
    (5, "Ahmed", "Lahore"),
    (6, "Zara", "Peshawar")
]

cursor.executemany(
    "INSERT INTO customers VALUES (?, ?, ?)",
    customers
)


# Insert orders data
orders = [
    (1,1,4500),
    (2,1,7200),
    (3,2,3000),
    (4,3,9800),
    (5,4,6500),
    (6,5,5500),
    (7,6,4000),
    (8,2,7000),
    (9,3,3000),
    (10,5,8000)
]

cursor.executemany(
    "INSERT INTO orders VALUES (?, ?, ?)",
    orders
)


conn.commit()

print("Database created successfully")

conn.close()