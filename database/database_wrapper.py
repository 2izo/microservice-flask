from abc import ABC
import abc

class DatabaseWrapper(ABC):
    """Abstract class wrapping databases with important methods
    """

    @abc.abstractmethod
    def create_table(self, table_name:str, columns: list[str]) -> None:
        """Creates table

        Args:
            table_name (str): Table name
            columns (list[str]): Columns to be created within the table
        """
        pass
    @abc.abstractmethod

    def insert_row(self, table_name: str, row_data: dict) -> None:
        """Inserts row inside the table

        Args:
            table_name (str): Table name
            data (dict): Row data
        """
        pass
    
    @abc.abstractmethod
    def get_rows(self, table_name: str, columns: list[str], where_clause: str) -> list:
        """Gets rows from table

        Args:
            table_name (str): Table name
            columns (list[str]): columns list to be retrieved
            where_clause (str): Where clause statement

        Returns:
            list: List of table entries
        """
        pass

    @abc.abstractmethod
    def update_row(self, table_name: str, data: dict, where_clause: str):
        """Updates row with new data

        Args:
            table_name (str): Table name
            data (dict): Data to overwrite old data
            where_clause (str): Where clause statement
        """
        pass

    @abc.abstractmethod
    def delete_row(self, table_name: str, where_clause: str) -> None:
        """Deletes row from table

        Args:
            table_name (str): Table name
            where_clause (str): Where clause statement
        """
        pass

    @abc.abstractmethod
    def execute_custom_command(self, sql: str):
        """Executes custom mysql command by user

        Args:
            sql (str): SQL statement to be executed

        Returns:
            _type_: _description_
        """
        pass

    @abc.abstractmethod
    def close_connection(self):
        """Closes connection to the database
        """
        pass