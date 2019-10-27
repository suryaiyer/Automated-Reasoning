from model_checking import TT_Entails
from resolution import PL_resolution

#Knowledge Base:
# Modus Ponens
#KB = "( P => Q ) ^ P"
#a = "Q"

# Wumpus World
#KB = "!P11 ^ ( B11 <=> ( P12 v P21 ) ) ^ ( B21 <=> ( P11 v P22 v P31 ) ) ^ !B11 ^ B21"
#KB = "!P12"
#a = "!P12"

# Three doors
#KB = "! ( G ^ ( S => M ) ) ^ ! ( !G ^ !S ) ^ ! ( G ^ !M )"
#a = "!G"

# Unicorn
#KB = "( My => I ) ^ ( !My => ( !I ^ m ) ) ^ ( ( I v m ) => H ) ^ ( H => Ma )"
#a = "H"

# Doors of Enlightenment

KB = "( A <=> X ) ^ ( B <=> ( Y v Z ) ) ^ ( C <=> ( A ^ B ) ) ^ ( D <=> ( X ^ Y ) ) ^ ( E <=> ( X ^ Z ) ) ^ ( F <=> ( D v E ) ) ^ ( G <=> ( C => F ) ) ^ ( H <=> ( ( G ^ H ) => A ) ) ^ ( X v Y v Z v W )"
a = "!W"

#CNF converted
three_doors = [['!G', 'S'], ['!G', '!M'],
               ['G', 'S'], ['!G', 'M']]
modus_ponens = [['P'], ['!P', 'Q']]
wumpus_world = [['!P11'], ['!B11', 'P12', 'P21'], ['!P12', 'B11'],
                ['!P21', 'B11'], ['!B21', 'P11', 'P22', 'P31'], ['!P11', 'B21'],
                ['!P22', 'B21'], ['!P31', 'B21'], ['!B11'], ['B21']]
horned_clauses = [['!Myt', 'I'], ['Myt', '!I'], ['Myt', 'Mam'],
                  ['!I', 'H'], ['!Mam', 'H'], ['!H', 'Mag']]
doors = [['!A', 'X'], ['!X', 'A'],
         ['!B', 'Y', 'Z'], ['!Y', 'B'], ['!Z', 'B'],
         ['!C', 'A'], ['!C', 'B'], ['!A', '!B', 'C'],
         ['!D', 'X'], ['!D', 'Y'], ['!X', '!Y', 'D'],
         ['!E', 'X'], ['!E', 'Z'], ['!X', '!Z', 'E'],
         ['!F', 'D', 'E'], ['!D', 'F'], ['!E', 'F'],
         ['!G', '!C', 'F'], ['G', 'C'], ['G', '!F'],
         ['!H', '!G', 'A'], ['G', 'A'], ['H', 'A'],
         ['X', 'Y', 'Z', 'W']]


print('Modus Ponens test:')
print('Knowledge base')
print()
print('Query:',)
