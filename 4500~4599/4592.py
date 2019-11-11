
# 문제
# Al의 초콜릿 망고 회사는 방문자들이 2d 단지에 얼마나 많은 초콜릿 망고가 있는지 추측할 수 있는 웹 사이트를 갖고 있다.
# 방문자들은 1부터 99까지의 수를 추측한 후 "제출" 버튼을 누르는데,
# 안타깝게도 서버로부터 응답시간이 종종 길어져 방문자들이 이성을 잃은 나머지 "제출"을 연타하는 사태가 발생한다.
# 이게 우리가 해결해야 할 문제다.
# ACM의 직원을 도와 연타된 중복을 걸러보자.
#
# 입력
# 각 줄마다 처음으로 정수 N(0 < N ≤ 25)이 주어진다.
# 그 다음 N개에 걸쳐 1부터 99 사이의 수가 주어진다.
# 마지막 줄에 입력의 끝을 알리는 0이 주어진다.

# 출력
# 각 케이스마다 한 줄씩 중복을 제거한 원래의 제출 상태를 출력한다.
# 각 줄의 마지막에는 한 칸을 띄고 '$' 표시가 붙는다.

while True:
    arr = list(input().split())

    if arr[0] is '0':
        break

    before = arr[1]

    print(before, end=" ")

    for c in arr[2:]:
        if c == before:
            continue

        print(c, end=" ")
        before = c

    print("$")
