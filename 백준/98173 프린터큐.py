from collections import deque

# 현재 큐 가장 앞의 문서의 중요도를 확인
# 나머지 문서들 중 현재 중요도가 높은 문서가 하나라도 있다면
# 이 문서를 인쇄하지 않고 popleft+push

T = int(input())

for tc in range(1, T+1):
    # N : 문서의 개수
    # M : 몇번쨰로 인쇄되었는지 궁금한 문서
    N, M = map(int, input().split())
    # 중요도 리스트
    doc = list(map(int, input().split()))

    # 순서와 중요도가 함께 저장된 리스트
    real_doc = deque([[i+1, p] for i, p in enumerate(doc)])
    
    cnt = 0

    while real_doc:
        now = real_doc.popleft()

        if any(now[1] < other[1] for other in real_doc):
            real_doc.append(now)
        else:
            cnt += 1

            if now[0] == M+1:
                print(cnt)
                break