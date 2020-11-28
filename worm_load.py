import psycopg2


def get_credentials()
    return {
        "database": "worms",
        "user": "james",
        "password": "",
        "host": "127.0.0.1",
        "port": 5432}


def execute_query(query: str) -> None:
    credentials = get_credentials()
    with psycopg2.connect(**credentials) as connection:
        cursor = connection.cursor
        cursor.execute(query)
    return
