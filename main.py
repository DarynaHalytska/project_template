from app.io.input import input_text_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import output_text_to_console, write_to_file_builtin

def main():
    path = "data/results.txt"

    input_text_res = input_text_from_console()
    output_text_to_console(input_text_res)
    write_to_file_builtin(path, input_text_res)

    read_file_res = read_from_file_builtin("requirements.txt")
    output_text_to_console(read_file_res)
    write_to_file_builtin(path, read_file_res)

    read_file_pd_res = read_from_file_pandas("data/text.csv")
    output_text_to_console(read_file_pd_res)
    write_to_file_builtin(path, read_file_pd_res)

if __name__ == "__main__":
    main()