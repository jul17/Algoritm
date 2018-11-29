def dfs(list_pairs, one_tribe, i):
    j = 0
    while j < len(list_pairs):
        if (list_pairs[j][0] == i):
            person = list_pairs[j][1]
            devide_men_and_women(one_tribe, person)
            list_pairs.pop(j)
            dfs(list_pairs, one_tribe, person)
            j = 0
        else:
            j += 1
    return one_tribe


def devide_men_and_women(one_tribe, person):
    if (person % 2 == 0):
        one_tribe[0].append(person)
    else:
        one_tribe[1].append(person)


def calculate_all_possible_pairs(list_of_tribe):
    all_possible_pairs = []
    for tribe in list_of_tribe:
        for men in tribe[0]:
            for other_tribe in list_of_tribe:
                if tribe != other_tribe:
                    for women in other_tribe[1]:
                        all_possible_pairs.append([women, men])
    return all_possible_pairs


def split_pairs_on_tribe(list_pairs):
    list_of_tribe = []
    while (len(list_pairs) > 0):
        one_tribe = [[], []]
        if (list_pairs[0][0] % 2 == 0):
            one_tribe[0].append(list_pairs[0][0])
        else:
            one_tribe[1].append(list_pairs[0][0])
        one_tribe = dfs(list_pairs, one_tribe, list_pairs[0][0])
        list_of_tribe.append(one_tribe)
    return list_of_tribe


def input_pair_from_console():
    number_of_pairs = input()
    list_pairs = []
    for i in range(0, int(number_of_pairs)):
        var = input().split()
        list_pairs.append([int(var[0]), int(var[1])])
    return list_pairs


def print_result(all_possible_pairs):
    print("Count of possible pairs: " + str(len(all_possible_pairs)))
    print("All possible pairs: " + str(all_possible_pairs))


if __name__ == "__main__":
    list_pairs = input_pair_from_console()
    list_of_tribe = split_pairs_on_tribe(list_pairs)
    all_possible_pairs = calculate_all_possible_pairs(list_of_tribe)
    print_result(all_possible_pairs)
