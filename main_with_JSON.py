import json
import os
from time import sleep

class Cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'

arquivo = os.path.join(os.path.dirname(__file__), 'usuarios.json')
pets_arquivo = os.path.join(os.path.dirname(__file__), 'pets.json')
abrigos_arquivo = os.path.join(os.path.dirname(__file__), 'abrigos.json')

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

def salvar_abrigos(abrigos_list):
    try:
        with open(abrigos, 'w') as f:
            json.dump(abrigos_list, f, indent=4, ensure_ascii=False)
    except IOError:
        print("ERRO AO SALVAR ABRIGOS.")

def adicionar_usuario(nome, idade, email, senha, aptSize):
    usuarios = carregar_usuarios()
    usuarios.append({'nome': nome, 'idade': idade, 'email': email, 'senha':senha, 'aptSize': aptSize})
    salvar_usuarios(usuarios)
    print("😎 USUÁRIO ADICIONADO COM SUCESSO!")

def adicionar_pet(nomePet, idadePet, racaPet, abrigo, tamanho):
    lista_pets = carregar_pets()
    lista_pets.append({'nomePet': nomePet, 'idadePet': idadePet, 'racaPet': racaPet, 'abrigo': abrigo, 'tamanho': tamanho})
    salvar_pets(lista_pets)
    print("😎 PET ADICIONADO COM SUCESSO!")

def cadastrar_abrigo(nome_abrigo, endereco_abrigo, capacidade):
    abrigos_list = carregar_abrigos()
    abrigos_list.append({'nome_abrigo': nome_abrigo, 'endereco_abrigo': endereco_abrigo, 'capacidade': capacidade})
    salvar_abrigos(abrigos_list)
    print("ABRIGO CADASTRADO COM SUCESSO!")

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

def listar_pets():
    listar_pets = carregar_pets()
    if listar_pets:
        print("=" * 50)
        print("LISTA DE pets:") 
        print("-" * 50)
        for pets in listar_pets:
            print("*" * 50)
            print(f"NOME: {pets['nomePet']}, IDADE: {pets['idadePet']}")
            print("*" * 50)
            print("=" * 50)
    else:
        print("😒 NENHUM USUÁRIO CADASTRADO.")

def listar_abrigos():
    abrigos_list = carregar_abrigos()
    if abrigos_list:
        print("=" * 50)
        print("LISTA DE ABRIGOS:")
        print("=" * 50)
        for abrigo in abrigos_list:
            print(f"NOME: {abrigo['nome_abrigo']}, endereco: {abrigo['endereco_abrigo']}, capacidade: {abrigo['capacidade']}")
            print("*" * 50)
    else:
        print("NENHUM ABRIGO CADASTRADO.")

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

def menu_inicial():
    print(cor.CIANO + "=" * 55 + cor.RESET)
    print(cor.VERMELHO + " ---->>> BEM VINDO A PETCON <<<---- ")
    print("          1 - lOGIN ")
    print("          2 - MÓDULO ESTOQUE ")
    print("          3 - SAIR ")
    print(cor.CIANO + "=" * 55 + cor.RESET)

def exibir_menu():
    print("\nMENU:")
    print("1. Cadastra-se")
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
                                  print(2)
                              elif opcao_logado == '3':
                                  print(3)
                              elif opcao_logado == '4':
                                  print(4)
                              elif opcao_logado == '5':
                                  print(5)
                                  listar_pets()
                              elif opcao_logado == '6':
                                  print(6)
                              elif opcao_logado == '7':
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
