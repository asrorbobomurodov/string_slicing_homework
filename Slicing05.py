def main(s,n):
    """
    The s string variable is given. return n characters from the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    return f'"{s[-n:]}"'
print(main("python",3)) 
print(main("codeschool.uz", 3))
