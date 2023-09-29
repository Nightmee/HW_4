my_list = ['чай','кава','печево']

my_dictionery = {'вовк','собака','кіт'}

my_set = {'Алекс','Боб','Пітер'}

my_tuple = (6, 5, 4, 3, 2)

my_list.append(my_dictionery)
my_list.append(my_tuple)
print(my_list)

def array_diff(arr1, arr2):
    return [x for x in arr1 if x not in arr2]

result_func = array_diff([1,2,2,2,3,],[2])

print(result_func)