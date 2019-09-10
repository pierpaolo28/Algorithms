class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]

    def lookup(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                if string in self.table[hv]:
                    return hv
        return -1

    def calculate_hash_value(self, string):
        value = ord(string[0])*100 + ord(string[1])
        return value


# Setup
hash_table = HashTable()

# Calculating_hash_value
print(hash_table.calculate_hash_value('HASH'))

# Looking-up edge case
print(hash_table.lookup('HASH'))

# Storing a value
hash_table.store('STORE')
print(hash_table.lookup('STORE'))

# Storing edge case
hash_table.store('TEST')
print(hash_table.lookup('TEST'))