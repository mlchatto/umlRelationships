class Patient:
    def __init__(self, name: str, age: int, bill_amount: float, bill_discount: int):
        self.__name = name
        self.__age = age
        self.__amount = bill_amount
        self.__bill_discount = bill_discount

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def bill_amount(self):
        return self.__amount

    @property
    def bill_discount(self):
        return self.__bill_discount

    @name.setter
    def name(self, name: str):
        self.__name = name

    @age.setter
    def age(self, age: int):
        self.__age = age

        if self.__age < 0:
            print("Age cannot be negative. Setting age to 0.")
            self.__age = 0

        else:
            self.__age = age

    @bill_amount.setter
    def bill_amount(self, amount: float):
        self.__amount = amount

        if self.__amount < 0:
            print("Bill amount cannot be negative. Setting bill amount to 0.")
            self.__amount = 0

        else:
            self.__amount = amount

    @bill_discount.setter
    def bill_discount(self, discount: float):
        self.__bill_discount = discount

        if self.__bill_discount < 0:
            print("Bill discount cannot be negative. Setting bill discount to 0.")
            self.__bill_discount = 0

        else:
            self.__bill_discount = discount

    def calculate_bill(self, bill_discount: float):
        return self.__amount - (self.__amount * bill_discount)


class Senior_Patient(Patient):
    def __init__(self, name: str, age: int, bill_amount: float):
        super().__init__(name, age, bill_amount)

    def calculate_bill(self):
        discount = 0.2 * self.bill_amount
        return self.bill_amount - discount

class PhilHealth_Patient(Patient):
    def __init__(self, name: str, age: int, bill_amount: float):
        super().__init__(name, age, bill_amount)

    def calculate_bill(self):
        discount = 0.15 * self.bill_amount
        return self.bill_amount - discount


regular_patient = Patient("Percy Jackson", 15000, 0)
senior_patient = Senior_Patient("Annabeth Chase", 65, 20000, 0.2)
philhealth_patient = PhilHealth_Patient("Grover Underwood", 25, 10000, 0.15)

patients = [regular_patient, senior_patient, philhealth_patient]
for patient in patients:
    print("Hospital Billing System")
    print("\n-----------------------------")
    patient.name()
    patient.age()
    patient.bill_amount()
