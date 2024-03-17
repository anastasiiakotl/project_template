import app.io.input as my_input
import app.io.output as my_output


def main():
    text_from_console = my_input.input_text_from_console()

    file_content_native = my_input.read_from_file_native('input.txt')

    file_content_pandas = my_input.read_from_file_with_pandas('input.csv')

    files = [text_from_console, file_content_native, str(file_content_pandas)]

    for file in files:
        my_output.output_text_to_console(file)

    for file in files:
        my_output.write_to_file_native('output.txt', file)


if __name__ == "__main__":
    main()
