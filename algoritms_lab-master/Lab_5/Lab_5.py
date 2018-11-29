import math

from pip._vendor.distlib.compat import raw_input


def calculate_length_between_spillars(height_first, height_second, length_between_pillars,):
    return math.sqrt(int(length_between_pillars)**2+(int(height_first)-int(height_second))**2)

def choose_longest_way(height_first, height_second, length_between_pillars):
    first_way=calculate_length_between_spillars(height_first,1,length_between_pillars)
    second_way=calculate_length_between_spillars(height_first,height_second,length_between_pillars)
    if(first_way>second_way):
        return first_way
    else:
        return second_way

def calculate_next_result(result,next_height,length_between_pillars):
    result[0][0]=result[0][0]+choose_longest_way(result[0][1],next_height, length_between_pillars)
    result[1][0]=result[1][0]+choose_longest_way(result[1][1],next_height,length_between_pillars)

def choose_result(result):
    if(result[0][0]>result[1][0]):
        return result[0][0]
    else:
        return result[1][0]
def set_start_result():
    return [[0,1],[0,array_height_pillars[0]]]

def iterative_process(length_between_pillars, array_height_pillars,result):
    for i in range(1,len(array_height_pillars)):
        calculate_next_result(result, array_height_pillars[i],length_between_pillars)
    return result


if __name__ == '__main__':
    length_between_pillars = int(input())
    string_input_data=raw_input()
    array_height_pillars=string_input_data.split()
    result=set_start_result()
    result=iterative_process(length_between_pillars, array_height_pillars, result)
    print(choose_result(result))


