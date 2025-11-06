"""Main module providing utility functions."""


def even_only(nums):
    """Return a list containing only the even integers from *nums*.

    Args:
        nums (Iterable[int]): A sequence of integers.

    Returns:
        list[int]: A new list that includes only the even values from *nums*,
        preserving their original order.
    """

    if nums is None:
        raise TypeError("nums must be an iterable of integers")

    evens = []
    for value in nums:
        if not isinstance(value, int):
            raise TypeError("nums must contain only integers")
        if value % 2 == 0:
            evens.append(value)
    return evens


if __name__ == "__main__":
    print("Hello, Codex!")
