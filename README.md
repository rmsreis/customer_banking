# Customer Banking System

This repository contains a simple customer banking system to manage Savings and CD (Certificate of Deposit) accounts. It allows users to input account details, calculate interest, and update balances accordingly.

## Modules

1. **accounts.py**: Defines the `Account` class with methods to set balance, set interest rate, calculate interest, and update balance with interest.

2. **savings_account.py**: Contains the `create_savings_account` function that creates a savings account, calculates interest earned, and updates the account balance.

3. **cd_account.py**: Contains the `create_cd_account` function that creates a CD account, calculates interest earned, and updates the account balance.

4. **customer_banking.py**: Main script that interacts with the user, prompts for account details, and displays the updated balances and interest earned.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/customer-banking-system.git
   cd customer-banking-system

2. **Ensure Python is installed:**
This project requires Python 3.x. You can check your Python version using:
    ```bash
    python --version

## Usage


1. **Run the Main Script:**
    ```bash
    python customer_banking.py

This will start the program, and you will be prompted to enter the initial balance, interest rate, and the number of months for both Savings and CD accounts.

## Example

Here is an example of how to use the system:

1. **Running the Script:**
    ``bash
    python customer_banking.py

2. **User Input:**
<pre style="color:white">

Welcome to Customer Banking

<span style="color:lightblue">Enter the initial balance for the Savings Account:</span> 1000

<span style="color:green"> Enter the annual interest rate (APR) for the Savings Account:</span> 5

<span style="color:blue">Enter the number of months the savings account will accrue interest:</span> 12

Savings Account Updated Balance: 1051.16, Interest Earned: 51.16

Enter the initial balance for the CD Account: 2000
Enter the annual interest rate (APR) for the CD Account: 3
Enter the number of months the CD account will accrue interest: 12

CD Account Updated Balance: 2060.30, Interest Earned: 60.30
</pre>


#### @Created by Roberto dos Reis -- June 2024



