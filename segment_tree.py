# Segment Tree: Arreglo que permite
# 	sumar A[lo:hi] -> O(n) a O(Logn)
# 	cambiar un valor dentro de A "A[n] = x" -> O(1) a O(Logn)

class SegmentTree:
	def __init__(self, A):
		hojas = 1
		while hojas < len(A): hojas*=2
		self.tree = [0 for n in range(2*hojas)]
		for n in range(len(A)):
			self.tree[n+hojas] = A[n]
		for n in range(hojas-1, 0, -1):
			self.tree[n] = self.tree[2*n]+self.tree[2*n+1]
		self.hojas = hojas
		return

	def suma(self, lo, hi):
		return self.aux_sum(lo,hi,1, 0, self.hojas) if len(self.tree) else 0

	def aux_sum(self, lo,hi,n, L, R):
		assert L<=lo<hi<=R
		middle = L + ((R-L)//2)
		if L == lo and R==hi:
			result = self.tree[n]
		elif hi <= middle:
			result = self.aux_sum(lo, hi, 2*n, L, middle)
		elif lo >= middle:
			result = self.aux_sum(lo, hi, 2*n+1, middle, R)
		else:
			result = self.aux_sum(lo, middle, 2*n, L, middle)
			result += self.aux_sum(middle, hi, 2*n+1, middle, R)
		return result

	def set(self, n, value):
		n = n+self.hojas
		self.tree[n] = value
		while n!=1:
			n//=2
			self.tree[n] = self.tree[2*n]+self.tree[2*n+1]
		return

A = [2,3,5,-1,0]
s = SegmentTree(A)
print(s.tree)
print(s.suma(0,3))