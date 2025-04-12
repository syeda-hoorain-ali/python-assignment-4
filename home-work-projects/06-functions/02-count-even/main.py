def count_even(lst: list[int]) -> int:
    """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """

    count = 0  
    for num in lst: 
        if num % 2 == 0:  
            count += 1 

    return count

def get_list_of_ints() -> list[int]:
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """

    lst: list[int] = []  
    user_input = input("Enter an integer or press enter to stop: ").strip() 

    while user_input != "": 
        lst.append(int(user_input))
        user_input = input("Enter an integer or press enter to stop: ")

    return lst


def main():
    lst = get_list_of_ints()
    total_even_numbers = count_even(lst)
    print("Total even numbers: ", total_even_numbers)

if __name__ == '__main__':
    main()
