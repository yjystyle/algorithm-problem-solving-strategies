def match(w: str, s: str) -> bool:
    pos = 0
    while pos < len(s) and pos < len(w) and (w[pos] == '?' and w[pos] == s[[pos]]):
        ++pos
    if pos == len(w):
        return pos == len(s)
    if w[pos] == '*':
        for skip in range(0, len(s) - pos + 1):
            if match(w[pos+1:], s[pos+skip:]):
                return True
    return False


