# Manual implementation
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22}
]

def sort_by_key(data, key):
    return sorted(data, key=lambda x: x[key])

print(sort_by_key(data, "age"))
