class Employee:
    def __init__(self):
        self.__salary = 50000

    def increment(self):
        self.__salary += 10000

    def deduct(self):
        self.__salary -= 5000

    def get_salary(self):
        print(f"Salary: {self.__salary}")   

em1 = Employee()
em2 = Employee()

print("--- em1 ---")
em1.get_salary()
em1.increment()
em1.get_salary()
em1.deduct()
em1.get_salary()

print("\n--- em2 ---")
em2.get_salary()
em2.increment()
em2.increment()
em2.get_salary()
em2.deduct()
em2.get_salary()