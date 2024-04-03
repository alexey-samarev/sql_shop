"""Модуль для загрузки тестовых данных в бд"""

from migrate import migrate, execute_command
from database import Database


def execute_many_command(sql_command: str, data: list[tuple[str | int]],
) -> None:
    """Выполнить команду с различными данными.
    
    Args:
    
        sql-command (str): сама sql команда.
        data (list[tuple])
    """

db = Database(settings=settings)
with db() as conn:
    cur = conn.cursor()
    cur.executemany(sql_command, data)
    conn.commit()


rack_insert = """
INSERT INTO rack(name)
VALUES(%s)
"""
rack_insert_values = [("А"), ("Б"), ("Ж")]
def load() -> None:
    """Основная функция модуля."""
    migrate()
    execute_many_command(rack_insert, rack_insert_values)

if __name__  == "__main__"
