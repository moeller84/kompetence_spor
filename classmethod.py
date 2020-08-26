class Organization:
    def __init__(self, name, sales_people):
        self.sales_people = sales_people

    @classmethod
    def from_json(cls, json_file):
        data = json.loads(pathlib.Path(json_file).read_text())
        return cls(sales_people=[SalesP
            (name=data["name"],
            sales_budget=data["sales_budget"])
                                 ])

    class SalesPerson:
        def __init__(self, name, sales_budget):
            self.name = name
            self.sales_budget = sales_budget

        def work(self):
            print(f"{self.name} is doing {self.work}")