def output_text_to_console(text):
    print(text)

def write_to_file_builtin(file_path, text):
    with open(file_path, "w") as file:
        file.write(text + "\n")
