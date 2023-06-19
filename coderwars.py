# def persistence(n): KATA 6
#     counter = 1
#     if len(str(n))==1:
#         return 0
#     n_array= [int(i) for i in list(str(n))]
#     mult =1
#     for i in range(len(n_array)):
#         mult = mult*n_array[i]
#     return persistence(mult) + counter
           
# print(persistence(0))

# import itertools

# def permutation(s):
#     permutations = list(set(itertools.permutations(s)))
#     new_permutations = ["".join(permutations[i]) for i in range(len(permutations))]
    
#     return new_permutations

# print(permutation("aabb"))

# import functools
# def solution (array_a, array_b):
#     absolute_difference = [abs(array_a[i]-array_b[i])**2 for i in range(len(array_a))]
#     prom = functools.reduce(lambda accu,item: accu+item,absolute_difference)/len(absolute_difference)
    
#     return prom


# solution ([1, 2, 3], [4, 5, 6] )

# def snail(snail_map):
#     len_ref= len(snail_map)
#     snail_array =[]
#     if len(snail_map[0])==0:
#         return []
#     n =1
#     while n <= len_ref:
#         if n%2 == 1:
#             part_1=  [snail_map[0][i] for i in range(len(snail_map))]
#             part_2 = [snail_map[i][len(snail_map)-1] for i in range(1,len(snail_map))]
#             snail_map=[row[:len(snail_map)-1] for row in snail_map ]
#             del snail_map [0]
#         else:
#             part_1=  [snail_map[len(snail_map)-1][i] for i in range(len(snail_map)-1,-1,-1)]
#             part_2 = [snail_map[i][0] for i in range(len(snail_map)-2,-1,-1)]
#             snail_map=[row[1:len(snail_map)] for row in snail_map ]
#             del snail_map [len(snail_map)-1]

        
#         snail_array += part_1 + part_2
#         n+=1
    
    
#     return snail_array


def solution(args):
    for i in range ()
        
        
    
    
