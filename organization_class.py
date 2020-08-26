class Organization:
    def __init__(self, name, sales_people):
        self.name = name
        self.sales_people = sales_people

    @property
    def num_employees(self):
        return f'{len(self.sales_people)}'

    def work(self):
        for sales_person in self.sales_people:
            sales_person.work()

    def __repr__(self):
        return f'<{self.name} has {len(self.num_employees)} employees>'


class CustomerServiceCenter(Organization):
    def __init__(self, num_employees, contact_method):
        super().__init__('KSC', num_employees)
        self.contact_method = contact_method

    def work(self):
        print(f'{self.num_employees} employees did {self.contact_method}')


class FranchiseOffice(Organization):
    def __init__(self, num_employees, contact_method):
        super().__init__("franchise", num_employees)
        self.contact_method = contact_method

    def work(self):
        print(f'{self.num_employees} employees did {self.contact_method}')

class SalesPerson:
    def __init__(self, name, work):
        self.name = name
        self.work = work

    def work(self):
        print(f"{self.name} is doing {self.work}")
