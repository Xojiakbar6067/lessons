import requests as req
#b=lambda x,y: x**2+y**4
#print(b(int(input('x= ')),int(input('y= '))))

#link='https://icanhazip.com/'
#print(req.get(link).text)

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'}

link='https://httpbin.org/post'

date={ "comments": "helloooo",
    "custemail": "alish@mail.ru",
    "custname": "alish",
    "custtel": "+998989898989",
    "delivery": "20:15",
    "size": "large",
    "topping": "cheese"}

print(req.post(url=link, headers=header).text)