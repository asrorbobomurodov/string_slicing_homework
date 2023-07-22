def main(s,n):
    """
    The s string variable is given. return all characters except n characters at the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    return f'"{s[:-n]}"'
print(main("codeschooluz",3))
print(main("apple",1))