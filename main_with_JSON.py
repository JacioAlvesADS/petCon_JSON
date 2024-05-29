import json
import os
from time import sleep

class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'

arquivo = os.path.join(os.path.dirname(__file__), 'usuarios.json')
pets_arquivo = os.path.join(os.path.dirname(__file__), 'pets.json')
abrigos = os.path.join(os.path.dirname(__file__), 'abrigos.json')

def carregar_usuarios():
    if not os.path.exists(arquivo):
        return []
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
    
def carregar_pets():
    pets = []
    try:
        if os.path.exists(pets_arquivo):
            with open(pets_arquivo, 'r') as f:
                pets = json.load(f)
        if not isinstance(pets, list):
            pets = []
    except (json.JSONDecodeError, FileNotFoundError):
        pass
    return pets

def carregar_abrigos():
    abrigos_list = []
    try:
        if os.path.exists(abrigos):
            with open(abrigos, 'r') as f:
                abrigos_list = json.load(f)
        if not isinstance(abrigos_list, list):
            abrigos_list = []
    except (json.JSONDecodeError, FileNotFoundError):
        pass
    return abrigos_list

def salvar_usuarios(usuarios):
    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

def salvar_pets(lista_pets):
    try:
        with open(pets_arquivo, 'w') as f:
            json.dump(lista_pets, f, indent=4, ensure_ascii=False)
    except IOError:
        print("😡 ERRO AO SALVAR PETS.")

def adicionar_usuario(nome, idade, email, senha, aptSize):
    usuarios = carregar_usuarios()
    usuarios.append({'nome': nome, 'idade': idade, 'email': email, 'senha': senha, 'aptSize': int(aptSize)})
    salvar_usuarios(usuarios)
    aptSize = int(aptSize)
    print("😎 USUÁRIO ADICIONADO COM SUCESSO!")

def adicionar_pet(nomePet, idadePet, racaPet, abrigo, tamanho):
    lista_pets = carregar_pets()
    lista_pets.append({'nomePet': nomePet, 'idadePet': idadePet, 'racaPet': racaPet, 'abrigo': abrigo, 'tamanho': tamanho})
    salvar_pets(lista_pets)
    print("😎 PET ADICIONADO COM SUCESSO!")

def listar_usuarios():
    usuarios = carregar_usuarios()
    if usuarios:
        print("=" * 50)
        print("LISTA DE USUÁRIOS:") 
        print("-" * 50)
        for usuario in usuarios:
            print("*" * 50)
            print(f"NOME: {usuario['nome']}, IDADE: {usuario['idade']}")
            print("*" * 50)
            print("=" * 50)
    else:
        print("😒 NENHUM USUÁRIO CADASTRADO.")

def encontrar_pets_adequados(aptSize):
    pets = carregar_pets()
    pets_adequados = []

    if aptSize <= 50:
        tamanho_adequado = "P"
    elif aptSize <= 100:
        tamanho_adequado = "M"
    else:
        tamanho_adequado = "G"

    for pet in pets:
        if pet['tamanho'] == tamanho_adequado:
            pets_adequados.append(pet)

    return pets_adequados

def listar_pets():
    listar_pets = carregar_pets()
    if listar_pets:
        print("=" * 50)
        print("LISTA DE PETS:") 
        print("-" * 50)
        for pets in listar_pets:
            print("*" * 50)
            print(f"NOME: {pets['nomePet']}, IDADE: {pets['idadePet']}")
            print("*" * 50)
            print("=" * 50)
    else:
        print("😒 NENHUM PET CADASTRADO.")

def listar_abrigos_disponiveis():
    abrigos_disponiveis = carregar_abrigos()
    if abrigos_disponiveis:
        print("=" * 50)
        print("ABRIGOS DISPONÍVEIS:")
        print("-" * 50)
        for abrigo in abrigos_disponiveis:
            print("*" * 50)
            print(f"NOME: {abrigo['nome']}, LOCALIZAÇÃO: {abrigo['localizacao']}")
            print("*" * 50)
            print("=" * 50)
    else:
        print("😒 NENHUM ABRIGO CADASTRADO.")

def adicionar_abrigo(nome, localizacao):
    abrigos_list = carregar_abrigos()
    abrigos_list.append({'nome': nome, 'localizacao': localizacao})
    with open(abrigos, 'w') as f:
        json.dump(abrigos_list, f, indent=4, ensure_ascii=False)
    print("😎 ABRIGO ADICIONADO COM SUCESSO!")

