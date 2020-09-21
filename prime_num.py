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
    def isprime(n):  # 一个判断质数的方法，如果是质数，就返回这个数，如果不是质数，就什么也不返回
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            return n

    num = int(input("number: "))
    i = 1  # 哨兵变量为1
    if num >= 2:

        while i <= num:
            i = i + 1
            if num % i == 0:  # 如果i为因子
                print(isprime(i))  # 先看这个因子是不是质数，是就输出
                num = num / i
                print("num is %s now!" % num) # 现在打num
                i = 1  # 记得把哨兵重新设置为1，这样循环才会更新，我一开始用for语句循环，发现没法从头开始循环
                pass
            else:
                pass
    else:
        print("error")


    pass


def assertEqual(a1, a2):

    if len (a1) == 0:
        print('❌ Not pass')
    else:
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
