def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


# Main program
arr = [10, 20, 30, 40, 50, 60, 70]

target = int(input("Enter number to search: "))

if binary_search(arr, target):
    print("Number found")
else:
    print("Number not found")
