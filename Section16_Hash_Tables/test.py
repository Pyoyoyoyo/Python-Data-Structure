class Employee:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.salary = self.set_salary()

    def set_salary(self):
        if self.rank == "New Employee":
            return 30000
        elif self.rank == "Employee":
            return 40000
        elif self.rank == "Senior Employee":
            return 60000
        elif self.rank == "Management":
            return 100000
        else:
            return 0

    def get_details(self):
        return f"Employee: {self.name}, Rank: {self.rank}, Salary: ${self.salary}"


class PayrollManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_payroll(self):
        total_payroll = sum(employee.salary for employee in self.employees)
        return total_payroll

    def list_employees(self):
        for employee in self.employees:
            print(employee.get_details())


class Organization:
    def __init__(self):
        self.payroll_manager = PayrollManager()

    def add_employee(self, name, rank):
        employee = Employee(name, rank)
        self.payroll_manager.add_employee(employee)

    def get_payroll(self):
        print("\nEmployee Details:")
        self.payroll_manager.list_employees()

        total_payroll = self.payroll_manager.calculate_total_payroll()
        print(f"\nTotal Payroll for the Organization: ${total_payroll}")


# Example usage
if __name__ == "__main__":
    org = Organization()

    org.add_employee("Alice", "New Employee")
    org.add_employee("Bob", "Employee")
    org.add_employee("Charlie", "Senior Employee")
    org.add_employee("Dave", "Management")

    org.get_payroll()
