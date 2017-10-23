class HashTable:
    def __init__(self, size):
      self.size = size
      self.keys = [None] * size
      self.data = [None] * size

    def hash(self, key):
      return key % self.size

    def __setitem__(self, key, datum):
      hashvalue = self.hash(key)
      if self.keys[hashvalue] is None:
          self.keys[hashvalue], self.data[hashvalue] = (key, None), (datum, None)
      else:
          self.keys[hashvalue], self.data[hashvalue] = (key, self.keys[hashvalue]), (datum, self.data[hashvalue])

    def __getitem__(self, key):
        hashvalue = self.hash(key)
        if self.keys[hashvalue] is None:
          return False
        elif self.keys[hashvalue][0] == key:
            return self.data[hashvalue][0]
        else:
            keynode, datanode = self.keys[hashvalue], self.data[hashvalue]
            while keynode[0] != key and keynode[1] is not None:
                keynode, datanode = keynode[1], datanode[1]
            if keynode is None:
                return False
            else:
                return datanode[0]

h = HashTable(size=11)
h[54] = "cat"
h[26] = "dog"
h[93] = "lion"
h[17] = "tiger"
h[77] = "bird"
h[31] = "cow"
h[44] = "goat"
h[55] = "pig"
h[20] = "chicken"
print h.keys, h.data

print h[77]