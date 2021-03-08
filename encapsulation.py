#encapsulation is used to restrict access to methods and variables
#This prevents data from direct modification.
# to make private attributes we use "_" or "__" as prefix.

class computer:

    def __init__(self):
        #defining the private attribute
        self.__maxprice=900

    def sell(self):
        print("selling price={}".format(self.__maxprice))

    def setMaxPrice(self,price):
        self.__maxprice=price

#instance of class computer
device=computer()
device.sell()

#updated price
device.__maxprice=1000
device.sell()
#but the price didnt change from 900 to 1000

#using setMaxPrice() function
device.setMaxPrice(1000)
device.sell()
#price change from 900 to 1000