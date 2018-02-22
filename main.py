def validate(n):
    sum = 0
    arr = list(str(n))
    if len(arr) % 2 == 0:
        for i in range(0,len(arr),2):
            if int(arr[i]) * 2 > 9:
                arr[i] = str(int(arr[i]) * 2 - 9)
            else:
                arr[i] = str(int(arr[i]) * 2)
    for number in arr:
        sum += int(number)
    if sum % 10 == 0:
        return True
    else:
        return False