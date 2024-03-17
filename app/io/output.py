def output_text_to_console(text):
    """
    Outputs the given text to the console.

    Args:
        text (str): The text to be output to the console.

    Returns:
        None
    """
    print(text)


def write_to_file_native(file_path, content):
    """
    Writes the specified content to a file using Python's built-in capabilities.

    Args:
        file_path (str): The path to the file where the content should be written.
        content (str): The content to be written to the file.

    Returns:
        str: A message indicating the success or failure of the operation.

    Raises:
        FileNotFoundError: If the file is not found.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return "Write successful"
    except FileNotFoundError:
        return "File not found"
