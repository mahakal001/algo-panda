def find_root_interval(x):

    min = 1
    max = x

    count = 0
    while min <= max:
        count += 1
        mid = (min + max) // 2
        if pow(mid, 2) < x:
            min = mid + 1
        elif pow(mid, 2) > x:
            max = mid - 1
        else:
            return mid,mid, count


    return max, min, count

min,max,count = find_root_interval(int(input()))
print("Root of given number lies in the follwoing interval: ", min, max)
print("Total iteration performed: ", count )