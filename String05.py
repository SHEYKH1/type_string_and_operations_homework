def main(s1,s2):
    """
    s1 and s2 strings are given. return the result by adding a space (" ") between them.
    Args:
        s1: str
        s2: str
    Returns:
        str: return answer.
    """
    S=s1+ " " +s2
    return S
s1="123"
s2="321"

print(main(s1,s2))