def join_list_with_delimeter(delimeter: str, list: list[str]) -> str:
    """Joins list of string element with passed delimeter

    Args:
        delimeter (str): Delimeter that will join the list
        list (list[str]): List of string elements

    Returns:
        str: String of the joined elements
    """
    return delimeter.join(list)

def wrap_list_elements_between_string(wrapper: str, list: list[str]) -> list[str]:
    """Wrapps the elements of the list between the wrapper string

    Args:
        wrapper (str): Wrapper string
        list (list[str]): List of strings

    Returns:
        list[str]: List of string after the elements wrapped
    """
    return [f"{wrapper}{element}{wrapper}" for element in list]

def convert_dict_to_sql_set_value(data: dict) -> str:
    """Converts dictionary to sql set value

    Args:
        data(dict): Data to be converted

    Returns:
        str: String after conversion, Eg. (name = 'Mike', age = 52, country = 'USA')
    """
    key_value_list = [f'{key}="{value}"' for key, value in data.items()]
    return join_list_with_delimeter(',', key_value_list)