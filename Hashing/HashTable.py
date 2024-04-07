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


def auto_resize(hashtable: tuple[list, list],
                size) -> tuple[tuple[list, list], int]:
    lf = loadFactor(hashtable, size)

    if lf > 75:
        hashtable, size = resize_hashtable(hashtable, size, True)
    elif lf < 30 and size > 7:
        hashtable, size = resize_hashtable(hashtable, size, False)

    return hashtable, size


def hashtable_iter(hashtable, key: str, size: int, collision_list=[]):
    address = start = hash_function(key, size)
    collision_list.append(address)
    keys, values = hashtable

    while keys[address] != "#":
        # adress, key, value returned by the generator
        yield address, keys[address], values[address]
        
        if keys[address] is None:
            collision_list.append(address)
            break
        address = collision_resolver(key, address, size)
        if address == start:
            break

        collision_list.append(address)


def next_prime(num: int) -> int:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    while not is_prime(num):
        num += 1
    return num


def put_helper(hashtable: tuple[list, list],
               key: str, data: any, size: int) -> None:

    keys, values = hashtable
    # exhaust the generstor to the the right adress
    for address, _, _ in hashtable_iter(hashtable, key, size):
        continue

    # insert the record
    keys[address] = key
    values[address] = data


def resize_hashtable(hashtable: tuple[list, list], size: int,
                     increase: bool) -> tuple[tuple[list, list], int]:

    if size == 7 and not increase:
        return hashtable, size

    # if increase is True double the size of the Hashtable else reduce it to half the size then to the nearest prime number
    new_size = next_prime(size * 2 if increase else size // 2)
    new_table = create_hashtable(new_size)

    # loop through each key and val in the hashtable
    for key, val in zip(*hashtable):
        # if its a valid key then insert it into the new table
        if key and key != "#":
            put_helper(new_table, key, val, new_size)

    return new_table, new_size


def put(hashtable: tuple[list, list], key: str,
        data: any, size: int) -> tuple[tuple[list, list], int]:
    # insert int the table
    put_helper(hashtable, key, data, size)
    # resize the table
    return auto_resize(hashtable, size)


def Update(hashtable: tuple[list, list],
           key: str,
           columnName: str,
           data: any,
           size: int,
           collision_path: dict[list],
           opNumber: int) -> None:

    # hash and collision resolve to get the record to update
    for _, k, v in hashtable_iter(
            hashtable, key, size, collision_path[opNumber]):
        # if its the right key update the record
        if k == key:
            v[columnName] = data
            print('item updated')
            return

    # if record not found then output
    print("Item could not be updated")


def get(hashtable: tuple[list, list], key: str, size: int,
        collision_path: dict[list], opNumber: int) -> any:
    # hash and collision resolve to get the record
    for _, k, v in hashtable_iter(
            hashtable, key, size, collision_path[opNumber]):
        # if its the right key return its value
        if k == key:
            return v

    print("Item not found")
    return


def delete(hashtable: tuple[list, list],
           key: str,
           size: int,
           collision_path: dict[list],
           opNumber: int) -> tuple[tuple[list, list], int]:

    keys = hashtable[0]

    # hash and collision resolve to get the record
    for address, k, _ in hashtable_iter(
            hashtable, key, size, collision_path[opNumber]):
        # if its the right key delete it
        if k == key:
            keys[address] = "#"
            print("Item Deleted")
            return auto_resize(hashtable, size)

    print("Item Item could not be deleted")
    return hashtable, size
