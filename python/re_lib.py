# 고객 문의 사항 예시
data = """
안녕하세요!
멋사 제품을 항상 저를 만족시킵니다.
상당히 잘 사용하고 있는데 제가 멤버쉽에 잘 가입되었는지 궁금합니다.
제 이름은 홍길동이고 주민번호는 900101-1234567 이며 전화번호는 010-1234-5678입니다.
확인 부탁드립니다!
"""

#900101-1234567 마스킹처리 
# 단어 단어를 쪼개서 그 부분이
# 14개의 문자로 이어진 부분이 있으면
# - 구분하고 앞부분, 뒷부분이 숫자이면
# 주민등록번호라고 의심을 해서
# 마스킹을 하겠습니다.
result =[]
tmp=''
for line in data.split("\n"):
    word_result=[]
    for word in line.split(' '):
        if len(word)==14:
            word = word[:6] + "-*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

# solution2
import re

p = re.compile("(\d{6})[-]\d{7}")
print(p.sub("\g<1>-*******", data))

pattern = re.compile("ab")
data = "abb"
print(pattern.match(data))

#.을 이용한 매칭 : 줄바꿈을 제외한 다른 문자 하나를 의미
p = re.compile("a.b")
print(p.match("abb"))
print(p.match("ab"))
print(p.match("acb"))
print(p.match("a?b"))
print(p.match("a\nb"))

#'*' 반복 (0번 반복도 포함)
p = re.compile("a*b")
print(p.match("abb"))
print(p.match("ab"))
print(p.match("bbbbbbbbbbb"))
print(p.match("aaaaaaaaaaaab"))
print(p.match("a?b"))
print(p.match("a\nb"))

#'+' 반복 (0번 반복 포함 X)
p = re.compile("a+b")
print(p.match("abb"))
print(p.match("ab"))
print(p.match("bbbbbbbbbbb"))
print(p.match("aaaaaaaaaaaab"))
print(p.match("a?b"))
print(p.match("a\nb"))

#'{}'반복
p = re.compile("a{4}b")
print(p.match("abb"))
print(p.match("ab"))
print(p.match("aaaabbbbbbbbbbb"))
print(p.match("aaaaaaaaaaaab"))
print(p.match("a?b"))
print(p.match("a\nb"))

#?'반복 : 0 또는 1회 반복
p = re.compile("a?b")
print(p.match("bb"))
print(p.match("abb"))
print(p.match("aabb"))

#단어 패턴 인식
p = re.compile("[a-z]+")
print(p.match("aabb"))
print(p.match("hello world"))
print(p.match("Hello world"))
print(p.match("3 hello world"))

#findall
p = re.compile("[a-z]+")
print(p.findall("aabb"))
print(p.findall("hello world"))
print(p.findall("Hello world"))
print(p.findall("3 hello world"))