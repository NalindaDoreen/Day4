def compute(ls):
    
    sum_no=0
    for i in ls:
        if isinstance(i,int):
            sum_no+=i

        elif isinstance(i,list):
            sum_no+=compute(i)
        
    return sum_no

if __name__ == '__main__':
    print(compute(['b',2,[4,7]]))