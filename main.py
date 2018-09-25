import sys
import automato_pilha

def read_file():
    config = {}
    transition = {}

    aux = 0
    file_name = str(sys.argv[1])
    file = open(file_name, 'r')
    
    for i in range(1, 8):
        conteudo = file.readline().strip('\n').split(' ')
        config[i] = conteudo
    
    for i in file:
        aux = aux + 1
        transition[aux] = i.strip('\n').split(' ')
    return config, transition

def read_word():
    word = sys.argv[2]
    return word

def main():
    read_file()
    read_word()

    config = {}
    transitions = {}
    
    config, transitions = read_file()
    word = read_word()
    
    automato_pilha.machine(config, word, transitions)

main()
