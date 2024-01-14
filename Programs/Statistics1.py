#Os dados estão enviesados a cada 6 bits pois transformando os bits em inteiros esperávamos uma distribuição normal
#Mas a existem intervalos de números em que não houve sequer um único inteiro atribúido
#Logo os dados estão enviesados

import matplotlib.pyplot as plt


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
teste = convert_to_string(teste)

teste = [int(x) for x in teste]
size = len(teste)
int_list = []
i = 0

while (i + 6) <=  size:
    new_int = 0
    for j in range(0, 6):
        new_int += teste[i + j] * 2**(5-j)
    
    int_list.append(new_int)
    i += 6


def plot_histogram(int_list):
    plt.hist(int_list, bins=max(int_list)-min(int_list)+1, align="left", edgecolor="black") #(esta linha pertence `a de cima)
    plt.xlabel("Integers")
    plt.ylabel("Frequency")
    plt.title("Histogram of Integers")
    plt.grid(True)
    plt.show()

plot_histogram(int_list)    
