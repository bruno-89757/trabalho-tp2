"""


Implementa as operações CRUD para os alunos:
- criar_aluno
- listar_alunos
- atualizar_aluno
- remover_aluno

Usa a classe Aluno definida em models.py.
"""

from models import Aluno

alunos = []  # Lista global de alunos

def criar_aluno(nome, idade, categoria_carta):
    """
    Adiciona um novo aluno à lista de alunos.

    Args:
        nome (str): Nome do aluno
        idade (int): Idade do aluno
        categoria_carta (str): Categoria da carta

    Returns:
        None
    """
    aluno = Aluno(nome, idade, categoria_carta)
    alunos.append(aluno)
    print(f"Aluno {nome} adicionado com sucesso!")

def listar_alunos():
    """
    Lista todos os alunos cadastrados.

    Returns:
        None
    """
    if not alunos:
        print("Nenhum aluno cadastrado.")
    for i, aluno in enumerate(alunos):
        print(f"{i+1}. {aluno}")

def atualizar_aluno(index, nome, idade, categoria_carta):
    """
    Atualiza os dados de um aluno existente.

    Args:
        index (int): Índice do aluno na lista
        nome (str): Novo nome
        idade (int): Nova idade
        categoria_carta (str): Nova categoria de carta

    Returns:
        None
    """
    if 0 <= index < len(alunos):
        alunos[index].nome = nome
        alunos[index].idade = idade
        alunos[index].categoria_carta = categoria_carta
        print(f"Aluno {index+1} atualizado com sucesso!")
    else:
        print("Índice inválido.")

def remover_aluno(index):
    """
    Remove um aluno da lista.

    Args:
        index (int): Índice do aluno na lista

    Returns:
        None
    """
    if 0 <= index < len(alunos):
        removed = alunos.pop(index)
        print(f"Aluno {removed.nome} removido com sucesso!")
    else:
        print("Índice inválido.")
