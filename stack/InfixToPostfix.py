#hi fetch commit
class conversion:
    
	def __init__(self):
		self.ans=""
		self.stack=[]
		self.precedence={'+':1,'-':1,'*':2,'/':2,'^':3}


	def isEmpty(self):
		return True if len(self.stack)==0 else False

	def peek(self):
		if len(self.stack)!=0:
			return self.stack[len(self.stack)-1]
		else:
			return 

	def push(self,data):

		self.stack.append(data)

	def pop(self):
		if len(self.stack)==0:
			return
		else:
			return self.stack.pop()

	def isoperand(self,op):
		return op.isalpha()

	def greater(self,ch):

		if self.isEmpty() or self.peek()=='(':
			return True

		a=self.precedence[ch] 
		b=self.precedence[self.peek()]

		print('a=',a,'b=',b)

		if a>b:
			return True

		elif a==3:
			return True

		else:
			return False


	def InfixtoPostfix(self,string):

		for i in string:

			if self.isoperand(i):
				self.ans+=i
				print('ans=',self.ans)

			elif i=='(':
				self.push(i)
				print('stack=',self.stack)

			elif i==')':

				while (not self.isEmpty()) and (self.peek()!='('):
					print('peek=',self.peek())
					a=self.pop()
					print(a)

					self.ans+=a

				if not self.isEmpty():
					self.pop()

			else:
				if self.greater(i):
					self.push(i)
					print('stack=',self.stack)
				else:
					while not self.isEmpty() and not (self.greater(i)):
						self.ans+=self.pop()

					self.push(i)

					print('stack=',self.stack)

		while not self.isEmpty():
			self.ans+=self.pop()

		print(self.ans)

string="k+L-M*N+(o^P)*W/U/V*T+Q^J^A"

obj=conversion()

obj.InfixtoPostfix(string)
