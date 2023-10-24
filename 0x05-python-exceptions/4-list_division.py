#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    i = 0

    if list_length <= 0:
        print("out of range")
        return (n_list)
    while i < list_length:
        try:
            n_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            n_list.append(0)
        except TypeError:
            print("wrong type")
            n_list.append(0)
        except iError:
            print("out of range")
            n_list.append(0)
        finally:
            i += 1
    return (n_list)
