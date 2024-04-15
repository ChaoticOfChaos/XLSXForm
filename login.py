import pandas as pd

def login() -> tuple:
    # Abre a tabela de logins
    tab = pd.read_csv('./User/Logins.csv')
    inpMail = input('E-mail -> ')
    inpPass = input('Password -> ')

    # Verifica se aquele E-mail existe na base-de-dados
    if (tab['Email']  == inpMail).any():
        # Caso exista, ele pega a senha daquele E-mail
        Pass = tab.loc[tab['Email'] == inpMail, 'Password'].values[0]

        # E compara para saber se a senha bate um com a outra
        if (Pass == inpPass):

            # Caso seja a mesma senha. Ele retorna uma tupla contendo: [0]Resposta do Login | [1]E-Mail | [2]Senha | [3]Nome do Usuário
            return (True, inpMail, inpPass, tab.loc[tab['Email'] == inpMail, 'Name'].values[0])
    
    # Caso o Login seja falho, a Resposta é falsa, e todos as infos são vazias
    return (False, '', '', '')