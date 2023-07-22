def main(s,n):
    """
    The s string variable is given. return n characters from the beginning.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    return f'"{s[0:n]}"'
print(main("Asror", 3))
print(main("positive", 2))