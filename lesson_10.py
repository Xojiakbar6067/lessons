# class Father:
#     def __init__(self, name, profession):
#         self.name=name
#         self.profession=profession
#     def work(self):
#         print('umeliy injiner')
# class Child(Father):
#     def sing(self):
#         print('horoshiy pevets')
# ditya=Child.work()
# ditya=Child.sing()

# class Car:
#     def __init__(self, model, color, year):
#         self.model=model
#         self.color=color
#         self.year=year
# class SuperCar(Car):
#     def __init__(self, model, color, year, sponsor):
#         super().__init__(model, color, year)
#         self.sponsor=sponsor
#
# impala=Car(model='chevrolet', color='red', year=2020)
# amg_one=SuperCar(model='mersedes-benz', color='grey', year=2022, sponsor='petronas')
#
# print(impala.model, amg_one.sponsor)

# class Animal:
#     def make_sound(self, s):
#         print(s)
# class Horse(Animal):
#     def dibi(self):
#         print('встат на дыбы')
# class Pony(Animal, Horse):
#     pass
# pony1=Pony()
# pony1.make_sound('igogo')
# pony1.dibi()

# class Animal:
#     @classmethod
#     def make_sound(cls, s):
#         print(s)
# Animal.make_sound('igogo')


# class Myclass:
#     def __init__(self, value):
#         self.value=value
#
#     @classmethod
#     def from_string(cls, string):
#         return cls(int(string))
#
# my_obj=Myclass.from_string('10')
# print(my_obj.value)

# class Rectangle:
#     def __init__(self, width, height):
#         self.width=width
#         self.height=height
#
#     @property
#     def area(self):
#         return self.width*self.height
#
# rectangle=Rectangle(4, 5)
# print(rectangle.area)
#
# rectangle.width=6
# print(rectangle.area)
#
# rectangle.height=8
# print(rectangle.area)
#
# rectangle.width=10
# print(rectangle.area)

# class Worker:
#     def __init__(self, name, position):
#         self.name=name
#         self.position=position
#     def work(self):
#         print('rabotaet')
# class HR(Worker):
#     def __init__(self, name, position):
#         super().__init__(name, position)
#
#     def show_info(self, name):
#         return name.position
#
# jordan=Worker('jordan', 'junior')


class Player:
    def __init__(self, speed, power, accuracy, stamina):
        self.speed=speed
        self.power=power
        self.accuracy=accuracy
        self.stamina=stamina

class Atacker(Player):
    def __init__(self, speed, power, accuracy, stamina):
        super().__init__(speed, power, accuracy, stamina)
    def atack(self):
        print('хороший нападаюший')
class Defender(Player):
    def __init__(self, speed, power, accuracy, stamina):
        super().__init__(speed, power, accuracy, stamina)
    def defed(self):
        print('хороший зашитник')
class Goalkeeper(Player):
    def __init__(self, speed, power, accuracy, stamina):
        super().__init__(speed, power, accuracy, stamina)
    def goalkeep(self):
        print('зашишает ворота')
class Half_defender(Player):
    def __init__(self, speed, power, accuracy, stamina):
        super().__init__(speed, power, accuracy, stamina)
    def middle(self):
        print('подоет мяч атакуюшему')

player1=Atacker('hight', 'hight', 'midle', 'low')
print(player1.power)