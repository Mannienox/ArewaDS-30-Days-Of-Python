#Exercises: Day 21

#Exercise: Level 1

class Statistics:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data) if len(self.data) > 0 else None

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            return sorted_data[n // 2]

    def sum (self):
        return sum(self.data)
    def mode(self):
        from collections import Counter
        counts = Counter(self.data)
        max_count = max(counts.values())
        mode = [num for num, count in counts.items() if count == max_count]
        return mode if mode else None

    def range(self):
        return max(self.data) - min(self.data) if self.data else None

    def var(self):
        if len(self.data) <= 1:
            return None
        mean_val = self.mean()
        return sum((x - mean_val) ** 2 for x in self.data) / (len(self.data) - 1)

    def std(self):
        import math
        variance = self.var()
        return math.sqrt(variance) if variance is not None else None

    def min(self):
        return min(self.data) if self.data else None

    def max(self):
        return max(self.data) if self.data else None

    def count(self):
        return len(self.data)

    def percentile(self, percentile):
        sorted_data = sorted(self.data)
        index = (percentile / 100) * (len(sorted_data) - 1)
        if index.is_integer():
            return sorted_data[int(index)]
        else:
            lower = sorted_data[int(index)]
            upper = sorted_data[int(index) + 1]
            return (lower + upper) / 2

    def freq_dist(self):
        from collections import Counter
        return dict(Counter(self.data))

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]


# Exercise: Level 2
class PersonAccount:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.incomes = {}
        self.expenses = {}

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_info(self):
        return f"Account Information for {self.first_name} {self.last_name}:\n" \
               f"Total Income: {self.total_income()}\n" \
               f"Total Expense: {self.total_expense()}\n" \
               f"Account Balance: {self.account_balance()}"

    def add_income(self, amount, description):
        if amount > 0:
            self.incomes[description] = amount
            print(f"Income of {amount} added with description: '{description}'")
        else:
            print("Income amount should be greater than 0.")

    def add_expense(self, amount, description):
        if amount > 0:
            self.expenses[description] = amount
            print(f"Expense of {amount} added with description: '{description}'")
        else:
            print("Expense amount should be greater than 0.")

    def account_balance(self):
        return self.total_income() - self.total_expense()


