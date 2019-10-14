
operators = ['!','v','^','<=>','=>']
class TreeNode():
	def __init__(self,val):
		self.val = val
		self.parent = None
		self.children= []
	
	def add_child(self,child):
		self.children.append(child)
	
	def add_parent(self,parent):
		self.parent = parent	
		
		
def parser(list_val):
	i = 0
	print(list_val)
	root = None
	operator_list = []
	leaf_list = []
	while i < len(list_val):
	#	print(i)
		if list_val[i] == '!':
			tree_node = TreeNode(list_val[i])
			i = i + 1
			operator_list.append(tree_node)
			
		elif list_val[i] == '(':
			#operator_list.append(tree_node)
			count = 1
			i = i + 1
			list_subset = []
			while count != 0:
				if list_val[i] == '(':
					count = count + 1
					list_subset.append(list_val[i])
					i = i + 1
					
				elif list_val[i] == ')':
					count = count - 1
					if count != 0:
						list_subset.append(list_val[i])
					i = i + 1
				
				else:
					list_subset.append(list_val[i])
					i = i + 1
				
			leaf_node = parser(list_subset)
			
			if len(operator_list) > 0:
				if operator_list[len(operator_list)-1].val == '!':
					
					leaf_node.add_parent(operator_list[len(operator_list)-1])
					operator_list[len(operator_list)-1].add_child(leaf_node)		
					leaf_list.append(operator_list[len(operator_list)-1])
					operator_list.remove(operator_list[len(operator_list)-1])
				
				else:
					leaf_list.append(leaf_node)
			else:
				leaf_list.append(leaf_node)

			
		elif list_val[i] not in operators:
			leaf_node = TreeNode(list_val[i])
			i = i + 1
			
			if len(operator_list) > 0:
				if operator_list[len(operator_list)-1].val == '!':
					leaf_node.add_parent(operator_list[len(operator_list)-1])
					operator_list[len(operator_list)-1].add_child(leaf_node)		
					leaf_list.append(operator_list[len(operator_list)-1])
					operator_list.remove(operator_list[len(operator_list)-1])
				else:
					leaf_list.append(leaf_node)
			
			else:
				leaf_list.append(leaf_node)
			
		elif list_val[i] in operators:
			tree_node = TreeNode(list_val[i])
			operator_list.append(tree_node)
			i = i + 1
	
	if operator_list == []:
		return leaf_list[0]
	
	else:
		for i in range(len(leaf_list)):
			print(leaf_list)
			operator_list[0].add_child(leaf_list[i])
			leaf_list[i].add_parent(operator_list[0])
		return operator_list[0]
			

def not_func(value):
	return not value

def or_func(list):
	for i in list:
		if i:
			return True
	
	return False

def and_func(list):
	for i in list:
		if not i:
			return False
	return True


def imply_func(list):
	if list[0] == True and list[1] == False:
		return False
	else:
		return True


def biimply_func(list):
	if list[0] != list[1]:
		return False
	else:
		return True

def evaluate(root,dict):
	
	if root.val not in operators:
		return dict[root.val]
	
	elif root.val == '!':
		return not_func(evaluate(root.children[0],dict))
	
	elif root.val == 'v':
		return or_func([evaluate(child,dict) for child in root.children])
	
	elif root.val == '^':
		return and_func([evaluate(child,dict) for child in root.children])
	
	elif root.val == '=>':
		return imply_func([evaluate(child,dict) for child in root.children])
	
	elif root.val == '<=>':
		return biimply_func([evaluate(child,dict) for child in root.children])
		

def print_dfs(root,c):
	str = ""
	for i in range(c):
		str = str + '  '
	str = str + root.val
	print(str)
	for i in range(len(root.children)):
		print_dfs(root.children[i],c + 1)

dict = {'A' : False,'B' : False,'C' : False}
expr = "A v ( B <=> C )"
list_val = expr.split(' ')		
root = parser(list_val)
print(evaluate(root,dict))

print_dfs(root,0)