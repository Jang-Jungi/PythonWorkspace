''' 13단계 집합과 맵'''
# 수정예정이라 문제가 없다.

''' 14단계 백트래킹 '''
# # 15649 N과 M(1)
# N,M = map(int,input().split())
# visited = [False]* N # 탐사 여부 check
# out = [] # 출력 내용

# def solve(depth, N, M):
#     if depth == M: # 탈출 조건
#         print(' '.join(map(str, out))) # list를 str로 합쳐 출력
#         return
#     for i in range(len(visited)): # check
#         if not visited[i]: 
#             visited[i] = True     # 탐사 시작(중복 제거)
#             out.append(i+1)       # 탐사 내용
#             solve(depth+1, N, M)  # 깊이 우선 탐색
#             visited[i] = False    # 깊이 탐사 완료
#             out.pop()             # 탐사 내용 제거

# solve(0, N, M)
