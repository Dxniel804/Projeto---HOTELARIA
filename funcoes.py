from dicionario import *
import os

def lean():
    print('════════════════════════════════════════════════ ♦️')

def cadast():
    loop = 1
    while loop == 1:
        print("╔════════════════════════════════════════════════╗")
        print("║              ♦️  PalaceHotel  ♦️                 ║")
        print("║                                                ║")
        print("║════════════════════════════════════════════════║")
        print("║   1.  CADASTRAR   ✏️                           ║")
        print("║                                                ║")
        print("║════════════════════════════════════════════════║")
        print("║   2.  LOGIN  🔑                                ║")
        print("║                                                ║")
        print("║════════════════════════════════════════════════║")
        print("║   3.  SAIR  🚪                                 ║")
        print("║                                                ║")
        print("╚════════════════════════════════════════════════╝")
        print("")
        print("Selecione a opção")
        print("")
        var = int(input("------> "))
        os.system("cls")

        if var == 1:
            cadastrar_cliente()
        elif var == 2:
            entrar_cliente()
        elif var == 3:
            loop = 0
            print('SAINDO...')
        else:
            print('Opção inválida, tente novamente.')

def cadastrar_cliente():
    print("╔════════════════════════════════════════════════╗")
    print("║                ♦️  CADASTRO  ♦️                  ║")
    print("║                Seja bem vindo                  ║")
    print("╚════════════════════════════════════════════════╝")
    
    nome_usuario = input("Digite seu nome de usuário: ")
    lean()
    criar_email = input("Digite o email: ")
    lean()
    criar_senha = input("Digite a senha: ")
    lean()
    verificar_senha = input("Digite sua senha novamente:")
    while j == 1: 
        if verificar_senha == criar_senha:
            print("\n- SENHA CRIADA")
            break
        else:
            print("Senha incorreta. Tente novamente.")
        criar_senha = input("Digite a senha: ")
        verificar_senha = input("Digite sua senha novamente:")
    lean()
    idade = int(input("Informe sua idade: "))
    lean()
  
    if idade > 100:
        print('Tente novamente..')
        lean()
        os.system('pause')
        os.system('cls')

    elif idade >= 18:
        cadastro.append({
            "nome": nome_usuario,
            "email": criar_email,
            "senha": criar_senha,
        })
        print("AGUARDE...")
        lean()
        print("Você se cadastrou com sucesso.")

    else:
        print('')
        lean()
        print("Desculpe, você deve ter pelo menos 18 anos para se cadastrar.")
        lean()
    os.system("pause")
    os.system("cls")

def entrar_cliente():
    print("╔════════════════════════════════════════════════╗")
    print("║                ♦️   ENTRAR   ♦️                  ║")
    print("║                Seja bem vindo                  ║")
    print("╚════════════════════════════════════════════════╝")
    
    entrar_email = input("Diga seu email \n--> ")
    lean()
    entrar_senha = input("Diga sua senha \n--> ")
    lean()

    if entrar_email == admin_email and entrar_senha == admin_password:
        print("Email e senha corretos")
        lean()
        os.system('pause')
        os.system('cls')

        print("BEM VINDO !")
        lean()
        senha_admin = input("Digite a senha do Admin: ")
        lean()
        if senha_admin == admin_password:
            local_admin()
        else:
            print("Senha ADM incorreta")
            lean()

    else:
        for user in cadastro:
            if entrar_email == user["email"] and entrar_senha == user["senha"]:
                print("Email e senha corretos")
                lean()
                os.system('pause')
                os.system('cls')

                print("BEM VINDO !")
                lean()
                local_cliente()
                return
        print("Email ou Senha estão incorretos")
        lean()
        os.system('pause')
        os.system('cls')
    
