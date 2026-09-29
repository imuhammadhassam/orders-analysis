import sqlite3


# Connect database
conn = sqlite3.connect("orders.db")

cursor = conn.cursor()


# -----------------------------------
# 1. INNER JOIN QUERY
# -----------------------------------

print("\nCustomer orders (JOIN):")

cursor.execute("""
SELECT customers.name, orders.amount
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;
""")


for row in cursor.fetchall():
    print(row)



# -----------------------------------
# 2. GROUP BY SUM QUERY
# -----------------------------------

print("\nTotal spend per customer:")

cursor.execute("""
SELECT customers.name,
SUM(orders.amount) AS total_spent
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id
GROUP BY customers.name
ORDER BY total_spent DESC;
""")


for row in cursor.fetchall():
    print(row)



conn.close()