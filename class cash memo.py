
# it is number class that has phone number of customer as a attribute
class num:
    def __init__(self,num):
        self.__num=num
    def __str__(self):
        return f'No :{self.__num} '
    def set_number(self,n):
        self.__num=n
    def get_number(self):
        return self.__num
# here we are taking number of a customer as input
number=input('Enter phone number: ')
no=num(number)


#it is a name class that has customer name as a attribute
class name:
    def __init__(self,first_name,last_name):
        #name of customer
        self.__first_name=first_name
        self.__last_name=last_name
    def set_frstName(self,f):
        self.__first_name=f
    def get_frstName(self):
        return self.__first_name
    def set_lastName(self,l):
        self.__last_name=l
    def get_lastName(self):
        return self.__last_name

    def __str__(self):
        return f'Name :{self.__first_name} {self.__last_name}'
first_name=input('Enter first name: ')
last_name=input('Enter last name: ')
n=name(first_name,last_name)


# it is a date class that involves date when a item is purchased
# it has current date,month and year as a attribute
class date:
    #date when item is bought
    def __init__(self,date,month,year):
        self.__date=date
        self.__month=month
        self.__year=year
    def set_date(self,date):
        self.__date=date
    def get_date(self):
        return  self.__date
    def set_month(self,month):
        self.__month=month
    def get_month(self):
        return   self.__month
    def set_year(self,year):
        self.year=year
    def get_year(self):
        return  self.__year

    def __str__(self):
        return f'Date: {self.__date}/{self.__month}/{self.__year}'
current_date=int(input('Enter the todays date: '))
month=int(input('Enter the month: '))
year=int(input('Enter the year: '))
d=date(current_date,month,year)


# this class contains address information
class address:
    # address of customer
    def __init__(self,street_name,house_no,city,state):
        self.__street_name=street_name
        self.__house_no=house_no
        self.__city=city
        self.__state=state

    def set_street(self,s):
        self.__street_name=s
    def get_street(self):
        return  self.__street_name
    def set_house_no(self,h):
        self.__house_no=h
    def get_house_no(self):
        return  self.__house_no
    def set_city(self,c):
        self.__city=c
    def get_city(self):
        return  self.__city
    def set_state(self,state):
        self.__state=state
    def get_state(self):
        return   self.__state
    def __str__(self):
        return f'Address: {self.__street_name}-{self.__house_no}, {self.__city}, {self.__state}'
street=input('Enter street : ')
house_no=int(input('Enter house no: '))
city_name=input('Enter city name: ')
state_name=input('Enter state name: ')
a=address(street,house_no,city_name,state_name)

# this class contains information about item being purchased
class qty:
    l=0
    j=0
    list=[]
    q_list=[]
    s=0
    total=0
    total_expense=0
    def __init__(self,item_name,quantity,price):
        self.__item_name=item_name
        qty.list.append( self.__item_name)
        self.__item_quantity=quantity
        qty.list.append(self.__item_quantity)
        # price of each item
        self.__item_price=price
        qty.list.append(self.__item_price)
        qty.total=self.__item_quantity*self.__item_price
        qty.list.append(qty.total)
        qty.q_list.append(qty.list)
        qty.list=[]
        qty.total_expense+= qty.total
    def set_itemName(self,name):
        self.__item_name=name
    def get_itemName(self,name):
        return self.__item_name
    def  set_quantity(self,q):
        self.__item_quantity=q
    def get_quantity(self):
        return self.__item_quantity
    def  set_price(self,p):
        self.__item_price=p
    def get_price(self):
        return  self.__item_price





no_of_products=int(input('Enter the number of purchases: '))
for c in range(no_of_products):
    item_name=input('write item name you : ')
    item_quantity=int(input('Enter quantity of each item: '))
    price=int(input('Enter price : '))
    x=qty(item_name,item_quantity,price)


def main():
    print(' -----------------------------------------------------------------')
    print('MOBILO')
    print()
    print('Mobile City')
    print()
    print('Deals In All Kinds Of Mobile Sets And Accessories')
    print()
    print(no)
    print()
    print(d)
    print()
    print(n)
    print()
    print(a)
    print()
    # this loop is printing headings for quantity items h
    l=0
    j=0
    s=0
    ar=['Qty','Item','Rate','Total']
    while j <len(ar):
        s=ar[j]
        while len(s)<17:
            s=s+chr(32)
        print(s,end='')
        j=j+1
    print()
    # this loop prints  item name , quantity and price of item
    # x.q_list contains all information about  item name , quantity and price of item
    s=0
    for c in x.q_list:
        for r in c:
            s=str(r)
            while len(s)<17:
                s=s+chr(32)
            print(s,end='')
        print()
# this will print total expense
    print(f'Total expense: {x.total_expense}')
main()
