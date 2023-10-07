# class MinStack(list):
#     class __Node:
#         def __init__(self, val, min_node_element,
#                     prev_node=None) -> None:
#             self.val = val
#             self.prev_node = prev_node
#             self.min_node_element = min_node_element

#     def __init__(self) -> None:
#         self.__minElement = None
#         self.__tail = None
#         self.__length = 0

#     def push(self, value: int) -> None:
#         if self.__tail:
#             new_node = self.__Node(value, value)
#             new_node.prev_node = self.__tail
#             self.__tail = new_node

#             self.__tail.min_node_element = min(self.__tail.min_node_element,
#                                                new_node.prev_node.min_node_element)
#         else:
#             new_node = self.__Node(value, value)
#             self.__tail = new_node

#     def pop(self) -> None:
#         if self.__tail:
#             val_to_return = self.__tail.val
#             self.__tail = self.__tail.prev_node
#             return val_to_return
#         else:
#             raise ValueError('The Stack is already empty')

#     def top(self) -> int:
#         if self.__tail:
#             return self.__tail.val
#         else:
#             raise ValueError('The Stack is already empty')

#     def getMin(self) -> int:
#         return self.__tail.min_node_element


# def binary_search(nums, target):
#     l = 0
#     r = len(nums) - 1
#     m = (l + r) // 2

#     while l < r:
#         if nums[m] == target:
#             return m
        
#         elif nums[m] > target:
#             l = m
#             m = (l + r) // 2
#         elif nums[m] < target:
#             r = m
#             m = (l + r) // 2
#     return -1

# nums = [-1,0,3,5,9,12]
# target = 9
# print(binary_search(nums, target))

from math import *
def func(x):
    return 1.8 * x**2 - sin(10*x)

def first_deriv(x):
    return 3.6 * x - 10 * cos(10* x)

def ratio(x):
    return func(x) / first_deriv(x)

acc = 0.0001
n = 0
xn = -3.1415 / 18

while(abs(func(xn)) > acc):
    
    print(f"{n}  {xn}  {func(xn)}  {first_deriv(xn)}  {ratio(xn)}")
    xn = xn - ratio(xn)
    n += 1
print(f"{n}  {xn}  {func(xn)}  {first_deriv(xn)}  {ratio(xn)}")
