#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            q = my_list_1[i] / my_list_2[i]
        except TypeError:
            q = 0
            print("wrong type")
        except ZeroDivisionError:
            q = 0
            print("division by 0")
        except IndexError:
            q = 0
            print("out of range")
        finally:
            new_list.append(q)
    return (new_list)
