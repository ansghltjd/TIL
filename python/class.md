#클래스(Class)

>Contents
>
>* 클래스의 속성과 메서드
>  * 클래스의 인스턴스 생성과 사용
>  * 생성자 \__init__
>  * 예제 1:은행 계좌 클래스
>  * 예제 2: 도서관 관리 시스템
>* 예제 3: 은행 관리 시스템

##  클래스의 속성과 메서드

* 모듈
  * 클래스는 속성(변수)과 메서드(함수)를 가질 수 있습니다.

```python
class Car:
    # 속성
    color = 'red'
    speed = 0
    
    # 메서드
    def speed_up(self):
        self.speed += 10
```

## 클래스의 인스턴스 생성과 사용
* 클래스의 인스턴스를 생성하는 방법은 다음과 같습니다.
```python
my_car = Car()
```
* 이렇게 생성된 인스턴스를 통해 클래스의 속성과 메서드를 사용할 수 있습니다.

```python
print(my_car.color)  # 'red'
my_car.speed_up()
print(my_car.speed)  # 10
```

## 생성자 init

* 클래스가 인스턴스화될 때 실행되는 특별한 메서드를 생성자라고 합니다. 파이썬에서는 \__init__ 메서드가 생성자로 사용됩니다. 생성자는 클래스의 속성을 초기화하는 등의 작업을 주로 담당합니다.
```python
class Car:
    def __init__(self, color, speed=0):
        self.color = color
        self.speed = speed

    def speed_up(self):
        self.speed += 10
```
* 이렇게 정의된 클래스를 인스턴스화할 때는 다음과 같이 할 수 있습니다.
```python
my_car = Car('blue')
```