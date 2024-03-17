import pandas as pd


def input_text_from_console():
    """
    This function prompts the user to input text from the console.

    Returns:
        str: The text inputted by the user.
    """
    return input("Enter text: ")


def read_from_file_native(file_path):
    """
    This function reads content from a file using Python's built-in capabilities.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content read from the file.

    Raises:
        FileNotFoundError: If the file is not found.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError("File not found")


def read_from_file_with_pandas(file_path):
    """
    This function reads content from a file using the pandas library.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        pandas.DataFrame: The data read from the file as a pandas DataFrame.

    Raises:
        FileNotFoundError: If the file is not found.
    """
    try:
        data = pd.read_csv(file_path)  # assuming the file is a CSV, adjust accordingly
        return data
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
