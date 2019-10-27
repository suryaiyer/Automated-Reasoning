from model_checking import TT_Entails
from resolution import PL_resolution


def execute(problem,KB_model,alpha,KB_resolution):
	#print('\n')
	print(problem,':',"\n")
	print('Knowledge base',KB_model,)
	
	for a in alpha:
		print('Query:',a,'\n')
	
		aEntails = TT_Entails(KB,a);
		if a[0] == '!':
			bEntails = TT_Entails(KB_model, a[1:len(a)] )
		else:
			bEntails = TT_Entails(KB_model, '!' + a)
	
		if aEntails == False and bEntails == False:
			print("Ans for",problem,"with model checking: MAYBE")
		else:
			print("Ans for",problem,"with model checking: ", aEntails)
			print("So by modelchecking",KB,"entails",a,"\n")
	
		if a[0] == '!':
			aResolution = PL_resolution(KB_resolution, [a[1:len(a)]])
			bResolution = PL_resolution(KB_resolution, [a])
		else:
			aResolution = PL_resolution(KB_resolution, ['!' + a])
			bResolution = PL_resolution(KB_resolution, [a])

		if aEntails == False and bEntails == False:
			print("Ans for",problem,"with model checking: MAYBE")
		elif aResolution:
			print("Ans for",problem,"with Resolution: ", True)
			print("So by Resolution",KB,"entails",a,"\n")
		else:
			print("Ans for",problem,"with Resolution: ", False)
		
			
# Modus Ponens
KB = "( P => Q ) ^ P"
modus_ponens = [['P'], ['!P', 'Q']]
a = ["Q"]
execute("Modus Ponens Test",KB,a,modus_ponens)		 


# Wumpus World
KB = "!P11 ^ ( B11 <=> ( P12 v P21 ) ) ^ ( B21 <=> ( P11 v P22 v P31 ) ) ^ !B11 ^ B21"
a = ["!P12"]

wumpus_world = [['!P11'], ['!B11', 'P12', 'P21'], ['!P12', 'B11'],
                ['!P21', 'B11'], ['!B21', 'P11', 'P22', 'P31'], ['!P11', 'B21'],
                ['!P22', 'B21'], ['!P31', 'B21'], ['!B11'], ['B21']]

execute("Wumpus World",KB,a,wumpus_world)		 
				
				
# Unicorn
KB = "( My => I ) ^ ( !My => ( !I ^ m ) ) ^ ( ( I v m ) => H ) ^ ( H => Ma )"
horned_clauses = [['!Myt', 'I'], ['Myt', '!I'], ['Myt', 'Mam'],
                  ['!I', 'H'], ['!Mam', 'H'], ['!H', 'Mag']]
a = ["H"]
execute("Unicorn",KB,a,horned_clauses)


# Doors of Enlightenment

KB = "( A <=> X ) ^ ( B <=> ( Y v Z ) ) ^ ( C <=> ( A ^ B ) ) ^ ( D <=> ( X ^ Y ) ) ^ ( E <=> ( X ^ Z ) ) ^ ( F <=> ( D v E ) ) ^ ( G <=> ( C => F ) ) ^ ( H <=> ( ( G ^ H ) => A ) ) ^ ( X v Y v Z v W )"
a = ['X','Y','Z','W']		 
doors = [['!A', 'X'], ['!X', 'A'],
         ['!B', 'Y', 'Z'], ['!Y', 'B'], ['!Z', 'B'],
         ['!C', 'A'], ['!C', 'B'], ['!A', '!B', 'C'],
         ['!D', 'X'], ['!D', 'Y'], ['!X', '!Y', 'D'],
         ['!E', 'X'], ['!E', 'Z'], ['!X', '!Z', 'E'],
         ['!F', 'D', 'E'], ['!D', 'F'], ['!E', 'F'],
         ['!G', '!C', 'F'], ['G', 'C'], ['G', '!F'],
         ['!H', '!G', 'A'], ['G', 'A'], ['H', 'A'],
         ['X', 'Y', 'Z', 'W']]

execute("Doors of Enlightenment",KB,a,doors)
