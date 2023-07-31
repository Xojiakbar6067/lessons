#def my():
#    x=['jordan','pasha','pavel']
 #   if 'jordan' in x:
  #      print(x)
   # else:
    #    pass
#my()

#def creat_list():
 #   my=[]
  #  return my
#print(creat_list())

'''def spaw(a,b):
    print(a+b+6)
spaw(6,4)

def swap(a,b,c=8):
    return a+b*c
print(swap(2,5))'''

#def fun(a,b):
#    return sum(range(a,b))
#print(fun(1,51))

'''all_product={'sklad':{'name':'xleb','kolichestvo':34}}
def get_product(a):
    print(all_product['sklad'][a])
get_product('name')

def '''

'''def fun(b,a=1):
    chisla=range(a,b)
    chotnoe=[]
    nechotnoe=[]
    for i in chisla:
        if i %2==0:
            chotnoe.append(i)
        else:
            nechotnoe.append()'''

clients={}
free_rooms=[i for i in range(1,21)]
busy_room=[]

def add():
    name=input('imya klienta')
    room=int(input('nomer komnati'))
    clients[name]=room
    free_rooms.pop(room)
    busy_room.append(room)
    print(f'klient {name} dobavlen na komnatu {room}')