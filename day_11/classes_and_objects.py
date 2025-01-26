from collections import Counter
import math

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        """Return the count of data."""
        return len(self.data)

    def sum(self):
        """Return the sum of data."""
        return sum(self.data)

    def min(self):
        """Return the minimum value in the data."""
        return min(self.data)

    def max(self):
        """Return the maximum value in the data."""
        return max(self.data)

    def range(self):
        """Return the range (max - min) of the data."""
        return self.max() - self.min()

    def mean(self):
        """Return the mean of the data."""
        return self.sum() / self.count()

    def median(self):
        """Return the median of the data."""
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n // 2
        if n % 2 == 0:  # Even number of data points
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:  # Odd number of data points
            return sorted_data[mid]

    def mode(self):
        """Return the mode of the data and its count."""
        freq = Counter(self.data)
        max_count = max(freq.values())
        modes = [key for key, value in freq.items() if value == max_count]
        return {"mode": modes[0], "count": max_count}

    def var(self):
        """Return the variance of the data."""
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / self.count()

    def std(self):
        """Return the standard deviation of the data."""
        return math.sqrt(self.var())

    def freq_dist(self):
        """Return the frequency distribution of the data."""
        freq = Counter(self.data)
        total = self.count()
        return [(value / total * 100, key) for key, value in freq.items()]

# Example usage
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count())  # 25
print('Sum: ', data.sum())  # 744
print('Min: ', data.min())  # 24
print('Max: ', data.max())  # 38
print('Range: ', data.range())  # 14
print('Mean: ', data.mean())  # 30
print('Median: ', data.median())  # 29
print('Mode: ', data.mode())  # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std())  # 4.2
print('Variance: ', data.var())  # 17.5
print('Frequency Distribution: ', data.freq_dist())

#Exercise level 2
#creating a class called PersonAccount that has the following attributes: first_name, last_name, incomes, expenses
class PersonAccount:
    def __init__(self, firstname, lastname):
        """Initialize the PersonAccount with firstname, lastname, incomes, and expenses."""
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []  # List of tuples: (amount, description)
        self.expenses = []  # List of tuples: (amount, description)

    def total_income(self):
        """Calculate and return the total income."""
        return sum(amount for amount, _ in self.incomes)

    def total_expense(self):
        """Calculate and return the total expense."""
        return sum(amount for amount, _ in self.expenses)

    def account_info(self):
        """Return a summary of the account information."""
        info = f"Account Holder: {self.firstname} {self.lastname}\n"
        info += f"Total Income: {self.total_income()}\n"
        info += f"Total Expense: {self.total_expense()}\n"
        info += f"Account Balance: {self.account_balance()}\n"
        return info

    def add_income(self, amount, description):
        """Add an income with its description."""
        self.incomes.append((amount, description))
        print(f"Income added: {amount} ({description})")

    def add_expense(self, amount, description):
        """Add an expense with its description."""
        self.expenses.append((amount, description))
        print(f"Expense added: {amount} ({description})")

    def account_balance(self):
        """Calculate and return the account balance (total_income - total_expense)."""
        return self.total_income() - self.total_expense()

# Example usage
account = PersonAccount("John", "Doe")

# Adding incomes
account.add_income(5000, "Salary")
account.add_income(200, "Freelance Project")

# Adding expenses
account.add_expense(1500, "Rent")
account.add_expense(200, "Utilities")
account.add_expense(300, "Groceries")

# Printing account info
print(account.account_info())
