import json

from faker import Faker
import random
from random import randint
fake = Faker('en_US')

no_leads = 5
no_tied_agent = 4
no_customer_service = 3

my_dict = {}
my_dict['leads'] = []
my_dict['tied_agents'] = []
my_dict['customer_service'] = []

for _ in range(no_leads):
    lead_dict = {'name': fake.name(),
               'cost': float(random.randrange(50, 100)),
               'value': float(random.randrange(100, 200))}
    my_dict['leads'].append(lead_dict)

for _ in range(no_tied_agent):
    tied_agent_dict = {'name': fake.name(),
                       'type': 'tied agent'}
    my_dict['tied_agents'].append(tied_agent_dict)

for _ in range(no_customer_service):
    cust_serv_dict = {'name': fake.name(),
                      'type' : 'customer service'}
    my_dict['customer_service'].append(cust_serv_dict)

with open('data.json', 'w') as outfile:
    json.dump(my_dict, outfile)