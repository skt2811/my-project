class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key, value)

    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        previous = None
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                return
            previous = current
            current = current.next

# Create a HashTable instance
table1 = HashTable(20)

# Insert data into the HashTable
data = {
    206131: "Savini",
    206075: "Senuri",
    206053: "Kalani",
    206083: "Chathumini",
    206104: "Reema"
}

for key, value in data.items():
    table1.insert(key, value)

# Search for a specific key
index_number = 206131
name = table1.search(index_number)
if name is not None:
    print("Name found:", name)
else:
    print("Name not found.")
