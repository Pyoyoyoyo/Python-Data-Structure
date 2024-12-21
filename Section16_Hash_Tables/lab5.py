# Part A: Selection Sort (Sorting the array in ascending order)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the smallest element in the unsorted part of the array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found smallest element with the current element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Part B: Binary Search (Searching for an element in the sorted array)
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Element found at index mid
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Element not found


# Main program to get input from the user
def main():
    # Get the size of the array from the user
    n = int(input("Enter the number of elements in the array: "))

    # Get the array elements from the user
    arr = []
    print("Enter the elements:")
    for i in range(n):
        element = int(input(f"Element {i + 1}: "))
        arr.append(element)

    # Get the target value to search for
    target = int(input("Enter the value to search for: "))

    # Step 1: Sort the array
    selection_sort(arr)

    # Step 2: Perform binary search
    result = binary_search(arr, target)

    # Display the sorted array and the result of the binary search
    print("Sorted array:", arr)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")


# Run the main function
if __name__ == "__main__":
    main()
