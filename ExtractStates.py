#given a cplex solution this function extract the states

def extractS(solution):
    
    L = []
    D = solution.as_df(name_key='X', value_key='value').to_dict()['X']
    for i in D.values():
        L.append( (int(i[1:3][0]), int(i[1:3][1])) )
    
    return list(set(L)) #unique states
        
def extractSA(solution):
    
    L = []
    D = solution.as_df(name_key='X', value_key='value').to_dict()['X']
    for i in D.values():
        L.append( ( (int(i[1:3][0]), int(i[1:3][1]) ), i[3:len(i)]) )
    
    return L
          