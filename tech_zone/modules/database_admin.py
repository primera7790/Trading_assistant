import sqlite3
from pathlib import Path

database_path = Path(Path(__file__).parent.parent, 'database')


def table_create():
    database_new = sqlite3.connect('')
    cursor_new = database_new.cursor()

    cursor_new.execute('''CREATE TABLE {table_name} (
        {column}
    )''')

    database_new.commit()
    database_new.close()


def table_insert(balance='0', volume='0', result='0', day_result='0', previous_trade_id='0'):
    database = sqlite3.connect(Path(database_path, 't_a.db'))
    cursor = database.cursor()
    cursor.execute(f'INSERT INTO user_values VALUES ("{balance}", "{volume}", "{result}", "{day_result}", "{previous_trade_id}")')
    database.commit()
    database.close()
    return print('Values added')


def table_update(column, value):
    database = sqlite3.connect(Path(database_path, 't_a.db'))
    cursor = database.cursor()
    cursor.execute(f'UPDATE user_values SET {column} = "{value}"')
    database.commit()
    database.close()


def table_select(select):
    database = sqlite3.connect(Path(database_path, 't_a.db'))
    cursor = database.cursor()
    cursor.execute(f'SELECT {select} FROM user_values')
    value = cursor.fetchone()[0]
    database.commit()
    database.close()
    return value


def table_delete(where):
    database = sqlite3.connect(Path(database_path, 't_a.db'))
    cursor = database.cursor()
    cursor.execute(f'DELETE FROM user_values WHERE {where}')
    database.commit()
    database.close()
    return print('Values deleted')


# def testing(select):
#     database = sqlite3.connect(Path(database_path, 't_a.db'))
#     cursor = database.cursor()
#     cursor.execute(f'SELECT {select} FROM user_values')
#     value = cursor.fetchall()
#     database.commit()
#     database.close()
#     return value


def main():
    # table_create()
    # table_insert()
    # table_update('previous_trade_id', 0)
    # table_delete('rowid = 2')
    print(table_select('previous_trade_id'))
    # print(testing('*'))


if __name__ == '__main__':
    main()