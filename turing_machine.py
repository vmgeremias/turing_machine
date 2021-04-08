# Começo o programa lendo  o arquivo de entrada e retirando o \n
print("Qual o nome do arquivo para leitura")
file = open(input(), "r")
linha = file.readline().replace("\n", "")
# A variavel de comandos será onde fica todas as instrucoes da nossa maquina de Turing
# A variaveis de estados_iniciados será utilizada para demarcar os novos estados e colocar nos comandos uma instrucao para caso o ponteiro
# chegar no simbolo de limite a esquerda, voltar para a direita.
comandos = []
estados_iniciados = []

# Leio a primeira linha da entrada para verificar o tipo de máquina
if (linha == ";S"):
    # Adiciono o novo tipo da máquina
    comandos.append([";I"])
    # Adiciono instrucoes para colocar o simbolo de limite a esquerda e modifico o estado inicial para um estado new0
    # Todos os estados na fita de estrada irão possui "new" na frente. Exemplo: 1 -> new1, 2 -> new2
    comandos.append(["0", "*", "*", "l", "firstIcon"])
    comandos.append(["firstIcon", "_", "¢", "r", "new0"])
    comandos.append(["firstIcon", "*", "*", "*", "new0"])

    linha = file.readline()
    # Iteração por linha
    while(linha != ""):
        # Verifico se a linha é um comentário e ignoro
        if (linha[0] == ";"):
            comandos.append([linha.replace("\n", "")])
            linha = file.readline()
            continue

        # realizo a divisão de cada segmento do comando e retiro o \n do final
        linha = linha.split(' ')
        linha[4] = linha[4].replace("\n", "")

        # Caso o estado não seja de parada (halt-reject ou halt-accept), adiciono o "new" na frente
        # e coloco a instrucao na variavel
        if (linha[4] != "halt-reject" and linha[4] != "halt-accept"):
            comandos.append(["new"+linha[0], linha[1], linha[2],
                             linha[3], "new"+linha[4]])
        else:
            comandos.append(["new"+linha[0], linha[1], linha[2],
                             linha[3], linha[4]])

        # Verifico se o estado já foi computado pelo menos uma vez, caso não coloco na lista e adiciono a instrucao
        # para caso chegue no limite pela esquerda nesse estado, ir para a direita
        if ("new"+linha[0] not in estados_iniciados):
            estados_iniciados.append("new"+linha[0])
            comandos.append(["new"+linha[0], "¢", "¢", "r", "new"+linha[0]])
        linha = file.readline()
    file.close()

    # Por fim coloco cada instrucao obtida no arquivo de saida
    file = open("out.txt", "w")
    for linha in comandos:
        # Tratamento para comentários
        if (linha[0][0] == ";"):
            file.write(linha[0]+"\n")
        else:
            file.write(
                ' '.join([linha[0], linha[1], linha[2], linha[3], linha[4]+"\n"]))

    file.close()
elif (linha == ";I"):
    # flag para saber se o estado first icon
    flag_firstIcon = 0
    # Adiciono o novo tipo da máquina
    comandos.append([";S"])
    linha = file.readline()
    # Iteração por linha
    while(linha != ""):
        # Verifico se a linha é um comentário e ignoro
        if (linha[0] == ";"):
            comandos.append([linha.replace("\n", "")])
            linha = file.readline()
            continue

        # realizo a divisão de cada segmento do comando e retiro o \n do final
        linha = linha.split(' ')
        linha[4] = linha[4].replace("\n", "")

        # Removo os comandos no qual possuem o simbolo de parada
        if ((linha[1] == "¢" and linha[2] == "¢") or linha[0] == "0"):
            linha = file.readline()
            continue

        # Caso o estado não seja de parada (halt-reject ou halt-accept), adiciono o "new" na frente
        # e coloco a instrucao na variavel
        if (linha[4] != "halt-reject" and linha[4] != "halt-accept" and "firstIcon" not in linha[0]):
            comandos.append(["new"+linha[0], linha[1], linha[2],
                             linha[3], "new"+linha[4]])
        # Fazer a instrucao para o novo caminho do estado inicial
        elif ("firstIcon" in linha[0] and flag_firstIcon == 0):
            novoInicio = linha[4]
            comandos.append(["0", "*", "*", "r", "auxInicio"])
            comandos.append(["auxInicio", "*", "*", "l", "new"+novoInicio])
            flag_firstIcon = 1
        else:
            comandos.append(["new"+linha[0], linha[1], linha[2],
                             linha[3], linha[4]])

        linha = file.readline()
    file.close()

    # Por fim coloco cada instrucao obtida no arquivo de saida
    file = open("out.txt", "w")
    for linha in comandos:
        # Tratamento para comentários
        if (linha[0][0] == ";"):
            file.write(linha[0]+"\n")
        else:
            file.write(
                ' '.join([linha[0], linha[1], linha[2], linha[3], linha[4]+"\n"]))

    file.close()
else:
    print("Máquina não detectada")
