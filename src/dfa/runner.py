"""
EIF203 Estructuras Discretas - Semestre I, 2026
Universidad Nacional

Autores:
   Adrian Muñoz Cisneros
   Marco Vinicio Coto Dall' Anesse
   Gabriel Chavarria Barquero
   Joao Arauz Rodriguez
"""

def run_dfa(dfa, cadena):
    estado_actual = dfa.start_state

    for simbolo in cadena:
        # Verificar si el símbolo pertenece al alfabeto
        if simbolo not in dfa.alphabet:
            print(f"  Simbolo '{simbolo}' no esta en el alfabeto.")
            return False

        siguiente = None

        # Buscar transición válida
        for t in dfa.transitions:
            if t.from_state == estado_actual and t.symbol == simbolo:
                siguiente = t.to_state
                break

        # Si no hay transición → rechaza
        if siguiente is None:
            print(f"  No hay transicion desde {estado_actual} con '{simbolo}'.")
            return False

        print(f"  {estado_actual} --{simbolo}--> {siguiente}")
        estado_actual = siguiente

    # Verificar si termina en estado de aceptación
    for state in dfa.states:
        if state.id == estado_actual and state.accepting:
            return True

    return False
