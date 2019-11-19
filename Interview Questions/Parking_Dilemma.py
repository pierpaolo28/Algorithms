def carParkingRoof(cars, k):
    # Write your code here
    result  = 1000000000000000
    cars.sort()
    for i in range(len(cars)- k +1):
        result = int(min(result, cars[i +k -1] - cars[i] +1))
    return result