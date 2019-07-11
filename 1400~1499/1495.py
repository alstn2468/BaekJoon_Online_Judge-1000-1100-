 
# 문제
# Day Of Mourning의 기타리스트 강토는 다가오는 공연에서 연주할 N개의 곡을 연주하고 있다. 
# 지금까지 공연과는 다른 공연을 보여주기 위해서 이번 공연에서는 매번 곡이 시작하기 전에 볼륨을 바꾸고 연주하려고 한다.
# 먼저, 공연이 시작하기 전에 각각의 곡이 시작하기 전에 바꿀 수 있는 볼륨의 리스트를 만들었다. 
# 이 리스트를 V라고 했을 때, V[i]는 i번째 곡을 연주하기 전에 바꿀 수 있는 볼륨을 의미한다. 
# 항상 리스트에 적힌 차이로만 볼륨을 바꿀 수 있다. 
# 즉, 현재 볼륨이 P이고 지금 i번째 곡을 연주하기 전이라면, i번 곡은 P+V[i]나 P-V[i] 로 연주해야 한다. 
# 하지만, 0보다 작은 값으로 볼륨을 바꾸거나, M보다 큰 값으로 볼륨을 바꿀 수 없다.
# 곡의 개수 N과 시작 볼륨 S, 그리고 M이 주어졌을 때, 마지막 곡을 연주할 수 있는 볼륨 중 최댓값을 구하는 프로그램을 작성하시오. 
# 모든 곡은 리스트에 적힌 순서대로 연주해야 한다.
# 
# 입력
# 첫째 줄에 N, S, M이 주어진다. (1 ≤ N ≤ 100, 1 ≤ M ≤ 1000, 0 ≤ S ≤ M) 
# 둘째 줄에는 각 곡이 시작하기 전에 줄 수 있는 볼륨의 차이가 주어진다. 
# 이 값은 1보다 크거나 같고, M보다 작거나 같다.
# 
# 출력
# 첫째 줄에 가능한 마지막 곡의 볼륨 중 최댓값을 출력한다. 
# 만약 마지막 곡을 연주할 수 없다면 (중간에 볼륨 조절을 할 수 없다면) -1을 출력한다.

N, S, M = map(int, input().split())
volume = list(map(int, input().split()))
dp = [{} for _ in range(N + 1)]
dp[0][S] = True

for i in range(N):
    for key in dp[i].keys():
        if key - volume[i] >= 0:
            dp[i + 1][key - volume[i]] = True
            
        if key + volume[i] <= M:
            dp[i + 1][key + volume[i]] = True
            
if len(dp[N]) > 0:
    print(sorted(dp[N].keys(), reverse=True)[0])
    
else:
    print(-1)