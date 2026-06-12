"""
EIF203 Estructuras Discretas - Semestre I, 2026
Universidad Nacional

Autores:
   Adrian Muñoz Cisneros
   Marco Vinicio Coto Dall' Anesse
   Gabriel Chavarria Barquero
   Joao Arauz Rodriguez

Ejemplo demostrativo de un DFA modelado con automata-lib.
Reconoce fechas con formato dd/mm/aa donde d, m, a son digitos del 0-9.
"""

from automata.fa.dfa import DFA

digitos = set('0123456789')

dfa = DFA(
    states={
        'FD',
        'SD',
        'FS',
        'FM',
        'SM',
        'SS',
        'FY',
        'SY',
        'VD',
        'INV'
    },
    input_symbols={'0','1','2','3','4','5','6','7','8','9','/'},
    transitions={
        'FD': {d: 'SD' for d in digitos} | {'/': 'INV'},
        'SD': {d: 'FS' for d in digitos} | {'/': 'INV'},
        'FS': {d: 'INV' for d in digitos} | {'/': 'FM'},
        'FM': {d: 'SM' for d in digitos} | {'/': 'INV'},
        'SM': {d: 'SS' for d in digitos} | {'/': 'INV'},
        'SS': {d: 'INV' for d in digitos} | {'/': 'FY'},
        'FY': {d: 'SY' for d in digitos} | {'/': 'INV'},
        'SY': {d: 'VD' for d in digitos} | {'/': 'INV'},
        'VD': {d: 'INV' for d in digitos} | {'/': 'INV'},
        'INV': {d: 'INV' for d in digitos} | {'/': 'INV'},
    },
    initial_state='FD',
    final_states={'VD'}
)

print("Accepts '11/06/26':", dfa.accepts_input('11/06/26'))
print("Accepts '01/01/00':", dfa.accepts_input('01/01/00'))
print("Rejects '1106/26':", dfa.accepts_input('1106/26'))
print("Rejects '11/0626':", dfa.accepts_input('11/0626'))
print("Rejects '11/06/2':", dfa.accepts_input('11/06/2'))