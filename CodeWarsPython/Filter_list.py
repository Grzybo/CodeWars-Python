



def filter_list(l):
    new_list = []
    for i in l:        
        if type(i) == int and i >= 0:
            new_list.append(i)
    return new_list

print(filter_list([1,2,'a']))


     

  