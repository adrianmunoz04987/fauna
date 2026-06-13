"""
EIF203 Estructuras Discretas - Semestre I, 2026
Universidad Nacional

Autores:
   Adrian Muñoz Cisneros
   Marco Vinicio Coto Dall' Anesse
   Gabriel Chavarria Barquero
   Joao Arauz Rodriguez

Modulo que implementa las funciones de analisis de un DFA:
completitud, estados inalcanzables y estados inutiles.
"""


def is_complete(dfa):
    """
    Verifica si el DFA es completo en sus transiciones.
    Un DFA es completo si para cada estado existe una transicion
    definida para cada simbolo del alfabeto.

    :param dfa: El automata a analizar.
    :type dfa: DFA
    :returns: Lista de transiciones faltantes como cadenas '(estado, simbolo)',
              vacia si el DFA es completo.
    :rtype: list
    """
    faltantes = []
    for state in dfa.states:
        for symbol in dfa.alphabet:
            existe = False
            for t in dfa.transitions:
                if t.from_state == state.id and t.symbol == symbol:
                    existe = True
                    break
            if not existe:
                faltantes.append(f"({state.id}, {symbol})")
    return faltantes


def unreachable_states(dfa):
    """
    Retorna los estados inalcanzables del DFA usando BFS desde el estado inicial.
    Un estado es inalcanzable si no existe ningun camino desde el estado
    inicial que llegue a el.

    :param dfa: El automata a analizar.
    :type dfa: DFA
    :returns: Lista de IDs de estados inalcanzables.
    :rtype: list
    """
    alcanzados = set()
    por_visitar = [dfa.start_state]

    while por_visitar:
        actual = por_visitar.pop()
        if actual in alcanzados:
            continue
        alcanzados.add(actual)
        for t in dfa.transitions:
            if t.from_state == actual and t.to_state not in alcanzados:
                por_visitar.append(t.to_state)

    todos = [s.id for s in dfa.states]
    return [s for s in todos if s not in alcanzados]


def useless_states(dfa):
    """
    Retorna los estados inutiles del DFA.
    Un estado es inutile si no existe ningun camino desde ese estado
    hasta algun estado de aceptacion.

    :param dfa: El automata a analizar.
    :type dfa: DFA
    :returns: Lista de IDs de estados inutiles.
    :rtype: list
    """
    # BFS inverso: partimos de los estados de aceptacion
    utiles = set(s.id for s in dfa.states if s.accepting)
    por_visitar = list(utiles)

    while por_visitar:
        actual = por_visitar.pop()
        for t in dfa.transitions:
            if t.to_state == actual and t.from_state not in utiles:
                utiles.add(t.from_state)
                por_visitar.append(t.from_state)

    todos = [s.id for s in dfa.states]
    return [s for s in todos if s not in utiles]
