import random
from gameplay import *
class Block(Gameplay):

	shapes=[[[[0,0],[0,-1],[1,0],[1,-1]],[[0,0],[0,-1],[1,0],[1,-1]],[[0,0],[0,-1],[1,0],[1,-1]],[[0,0],[0,-1],[1,0],[1,-1]]],
			[[[0,0],[1,0],[2,0],[3,0]],[[0,0],[0,-1],[0,-2],[0,-3]],[[0,0],[1,0],[2,0],[3,0]],[[0,0],[0,-1],[0,-2],[0,-3]]],
			[[[0,0],[1,0],[2,0],[2,-1]],[[1,0],[1,-1],[1,-2],[0,-2]],[[0,0],[0,-1],[0,-2],[1,0]],[[0,0],[0,-1],[1,-1],[2,-1]]],
			[[[1,0],[2,0],[0,-1],[1,-1]],[[0,0],[0,-1],[1,-1],[1,-2]],[[1,0],[2,0],[0,-1],[1,-1]],[[0,0],[0,-1],[1,-1],[1,-2]]],
			[[[0,0],[1,0],[2,0],[1,-1]],[[0,-1],[1,-1],[1,0],[1,-2]],[[0,-1],[1,0],[1,-1],[2,-1]],[[0,-1],[0,0],[0,-2],[1,-1]]],
			[[[1,0],[0,0],[1,-1],[2,-1]],[[1,0],[0,-1],[1,-1],[0,-2]],[[1,0],[0,0],[1,-1],[2,-1]],[[1,0],[0,-1],[1,-1],[0,-2]]],
			[[[0,0],[1,0],[2,0],[0,-1]],[[0,0],[1,0],[1,-1],[1,-2]],[[0,0],[0,-1],[1,-1],[2,-1]],[[0,0],[0,-1],[0,-2],[1,-2]]]
			]

	offsetx = 15
	offsety = 0
	shape = 0
	shapeid=0
	codinat = []; oldcodinat = []
	qt = False

	def __init__(self):
		pass
	def newblock(self):
		#print "HaHa New block"
		self.offsetx = 15
		self.offsety =0
		self.shape=random.randint(0,6)
		self.shapeid=0
		self.oldcodinat = self.codinat
		c1 = self.shapes[self.shape][self.shapeid]
		#print c1
		self.codinat = []
		for i in range(len(c1)):
			self.codinat.append([c1[i][0]+self.offsetx,c1[i][1]+self.offsety])
		#print self.codinat
		self.setvalues(1)
		return
		'''
		if x==0:	#like  XXXX
			self.codinat = [[15,0],[16,0],[17,0],[18,0]]
		elif x==1:
			self.codinat = [[18,1],[16,0],[17,0],[17,1]]
		elif x==2:
			self.codinat = [[16,1],[16,0],[17,0],[17,1]]
		elif x==3:
			self.codinat = [[15,0],[16,0],[17,0],[16,1]]
		elif x==4:
			self.codinat = [[15,0],[16,0],[17,0],[17,1]]'''
		'''#print self.codinat
		for element in self.codinat:
			if element in self.oldcodinat:
				self.qt = True
				self.codinat = self.oldcodinat'''

	def setvalues(self,val):
		#print "VAL IS +",val 
		self.gameboard[self.codinat[0][1]][self.codinat[0][0]]=val
		self.gameboard[self.codinat[1][1]][self.codinat[1][0]]=val
		self.gameboard[self.codinat[2][1]][self.codinat[2][0]]=val
		self.gameboard[self.codinat[3][1]][self.codinat[3][0]]=val
		return

	def check(self,a,b):
		flag1=0;flag2=0;flag3=0;flag4=0

		if self.gameboard[self.codinat[0][1]+b][self.codinat[0][0]+a]!=0:
			if not [self.codinat[0][0]+a,self.codinat[0][1]+b] in self.codinat:
				flag1 = 1;
		if self.gameboard[self.codinat[1][1]+b][self.codinat[1][0]+a] != 0:
			if not [self.codinat[1][0]+a,self.codinat[1][1]+b] in self.codinat:
				flag2 = 1;
		if self.gameboard[self.codinat[2][1]+b][self.codinat[2][0]+a] != 0:
			if not [self.codinat[2][0]+a,self.codinat[2][1]+b] in self.codinat:
				flag3 = 1;
		if self.gameboard[self.codinat[3][1]+b][self.codinat[3][0]+a] != 0:
			if not [self.codinat[3][0]+a,self.codinat[3][1]+b] in self.codinat:
				flag4 = 1;
		if flag1==1 or flag2==1 or flag3==1 or flag4==1 or self.codinat[0][1]+b==30 or self.codinat[1][1]+b==30 or self.codinat[2][1]+b==30 or self.codinat[3][1]+b==30 or self.codinat[0][0]+a<=1 or self.codinat[0][0]+a>=34 or self.codinat[1][0]+a<=1 or self.codinat[1][0]+a>=34 or self.codinat[2][0]+a<=1 or self.codinat[2][0]+a>=34 or self.codinat[3][0]+a<=1 or self.codinat[3][0]+a>=34:
			return 0
		else:
			return 1



	def movecodinat(self,a,b):
		self.codinat[0][0] += a;self.codinat[0][1] += b
		self.codinat[1][0] += a;self.codinat[1][1] += b
		self.codinat[2][0] += a;self.codinat[2][1] += b
		self.codinat[3][0] += a;self.codinat[3][1] += b
		return




	def moveleft(self,changeleft):
		if changeleft:
			if self.check(-1,0)==1:
				self.setvalues(0)
				self.movecodinat(-1,0)
				self.offsetx-=1
				self.setvalues(1)
		return
	
	def moveright(self,changeright):
		if changeright:
			if self.check(1,0)==1:
				self.setvalues(0)
				self.movecodinat(1,0)
				self.offsetx+=1
				self.setvalues(1)
		return
	def movedown(self):
		if self.check(0,1)==1:
			#print self.codinat
			self.setvalues(0)
			self.movecodinat(0,1)
			self.offsety+=1
			self.setvalues(1)
		else:
			self.newblock()
		return
	def directbottom(self):
		while self.check(0,1)==1:
			self.setvalues(0)
			self.movecodinat(0,1)
			self.setvalues(1)
		self.newblock()


'''
g1 = Gameplay()
b1 = Block()
b1.draw()
b1.#printboard()
b1.moveleft()
b1.moveleft()
b1.moveleft()
b1.moveleft()
b1.moveleft()
b1.moveleft()
b1.moveleft()
b1.moveleft()
b1.moveleft()
b1.#printboard()'''
