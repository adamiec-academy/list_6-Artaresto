def generate_assignments(previous_assignments, coders):
    
    my_list = coders.copy()
    new_ass = {}
    shuffle(my_list)
    
    for key, value in previous_assignments.items():
        while True:
            if key != my_list[0] and value != my_list[0]:
                for k, v in new_ass.items():
                    if k == my_list[0] and v == key:
                        break
                else:
                    new_ass[key] = my_list[0]
                    my_list.remove(my_list[0])
        
                    break
            else:
                shuffle(my_list)
    return new_ass
