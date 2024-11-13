""" Special Rearrangement project

used to separate even and odd numbers
"""
def special_rearrangement(nums):
    """
    :param nums: separating the even and odd numbers and rearrange them.
    :return: The even numbers and then the odd numbers.
    """
    if not nums:  #check if array is empty
        return 0

    even_num = []
    odd_num = []
    for i in nums:
        if i % 2 == 0:   # storing even numbers
            even_num.append(i)
        else:  # storing odd numbers
            odd_num.append(i)
    return even_num+odd_num

numbers = [10,9,12,5,55,90,88,-1,-44,0,11,77]
print(special_rearrangement(sorted(numbers)))
