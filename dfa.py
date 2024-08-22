alphabet = ['a','b']

def q0(text):
	if text == '':
		return 'q0'
	symbol = text[:1]
	#print(symbol)
	if symbol in alphabet:
		if symbol == 'a':
			s = q1(text[1:])
			return s
			
		else:
			s = q0(text[1:])
			return s
			

	
	else:
		return "rejected"
	



def q1(text):

	if text == '':
		#print('q')
		return 'q1'
	symbol = text[:1]
	#print(symbol)
	if symbol == 'b' :
		s = q0(text[1:])
		return s
	else:
		s = q1(text[1:])
		return s





def dfa_ends_with_a(text):
	final_state = ['q1']
	
	state = q0(text)
	#print(state)
	
	if final_state[0] == state :
		return "Accepted"
	else:
		return "Rejected"



print(dfa_ends_with_a(' '))
