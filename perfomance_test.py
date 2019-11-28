import requests
from datetime import datetime

rest_get_time = datetime.now()
response = requests.get('http://127.0.0.1:8000/rest/pizza/')
end_response = datetime.now()
entries_count = len(response.json())
print(f'{entries_count} pizza entries by rest: {end_response - rest_get_time}')

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
requests.post('http://127.0.0.1:8000/graphql/', data={"query": query})
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
requests.post('http://127.0.0.1:8000/graphql/', data={"query": query})
print(f'{entries_count} pizza entries with id and name by graphql: {datetime.now() - graphql_get_time}')

graphql_get_time = datetime.now()
query = """
    query {
        allPizzas {
            id
        }
    }
"""
requests.post('http://127.0.0.1:8000/graphql/', data={"query": query})
print(f'{entries_count} pizza entries with id by graphql: {datetime.now() - graphql_get_time}')

graphql_get_time = datetime.now()
query = """
    query {
        pizzasOptimized {
            id
        }
    }
"""
requests.post('http://127.0.0.1:8000/graphql/', data={"query": query})
print(f'{entries_count} pizza entries with id by optimized graphql: {datetime.now() - graphql_get_time}')

rest_get_time = datetime.now()
response = requests.get('http://127.0.0.1:8000/rest/toppings/')
end_response = datetime.now()
entries_count = len(response.json())
print(f'{entries_count} toppings entries by rest: {end_response - rest_get_time}')

graphql_get_time = datetime.now()
query = """
    query {
        allToppings {
            id,
            name,
            quantity,
            pizza {
                id,
                name,
                price
            }
        }
    }
"""
requests.post('http://127.0.0.1:8000/graphql/', data={"query": query})
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
requests.post('http://127.0.0.1:8000/graphql/', data={"query": query})
print(f'{entries_count} toppings entries with name and pizza name optimized: {datetime.now() - graphql_get_time}')
