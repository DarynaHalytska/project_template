import pandas as pd

def input_text_from_console():
    return input("Введіть текст: ")

def read_from_file_builtin(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data

def read_from_file_pandas(file_path):
    data = pd.read_csv(file_path)
    return data.to_string()
