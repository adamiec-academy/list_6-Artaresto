def generate_assingments(previous_assingments, coders):
    
    my_list = coders.copy()
    new_ass = previous_assingments.copy()
    shuffle(my_list)
    
    for key, value in previous_assingments.items():
        while True:
            if previous_assingments[key] != my_list[0] and previous_assingments[value] != my_list[0] and new_ass.items() != dict(map(reversed, new_ass.items())):   
                new_ass[key] = my_list[0]
                my_list.pop(0)
                break
            else:
                shuffle(my_list)

    return new_ass
    
