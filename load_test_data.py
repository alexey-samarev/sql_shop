"""Модуль для загрузки тестовых данных в бд."""

from database import Database
from migrate import migrate
from settings import settings


def execute_many_command(
    sql_command: str,
    data: list[tuple[str | int]],
) -> None:
    """Выполнить команду c  разлиными данными.

    Args:
    ----
        sql_command (str): сама sql команда.
        data (list[tuple[str  |  int]]): данные в нужном формате

    """
    db = Database(settings=settings)
    with db() as conn:
        cur = conn.cursor()
        cur.executemany(sql_command, data)
        conn.commit()


rack_insert = """
INSERT INTO rack(name)
VALUES (%s)
"""
rack_insert_values = [("А",), ("Б",), ("Ж",)]

order_insert = """
INSERT INTO ordert(order_number, consumer_name)
VALUES (%s, %s)
"""
order_insert_values = [(10, "A"), (11, "B"), (14, "C"), (15, "D")]

product_insert = """
INSERT INTO product(name, article)
VALUES (%s, %s)
"""
product_insert_values = [
    ("Ноутбук", 1),
    ("Телевизор", 2),
    ("Телефон", 3),
    ("Системный блок", 4),
    ("Часы", 5),
    ("Микрофон", 6),
]


def load() -> None:
    """Основная функция модуля."""
    migrate()
    execute_many_command(rack_insert, rack_insert_values)
    execute_many_command(order_insert, order_insert_values)
    execute_many_command(product_insert, product_insert_values)


if __name__ == "__main__":
    load()
    