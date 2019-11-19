def balancedSum(sales):
    # Write your code here
    final_sum = sum(sales)
    added_nums = 0
    for index, elements in enumerate(sales):
        final_sum -= elements
        if added_nums == final_sum:
            return index
        added_nums += elements

    return "No possible solution"