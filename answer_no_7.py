import sqlite3

# Connect to the database
conn = sqlite3.connect('mall_vouchers.db')
c = conn.cursor()

# Get the voucher code from the user
voucher_code = input('Enter your voucher code: ')

# Check if the voucher is valid and has not expired
c.execute('SELECT * FROM Vouchers WHERE code=? AND redeemed=0 AND expiry_date>=date()',
          (voucher_code,))
voucher = c.fetchone()

if voucher:
    # Get the customer information
    c.execute('SELECT * FROM Customers WHERE id=?', (voucher[1],))
    customer = c.fetchone()

    # Get the transaction information
    transaction_amount = int(input('Enter your transaction amount: '))
    transaction_date = input('Enter the transaction date (YYYY-MM-DD): ')

    # Add the transaction to the database
    c.execute('INSERT INTO Transactions (customer_id, amount, date) VALUES (?, ?, ?)',
              (voucher[1], transaction_amount, transaction_date))
    transaction_id = c.lastrowid

    # Mark the voucher as redeemed
    c.execute('UPDATE Vouchers SET redeemed=1 WHERE code=?', (voucher_code,))

    # Calculate the total amount and discount
    total_amount = transaction_amount - 10000
    discount = 10000

    # Print the receipt
    print('Transaction ID:', transaction_id)
    print('Customer Name:', customer[1])
    print('Transaction Amount:', transaction_amount)
    print('Discount:', discount)
    print('Total Amount:', total_amount)

    # Commit the changes to the database
    conn.commit()
else:
    print('Invalid voucher code or voucher has already been redeemed or expired.')

# Close the database connection
conn.close()
