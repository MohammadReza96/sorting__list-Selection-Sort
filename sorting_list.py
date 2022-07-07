def sorting_list(*args):
    result=list(args)
    for item in range(len(result)):
        for items in range(item+1,len(result)):
            if result[item]>result[items]:
                result[item],result[items]=result[items],result[item]
    return result

li=[5,2,7,1,6,9,13,31,43,34,23,11,-1,55,23,12,11,5]
print(sorting_list(*li))
print(sorting_list(2,5,10,2,3,7,2,8))

