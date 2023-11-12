def solution(N, stages):
    # {스테이지1 : 실패율, 스테이지2 : 실패율, 스테이지3 : 실패율 ...}
    n_stage = {}

    # 도전자수
    challenger = len(stages)

    # 1 ~ N 만큼
    for i in range(1, N+1):
        # 스테이지 도전자 수가 0이 아닐때
        # 실패한 도전자 수를 찾아서 실패율을 구하여
        # n_stage의 딕셔너리 {스테이지 번호(i) : 실패율}에 넣는다.
        # 다음 스테이지 실패율을 구하기 위해 도전자 수에 실패한 도전자 수를 뺀다.
        if challenger != 0:
            fail_num = stages.count(i)
            n_stage[i] = fail_num / challenger
            challenger -= fail_num
            
        # 도전자 수가 0일 경우
        # 실패율을 0으로 한다.
        # n_stage의 딕셔너리 {스테이지 번호(i) : 실패율}에 넣는다.
        
        else:
            n_stage[i] = 0
            
    # n_stage를 value 기준으로 내림차순 정렬하여 key값만 뽑아 list에 넣기
    answer = sorted(n_stage, key=lambda x:n_stage[x], reverse=True)
    return answer