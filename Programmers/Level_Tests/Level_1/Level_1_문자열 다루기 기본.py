def solution(s):
    if len(s) == 4 or len(s) == 6:
        for c in s:
            if not c.isdigit():
                return False
        return True
    else:
        return False