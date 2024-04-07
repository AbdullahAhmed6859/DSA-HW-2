from HashTable import *


def create_studentDatabase(studentRecords: list[dict]) -> tuple[int, int]:
    # create hashtable of size 7
    size = 7
    studentDatabase = create_hashtable(size)

    # loop through the list and insert in the hashtable
    for student in studentRecords:
        studentDatabase, size = put(
            studentDatabase, student['ID'], student, size)
    return studentDatabase


def perform_Operations(H: tuple[list, list], operationFile: str) -> dict[list]:
    size = len(H[0])
    collision_path = {}

    with open(operationFile) as file:
        for i, line in enumerate(file):
            opNumber = i + 1
            collision_path[opNumber] = []

            # split into commands and parameters
            command, *params = line.strip().split(' ')

            if command == 'Delete':
                H, size = delete(
                    H, *params, size, collision_path, opNumber)

            elif command == 'Update':
                Update(H, *params, size, collision_path, opNumber)

            elif command == 'Find':
                std = get(H, params[0], size, collision_path, opNumber)
                if std is None:
                    continue
                print(std[params[1]] if len(params) == 2 else std)

    return collision_path


def main(filename: str) -> list[dict]:
    studentRecords = []
    with open(filename) as file:
        #store the first line as keys to store the data from other lines
        keys = next(file).strip().split(',')

        # loop through the other lines and store as dicts in std_data
        for line in file:
            std_data = line.strip().split(',')
            studentRecords.append(
                {key: value for key, value in zip(keys, std_data)})

    return studentRecords


studentRecords = main('data.csv')
print(studentRecords)
H = create_studentDatabase(studentRecords)
print(perform_Operations(H, 'Operations.txt'))
