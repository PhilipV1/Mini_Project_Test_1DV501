import HashSet as hset


words = hset.HashSet()
words.init()

hash_codes = []
names = ["Adam", "David", "Amer", "Ceve", "Owen", "Ella", "Jonas", "Morgan"]
# , "Fredrik", "Zoe", "Fred", "Albin", "Ola", "Simon"]

for name in names:
    hash_codes.append((words.get_hash(name), name))

print(f"Hash codes:\n {hash_codes}")

# Visual representation of how the hash codes converts to indices
indices = []
for codes in hash_codes:
    indices.append((codes[0] % 8, codes[1]))
print(f"Indices:\n{indices}")


