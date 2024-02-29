# TDD 및 유닛 테스팅

### 1. 필요성

- TDD (Test-Driven Development)는 소프트웨어 개발 프로세스에서 테스트 케이스를 먼저 작성하고, 이 테스트를 통과하는 코드를 개발하는 방식입니다. 이 접근 방식은 코드의 신뢰성을 높이고, 오류를 줄이며, 유지보수를 용이하게 합니다.
- **유닛 테스팅**은 소프트웨어의 가장 작은 단위인 '유닛'을 독립적으로 검증하는 테스트입니다. 이를 통해 각 기능의 정확성을 보장하고, 리팩토링 시 기존 기능이 올바르게 작동하는지 확인할 수 있습니다.

>파이썬의 unittest 모듈을 사용한 유닛 테스트의 예제

* 간단한 수학 함수 테스트:

```python
import unittest

def add(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
```

* 문자열 반전 함수 테스트:
```python
def reverse_string(s):
    return s[::-1]

class TestStringFunctions(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
```

* 사용자 정의 클래스 메서드 테스트:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18

class TestPersonClass(unittest.TestCase):
    def test_is_adult(self):
        adult = Person("John", 20)
        self.assertTrue(adult.is_adult())
```