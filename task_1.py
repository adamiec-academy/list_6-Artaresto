def generate_assignments(previous_assignments, coders):
    mixed_coders = coders.copy()
    
    
    
    while True:
        shuffle(mixed_coders) 
        new_ass = {}
            
        for i in range(len(mixed_coders)):
            new_ass[coders[i]] = mixed_coders[i]
        
        if mixed_coders[i] != coders[i] or mixed_coders[i] != coders[mixed_coders.index(coders[i])] and coders[i] in previous_assignments.keys() and previous_assignments[coders[i]] != mixed_coders[i]:

            return new_ass
