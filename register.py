import pandas as pd

def register() -> bool:
    # Abre a tabela de logins
    tab = pd.read_csv('./User/logins.csv')

    # Faz um formulário básico para criar uma conta
    inpMail = input('E-Mail -> ')
    inpPass = input('Password -> ')
    confPass = input('Confirm Password -> ')
    inpName = input('Name -> ')
    # Verifica se: Aquele E-mail já foi cadastrado || Se a senha bate com a confirmação de senha || e se as informações não são vazias
    if (tab['Email'] == inpMail).any() or not inpPass == confPass or '' in [inpMail, inpPass, confPass, inpName]:
        return False
    
    # Caso tudo tenha dado certo, ele adiciona as infos no banco de dados
    length = len(tab['Email'])
    tab.loc[length, 'Email'] = inpMail
    tab.loc[length, 'Password'] = inpPass
    tab.loc[length, 'Name'] = inpName
    tab.to_csv('./User/logins.csv', index=False)
    return True