# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")

# STEP 2
# Select employee number and last name for all employees

df_first_five = pd.read_sql(
    """
    SELECT employeeNumber, lastName
    FROM employees
    """,
    conn,
)

# STEP 3
# Repeat Step 2 with the columns reversed

df_five_reverse = pd.read_sql(
    """
    SELECT lastName, employeeNumber
    FROM employees
    """,
    conn,
)

# STEP 4
# Alias the employee number column as ID

df_alias = pd.read_sql(
    """
    SELECT lastName, employeeNumber AS ID
    FROM employees
    """,
    conn,
)

# STEP 5
# Create a role column using a CASE expression

df_executive = pd.read_sql(
    """
    SELECT
        employeeNumber,
        lastName,
        jobTitle,
        CASE
            WHEN jobTitle IN ('President', 'VP Sales', 'VP Marketing') THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
    """,
    conn,
)

# STEP 6
# Find the length of each employee's last name

df_name_length = pd.read_sql(
    """
    SELECT LENGTH(lastName) AS name_length
    FROM employees
    """,
    conn,
)

# STEP 7
# Return the first two letters of each job title

df_short_title = pd.read_sql(
    """
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
    """,
    conn,
)

# STEP 8
# Sum the rounded total price for each order
sum_total_price = pd.read_sql(
    """
    SELECT ROUND(priceEach * quantityOrdered, 2) AS total_price
    FROM orderDetails
    """,
    conn,
).sum()

# STEP 9
# Return the order date split into day, month, and year components

df_day_month_year = pd.read_sql(
    """
    SELECT
        orderDate,
        strftime('%d', orderDate) AS day,
        strftime('%m', orderDate) AS month,
        strftime('%Y', orderDate) AS year
    FROM orderDetails
    """,
    conn,
)