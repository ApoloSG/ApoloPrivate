













def read_txt_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = file.read().replace("\n", "")
        return data.strip()
    except FileNotFoundError:
        return "File not found."
    

def convert_to_string(data):
    lines = data.split("\n")
    binary_string = "".join(lines)
    return binary_string


teste = read_txt_file("seq1.txt")
