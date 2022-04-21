import requests
import random
from datetime import datetime

PIZZA_NAMES = ('Margarita', 'BBQ', '4 Cheeze', 'Carbonara', 'Vegan', 'Meaty', 'Salami')
TOPPING_NAMES = ('Tomato', 'Cheeze', 'Pork', 'Beef', 'Mushrooms', 'Sauce', 'Salami', 'Mozarella', 'Chicken')

PIZZAS_QUANTITY_TO_CREATE = 1000
TOPPINGS_QUANTITY_TO_CREATE = 1000

rest_pizza_time = datetime.now()
for i in range(PIZZAS_QUANTITY_TO_CREATE):
    response = requests.post('http://127.0.0.1:8000/rest/pizza/',
                             data={
                                 'name': random.choice(PIZZA_NAMES),
                                 'price': random.randint(100, 500)
                             })
    if response.status_code != 201:
        print(response.status_code, response.json())
        exit(1)
    if i % 100 == 0:
        print(f'{i} of {PIZZAS_QUANTITY_TO_CREATE} pizzas created by rest')
print(f'Time elapsed on creating {PIZZAS_QUANTITY_TO_CREATE} pizzas by rest: {datetime.now() - rest_pizza_time}')


graph_pizza_time = datetime.now()
for i in range(PIZZAS_QUANTITY_TO_CREATE):
    query = """
        mutation {
            pizzaMut(input: {
              price: %(price)i, name: "%(name)s"
            })
            {
              pizza {
                name
              }
            }
        }
    """ % {
        'name': random.choice(PIZZA_NAMES),
        'price': random.randint(100, 500)
    }

    response = requests.post('http://127.0.0.1:8000/graphql/',
                             data={"query": query})
    if response.status_code != 200:
        print(response.status_code, response.json())
        exit(1)
    if i % 100 == 0:
        print(f'{i} of {PIZZAS_QUANTITY_TO_CREATE} pizzas created by graph')
print(f'Time elapsed on creating {PIZZAS_QUANTITY_TO_CREATE} pizzas by graphql: {datetime.now() - graph_pizza_time}')

all_pizzas = requests.get('http://127.0.0.1:8000/rest/pizza/').json()
MIN_PIZZA_INDEX = all_pizzas[0]['id']
MAX_PIZZA_INDEX = all_pizzas[-1]['id']

rest_toppings_time = datetime.now()
for i in range(TOPPINGS_QUANTITY_TO_CREATE):
    response = requests.post('http://127.0.0.1:8000/rest/toppings/',
                             data={
                                 'name': random.choice(TOPPING_NAMES),
                                 'quantity': random.randint(100, 300),
                                 'pizza': random.randint(MIN_PIZZA_INDEX, MAX_PIZZA_INDEX)
                             })
    if response.status_code != 201:
        print(response.status_code, response.json())
        exit(1)
    if i % 100 == 0:
        print(f'{i} of {TOPPINGS_QUANTITY_TO_CREATE} toppings created by rest')
print(f'Time elapsed on creating {TOPPINGS_QUANTITY_TO_CREATE} toppings by rest: {datetime.now() - rest_toppings_time}')

graph_toppings_time = datetime.now()
for i in range(TOPPINGS_QUANTITY_TO_CREATE):
    query = """
        mutation {
            toppingMut(input: {
                quantity: %(quantity)i, name: "%(name)s", pizza: %(pizza)s
            })
            {
                toppings {
                    name
                }
            }
        }
    """ % {
        'quantity': random.randint(100, 300),
        'name': random.choice(TOPPING_NAMES),
        'pizza': random.randint(MIN_PIZZA_INDEX, MAX_PIZZA_INDEX)
    }

    response = requests.post('http://127.0.0.1:8000/graphql/',
                             data={"query": query})
    if response.status_code != 200:
        print(response.status_code, response.json())
        exit(1)
    if i % 100 == 0:
        print(f'{i} of {TOPPINGS_QUANTITY_TO_CREATE} toppings created by graph')
print(f'Time elapsed on creating {TOPPINGS_QUANTITY_TO_CREATE} toppings by graphql: {datetime.now() - graph_toppings_time}')
