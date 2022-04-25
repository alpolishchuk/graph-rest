Демо-стенд для обзора GraphQL
=============================================

Deploy
------

Для деплоя необходимо в директории выполнить следующую команду:

```docker-compose build && docker-compose up -d```

После чего api будет доступно по адресу

```http://127.0.0.1:8000/``` - это Django
```http://127.0.0.1:6000/``` - это Flask

Для заполнения базы данными необходимо выполнить команду

```docker exec graph-rest_web_1 python3 fill_database.py```

Скрипт ```fill_database.py``` можно править по своему усмотрению. Так же при выполнении скрипт показывает тайминги работы API.

Для остановки контейнеров и удаления всего содержимого необходимо выполнить команду

```docker-compose down --remove-orphans```

API
---

API состоит из 2-х основных эндпоинтов:

```/rest/``` и ```/graphql/``` для REST API и GraphQL соответственно (для Flask REST API недоступно).

Все ```graphql```-запросы передаются методом ```POST``` на эндпоинт ```graphql```, формат запросов - ```JSON```
 
Примеры запросов ```GraphQL```

```{"query": "query { allPizzas { id, name } }" }``` - получение списка всех пицц с полями ```id``` и ```name```

```{"query": "query { allToppings { id, name, pizza { name } } }" }``` - получение списка всех наполнителей с полями ```id``` и ```name```, а так же имен пицц, к которым они привязаны.

```{"query": "query {  pizza(id: 2) { name } anotherPizza: pizza(name: \"Margarita\") { toppingsSet { id name } } }" }``` - запрос 2-х разных объектов - по ```id``` и по ```name```.

```{"query": "mutation { pizzaMut(input: { price: 400.0, name: \"Margarita\" }) { pizza { name } } }" }``` - создание пиццы

```{"query": "mutation { pizzaMut(input: { id: 1, price: 500.0, name: \"Margarita\" }) { pizza { name } } }" }``` - мутация пиццы

```{"query": "mutation { toppingMut(input: { id: 7, quantity: 40.0, name: \"Tomato\", pizza: 1 }) { toppings { name } } }" }```  - мутация наполнителя

Запросы с демонстрации
----------------------

Предупреждение:

В Django-эндпоинте доступны запросы только из раздела выше, запросы ниже - для Flask-эндпоинта. 
```
query {
    dictObject {
        floatField,
        intField,
        textField
    }
}

query {
    attrObject {
        floatAttr,
        intAttr,
        textAttr
    }
}

query {
    dictObject {
        floatField,
        intField,
        textField
    }
    attrObject {
        floatAttr,
        intAttr,
        textAttr
    }
}

query allPizzas($data: PizzaInputType) {
    allPizzas(data: $data) {
        name,
        price,
        toppingsCount,
    }
}

query {
    allToppings {
        id,
        name,
        quantity,
    }
}

query {
    allToppingsConnection(first: 20) {
        pageInfo {
             startCursor
             endCursor
             hasNextPage
             hasPreviousPage
          }
         totalCount
         edges{
             node {
                 id
             }
         }
    }
}

query filterableToppingsConnection ($filters: ToppingsFilter){
    filterableToppingsConnection(first: 20, filters: $filters) {
        pageInfo {
             startCursor
             endCursor
             hasNextPage
             hasPreviousPage
          }
         totalCount
         edges{
             node {
                 id
             }
         }
    }
}

mutation createPizza($data: CreatePizzaInputType!) {
    createPizza(data: $data) {
        id,
        name,
        price,
        toppings {
            id
            name
        }
    }
}

mutation updatePizza($data: UpdatePizzaInputType!) {
    updatePizza(data: $data) {
        id,
        name,
        price,
        toppings {
            id
            name
        }
    }
}
```