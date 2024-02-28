#클래스2(Class)   상속

>Contents 
>
>* 클래스의 상속

### 1. 필요성

* 상속은 객체지향 프로그래밍의 핵심 원칙 중 하나로, 코드의 재사용성을 높이고, 중복을 최소화하여 프로그램의 구조를 보다 효율적으로 관리할 수 있게 합니다. 상속을 통해 기존 클래스의 속성과 메소드를 물려받아 새로운 클래스를 정의할 수 있으며, 이를 통해 공통적인 기능을 가진 클래스를 베이스로 하여 확장성 있는 소프트웨어를 개발할 수 있습니다.

```python
class 부모클래스:
    def __init__(self):
        pass
        
class 자식클래스(부모클래스):
    def __init__(self):
        super().__init__()
```

>여기서 super().\__init__()는 부모 클래스의 \__init__ 메소드를 호출하는 역할을 합니다. 이를 통해 자식 클래스는 부모 클래스의 속성을 모두 물려받게 됩니다.

<br>
<br>

```python
class BlackBox:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class TravelBlackBox(BlackBox):
    #__init__ 메소드를 생략해도 부모 클래스 변수 사용가능
    #b2=TravelBlackBox('하양이',100000)
    def set_travel_mode(self,min):
        print(str(min) + "분 동안 여행모드 ON)
```

* TravelBlackBox 클래스에 변수 한개를 추가하고싶을 떄

```python
class BlackBox:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class TravelBlackBox(BlackBox):
    def __init__(self,name,price,sd):
        super().__init__(name,price)
        self.sd=sd
    def set_travel_mode(self,min):
        print(str(min) + "분 동안 여행모드 ON)
```