def local_admin():
    while True:  # Loop para o menu da área administrativa
        print("╔════════════════════════════════════════════════╗")
        print("║         ♦️  Área de Administração  ♦️            ║")
        print("╚════════════════════════════════════════════════╝")
        print('')
        print("1 - Cadastrar Atendente")
        print("2 - Listar Atendentes")
        print("3 - LOGIN ATENDENTE")
        print("4 - Sair")
        escolha = int(input("---> "))  # Recebe a escolha do administrador
        os.system('pause')
        os.system('cls')

        if escolha == 1:
            cadastrar_atendente()  # Chama a função para cadastrar atendente
        elif escolha == 2:
            listar_atendentes()  # Chama a função para listar atendentes
        elif escolha == 3:
            login_atendente()
        elif escolha == 4:
            break  # Encerra o loop e sai do menu
        else:
            print("Opção inválida. Tente novamente.")
        os.system("pause")
        os.system("cls")

def cadastrar_atendente():
    print("╔════════════════════════════════════════════════╗")
    print("║         ♦️  Cadastrar Atendente  ♦️              ║")
    print("╚════════════════════════════════════════════════╝")
    print('')
    nome_atendente = input("Nome do atendente: ")  # Solicita o nome do atendente
    senha_atendente = input("Senha do atendente: ")  # Solicita a senha do atendente
    
    atendentes.append({
        "nome": nome_atendente,
        "senha": senha_atendente
    })  # Adiciona o atendente à lista de atendentes

    print("Atendente cadastrado com sucesso. Obrigado!!")
    os.system("pause")
    os.system("cls")

def login_atendente():
    print("╔════════════════════════════════════════════════╗")
    print("║         ♦️  Login Atendente  ♦️                  ║")
    print("╚════════════════════════════════════════════════╝")
    aten_nome = input("Digite seu nome: ")
    aten_senha = input('Digite sua senha novamente: ')
    print('')
    os.system("cls")
    

    for atendente in atendentes:
        if aten_senha == atendente['senha'] and aten_nome == atendente['nome']:
            print('Login feito com sucesso')
            os.system('pause')
            os.system('cls')
            local_atendente()
            return
    print('Nome ou senha incorreto. Tente novamente...')
    os.system('pause')
    os.system('cls')

def listar_atendentes():
    print("╔════════════════════════════════════════════════╗")
    print("║         ♦️  Lista de Atendentes  ♦️              ║")
    print("╚════════════════════════════════════════════════╝")
    if atendentes:
        for e, atendente in enumerate(atendentes, 1):
            print(f"{e}. Nome: {atendente['nome']}")  # Lista os atendentes cadastrados
    else:
        print("Nenhum atendente cadastrado.")
    os.system("pause")
    os.system("cls")

def local_atendente():
    while True:
        print("╔════════════════════════════════════════════════╗")
        print("║         ♦️  Área de Atendente  ♦️                ║")
        print("╚════════════════════════════════════════════════╝")
        print('')
        print('1. Alugar o quarto')
        print('2. Sair')
        escolha1 = int(input('--> '))
        os.system('cls')

        if escolha1 == 1:
            alugue_quarto(quartos_economicos, quartos_intermediarios, quartos_luxuosos)

        elif escolha1 == 2:
            break
        else:
            print('OPÇÃO INVALIDA...')
            os.system("pause")
            os.system("cls")

def alugue_quarto(quartos_economicos, quartos_intermediarios, quartos_luxuosos):
    print("╔════════════════════════════════════════════════╗")
    print("║         ♦️  Alugue Quarto  ♦️                    ║")
    print("╚════════════════════════════════════════════════╝")
    print('')
    nume_quarto = int(input('Digite o numero do quarto que deseja alugar para o cliente: '))

    for quartos in [quartos_economicos, quartos_intermediarios, quartos_luxuosos]:
        if nume_quarto in quartos:
            if quartos[nume_quarto]['status'] == 'Reservado':
                quartos[nume_quarto]['status'] = 'Alugado'
                print(f"Quarto {nume_quarto} alugado com sucesso!")
            else:
                print(f"Quarto {nume_quarto} não está reservado ou já está alugado.")
            break
    else:
        print(f"Quarto {nume_quarto} não foi encontrado.")
    os.system("pause")
    os.system("cls")

