def repeating_dec_sol(numerator, denominator):
    negative = False
    if denominator == 0:
        return 'Undefined'
    if numerator == 0:
        return '0'
    if numerator*denominator < 0:
        negative = True
    if numerator % denominator == 0:
        return str(numerator/denominator)

    num = abs(numerator)
    den = abs(denominator)

    result = ""
    result += str(num // den)
    result += "."

    quotient_num = []
    while num:
        # In case the remainder is equal to zero, there are no repeating
        # decimals. Therefore, we don't need to add any parenthesis and we can
        # break the while loop and return the result.
        remainder = num % den
        if remainder == 0:
            for i in quotient_num:
                result += str(i[-1])
            break
        num = remainder*10
        quotient = num // den

        # If the new numerator and quotient are not already in the list, we
        # append them to the list.
        if [num, quotient] not in quotient_num:
            quotient_num.append([num, quotient])
        # If the new numerator and quotient are instead already in the list, we
        # break the execution and we prepare to return the final result.
        # We take track of the index position, in order to add the parenthesis
        # at the output in the right place.
        elif [num, quotient] in quotient_num:
            index = quotient_num.index([num, quotient])
            for i in quotient_num[:index]:
                result += str(i[-1])
            result += "("
            for i in quotient_num[index:]:
                result += str(i[-1])
            result += ")"
            break

        if negative:
            result = "-" + result

    return result


NUM, DEN = 1, 6
print("The result of the fraction", NUM, "/", DEN, "is equal to: ", repeating_dec_sol(NUM, DEN))



