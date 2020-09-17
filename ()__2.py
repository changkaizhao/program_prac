def test(s):
    cup = []

    for item in s:
        if(item == '('):
            cup.append(0)
        elif(item == ')'):
            lastV = cup.pop()
            if(lastV == 0):
                if(len(cup) == 0):
                    return 1
                else:
                    cup[-1] += 1
            else:
                if(len(cup) == 0):
                    return lastV * 2
                else:
                    cup[-1] += lastV * 2



if __name__ == '__main__':
    t = '(()(()()))'
    print(test(t))
