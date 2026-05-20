"""
EIF203 Estructuras Discretas - Semestre I, 2026
Universidad Nacional

Autores:
   Adrian Muñoz Cisneros
   Marco Vinicio Coto Dall' Anesse
   Gabriel Chavarria Barquero
   Joao Arauz Rodriguez
"""

def is_complete(dfa):
    for state in dfa.states:
        for symbol in dfa.alphabet:
            existe = False
            for t in dfa.transitions:
                if t.from_state == state.id and t.symbol == symbol:
                    existe = True
                    break
            if not existe:
                return False
    return True


def unreachable_states(dfa):
    alcanzados = [dfa.start_state]

    for t in dfa.transitions:
        if t.from_state in alcanzados and t.to_state not in alcanzados:
            alcanzados.append(t.to_state)

    todos = [s.id for s in dfa.states]

    return [s for s in todos if s not in alcanzados]


def useless_states(dfa):
    aceptacion = [s.id for s in dfa.states if s.accepting]

    utiles = aceptacion.copy()

    for t in dfa.transitions:
        if t.to_state in utiles and t.from_state not in utiles:
            utiles.append(t.from_state)

    todos = [s.id for s in dfa.states]

    return [s for s in todos if s not in utiles]