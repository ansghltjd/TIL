#클래스(Class)   

>Contents 
>
>* 클래스의 속성과 메서드
>  * 클래스의 인스턴스 생성과 사용
>  * 생성자 \__init__
>  * 예제 1:은행 계좌 클래스
>  * 예제 2: 도서관 관리 시스템
>* 예제 3: 학생 관리 시스템

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
<hr>

## 예제 1:은행 예제

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}가 입금되었습니다.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount}가 출금되었습니다.")
        else:
            print("잔액이 부족합니다.")

account = BankAccount("Alice") 
account.deposit(1000) -> "1000가 입금되었습니다"
account.withdraw(500) -> "500가 출금되었습니다"
```

## 예제 2: 도서관 관리 시스템

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book)

lib = Library()
lib.add_book(Book("Python Programming", "John Doe"))
lib.show_books() ->"'Python Programming' by John Doe"
```

## 예제 3: 학생 관리 시스템

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = sum([student.get_grade() for student in self.students])
        return value / len(self.students)

math = Course("Math", 2)
s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)

math.add_student(s1)
math.add_student(s2)

print(math.get_average_grade()) -> "85.0"
```