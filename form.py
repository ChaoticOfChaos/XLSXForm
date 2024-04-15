import random as rnd

def form(email: str, name: str) -> str:
    # Pergunta qual a localização do arquivo
    xlsxPath = input('Excel File Path -> ')

    # Perguntas genéricas W.I.P
    resp1 = input('Tabela é Importante? [y/n] ')
    resp2 = input('Houve Lucro na Tabela? [y/n] ')
    resp3 = input('Tabela com Mais de 500 Linhas? [y/n] ')
    resp4 = input('Tabela com Mais de 15 Colunas? [y/n] ')
    resp5 = input('Tabela já Foi Analizada Antes? [y/n] ')

    # Engenhoca responsável por criar um nome aleatório para o arquivo
    rNameList = [rnd.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(8)]
    rName = ''
    for char in rNameList:
        rName += char

    # Cria o .txt do formulário
    with open(f'./{rName}.txt', 'w') as file:
        file.write(xlsxPath + '\n')
        file.write(f'Analise Por: {name}/{email}\n')
        file.write('\n')
        file.write(f'Tabela e Importante? {resp1}\n')
        file.write(f'Houve Lucro na Tabela? {resp2}\n')
        file.write(f'Tabela com Mais de 500 Linhas? {resp3}\n')
        file.write(f'Tabela com Mais de 15 Colunas? {resp4}\n')
        file.write(f'Tabela ja Foi Analizada Antes? {resp5}\n')

    # Retorna o nome do arquivo
    return rName