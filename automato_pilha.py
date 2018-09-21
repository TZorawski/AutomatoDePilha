# Preenche word com valores do arquivo
def validate_word(word, config):
    valide_value = config[1]
    valide_value = valide_value + config[3]
    for i in word:
        if i not in valide_value:
            print ("-3: Valor inserido na fita incorreto")
            return -3
    return word

def machine(config, word, transitions):
    # Cria fila para controle do fluxo
    q = []
    validate_word(word, config)

    if (word == -1): # Valores inválidos na fita
        return -1
    
    # Configurações da máquina
    setting = {
        "word": word,
        "current_state": config[5][0],
        "stack": stack,
        "counter": 500 # Contador que 'verifica' looping
    }
    
    # Insere elemento no final da fila
    q.append(setting)

    while True:
        word = setting["word"]
        
        # Encontrou estado final
        if (q[0]['current_state'] in config[6]):
            print ("0: Computação terminada e aceita.")
            print (setting)
            return 0
            
        # Se a máquina estiver em looping
        if (q[0]['counter'] == 0):
            print ("-2: Computação não terminada. (interrupção por looping)")
            print (setting)
            return -2

        # Pega posição da fita na configuração atual
        head = q[0]['head_word']

        # Encontra transições possíveis
        for i in range(1, len(transitions) + 1, 1):
            # Se estado_atual_maquina == estado_atual_fita e letra_fita == letra_transicao
            if ((q[0]['current_state'] == transitions[i][0]) and (word[head] == transitions[i][2])):
                # Nova disposição da fita
                new_word = word
                # -> Troca letra_fita por nova_letra_transicao
                if (head > 0):
                    new_word = (word[0:head] + transitions[i][3]) + word[head + 1:]
                else:
                    new_word = transitions[i][3] + word[head + 1:]

                # Nova posição da head da fita
                new_head_word = head
                if (transitions[i][4] == 'R'):
                    # Adiciona espaço em branco no final da word
                    if (new_head_word == len(new_word) - 1):
                        new_word = (new_word) + config[3][0]
                    
                    new_head_word = new_head_word + 1 # Moveu para direita
                elif (transitions[i][4] == 'L'):
                    # Adiciona espaço em branco no início da word
                    if (new_head_word == 0):
                        new_word = config[3][0] + (new_word)
                        new_head_word += 1
                    
                    new_head_word = new_head_word - 1 # Moveu para esquerda
                else:
                    new_head_word = new_head_word # Mantêm na mesma posição

                new_setting = {
                    "word": new_word,
                    "current_state": transitions[i][1],
                    "word": new_word
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
        setting["head_stack"] = q[1]["head_stack"]
        setting["counter"] = q[1]["counter"]
        q.pop(0) # Tira estado atual da fila

