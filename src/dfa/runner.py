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

    for simbolo in cadena: # Si el simbolo no esta en el alfabeto, la cadena es rechazada
            if simbolo not in dfa.alphabet:
               print(f"  Simbolo '{simbolo}' no esta en el alfabeto.")
               return False

        siguiente = None

        for t in dfa.transitions: # Buscamos la transicion que corresponde al estado actual y al simbolo
            if t.from_state == estado_actual and t.symbol == simbolo:
                siguiente = t.to_state
                break


        if siguiente is None: # Si no hay transicion definida se rechaza la cadena
            print(f"  No hay transicion desde {estado_actual} con '{simbolo}'.")
            return False


        print(f"  {estado_actual} --{simbolo}--> {siguiente}")
        estado_actual = siguiente


    for state in dfa.states: # Se revisa si el estado donde quedamos es de aceptacion
        if state.id == estado_actual and state.accepting:
            return True


    return False # Si no es de aceptacion, la cadena es rechazada
