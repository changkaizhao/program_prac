# x = int(input("x="))
# a = 2
# s = []
# for i in range(1, x+1):
#     if x > a and x % a == 0:
#         s.append(a)
#     a = a + 1
# print("answer is", s)


def factorial(n):
    # 在这里写程序
    pass


def inList(n, l):
    return n in l


def assertEqual(a1, a2):
    if len(a1) == len(a2):
        for i in a1:
            if i in a2:
                a2.remove(i)
        if len(a2) == 0:
            print('✅ pass')
        else:
            print('❌ Not pass')

    else:
        print('❌ Not pass')


def test_factorial():

    a1 = factorial(1)
    assertEqual(a1, [1])

    a1 = factorial(2)
    assertEqual(a1, [1, 2])

    a1 = factorial(10)
    assertEqual(a1, [1, 2, 5, 10])

    a1 = factorial(6)
    assertEqual(a1, [1, 2, 3, 6])

    a1 = factorial(8)
    assertEqual(a1, [1, 2, 4, 8])

    a1 = factorial(20)
    assertEqual(a1, [1, 2, 4, 5, 10, 20])


if __name__ == '__main__':
    test_factorial()
