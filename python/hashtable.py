class HashTable:
    def __init__(self, size):
      self.size = size
      self.keys = [None] * size
      self.data = [None] * size

    def hash(self, key):
      return key % self.size

    # open address rehash
    def rehash(self, key, shift=1):
      return (key + shift*shift) % self.size

    def __setitem__(self, key, datum):
      hashvalue = self.hash(key)
      if self.keys[hashvalue] is None:
          self.keys[hashvalue], self.data[hashvalue] = key, datum
      elif self.keys[hashvalue] == key:
          self.data[hashvalue] = data
      else:
          shift = 1
          while self.keys[hashvalue] is not None:
              hashvalue = self.rehash(hashvalue, shift)
              shift += 1
          if self.keys[hashvalue] is None:
              self.keys[hashvalue], self.data[hashvalue] = key, datum
          elif self.keys[hashvalue] == key:
              self.data[hashvalue] = data

    def __getitem__(self, key):
        hashvalue = self.hash(key)
        if self.keys[hashvalue] == key:
            return self.data[hashvalue]
        else:
            shift = 1
            while self.keys[hashvalue] != key and shift != self.size:
                hashvalue = self.rehash(hashvalue, shift)
                shift += 1
            if shift == self.size:
                return False
            else:
                return self.data[hashvalue]

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

print h[18]