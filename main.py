# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(list1):

    if len(list1) == len(set(list1)):
        return "List have unique elements"
    else:
        return "List have duplicate elements"
    return -1

def reverse_string(string):
    return string[::-1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    print(print_hi(list1))
    print(reverse_string("Devansh"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
