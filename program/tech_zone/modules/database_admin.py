import sqlite3
from pathlib import Path

database_path = Path(Path(__file__).parent.parent, 'database')


def database_init(function_to_decorate):
    def open_close_wrapper(*args):
        database = sqlite3.connect(Path(database_path, 'assistant.db'))
        cursor = database.cursor()

        value = function_to_decorate(*args, cursor=cursor)

        database.commit()
        database.close()
        return value
    return open_close_wrapper


@database_init
def table_create(cursor=None):
    cursor.execute('''CREATE TABLE {table_name} (
        {column}
    )''')


@database_init
def table_insert(balance='0', volume='0', result='0', day_result='0', previous_trade_id='0', cursor=None):
    cursor.execute(
        f'INSERT INTO main_interface_userdata VALUES ("id" = "1", "balance" = {balance}, \
        "volume" = {volume}, \
        "result" = {result}, \
        "day_result" = {day_result}, \
        "previous_trade_id" = {previous_trade_id})'
    )
    return print('Values added')


@database_init
def table_update(column, value, cursor=None):
    cursor.execute(f'UPDATE main_interface_userdata SET {column} = "{value}"')


@database_init
def table_select(select, cursor=None):
    cursor.execute(f'SELECT {select} FROM main_interface_userdata')
    value = cursor.fetchone()[0]
    return value


@database_init
def table_delete(where, cursor=None):
    cursor.execute(f'DELETE FROM main_interface_userdata WHERE {where}')
    return print('Values deleted')


@database_init
def testing(select, cursor=None):
    cursor.execute(f'SELECT {select} FROM main_interface_userdata')
    value = cursor.fetchall()
    return value


def main():
    # table_create()
    # table_insert()
    table_update('previous_trade_id', 30)
    # table_delete('rowid = 2')
    # print(table_select('balance'))
    # print(testing('*'))


if __name__ == '__main__':
    main()
