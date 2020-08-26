import json
import pathlib
from faker import Faker
import random
from random import randint
fake = Faker('en_US')


class Organization:
    def __init__(self, cust_service, tied_agent, lead):
        self.cust_service = cust_service
        self.tied_agent = tied_agent
        self.lead = lead

    def total_sales(self):
        cs_sales = sum(cs.ind_sales()
                   for cs
                   in self.cust_service)
        ta_sales = sum(ta.ind_sales()
                       for ta
                       in self.tied_agent)
        return cs_sales + ta_sales

    def total_cost(self):
        cs_cost = sum(cs.ind_cost()
                   for cs
                   in self.cust_service)
        ta_cost = sum(ta.ind_cost()
                      for ta
                      in self.tied_agent)
        return cs_cost + ta_cost

    def leads_used(self):
        cs_leads_used = sum(cs.ind_leads_used()
                   for cs
                   in self.cust_service)
        ta_leads_used = sum(ta.ind_leads_used()
                            for ta
                            in self.tied_agent)
        return ta_leads_used + cs_leads_used

    def sales_cost(self):
        cs_scost = sum(cs.cost
                      for cs
                      in self.cust_service)
        ta_scost = sum(ta.cost
                      for ta
                      in self.tied_agent)
        return cs_scost + ta_scost

    def reporting(self):
        self.consume_leads()
        self.convert_leads()

        sales_cost = self.sales_cost()
        total_sales = self.total_sales()
        total_cost = self.total_cost()
        leads_used = self.leads_used()

        return print(f'total sales: {total_sales}, total cost: {total_cost+sales_cost}, leads used: {leads_used}')

    def consume_leads(self):
        for cs in self.cust_service:
           cs.used_leads.append(self.lead[:cs.consumption_max])
           del self.lead[:cs.consumption_max]

        for ta in self.tied_agent:
           ta.used_leads.append(self.lead[:ta.consumption_max])
           del self.lead[:ta.consumption_max]

        return None

    def convert_leads(self):
        cs_slice = round(self.cust_service[0].hitrate * self.cust_service[0].consumption_max)
        ta_slice = round(self.tied_agent[0].hitrate * self.tied_agent[0].consumption_max)

        for cs in self.cust_service:
            cs.converted_leads.append(cs.used_leads[0][:cs_slice])
            for lead in cs.converted_leads[0]:
                lead.status()
        for ta in self.tied_agent:
            ta.converted_leads.append(ta.used_leads[0][:ta_slice])
            for lead in ta.converted_leads[0]:
                lead.status()

        return None

    @classmethod
    def from_json(cls, json_file):
        dict = json.loads(pathlib.Path(json_file).read_text())

        return cls(
            cust_service=[
                CustomerServiceRep(name=fake.name(),
                                   used_leads=[],
                                   converted_leads=[])
                for _ in range(dict["customer_service"])
            ],
            tied_agent=[
                TiedAgent(name=fake.name(),
                          used_leads=[],
                          converted_leads=[]
                          )
                for _ in range(dict["tied_agents"])
            ],
            lead=[
                Lead(name=fake.name(),
                     lead_cost=float(random.randrange(50, 100)),
                     value=float(random.randrange(100, 200)),
                     conversion_status=False)
                for _ in range(dict["leads"])
            ],
        )


class SalesPerson:
    consumption_max = 10

    def __init__(self, name, used_leads, converted_leads):
        self.name = name
        self.used_leads = used_leads
        self.converted_leads = converted_leads

    def ind_sales(self):
        return sum(lead.value
                   for lead
                   in self.converted_leads[0])

    def ind_cost(self):
        return sum(lead.lead_cost
                   for lead
                   in self.converted_leads[0])

    def ind_leads_used(self):
        return len(self.used_leads[0])


class CustomerServiceRep(SalesPerson):
    hitrate = 0.2
    cost = 1000


class TiedAgent(SalesPerson):
    hitrate = 0.3
    cost = 1500


class Lead:

    def __init__(self, name, value, lead_cost, conversion_status):
        self.name = name
        self.value = value
        self.lead_cost = lead_cost
        self.conversion_status = conversion_status

    def status(self):
        self.conversion_status = True

        return None