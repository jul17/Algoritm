import math


def create_table_relations(input_string, count_of_worker):
    table_relations = []
    for i in range(count_of_worker):
        table_relations.append([])
        for j in range(count_of_worker):
            table_relations[i].append(0)
    for i in range(len(input_string)):
        if input_string[i] == "Y":
            table_relations[(int(i // count_of_worker))][i % count_of_worker] = 1
        else:
            table_relations[(int(i // count_of_worker))][i % count_of_worker] = 0
    return table_relations


def create_table_compensation(table_relations, count_of_worker):
    compensation_table = [0 for i in range(count_of_worker)]
    for i in range(count_of_worker):
        calculate_compensation_worker(i, table_relations, compensation_table, count_of_worker)
    return compensation_table


def calculate_compensation_worker(worker, table_relations, compensation_table, count_of_worker):
    compensation_worker = 0
    for i in range(count_of_worker):
        if compensation_table[i] > 0:
            continue
        if table_relations[worker][i] == 1:
            calculate_compensation_worker(i, table_relations, compensation_table, compensation_worker)
            compensation_worker += compensation_table[i]
    if compensation_worker > 0:
        compensation_table[worker] = compensation_worker
    else:
        compensation_table[worker] = 1
    return


def calculate_ceo_compensation_a(compensation_table):
    sum = 0
    for i in compensation_table:
        sum += i
    return sum


def calculate_ceo_compensation_b(compensation_table):
    sum = 0
    for i in range(len(compensation_table)):
        flag = True
        for j in table_relations:
            if j[i] == 1:
                flag = False
        if flag == True:
            sum += compensation_table[i]
    return sum


if __name__ == '__main__':
    # input_string = input()
    input_string = "NYYNNNYNNNYNNNNN"
    count_of_worker = int(math.sqrt(len(input_string)))
    table_relations = create_table_relations(input_string, count_of_worker)
    compensation_table = create_table_compensation(table_relations, count_of_worker)
    print(calculate_ceo_compensation_b(compensation_table))
    print(compensation_table)