def atualizar_abrigo(nome_antigo, novo_nome, nova_localizacao):
    abrigos_list = carregar_abrigos()
    for abrigo in abrigos_list:
        if abrigo['nome'] == nome_antigo:
            abrigo['nome'] = novo_nome
            abrigo['localizacao'] = nova_localizacao
            with open(abrigos, 'w') as f:
                json.dump(abrigos_list, f, indent=4, ensure_ascii=False)
            print("😙 ABRIGO ATUALIZADO COM SUCESSO!")
            return
    print("😒 ABRIGO NÃO ENCONTRADO.")

def excluir_abrigo(nome):
    abrigos_list = carregar_abrigos()
    for abrigo in abrigos_list:
        if abrigo['nome'] == nome:
            abrigos_list.remove(abrigo)
            with open(abrigos, 'w') as f:
                json.dump(abrigos_list, f, indent=4, ensure_ascii=False)
            print("😡 ABRIGO EXCLUÍDO COM SUCESSO!")
            return
    print("😒 ABRIGO NÃO ENCONTRADO.")

def buscar_abrigo(nome):
    abrigos_list = carregar_abrigos()
    for abrigo in abrigos_list:
        if abrigo['nome'] == nome:
            print(f"NOME: {abrigo['nome']}, LOCALIZAÇÃO: {abrigo['localizacao']}")
            return
    print("😒 ABRIGO NÃO ENCONTRADO.")

def login(email_passado, senha_passada):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario['email'] == email_passado and usuario['senha'] == senha_passada:
            return True, usuario['nome']
    return False, None

def atualizar_usuario(nome_antigo, novo_nome, nova_idade):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario['nome'] == nome_antigo:
            usuario['nome'] = novo_nome
            usuario['idade'] = nova_idade
            salvar_usuarios(usuarios)
            print("😙 USUÁRIO ATUALIZADO COM SUCESSO!")
            return
    print("😒 USUÁRIO NÃO ENCONTRADO.")

def excluir_usuario(nome):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario['nome'] == nome:
            usuarios.remove(usuario)
            salvar_usuarios(usuarios)
            print("😡 USUÁRIO EXCLUÍDO COM SUCESSO!")
            return
    print("😒 USUÁRIO NÃO ENCONTRADO.")

def buscar_usuario(nome):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario['nome'] == nome:
            print(f"NOME: {usuario['nome']}, IDADE: {usuario['idade']}")
            return
    print("😒 USUÁRIO NÃO ENCONTRADO.")

def atualizar_pet(nome_antigo, novo_nome, nova_idade, nova_raca, novo_abrigo, novo_tamanho):
    lista_pets = carregar_pets()
    for pet in lista_pets:
        if pet['nomePet'] == nome_antigo:
            pet['nomePet'] = novo_nome
            pet['idadePet'] = nova_idade
            pet['racaPet'] = nova_raca
            pet['abrigo'] = novo_abrigo
            pet['tamanho'] = novo_tamanho
            salvar_pets(lista_pets)
            print("😙 PET ATUALIZADO COM SUCESSO!")
            return
    print("😒 PET NÃO ENCONTRADO.")

def menu_inicial():
    print(cor.CIANO + "=" * 55 + cor.RESET)
    print(cor.VERMELHO + " ---->>> BEM VINDO A PETCON <<<---- ")
    print("          1 - LOGIN ")
    print("          2 - MÓDULO ESTOQUE ")
    print("          3 - SAIR ")
    print(cor.CIANO + "=" * 55 + cor.RESET)

def exibir_menu():
    print("\nMENU:")
    print("1. Cadastrar-se")
    print("2. Fazer Login!")
    print("3. Listar Usuários")
    print("4. Atualizar Cadastro")
    print("5. Excluir usuário")
    print("6. Buscar usuário")
    print("7. Sair")

