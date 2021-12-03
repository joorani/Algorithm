input = "ddddddd my name is sparta"


def find_max_occurred_alphabet(string):
    alpha_array = [0] * 26
    #문자인지 확인하고 빈도수 측정 array생성.
    for char in string:
      if not char.isalpha():
        continue; #문자이면
      index = ord(char) - ord('a')
      alpha_array[index] += 1


    #alpah_array에서 가장 큰 수가 몇 번 인덱스인지 확인
    max_occur = 0;
    max_alpha_index = 0;
    for index in range(len(alpha_array)):
        alpha_occur = alpha_array[index]
        if alpha_occur > max_occur:
          max_occur = alpha_occur
          max_alpha_index = index
    
    #가장 큰 수의 인덱스가 어떤 문자인지 리턴.
    temp = max_alpha_index + ord('a')
    return chr(temp)

result = find_max_occurred_alphabet(input)
print(result)

#문자인지 확인 방법 str.isalpha()
#알파벳 별 빈도수로 저장 - 아스키코드 ord()