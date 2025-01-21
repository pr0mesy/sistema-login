# Dicionário para armazenar os usuários e suas respectivas senhas
usuarios = {}

# Loop principal para o menu do sistema
while True:
    # Exibição do menu e solicitação de opção do usuário
    opcao = input('''
               
    (1) - Cadastrar
    (2) - Fazer Login 
    (3) - Sair
               
Escolha uma opção: ''')

    # Estrutura match-case para lidar com as diferentes opções
    match opcao:
        case '1':  # Opção de cadastro de usuário
            print("\n=== Cadastro de Usuário ===")
            novouser = input('Digite o seu usuário: ')  # Solicita o nome de usuário

            # Verifica se o nome de usuário já existe
            if novouser in usuarios:
                print('Nome de usuário existente. Tente outro nome!')
            else:
                # Solicita uma senha e cadastra o usuário no dicionário
                novasenha = input('Agora crie uma senha: ')
                usuarios[novouser] = novasenha  # Adiciona o par usuário: senha ao dicionário
                print("Cadastro realizado com sucesso!")

        case '2':  # Opção de login
            print("\n=== Login ===")
            # Permite até 3 tentativas de login
            for i in range(3):    
                userlogin = input('Digite o seu usuário: ')  # Solicita o nome de usuário
                senhalogin = input('Digite a sua senha: ')  # Solicita a senha

                # Verifica se o usuário e a senha estão corretos
                if userlogin in usuarios and usuarios[userlogin] == senhalogin:
                    print(f'Seja bem-vindo(a) novamente, {userlogin}!')
                    break  # Sai do laço de tentativas ao fazer login com sucesso
                else:
                    print('Usuário e/ou senha incorretos. Tente novamente.')
            else:  
                # Exibido apenas se todas as 3 tentativas falharem
                print('Você fez muitas tentativas incorretas. Tente novamente mais tarde.')

        case '3':  # Opção para sair do sistema
            print('Saindo do sistema... Até logo!')
            break  # Encerra o loop principal e finaliza o programa

        case _:  # Opção inválida
            print('Digite uma opção válida!')
