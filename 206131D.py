#Activity 1
class Node:
	def __init__(self, k, value):
		self.key = k
		self.value = value
		self.next = None


class HTable:
	def __init__(self, m):
		self.size = m
		self.table = [None] * m

	def _hash(self, k):
		return k % self.size

#Activity 2
	def insert(self, k, value):
		index = self._hash(k)
		if self.table[index] is None:
			self.table[index] = Node(k, value)
		else:
			current = self.table[index]
			while current.next:
				current = current.next
			current.next = Node(k, value)

#Activity 3
	def search(self, k):
		index = self._hash(k)
		current = self.table[index]
		while current:
			if current.key == k:
				return current.value
			current = current.next
		return False

#Activity 4
	def delete(self, k):
		index = self._hash(k)
		current = self.table[index]
		previous = None
		while current:
			if current.key == k:
				if previous:
					previous.next = current.next
				else:
					self.table[index] = current.next
				return
			previous = current
			current = current.next

# Activity 5
table1 = HTable(20)
table1.insert(206131, "Savini")
table1.insert(206075, "Senuri")
table1.insert(206053, "Kalani")
table1.insert(206083, "Chathumini")
table1.insert(206104, "Reema")

# Activity 6
index_number = 206131
if table1.search(index_number):
    name = table1.search(index_number)
    print("Name found:", name)
else:
    print("Name not found.")
