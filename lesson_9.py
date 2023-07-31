# class Car:
#     def __init__(self, model, color, year):
#         self.model=model
#         self.color=color
#         self.year=year
#     def stop(self):
#         print("машина остановилась")
#     def change_color(self, new_color):
#         self.color=new_color
# gentra=Car(model='chevrolet',color='white',year=2022)
# print(gentra.color)
# gentra.change_color(input('na kakoy svet?'))
# print(gentra.color)
# gentra.stop()
# class Comment:
#     def __init__(self,username, text, likes=0):
#         self.username=username
#         self.text=text
#         self.likes=likes
#
# user1=Comment(username='Bill',text='Wery well')
# print(user1.__dict__)
# for i,j in user1.__dict__.items():
#     print(i,j)

class Bank_accaunt:
    def __init__(self, name, balanc=0):
        self.name=name
        self.balanc=balanc
    def deposit(self, add_balanc):
        self.balanc+=add_balanc
    def cash(self, cash_balanc):
        self.balanc-=cash_balanc
    def my_balnc(self):
        print(f'{user1.name}_____{user1.balanc}$')
client_name=input('ведите имя: ')
user1=Bank_accaunt(name=client_name)
while True:
    print('-------------------------','\n''1-сделат депозит','\n''2-снят со счета','\n''3-показат баланс')
    operator=int(input('что хотите делат? '))
    if operator==1:
        user1.deposit(int(input('сумма для добавления: ')))
        print('счет успешно пополнено')
    elif operator==2:
        user1.cash(int(input('сколко снят со счета: ')))
        print('денги успешно сняти')
    elif operator==3:
        user1.my_balnc()
    else:
        print('не правилний команда!')