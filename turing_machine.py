# Começo o programa lendo  o arquivo de entrada e retirando o \n
file = open("entrada.in", "r")
linha = file.readline().replace("\n", "")
# A variavel de comandos será onde fica todas as instrucoes da nossa maquina de Turing
comandos = []
estados_estacionarios = 0

# Estados necessarios caso a palavra seja vazia e não escrever sem querer um branco
# o verdadeiro estado inicial (normalmente sendo 0) é 0init
comandos.append(["0", "_", '£', "l", "firstIcon"])
comandos.append(["0", "0", '0', "l", "firstIcon"])
comandos.append(["0", "1", '1', "l", "firstIcon"])
comandos.append(["firstIcon", "_", '¢', "r", "step"])
comandos.append(["step", "_", '£', "l", "returnFirst"])
comandos.append(["step", "0", '0', "r", "step"])
comandos.append(["step", "1", '1', "r", "step"])
comandos.append(["step", "£", '£', "r", "step"])
comandos.append(["returnFirst", "£", '£', "l", "returnFirst"])
comandos.append(["returnFirst", "0", '0', "l", "returnFirst"])
comandos.append(["returnFirst", "1", '1', "l", "returnFirst"])
comandos.append(["returnFirst", "¢", '£', "r", "0init"])

# Iteração por linha
while(linha != ""):
    # Verifico se a linha é um comentário e ignoro
    if (linha[0] == ";" or linha[0] == "\n"):
        linha = file.readline()
        continue

    # Realizo a divisão de cada segmento do comando e retiro o \n do final
    linha = linha.split(' ')
    linha[4] = linha[4].replace("\n", "")

    # Caso for o estado 0 troco por 0init
    linha[0] = "0init" if linha[0] == "0" else linha[0]
    linha[4] = "0init" if linha[4] == "0" else linha[4]

    # Faço a verificação para ver se é um estado estacionario
    # sempre preciso verificar se o comando escreve _
    # caso sim, mude para o simbolo £
    # Em alguns casos faço dois comandos para branco
    if (linha[3] == "*"):
        if (linha[1] == "_" and linha[2] == "_"):
            comandos.append([linha[0], linha[1], '£', "r",
                             "est"+str(estados_estacionarios)])
            comandos.append([linha[0], '£', '£', "r",
                             "est"+str(estados_estacionarios)])
            comandos.append(["est"+str(estados_estacionarios),
                             "0", "0", "l", linha[4]])
            comandos.append(["est"+str(estados_estacionarios),
                             "1", "1", "l", linha[4]])
            comandos.append(["est"+str(estados_estacionarios),
                             "_", "£", "l", linha[4]])
            comandos.append(["est"+str(estados_estacionarios),
                             "£", "£", "l", linha[4]])
        elif (linha[1] == "_"):
            comandos.append([linha[0], linha[1], linha[2], "r",
                             "est"+str(estados_estacionarios)])
            comandos.append([linha[0], "£", linha[2], "r",
                             "est"+str(estados_estacionarios)])
            comandos.append(["est"+str(estados_estacionarios),
                             "0", "0", "l", linha[4]])
            comandos.append(["est"+str(estados_estacionarios),
                             "1", "1", "l", linha[4]])
            comandos.append(["est"+str(estados_estacionarios),
                             "_", "£", "l", linha[4]])
            comandos.append(["est"+str(estados_estacionarios),
                             "£", "£", "l", linha[4]])
        elif(linha[2] == "_"):
            comandos.append([linha[0], linha[1], '£', "r",
                             "est"+str(estados_estacionarios)])
            comandos.append(["est"+str(estados_estacionarios),
                             "0", "0", "l", linha[4]])
            comandos.append(["est"+str(estados_estacionarios),
                             "1", "1", "l", linha[4]])
            comandos.append(["est"+str(estados_estacionarios),
                             "_", "£", "l", linha[4]])
            comandos.append(["est"+str(estados_estacionarios),
                             "£", "£", "l", linha[4]])
        else:
            comandos.append([linha[0], linha[1], linha[2], "r",
                             "est"+str(estados_estacionarios)])
            comandos.append(["est"+str(estados_estacionarios),
                             "0", "0", "l", linha[4]])
            comandos.append(["est"+str(estados_estacionarios),
                             "1", "1", "l", linha[4]])
            comandos.append(["est"+str(estados_estacionarios),
                             "_", "£", "l", linha[4]])
            comandos.append(["est"+str(estados_estacionarios),
                             "£", "£", "l", linha[4]])
        estados_estacionarios += 1
    else:
        if (linha[1] == "_" and linha[2] == "_"):
            comandos.append([linha[0], linha[1], '£', linha[3], linha[4]])
            comandos.append([linha[0], '£', '£', linha[3], linha[4]])
        elif (linha[1] == "_"):
            comandos.append([linha[0], linha[1], linha[2], linha[3], linha[4]])
            comandos.append([linha[0], '£', linha[2], linha[3], linha[4]])
        elif(linha[2] == "_"):
            comandos.append([linha[0], linha[1], '£', linha[3], linha[4]])
        else:
            comandos.append([linha[0], linha[1], linha[2], linha[3], linha[4]])

    linha = file.readline()
file.close()

# Por fim coloco cada instrucao obtida no arquivo de saida
file = open("saida.out", "w")
for linha in comandos:
    file.write(
        ' '.join([linha[0], linha[1], linha[2], linha[3], linha[4]+"\n"]))

file.close()
