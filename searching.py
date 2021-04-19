import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    if field not in {"unordered_numbers","ordered_numbers","dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as json_file:
        data = json.load(json_file)

        return data[field]


def linear_search(sequence,number):
    b = 0
    count = 0
    indicie = []
    while b < len(sequence):
        if sequence[b] == number:
            count = count + 1
            indicie.append(b)
        b = b + 1

    return {"positions": indicie, "count": count}






def main():
    sequential_data =read_data("sequential.json", "unordered_numbers")
    results = linear_search(sequential_data, 0)
    print(results)



if __name__ == '__main__':
    main()