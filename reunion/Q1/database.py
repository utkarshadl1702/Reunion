import random
import faker
import sqlite3
from datetime import datetime, timedelta

# Initialize faker for generating random data
fake = faker.Faker()

# Connect to the database
conn = sqlite3.connect('ecommerce_db.sqlite')
cursor = conn.cursor()

# Create the Customers table
cursor.execute('''
    CREATE TABLE Customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT,
        contact_number TEXT,
        email TEXT
    )
''')

# Create the Products table
cursor.execute('''
    CREATE TABLE Products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT
    )
''')

# Create the Variants table
cursor.execute('''
    CREATE TABLE Variants (
        variant_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        variant_name TEXT,
        FOREIGN KEY (product_id) REFERENCES Products(product_id)
    )
''')

# Create the Orders table
cursor.execute('''
    CREATE TABLE Orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        order_date DATE,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
''')

# Create the Prices table
cursor.execute('''
    CREATE TABLE Prices (
        price_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        variant_id INTEGER,
        price REAL,
        start_date DATE,
        end_date DATE,
        FOREIGN KEY (product_id) REFERENCES Products(product_id),
        FOREIGN KEY (variant_id) REFERENCES Variants(variant_id)
    )
''')

# Create the Addresses table
cursor.execute('''
    CREATE TABLE Addresses (
        address_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        shipping_address TEXT,
        city TEXT,
        state TEXT,
        postal_code TEXT,
        start_date DATE,
        end_date DATE,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
''')

# Helper function to generate random date within a range
def random_date(start_date, end_date):
    time_delta = end_date - start_date
    random_days = random.randint(0, time_delta.days)
    return start_date + timedelta(days=random_days)

# Generate sample data for Customers table
for _ in range(10):
    cursor.execute('INSERT INTO Customers (customer_name, contact_number, email) VALUES (?, ?, ?)',
                   (fake.name(), fake.phone_number(), fake.email()))

# Generate sample data for Products table
products = [("Product A",), ("Product B",), ("Product C",), ("Product D",), ("Product E",)]
cursor.executemany('INSERT INTO Products (product_name) VALUES (?)', products)

# Generate sample data for Variants table
variants = [("Product A Variant 1", 1), ("Product A Variant 2", 1), ("Product B Variant 1", 2)]
cursor.executemany('INSERT INTO Variants (variant_name, product_id) VALUES (?, ?)', variants)

# Generate sample data for Orders table (2 years of history)
start_date = datetime(2021, 1, 1)
end_date = datetime(2023, 7, 28)
for _ in range(200):  # Assuming 100 orders per year
    order_date = random_date(start_date, end_date)
    cursor.execute('INSERT INTO Orders (customer_id, order_date) VALUES (?, ?)',
                   (random.randint(1, 10), order_date))

# Generate sample data for Prices table
for product_id in range(1, 6):
    for variant_id in [None, 1, 2]:
        start_date = datetime(2021, 1, 1)
        for _ in range(24):  # Monthly prices for 2 years
            end_date = start_date.replace(day=1, month=start_date.month % 12 + 1, year=start_date.year + start_date.month // 12)
            price = round(random.uniform(10, 1000), 2)
            cursor.execute('INSERT INTO Prices (product_id, variant_id, price, start_date, end_date) VALUES (?, ?, ?, ?, ?)',
                           (product_id, variant_id, price, start_date, end_date))
            start_date = end_date

# Generate sample data for Addresses table
for customer_id in range(1, 11):
    start_date = datetime(2021, 1, 1)
    for _ in range(24):  # Monthly address changes for 2 years
        end_date = start_date.replace(day=1, month=start_date.month % 12 + 1, year=start_date.year + start_date.month // 12)
        shipping_address = fake.address()
        city = fake.city()
        state = fake.state()
        postal_code = fake.zipcode()
        cursor.execute('INSERT INTO Addresses (customer_id, shipping_address, city, state, postal_code, start_date, end_date) VALUES (?, ?, ?, ?, ?, ?, ?)',
                       (customer_id, shipping_address, city, state, postal_code, start_date, end_date))
        start_date = end_date

# Commit changes and close the connection
conn.commit()
conn.close()
