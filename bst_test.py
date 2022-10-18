import BstMap as bst
import timeit

my_dict = {"Clark": 43, "Adam": 35, "Bella": 24, "Jonathan": 19, "Victor": 29, "Trevor": 26}
my_map = bst.BstMap()

for v, k in my_dict.items():
    my_map.put(v, k)

print(my_map.to_string())

my_map.put("Bella", 28)
my_map.put("Jonathan", 25)
print(my_map.to_string())


print(f"Size of the tree: {my_map.size()}")

get_test = "Victor"
print(f"Get value for {get_test}: {my_map.get(get_test)}")

print(f"Amount of leafs = {my_map.count_leafs()}")

print(f"Max depth = {my_map.max_depth()}")

kv_lst = my_map.as_list()
print(f"Key value list:\n{kv_lst}")
