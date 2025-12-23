"""

Implementa as operações CRUD para aulas:
- marcar_aula
- listar_aulas
- atualizar_estado_aula
- cancelar_aula
"""

from models import Aula

aulas = []  # Lista global de aulas

def marcar_aula(aluno, instrutor, veiculo):
    """
    Cria e adiciona uma nova aula à lista de aulas.

    Args:
        aluno (Aluno): Aluno associado
        instrutor (Instrutor): Instrutor associado
        veiculo (Veiculo): Veículo utilizado

    Returns:
        None
    """
    aula = Aula(aluno, instrutor, veiculo)
    aulas.append(aula)
    print(f"Aula marcada: {aluno.nome} com {instrutor.nome} no veículo {veiculo.modelo}")

def listar_aulas():
    """
    Lista todas as aulas agendadas.

    Returns:
        None
    """
    if not aulas:
        print("Nenhuma aula agendada.")
    for i, aula in enumerate(aulas):
        print(f"{i+1}. {aula}")

def atualizar_estado_aula(index, estado):
    """
    Atualiza o estado de uma aula existente.

    Args:
        index (int): Índice da aula
        estado (str): Novo estado ('agendada', 'concluída', 'cancelada')

    Returns:
        None
    """
    if 0 <= index < len(aulas):
        aulas[index].estado = estado
        print(f"Aula {index+1} atualizada para {estado}")
    else:
        print("Índice inválido.")

def cancelar_aula(index):
    """
    Cancela e remove uma aula da lista.

    Args:
        index (int): Índice da aula

    Returns:
        None
    """
    if 0 <= index < len(aulas):
        removed = aulas.pop(index)
        print(f"Aula de {removed.aluno.nome} cancelada com sucesso!")
    else:
        print("Índice inválido.")