def mostraros_quartos(quartos):
    for numero, detalhes in quartos.items():
        print(f"Quarto {numero}: {detalhes['descricao']} - Status: {detalhes['status']}")

def local_cliente():
    while True:  # Loop para o menu da área de cliente
        print("╔════════════════════════════════════════════════╗")
        print("║         ♦️  Área de Cliente  ♦️                  ║")
        print("╚════════════════════════════════════════════════╝")
        print("")
        print("1. Quartos disponíveis e reservas")
        print("2. minhas reservas")
        print("3. Sair")
        escol = int(input("---> "))  # Recebe a escolha do cliente
        os.system("cls")

        if escol == 1:
            print("1 - Quartos econômicos ")
            print("2 - Quartos intermediários")
            print("3 - Quartos de luxo")
            print("4 - Sair")
            var_quartos = int(input("---> "))  # Recebe a escolha do tipo de quarto que o cliente tem interesse
            os.system("cls")

            if var_quartos == 1:
                print("Quartos econômicos disponíveis:\n")
                mostraros_quartos(quartos_economicos)
                print('')
                os.system("pause")
                lean()
                escolha_economico = int(input("Digite o numero do quarto para reserva: "))
                print("")
                if escolha_economico in quartos_economicos:
                    if quartos_economicos[escolha_economico]['status'] == 'Disponivel\n':
                        quartos_economicos[escolha_economico]['status'] = 'Reservado'
                        print(f"- Quarto {escolha_economico} reservado com sucesso!!!") 
                    else:
                        print('Este quarto está ocupado') 
                else:
                    print('Número de quarto inválido')
                os.system('pause')
                os.system("cls")
            
            elif var_quartos == 2:
                print("Quartos intermediários disponíveis:\n")
                mostraros_quartos(quartos_intermediarios)
                print('')
                os.system("pause")
                lean()
                escolha_intermediaria = int(input("Digite o numero do quarto para reserva: "))
                print("")
                if escolha_intermediaria in quartos_intermediarios:
                    if quartos_intermediarios[escolha_intermediaria]['status'] == 'Disponivel\n':
                        quartos_intermediarios[escolha_intermediaria]['status'] = 'Reservado'
                        print(f"- Quarto {escolha_intermediaria} reservado com sucesso!!!") 
                    else:
                        print('Este quarto está ocupado')
                else:
                    print('Número de quarto inválido')
                os.system('pause')
                os.system("cls")

            elif var_quartos == 3:
                print("Quartos luxuosos disponíveis:\n")
                mostraros_quartos(quartos_luxuosos)
                print('')
                os.system("pause")
                lean()
                escolha_luxuosa = int(input("Digite o numero do quarto para reserva: "))
                print("")
                if escolha_luxuosa in quartos_luxuosos:
                    if quartos_luxuosos[escolha_luxuosa]['status'] == 'Disponivel\n':
                        quartos_luxuosos[escolha_luxuosa]['status'] = 'Reservado'
                        print(f"- Quarto {escolha_luxuosa} reservado com sucesso!!!") 
                    else:
                        print('Este quarto está ocupado')
                else:
                    print('Número de quarto inválido')
                os.system('pause')
                os.system("cls")

            elif var_quartos == 4:
                os.system('cls')
                break

            else:
                print("Opção inválida! Tente novamente.")
                os.system("pause")
                os.system("cls")
        
        elif escol == 2:
            print("╔════════════════════════════════════════════════╗")
            print("║         ♦️  MINHAS RESERVAS  ♦️                  ║")
            print("╚════════════════════════════════════════════════╝")
            os.system("cls")
            os.system("pause")

            
       
       
       
        elif escol == 3:
            os.system('cls')
            break

        else:
            print("Opção inválida! Tente novamente.")
            os.system("pause")
            os.system("cls")

cadast()