def sum_ascii(key: str) -> int:
    return sum(ord(char) for char in key)


def create_hashtable(size: int) -> tuple[list, list]:
    return [None for _ in range(size)], [None for _ in range(size)]


def hash_function(key: str, size: int) -> int:
    return abs(int(sum_ascii(key) / 16 % size))


def collision_resolver(key, oldAddress, size) -> int:
    return ((sum_ascii(key) // size) + oldAddress) % size


def loadFactor(hashtable: tuple[list, list], size: int) -> int:
    return sum(1 for key in hashtable[0] if key and key != "#") * 100 / size


def auto_resize(hashtable: tuple[list, list], size) -> tuple[list, list]:
    lf = loadFactor(hashtable, size)

    if lf > 75:
        hashtable, size = resize_hashtable(hashtable, size, True)
    elif lf < 30:
        hashtable, size = resize_hashtable(hashtable, size, False)

    return hashtable, size


def next_prime(num: int) -> int:
    def is_prime(num: int) -> bool:
        if num == 1:
            return False
        elif num in (2, 3):
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i <= num ** 0.5:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    while not is_prime(num) or num < 7:
        num += 1
    return num


def put_helper(hashtable: tuple[list, list],
               key: str, data: any, size: int) -> None:

    keys, values = hashtable
    hash_address = hash_function(key, size)

    while keys[hash_address] or keys[hash_address] == "#" and keys[hash_address] != key:

        hash_address = collision_resolver(key, hash_address, size)

    keys[hash_address] = key
    values[hash_address] = data


def resize_hashtable(
        hashtable: tuple[list, list], size: int, increase: bool) -> tuple[list, list]:

    if size == 7 and not increase:
        return hashtable, size

    new_size = next_prime(size * 2 if increase else size // 2)
    new_table = create_hashtable(new_size)

    for key, val in zip(*hashtable):
        if key and key != "#":
            put_helper(new_table, key, val, new_size)

    return new_table, new_size


def put(hashtable: tuple[list, list], key: str, data: any, size: int) -> None:
    put_helper(hashtable, key, data, size)
    return auto_resize(hashtable, size)


def Update(hashtable: tuple[list, list],
           key: str,
           columnName: str,
           data: any,
           size: int,
           collision_path: dict[list],
           opNumber: int) -> None:

    keys, values = hashtable
    collision_path[opNumber] = []
    hash_address = hash_function(key, size)

    while True:
        collision_path[opNumber].append(hash_address)
        if keys[hash_address] == key:
            values[hash_address][columnName] = data
            print('record updated')
            break
        hash_address = collision_resolver(key, hash_address, size)
        if hash_address in collision_path[opNumber]:
            print("Item not found")
            break


def get(hashtable: tuple[list, list], key: str, size: int,
        collision_path: dict[list], opNumber: int) -> any:

    keys, values = hashtable
    collision_path[opNumber] = []
    hash_address = hash_function(key, size)

    while True:
        collision_path[opNumber].append(hash_address)
        if keys[hash_address] == "#":
            break
        if keys[hash_address] == key:
            return values[hash_address]

        hash_address = collision_resolver(key, hash_address, size)
        if hash_address in collision_path[opNumber]:
            break
    print("Item not found")


def delete(hashtable: tuple[list, list],
           key: str,
           size: int,
           collision_path: dict[list],
           opNumber: int) -> tuple[list, list]:

    keys = hashtable[0]
    collision_path[opNumber] = []
    hash_address = hash_function(key, size)

    while True:
        collision_path[opNumber].append(hash_address)
        if keys[hash_address] == key:
            keys[hash_address] = "#"
            print("Item Deleted")
            break

        hash_address = collision_resolver(key, hash_address, size)
        if hash_address in collision_path[opNumber]:
            print("Item not found")
            return hashtable, size

    return auto_resize(hashtable, size)
