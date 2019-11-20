Демо-стенд для доклада на MoscowPython MeetUp
=============================================

Deploy
------

Для деплоя необходимо в директории набрать следующие комманды:

```docker-compose build && docker-compose up -d```

После чего api будет доступно по адресу

```http://127.0.0.1:8000/```

API состоит из 2-х основных эндпоинтов:

```/rest/``` и ```/graphql/``` для REST API и GraphQL соответственно.

Все ```graphql```-запросы передаются методом ```POST``` на эндпоинт ```graphql```, формат запросов - ```JSON```
 
Примеры запросов ```GraphQL```

```{"query": "query { allPizzas { id, name } }" }``` - получение списка всех пицц с полями ```id``` и ```name```

```{"query": "query { allToppings { id, name, pizza { name } } }" }``` - получение списка всех наполнителей с полями ```id``` и ```name```, а так же имен пицц, к которым они привязаны.

```{"query": "query {  pizza(id: 2) { name } anotherPizza: pizza(name: \"Margarita\") { toppingsSet { id name } } }" }``` - запрос 2-х разных объектов - по ```id``` и по ```name```.

```{"query": "mutation { pizzaMut(input: { price: 400.0, name: \"Margarita\" }) { pizza { name } } }" }``` - создание пиццы

```{"query": "mutation { pizzaMut(input: { id: 1, price: 500.0, name: \"Margarita\" }) { pizza { name } } }" }``` - мутация пиццы

```{"query": "mutation { toppingMut(input: { id: 7, quantity: 40.0, name: \"Tomato\", pizza: 1 }) { toppings { name } } }" }```  - мутация наполнителя