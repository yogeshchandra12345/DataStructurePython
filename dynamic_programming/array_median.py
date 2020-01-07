import sys


def median(nums):
    """
    Calculate the median of a list of numbers
    :param nums: a list of which median is calculated
    :return: median
    """

    sorted_nums = sorted(nums)
    len_nums = len(sorted_nums)
    odd = len_nums % 2

    # If the length is odd, the median is the middle value of the sorted list.
    if odd:
        return sorted_nums[(len_nums - 1) // 2]

    # Otherwise it's the average of the middle two
    return (sorted_nums[len_nums // 2] + sorted_nums[(len_nums - 1) // 2]) / 2


def test_median():
    """Test the median function for correctness."""
    assert median([1, 2, 3]) == 2
    assert median([1, 2.9, 3]) == 2.9
    assert median([1, 2, 3, 4]) == 2.5
    assert median([2, 1, 4, 3]) == 2.5
    assert median([1, 3, 3, 4, 5, 6, 8, 9]) == 4.5


def main():
    """
    Calculates median of numbers in stdin.
    """
    # Read stdin until EOF
    nums_string = input()

    # Split on whitespace
    num_strings = nums_string.split()

    # Make a new list of floats of all the non-whitespace values.
    nums = [float(i) for i in num_strings if i]

    # Print median
    if not nums:
        print("You didn't enter any numbers.")
    else:
        print(median(nums))


if __name__ == '__main__':
    test_median()
    main()
