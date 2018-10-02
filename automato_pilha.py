# -*- coding: utf-8 -*-

def first_validations(word, config):
    valide_value = config[1]

    # Verifica se caracteres em word estão no alfabeto de entrada
    for i in word:
        if i not in valide_value:
            print ("-3: Valor inserido na palavra incorreto")
            return -3
    
    # Verifica se valor de epsilon não pertence ao alfabeto de entrada ou da pilha
    if (config[3][0] in valide_value or config[3][0] in config[2]):
        print ("-4: Epsilon inválido")
        return -4

    return 0

def machine(config, word, transitions):
    # Cria fila para controle do fluxo
    q = []
    stack = []

    validator = first_validations(word, config)

    if ((validator == -3) or (validator == -4)): # Verificação Falhou
        return -1

    stack.insert(0, config[4][0]) # Insere símbolo inicial na pilha
    
    # Configurações da máquina
    setting = {
        "word": word,
        "current_state": config[6][0],
        "stack": stack
    }
    
    # Insere elemento no final da fila
    q.append(setting)

    while True:        
        # Encontrou estado final
        if (((q[0]['current_state'] in config[7]) or (len(q[0]['stack']) == 0)) & (len(q[0]['word']) == 0)):
            
            print ("0: Computação terminada e aceita.")
            print (setting)
            return 0
        
        # Encontra transições possíveis
        for i in range(1, len(transitions) + 1, 1):
            if ((q[0]['current_state'] == transitions[i][0]) and # Estado atual == Estado da transição
            ((transitions[i][2] == config[3][0]) or ((len(q[0]['stack']) != 0) and (q[0]['stack'][0] == transitions[i][2]))) and # Topo fita == topo transição (se existir topo) ou topo transição == ε
            ((transitions[i][1] == config[3][0]) or ((len(q[0]['word']) != 0) and (q[0]['word'][0] == transitions[i][1])))): # Primeira letra da palavra == primeira letra da transição (se existir primeira letra) ou letra da transição == ε
                
                new_stack = {}

                new_word = q[0]['word']
                if ((transitions[i][1] != config[3][0])): # Letra da transição != ε, tira 1ª letra da palavra
                    new_word = new_word[1:]

                new_stack = q[0]['stack'][:]
                if (transitions[i][2] != config[3][0]): # Alfabeto do topo da pilha (transição) != ε, tira o topo da pilha
                    new_stack.pop(0)
                
                if (transitions[i][4] != config[3][0]): # Alfabeto de adição à pilha (transição) != ε, adiciona no topo da pilha
                    new_stack.insert(0, transitions[i][4])
                

                new_setting = {
                    "word": new_word,
                    "current_state": transitions[i][3],
                    "stack": new_stack
                }

                q.append(new_setting) # Insere no final da fila
        
        # Encerrou as opções possíveis e não encontrou estado final
        if (len(q) == 1): # q só tem q[0]
            print ("-1: Computação terminada e rejeitada.")
            print (setting)
            return -1

        # Configura máquina para próximo estado
        setting["word"] = q[1]["word"]
        setting["current_state"] = q[1]["current_state"]
        setting["stack"] = q[1]["stack"]
        q.pop(0) # Tira estado atual da fila
