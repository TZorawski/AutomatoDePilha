import sys
import automato_pilha


def read_file():
    config = {}
    transition = {}
    aux = 0
    file_name = sys.argv[1]
    file_name = str(file_name)
    file = open(file_name, 'r')
    for i in range(1, 8):
        conteudo = file.readline().strip('\n').split(' ')
        config[i] = conteudo
    for i in file:
        aux = aux + 1
        transition[aux] = i.strip('\n').split(' ')
    return config, transition

def read_stack():
    stack = sys.argv[2]
    return stack

def main():
    read_file()
    read_tapes()
    config = {}
    transitions = {}
    stack = []
    config, transitions = read_file()
    stack = read_stack()
    #automato_pilha.machine(config, stack, transitions)

main()
