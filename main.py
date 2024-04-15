# Importa as todas as funções para um único arquivo
from login import login
from register import register
from form import form
from help import Help

# Função usada para pegar o diretório atual
from os import getcwd

def main():
    print('-'*20)

    # Verifica se o usuário já efetuou o login, e anota as infos do usuário
    logedin = False
    email = ''
    password = ''
    name = ''

    while True:
        userInput = input('> ')

        match userInput.lower():
            case 'help':
                Help()

            case '?':
                Help()

            case 'login':
                # Caso você tente fazer o login duas vezes, ele não permite. Faça o logout antes
                if (logedin):
                    print(f'Login already done, {name}')

                else:
                    # Efetua o Login
                    l = login()
                    if (l[0]):
                        logedin = True
                        email = l[1]
                        password = l[2]
                        name = l[3]
                        print(f'Login successfully!, Welcome Back, {name}!')

                    else:
                        print('Login Error')

            # O Logout apenas apaga as infos que já tinhamos e coloca o verificador em falso
            case 'logout':
                logedin = False
                email = ''
                password = ''
                name = ''

            case 'register':
                if (register()):
                    print('Registration completed successfully!')
                else:
                    print('Registration Error. Try Again')

            case 'form':
                # Não permite fazer um formulário sem antes fazer login
                if (logedin):
                    r = form(email, name)
                    print(f'Analysis saved in: {getcwd()}\\{r}.txt')
                    
                else:
                    print('Login must be done before')
                
            case 'exit':
                break

        print('-'*20)
        print(' ')
        print('-'*20)


if (__name__ == '__main__'):
    main()