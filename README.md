# Arsen's test web-interface on Flask

## General info

This service was created by **Arsen Sogoyan** during the [Learn Python course](https://learn.python.ru/) (*14/05/2022 - 16/07/2022*).

**Note:** currently the client interface runs on local machine _only_ (`127.0.0.1:5000`).

## Features

- ### Current weather summary
By using the [Weather API](https://www.worldweatheronline.com/developer/api/) we are pulling a JSON-response containing weather info for *Moscow, Russia* and output current temperature and 'feels-like' temperature.

**Note:** [World Weather Online](https://www.worldweatheronline.com/developer/api/) has 30-day free API access, so upon expiry I switched to free [Weather API](https://www.weatherapi.com/api.aspx) that has no time limitations.

Using [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/) template, `index.html` page was created to accomodate not only weather but other info in column sections. 

- ### Python.org news
Parsing Python.org [Latest News page](https://www.python.org/blogs/) and using [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) library we recreated the Latest News widget on our page alongside the weather information.  
**Note:** The news are pulled from the web source and saved in a SQLite database managed by [`Flask-SQLAlchemy`](https://flask-sqlalchemy.palletsprojects.com/en/2.x/).