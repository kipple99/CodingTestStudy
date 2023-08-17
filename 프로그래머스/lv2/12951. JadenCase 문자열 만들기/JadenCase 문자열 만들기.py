def solution(s):
    sentence = s.lower()
    words = sentence.split(' ')
    answer_list = []

    for i in words:
        answer_list.append(i.capitalize())

    answer = ' '.join(answer_list)
    
    return answer