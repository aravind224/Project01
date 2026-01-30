def MoveZerosToEnd(arr, n):
    j = -1
    for i in range(0, n):
        if arr[i] == 0:
            j = i
            break

    if j == -1:
        return arr

    for i in range(j + 1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr


# This part runs ONLY when you manually run the file
if __name__ == "__main__":
    arr = [1, 2, 0, 4, 0, 5, 0, 3, 5, 6, 4, 0, 0]
    n = len(arr)
    print("Values:", MoveZerosToEnd(arr, n))
