def epley(weight, reps):
    return weight*(1+reps/30)

def round_weight(num, roundTo = 5):
    return round(num/roundTo) * roundTo
    
def calc_plates(weight, bar = 45):
    available_plates = [45, 35, 25, 10, 5, 2.5]
    result = []
    trueWeight = round_weight(weight)
    print(weight, "rounded to:", trueWeight)
    if trueWeight < bar:
        print("Weight must be at least the weight of the bar")
    elif trueWeight == bar:
        result += [0]
    else:
        remaining = trueWeight - bar
        remaining /= 2
        #print(remaining)
        for num in available_plates:
            while num <= remaining:
                result.append(num)
                remaining -= num
            #print(remaining)
    print(result)
