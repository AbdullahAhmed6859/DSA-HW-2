def get(hashtable: tuple[list, list], key: str, size: int,
        collision_path: dict[list], opNumber: int) -> any:

    keys, values = hashtable
    collision_path[opNumber] = []
    hash_address = hash_function(key, size)
    collision_path[opNumber].append(hash_address)
    
    while keys[hash_address] and keys[hash_address] != "#" and keys[hash_address] != key:
        hash_address = collision_resolver(key, hash_address, size)

        collision_path[opNumber].append(hash_address)
        if hash_address in collision_path[opNumber]:
            break
    
    if keys[hash_address] == key:
        return values[hash_address]
    else:
        print("Item not found")