def remove_elements(lista):
    for i in sorted([5, 4, 0], reverse=True):
        if i < len(lista):
         del lista[i]
    return lista

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,"Pink")
    list_to_add_elements.append("Yellow")
    return list_to_add_elements

def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    else:
        return False

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1)<3 or len(list_to_compare2)<3:
        return False
    else :
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else:
            return False

def list_of_lists(list_of_lists_to_modify):
    if len(list_of_lists_to_modify[0]) < 3:
        paso_3 = list_of_lists_to_modify[0]
    else:
        paso_3 = list_of_lists_to_modify[0][0:2]

    if len(list_of_lists_to_modify[1]) < 5:
        if len(list_of_lists_to_modify[1]) >= 2:
            paso_2 = list_of_lists_to_modify[1][1:]
        else:
            paso_2 = []
    else:
        paso_2 = list_of_lists_to_modify[1][1:4]

    if len(list_of_lists_to_modify[2]) < 3:
        paso_1 = list_of_lists_to_modify[2]
    else:
        paso_1 = list_of_lists_to_modify[2][-2:]

    return [paso_3, paso_2, paso_1]
