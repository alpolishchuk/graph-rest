import requests
from datetime import datetime

rest_get_time = datetime.now()
response = requests.get('http://127.0.0.1:8000/rest/pizza/')
entries_count = len(response.json())
print(f'{entries_count} pizza entries by rest: {datetime.now() - rest_get_time}')

graphql_get_time = datetime.now()
query = """
    query {
        allPizzas {
            id,
            name,
            price
        }
    }
"""
response = requests.post('http://127.0.0.1:8000/graphql/', data={"query": query})
print(f'{entries_count} pizza entries with all fields by graphql: {datetime.now() - graphql_get_time}')

graphql_get_time = datetime.now()
query = """
    query {
        allPizzas {
            id,
            name,
        }
    }
"""
response = requests.post('http://127.0.0.1:8000/graphql/', data={"query": query})
print(f'{entries_count} pizza entries with id and name by graphql: {datetime.now() - graphql_get_time}')

graphql_get_time = datetime.now()
query = """
    query {
        allPizzas {
            id
        }
    }
"""
response = requests.post('http://127.0.0.1:8000/graphql/', data={"query": query})
print(f'{entries_count} pizza entries with id by graphql: {datetime.now() - graphql_get_time}')

graphql_get_time = datetime.now()
query = """
    query {
        pizzasOptimized {
            id
        }
    }
"""
response = requests.post('http://127.0.0.1:8000/graphql/', data={"query": query})
print(f'{entries_count} pizza entries with id by optimized graphql: {datetime.now() - graphql_get_time}')

rest_get_time = datetime.now()
response = requests.get('http://127.0.0.1:8000/rest/toppings/')
entries_count = len(response.json())
print(f'{entries_count} toppings entries by rest: {datetime.now() - rest_get_time}')

graphql_get_time = datetime.now()
query = """
    query {
        allToppings {
            name,
            pizza {
                name
            }
        }
    }
"""
response = requests.post('http://127.0.0.1:8000/graphql/', data={"query": query})
print(f'{entries_count} toppings entries with name and pizza name: {datetime.now() - graphql_get_time}')

graphql_get_time = datetime.now()
query = """
    query {
        toppingsOptimized {
            name,
            pizza {
                name
            }
        }
    }
"""
response = requests.post('http://127.0.0.1:8000/graphql/', data={"query": query})
print(f'{entries_count} toppings entries with name and pizza name optimized: {datetime.now() - graphql_get_time}')
