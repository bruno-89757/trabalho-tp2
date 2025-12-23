"""

Interface de consola principal da aplicação da escola de condução.

Funcionalidades:
- Login de utilizador (admin / instrutor / aluno)
- Menus para gerir Alunos, Instrutores, Veículos e Aulas
- Integração com os módulos CRUD:
    - crud_aluno.py
    - crud_instrutor.py
    - crud_veiculo.py
    - crud_aula.py
- Permite criar, listar, atualizar e remover entidades
- Permite marcar, listar, atualizar estado e cancelar aulas
"""

from crud_aluno import criar_aluno, listar_alunos, atualizar_aluno, remover_aluno, alunos
from crud_instrutor import criar_instrutor, listar_instrutores, instrutores
from crud_veiculo import adicionar_veiculo, listar_veiculos, veiculos
from crud_aula import marcar_aula, listar_aulas, atualizar_estado_aula, cancelar_aula, aulas
from auth import login

# --- Menus ---

def menu():
    """
    Menu principal da aplicação.
    
    Returns:
        str: opção escolhida pelo utilizador
    """
    print("\n--- Escola de Condução ---")
    print("1. Alunos")
    print("2. Instrutores")
    print("3. Veículos")
    print("4. Aulas")
    print("5. Sair")
    return input("Escolha uma opção: ")

def menu_alunos():
    """
    Menu de gestão de alunos.

    Returns:
        str: opção escolhida pelo utilizador
    """
    print("\n--- Alunos ---")
    print("1. Criar aluno")
    print("2. Listar alunos")
    print("3. Atualizar aluno")
    print("4. Remover aluno")
    print("5. Voltar")
    return input("Escolha uma opção: ")

def menu_instrutores():
    """
    Menu de gestão de instrutores.

    Returns:
        str: opção escolhida pelo utilizador
    """
    print("\n--- Instrutores ---")
    print("1. Criar instrutor")
    print("2. Listar instrutores")
    print("3. Voltar")
    return input("Escolha uma opção: ")

def menu_veiculos():
    """
    Menu de gestão de veículos.

    Returns:
        str: opção escolhida pelo utilizador
    """
    print("\n--- Veículos ---")
    print("1. Adicionar veículo")
    print("2. Listar veículos")
    print("3. Voltar")
    return input("Escolha uma opção: ")

def menu_aulas():
    """
    Menu de gestão de aulas.

    Returns:
        str: opção escolhida pelo utilizador
    """
    print("\n--- Aulas ---")
    print("1. Marcar aula")
    print("2. Listar aulas")
    print("3. Atualizar estado")
    print("4. Cancelar aula")
    print("5. Voltar")
    return input("Escolha uma opção: ")

# --- Função principal ---

def main():
    """
    Função principal da aplicação.
    - Efetua login do utilizador
    - Mostra o menu principal e menus de cada entidade
    - Chama funções CRUD de acordo com a escolha do utilizador
    """
    user = login()
    if not user:
        return  # Termina se login falhar

    while True:
        choice = menu()

        # --- Menu Alunos ---
        if choice == "1":
            while True:
                op = menu_alunos()
                if op == "1":
                    nome = input("Nome: ")
                    idade = int(input("Idade: "))
                    carta = input("Categoria de carta: ")
                    criar_aluno(nome, idade, carta)
                elif op == "2":
                    listar_alunos()
                elif op == "3":
                    listar_alunos()
                    idx = int(input("Índice do aluno a atualizar: ")) - 1
                    nome = input("Novo nome: ")
                    idade = int(input("Nova idade: "))
                    carta = input("Nova categoria: ")
                    atualizar_aluno(idx, nome, idade, carta)
                elif op == "4":
                    listar_alunos()
                    idx = int(input("Índice do aluno a remover: ")) - 1
                    remover_aluno(idx)
                elif op == "5":
                    break  # Volta ao menu principal

        # --- Menu Instrutores ---
        elif choice == "2":
            while True:
                op = menu_instrutores()
                if op == "1":
                    nome = input("Nome: ")
                    categorias = input("Categorias (separadas por vírgula): ").split(",")
                    criar_instrutor(nome, [c.strip() for c in categorias])
                elif op == "2":
                    listar_instrutores()
                elif op == "3":
                    break

        # --- Menu Veículos ---
        elif choice == "3":
            while True:
                op = menu_veiculos()
                if op == "1":
                    modelo = input("Modelo: ")
                    matricula = input("Matrícula: ")
                    adicionar_veiculo(modelo, matricula)
                elif op == "2":
                    listar_veiculos()
                elif op == "3":
                    break

        # --- Menu Aulas ---
        elif choice == "4":
            while True:
                op = menu_aulas()
                if op == "1":
                    print("Escolha aluno:")
                    listar_alunos()
                    idx_a = int(input("Índice do aluno: ")) - 1

                    print("Escolha instrutor:")
                    listar_instrutores()
                    idx_i = int(input("Índice do instrutor: ")) - 1

                    print("Escolha veículo:")
                    listar_veiculos()
                    idx_v = int(input("Índice do veículo: ")) - 1

                    marcar_aula(alunos[idx_a], instrutores[idx_i], veiculos[idx_v])

                elif op == "2":
                    listar_aulas()

                elif op == "3":
                    listar_aulas()
                    idx = int(input("Índice da aula: ")) - 1
                    estado = input("Novo estado (agendada/concluída/cancelada): ")
                    atualizar_estado_aula(idx, estado)

                elif op == "4":
                    listar_aulas()
                    idx = int(input("Índice da aula: ")) - 1
                    cancelar_aula(idx)

                elif op == "5":
                    break

        # --- Sair ---
        elif choice == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

# --- Executa a aplicação ---
if __name__ == "__main__":
    main()
