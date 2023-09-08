# array = [int(x) for x in input("Enter the elements of the array, separated by spaces: ").split()]
# print("The array elements are: ",array)
# print("Accessing Array items with their Indexes :")
# for i in range(len(array)):
#     print("Index", i, ":", array[i])


# ------------------------------------------------------------------



array = [int(x) for x in input("Enter the elements of the array, separated by spaces: ").split()]
print("The array elements are: ",array)

if __name__ == "__main__":
    while True:
        index = int(input("Enter the index: "))
        if index < len(array):
            print("Element at index", index, "is:", array[index])
        else:
            print("Invalid index!")
        try_again = input("Do you want to try again with different number (yes/no):").lower()
        if try_again != "yes":
            break