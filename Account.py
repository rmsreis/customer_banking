""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance=0.0, interest_rate=0.0):
        """
        Initialize an Account with a balance and interest rate.
        """
        self.balance = balance
        self.interest_rate = interest_rate
        self.interest = 0.0  # Initialize interest attribute to 0.0

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """
        Set the account balance
        """
        self.balance = balance
    
    def set_interest_rate(self, interest_rate):
        """Set the account interest rate."""
        self.interest_rate = interest_rate

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """
        Set the account interest rate 
        """
        self.interest = interest
    
    def calculate_interest(self):
        """Calculate the interest earned based on the balance and interest rate."""
        return self.balance * self.interest_rate / 100
    
    
    def update_balance_with_interest(self):
        """
        Update the balance with the earned interest and 
        return the updated balance and interest earned.
        """
        interest = self.calculate_interest()
        self.balance += interest
        return self.balance, interest
