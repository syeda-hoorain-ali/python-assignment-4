def add_three_copies(my_list, data):
    """
    Appends the given data to the provided list three times.
    """

    for _ in range(3):
        my_list.append(data)


def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

if __name__ == "__main__":
    main()
