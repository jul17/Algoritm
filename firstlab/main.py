import csv
import datetime
from counter import Counter
from quick_sort import quickS
from selection_sort import Selection
from student import Student


def read_data():
    student_list = []
    try:
        with open('student.csv') as csv_file:
            cvs_reader = csv.reader(csv_file)
            for row in cvs_reader:
                new_student = Student(row[0], row[1], int(row[2]), int(row[3]))
                student_list.append(new_student)
    except FileExistsError:
        print("Data does not exist")
    return student_list


def work_time(begin, end):
    return end - begin


def print_result(al_name, work_time, number_of_compare, number_of_exchange, sorted_list):
    print(str(al_name) + "\nWork time " + str(work_time) + "\nCompare Number: " + str(number_of_compare) +
          "\nExchange Number: " + str(number_of_exchange) + "\nSorted List: " + str(sorted_list))


if __name__ == "__main__":
    student_list = read_data()
    begin = datetime.datetime.now().microsecond
    select_list = Selection(student_list)
    end = datetime.datetime.now().microsecond
    print_result("Selction sort", work_time(begin, end), Counter.number_of_comparison,
                 Counter.number_of_exchange, select_list)
    print()
    Counter.counter_reset()
    begin = datetime.datetime.now().microsecond
    select_list = quickS(student_list)
    end = datetime.datetime.now().microsecond
    print_result("Quick sort", work_time(begin, end), Counter.number_of_comparison,
                 Counter.number_of_exchange, select_list)
