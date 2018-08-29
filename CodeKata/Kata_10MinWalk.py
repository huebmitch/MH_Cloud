# Kata: Take a Ten Minute walk

walk1 = ['e', 'w', 'w', 'n', 'e', 'w']
walk2 = ['n', 'e', 's', 'w', 'n', 'e', 's', 'w', 'n', 's']

def isValidWalk(walk):
    x = (walk.count("n") - walk.count("s"))
    y = (walk.count("e") - walk.count("w"))

    if len(walk) != 10:
        return False
    elif x and y == 0:
        return True
    else:
        return False

print(isValidWalk(walk1))
print(isValidWalk(walk2))
