def minion_game(s):
    def is_vowel(c):
        return c == 'A' or c == 'E' or c == 'I' or c == 'U' or c == 'O'

    stuart_pts = 0
    kevin_pts = 0
    for i in range(len(s)):
        add = len(s) - i
        if is_vowel(s[i]):
            kevin_pts += add
        else:
            stuart_pts += add

    if stuart_pts > kevin_pts:
        print("Stuart " + str(stuart_pts))
    elif stuart_pts < kevin_pts:
        print("Kevin " + str(kevin_pts))
    else:
        print("Draw")
