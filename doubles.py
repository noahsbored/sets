def remove(ids):
    unique_ids = set(ids)
    for id in unique_ids:
        print(id)
    return unique_ids


ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
unique_ids = remove(ids)
print( unique_ids)
