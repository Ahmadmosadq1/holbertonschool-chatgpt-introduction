#!/usr/bin/env python3
"""
checkbook.py

A simple interactive checkbook application supporting deposits, withdrawals,
and balance inquiries.
"""

class Checkbook:
    """
    Class representing a simple checkbook ledger.
    
    You can deposit funds, withdraw funds (with overdraft protection),
    and query the current balance.
    """

    def __init__(self):
        """
        Function Description:
            Initialize a new Checkbook instance with zero balance.

        Parameters:
            None

        Returns:
            None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
            Add the specified amount to the current balance and display the result.

        Parameters:
            amount (float): The amount of money to deposit into the checkbook.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function Description:
            Subtract the specified amount from the current balance if sufficient
            funds exist, otherwise print an error message.

        Parameters:
            amount (float): The amount of money to withdraw from the checkbook.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function Description:
            Print the current balance to the console.

        Parameters:
            None

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Function Description:
        Run the interactive loop, prompting the user to deposit, withdraw,
        check balance, or exit.

    Parameters:
        None

    Returns:
        None
    """
    cb = Checkbook()
    while True:
        action = input(
            "What would you like to do? "
            "(deposit, withdraw, balance, exit): "
        ).strip().lower()

        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
checkbook.py

A simple interactive checkbook application supporting deposits, withdrawals,
and balance inquiries.
"""

class Checkbook:
    """
    Class representing a simple checkbook ledger.
    
    You can deposit funds, withdraw funds (with overdraft protection),
    and query the current balance.
    """

    def __init__(self):
        """
        Function Description:
            Initialize a new Checkbook instance with zero balance.

        Parameters:
            None

        Returns:
            None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
            Add the specified amount to the current balance and display the result.

        Parameters:
            amount (float): The amount of money to deposit into the checkbook.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function Description:
            Subtract the specified amount from the current balance if sufficient
            funds exist, otherwise print an error message.

        Parameters:
            amount (float): The amount of money to withdraw from the checkbook.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function Description:
            Print the current balance to the console.

        Parameters:
            None

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Function Description:
        Run the interactive loop, prompting the user to deposit, withdraw,
        check balance, or exit.

    Parameters:
        None

    Returns:
        None
    """
    cb = Checkbook()
    while True:
        action = input(
            "What would you like to do? "
            "(deposit, withdraw, balance, exit): "
        ).strip().lower()

        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

