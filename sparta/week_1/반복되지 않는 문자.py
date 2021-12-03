# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때,
# 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오.
# 만약 그런 문자가 없다면 _ 를 반환하시오.
# "abadabac" # 반복되지 않는 문자는 d, c 가 있지만 "첫번째" 문자니까 d를 반환해주면 됩니다!
def find_not_repeating_first_character(string):

    alphabet_array = [0]*26
    not_repeat_char_array = []

    #각 문자별 빈도수 확인
    for char in string:
        if not char.isalpha():
            continue
        index = ord(char) - ord('a')
        alphabet_array[index] += 1

    #alphabet_array 돌면서 값이 1인 문자만 배열에 담아줌
    for i in range(len(alphabet_array)):
        if(alphabet_array[i] == 1):
            not_repeat_char_array.append(chr(i + ord('a')))

    #string에 있는 문자가  반복되지 않은 문자 배열에 있는지 확인 후 있으면 바로 리턴.
    for char in string:
        if char in not_repeat_char_array:
            return char

    return "_"

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))