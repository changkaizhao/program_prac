# 题目链接 https://leetcode-cn.com/problems/maximum-69-number/


def test(num):
    # 逻辑代码写到这里
    return int(str(num).replace("6","9",1))
    # 替代第一个6变成9，重复一次


if __name__ == "__main__":
    test_nums = [6699, 9696,   69696969, 66669696,
                 9966969, 696, 99969, 999, 6666, 9996, 999996666]

    for n in test_nums:
        print(test(n))
