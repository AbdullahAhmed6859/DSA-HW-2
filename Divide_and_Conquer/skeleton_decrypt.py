def reverse_karatsuba(data: tuple[int, int] | list[tuple[int, int]]) -> tuple[int, int]:
    # base case: when data is a single tuple it will just return it
    if len(data) == 1:
        return data

    # genral case: when data is a list it will run reverse kartasuba algo on it
    a = reverse_karatsuba(data[0]) if isinstance(
        data[0], list) else data[0]
    
    b = reverse_karatsuba(data[2]) if isinstance(
        data[2], list) else data[2]

    # concatenate
    return int(str(b[0]) + str(a[0])), int(str(b[1]) + str(a[1]))


def main(filename: str) -> list[tuple[int, int]]:
    with open(filename) as f:
        # get number of test cases
        lines = int(next(f).strip())
        # call all test cases, store in a list and output
        return [reverse_karatsuba(eval(next(f).strip())) for _ in range(lines)]