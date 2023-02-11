# A program that allows the user to track their expenses and income
import csv


# class for all features
class budgetTracker:
#     CREATE_BUDGET = open("expense.csv", "w", newline="", encoding="utf-8")
#     ADD_BUDGET = open("expense.csv", "a", newline="", encoding="utf-8")

    # feature to add create expenses
    @classmethod
    def create_addExpenses(self, add_amount, add_date, add_category, add_description):
        with open("expense.csv", "w", newline="", encoding="utf-8") as CREATE_BUDGET:
            fieldnames = ["amount", "date", "category", "description"]
            writer = csv.DictWriter(CREATE_BUDGET, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({"amount": add_amount, "date": add_date, "category": add_category, "description": add_description})
    
    # feature to add new expenses
    @classmethod
    def newExpenses(self):
        pass

    # feature to view list of past expenses
    def pastExpenses(self):
        pass

    # feature to set budget goals
    def budgetGoals(self):
        pass

    # feature to generate reports
    def genReports(self):
        pass

    # feature to send notification or alerts when expenses reach a certain
    # threshold
    def budgetAlerts(self):
        pass

    # a feature to import or export expenses from or to a CSV file
    def importExport(self):
        pass

    # feature to store user data and allow only authorized users to access
    def userAuth(self):
        pass


add_amount = int(input("Add amount to your budget tracker:\n>> "))
add_date = input("Add date to your budget tracker:\n>> ")
add_category = input("Add category to your budget tracker:\n>> ")
add_description = input("Add description to your budget tracker:\n>> ")

bgt = budgetTracker.create_addExpenses(add_amount, add_date, add_category, add_description)
