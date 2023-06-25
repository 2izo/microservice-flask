import mysql.connector
import mysql.connector.cursor

from database.database_wrapper import DatabaseWrapper
from helpers.functions import convert_dict_to_sql_set_value, join_list_with_delimeter, wrap_list_elements_between_string

class MySqlWrapper(DatabaseWrapper):
    """Wrapper class for MySql database
    """

    # MySql database to work on
    __database = None
    # Cursor for the database
    __cursor = None

    def __init__(self, user: str, password: str, database: str) -> None:
        """Constructor for MySqlWrapper class

        Args:
            user (str): Username
            password (str): Password
            database (str): Database name
        """
        #   user="root",
        #     password="root",
        #     database="car_hiring_management"

        self.__database = mysql.connector.connect(
          user = user,
          password = password,
          database = database,
          host= 'db'
        )
        self.__cursor = self.__database.cursor()
    
    def create_table(self, table_name:str, columns: list[str]) -> None:
        """Creates table

        Args:
            table_name (str): Table name
            columns (list[str]): Columns to be created within the table
        """
        sql = f"CREATE TABLE IF NOT EXISTS `{table_name}` ({join_list_with_delimeter(',', columns)})"
        self.__cursor.execute(sql)
        self.__database.commit()

    def insert_row(self, table_name: str, row_data: dict) -> None:
        """Inserts row inside the table

        Args:
            table_name (str): Table name
            data (dict): Row data
        """
        values_list = wrap_list_elements_between_string("'",list(row_data.values()))
        joined_keys_string = join_list_with_delimeter(',', row_data.keys())
        joined_values_string = join_list_with_delimeter(',', values_list)
        sql = f"INSERT INTO {table_name} ({joined_keys_string}) VALUES ({joined_values_string})"
        self.__cursor.execute(sql)
        self.__database.commit()

    def get_rows(self, table_name: str, columns: list[str], where_clause: str) -> list:
        """Gets rows from table

        Args:
            table_name (str): Table name
            columns (list[str]): columns list to be retrieved
            where_clause (str): Where clause statement

        Returns:
            list: List of table entries
        """
        joined_columns_string = join_list_with_delimeter(',', columns)
        sql = f"SELECT {joined_columns_string} FROM {table_name}"
        # Check if there is a where clause
        if len(where_clause) > 0:
            sql += f" WHERE {where_clause}"
        self.__cursor.execute(sql)
        rows = self.__cursor.fetchall()

        return rows

    def update_row(self, table_name: str, data: dict, where_clause: str):
        """Updates row with new data

        Args:
            table_name (str): Table name
            data (dict): Data to overwrite old data
            where_clause (str): Where clause statement
        """
        sql = f"UPDATE {table_name} SET {convert_dict_to_sql_set_value(data)} WHERE {where_clause}"
        self.__cursor.execute(sql)
        self.__database.commit()

    def delete_row(self, table_name: str, where_clause: str) -> None:
        """Deletes row from table

        Args:
            table_name (str): Table name
            where_clause (str): Where clause statement
        """
        sql = f"DELETE FROM {table_name} WHERE {where_clause}"
        self.__cursor.execute(sql)
        self.__database.commit()

    def execute_custom_command(self, sql: str):
        """Executes custom mysql command by user

        Args:
            sql (str): SQL statement to be executed

        Returns:
            _type_: _description_
        """
        self.__cursor.execute(sql)
        self.__database.commit()
        return self.__cursor
    
    def close_connection(self):
        """Closes connection to the database
        """
        self.__cursor.close()
        self.__database.shutdown()
    
    