def main():
    while True:
        menu_inicial()
        try:
            opcao_inicial = int(input("INFORME UMA OPÇÃO: "))
        except ValueError:
            print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            continue

        if opcao_inicial == 1:
            while True:
                exibir_menu()
                opcao = input("ESCOLHA UMA OPÇÃO:\n>>> ")

                if opcao == "1":
                    nome = input("DIGITE O NOME:\n>>> ")
                    idade = input("DIGITE A IDADE:\n>>> ")
                    email = input("DIGITE O EMAIL:\n>>>")
                    senha = input("DIGITE A SENHA:\n>>>")
                    aptSize = input("DIGITE O TAMANHO DA SUA RESIDÊNCIA EM M²:\n>>>")
                    adicionar_usuario(nome, idade, email, senha, aptSize)
                elif opcao == "2":
                      email_passado = input("DIGITE O EMAIL:\n>>> ")
                      senha_passada = input("DIGITE A SENHA:\n>>> ")
                      sucesso, nome = login(email_passado, senha_passada)
                      if sucesso:
                          print(f"😎 BEM-VINDO, {nome}!")
                          while True:
                              
                              print("\nEscolha uma opção:\n1 - Adicionar novo Pet\n2 - Adotar um Pet\n3 - Alterar informações do pet\n4 - Excluir um Pet\n5 - Ver os pets disponíveis para adoção\n6 - Ver abrigos disponíveis\n7 - Encerrar a Sessão\n")
                              opcao_logado = input()

                            if opcao_logado == '1':
                                nomePet = input("Digite o nome do pet:\n>>> ")
                                idadePet = input("Digite a idade do pet:\n>>> ")
                                racaPet = input("Qual a raça do pet?\n>>> ")
                                abrigo = input("Qual abrigo o pet está?\n>>> ")
                                tamanho = input("Tamanho do pet P/M/G:\n>>> ")
                                adicionar_pet(nomePet, idadePet, racaPet, abrigo, tamanho)
                            elif opcao_logado == '2':
                                print("Buscando pets adequados...")
                                usuario_encontrado = False  
                                usuarios = carregar_usuarios()
                                print()
                                for usuario in usuarios:
                                    if usuario['email'] == email_passado: 
                                        usuario_encontrado = True 
                                        aptSize_usuario = usuario['aptSize']
                                        pets_adequados = encontrar_pets_adequados(aptSize_usuario)
                                        if pets_adequados:
                                            print("Pets adequados encontrados:")
                                            for i, pet in enumerate(pets_adequados, start=1):
                                                print(f"{i}. Nome: {pet['nomePet']}, Idade: {pet['idadePet']}, Raça: {pet['racaPet']}, Tamanho: {pet['tamanho']}")
                                            opcao_adocao = input("Selecione o número correspondente ao pet que deseja adotar (ou '0' para cancelar): ")
                                            if opcao_adocao.isdigit():
                                                opcao_adocao = int(opcao_adocao)
                                                if 0 < opcao_adocao <= len(pets_adequados):
                                                    pet_selecionado = pets_adequados[opcao_adocao - 1]
                                                    print(f"Você adotou o pet '{pet_selecionado['nomePet']}'!")
                                                    print("Restante dos Pets")
                                                    listar_pets()
                                                    
                                                else:
                                                    print("Opção inválida.")
                                            else:
                                                print("Opção inválida.")
                                        else:
                                            print("Nenhum pet adequado encontrado.")
                                        break 
                                if not usuario_encontrado:
                                    print("Usuário não encontrado.")
                            elif opcao_logado == '3':
                                nome_antigo = input("Digite o nome do pet a ser atualizado:\n>>> ")
                                novo_nome = input("Digite o novo nome do pet:\n>>> ")
                                nova_idade = input("Digite a nova idade do pet:\n>>> ")
                                nova_raca = input("Digite a nova raça do pet:\n>>> ")
                                novo_abrigo = input("Digite o novo abrigo do pet:\n>>> ")
                                novo_tamanho = input("Digite o novo tamanho do pet (P/M/G):\n>>> ")
                                atualizar_pet(nome_antigo, novo_nome, nova_idade, nova_raca, novo_abrigo, novo_tamanho)
                            elif opcao_logado == '4':
                                print(4)
                            elif opcao_logado == '5':
                                listar_pets()
                            elif opcao_logado == '6':
                                listar_abrigos_disponiveis()
                            elif opcao_logado == '7':
                                atualizar_usuario()
                            elif opcao_logado == '8':
                                break
                            else:
                                print("Opção inválida. Tente Novamente!")  
                    else:
                        print('Tente novamente!')
                elif opcao == "3":
                    listar_usuarios()
                elif opcao == "4":
                    nome_antigo = input("DIGITE O NOME A SER ATUALIZADO:\n>>> ")
                    novo_nome = input("DIGITE O NOVO NOME:\n>>> ")
                    nova_idade = input("DIGITE A NOVA IDADE:\n>>> ")
                    atualizar_usuario(nome_antigo, novo_nome, nova_idade)
                elif opcao == "5":
                    nome = input("DIGITE O NOME DO USUÁRIO A SER EXCLUÍDO:\n>>> ")
                    excluir_usuario(nome)
                elif opcao == "6":
                    nome = input("DIGITE O NOME DO USUÁRIO:\n>>> ")
                    buscar_usuario(nome)
                elif opcao == "7":
                    print("VOLTAR AO MENU ANTERIOR...")
                    sleep(2)
                    break
                else:
                    print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
        elif opcao_inicial == 2:
            print("MÓDULO EM DESENVOLVIMENTO")
        elif opcao_inicial == 3:
            print("🚀 SAINDO...")
            sleep(2)
            break
        else:
            print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()