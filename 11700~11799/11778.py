
# 문제
# 피보나치 수는 0과 1로 시작한다.
# 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다.
# 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n>=2)가 된다.
# n=17일때 까지 피보나치 수를 써보면 다음과 같다.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
# n과 m이 주어졌을 때, n번째 피보나치 수와 m번째 피보나치 수의 최대공약수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 n과 m이 주어진다.
# n과 m은 1,000,000,000,000,000,000보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 n번째 피보나치 수와 m번째 피보나치 수의 최대공약수를 1,000,000,007으로 나눈 나머지를 출력한다.

import sys
mod = 1_000_000_007


def get_gcd_of_fibonacci(n, m):
    gcd_val = get_gcd(n, m)

    ans = [[1, 0], [1, 0]]
    a = [[1, 1], [1, 0]]

    while gcd_val > 0:
        if gcd_val % 2 == 1:
            ans = [
                [(ans[0][0] * a[0][0] + ans[0][1] * a[1][0]) % mod,
                 (ans[0][0] * a[0][1] + ans[0][1] * a[1][1]) % mod],
                [(ans[1][0] * a[0][0] + ans[1][1] * a[1][0]) % mod,
                 (ans[1][0] * a[0][1] + ans[1][1] * a[1][1]) % mod]
            ]

        a = [
            [(a[0][0] * a[0][0] + a[0][1] * a[1][0]) % mod,
             (a[0][0] * a[0][1] + a[0][1] * a[1][1]) % mod],
            [(a[1][0] * a[0][0] + a[1][1] * a[1][0]) % mod,
             (a[1][0] * a[0][1]+a[1][1] * a[1][1]) % mod]
        ]

        gcd_val //= 2

    return ans[0][1] % mod


def get_gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2

    return n1


n, m = map(int, sys.stdin.readline().split())

print(get_gcd_of_fibonacci(n, m))
