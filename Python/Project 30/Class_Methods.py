class employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(self, string):
        return self(string.split("-")[0], string.split("-")[1])


e1 = employee("Salman", "1000$")
print("Name:", e1.name, "|| Salary:", e1.salary)
string = "Rafi-1000$"
e2 = employee.fromstr(string)
print("Name:", e2.name, "|| Salary:", e2.salary)
