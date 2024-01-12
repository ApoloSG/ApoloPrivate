from math import erfc, sqrt

def read_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read().replace('\n', '')  
            return data.strip()  
    except FileNotFoundError:
        return "File not found."

def convert_to_string(data):

    lines = data.split('\n')  
    binary_string = ''.join(lines)  
    return binary_string


def transform_list(string:str):
    return [int(x) for x in string]


def counters(mylist:list):
    Sn = 0
    n0 = 0
    n1 = 1

    for x in mylist:
        if x == 0:
            n0 += 1
            Sn += -1
        else:
            n1 += 1
            Sn += 1

    return [n0, n1, Sn, len(mylist)]


def calculate_Pv(mylist:list):
    Sobs = (abs(mylist[2]))/(mylist[3])
    return erfc(Sobs/(sqrt(2)))




def main():
    teste = read_txt_file("seq1.txt")
    teste = convert_to_string(teste)
    teste = transform_list(teste)
    teste = counters(teste)
    return calculate_Pv(teste)

print(main())





# Obrigado ChatGPT
