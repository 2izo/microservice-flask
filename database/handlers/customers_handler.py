from database.database_wrapper import DatabaseWrapper

class CustomersHandler:
    """ A class responsible for handling the operations on customer table 
    """

    # Wrapper for the database
    __database_wrapper: DatabaseWrapper = None
    # Customer table name
    __table_name: str = "customers"

    def __init__(self, database_wrapper: DatabaseWrapper) -> None:
        """Constructor for the CustomersHandler class

        Args:
            database_wrapper (DatabaseWrapper): Wrapper for the database that we will query on
        """
        self.__database_wrapper = database_wrapper

    def create_customer(self, data: dict):
        """Creates customer

        Args:
            data (dict): Customer data
        """
        self.__database_wrapper.insert_row(self.__table_name, data)

    def get_customers(self, columns: list[str], where_clause: str) -> list:
        """Gets customers

        Args:
            columns (list[str]): Columns to be retrieved
            where_clause (str): Where clause statement

        Returns:
            list: List of customers
        """
        return self.__database_wrapper.get_rows(self.__table_name, columns, where_clause)
    
    def update_customers(self, customer_data: dict, where_clause: str):
        """Updates customers

        Args:
            customer_data (dict): Customer data to overwrite the old data
            where_clause (str): Where clause statement
        """
        self.__database_wrapper.update_row(self.__table_name, customer_data, where_clause)

    def delete_customers(self, where_clause: str):
        """Deletes customers

        Args:
            where_clause (str): Where clause statement
        """
        self.__database_wrapper.delete_row(self.__table_name, where_clause)
    
        