from product import Product
class Stock(object):
    def __init__(self):
        self.goods = []

    def Add(self, product):
        self.goods.append(product)

    def Search(self):
        name = input('What product do you want to search for?')
        flag = False
        for i in range(len(self.goods)):
            if self.goods[i].name == name:
                flag = True
                break
        if flag == True:
            print('The product you want to search is here:')
            print('-' * 50)
            for i in range(len(self.goods)):
                if self.goods[i].name == name:
                    print('Product:' + self.goods[i].name + '     Supplier:' + self.goods[i].master)
        else:
            print('There is no such product.')

    def ListAll(self):
        if len(self.goods) == 0:
            print('There is nothing!')
        else:
            print('-' * 20 + 'The Stock List' + '-' * 20)
            for i in range(len(self.goods)):
                    print('Product:'+ self.goods[i].name + '     Supplier:' + self.goods[i].master)

    def UserAdd(self):
        name = input('please enter product:')
        master = input('please enter your name:')
        p = Product(name, master)
        self.Add(p)

    def UserDelete(self):
        print('Please enter the information of product which you want to delete.')
        name = input('please enter your product:')
        master = input('please enter your name:')
        for item in self.goods:
            if name == item.name and master == item.master:
                self.goods.remove(item)
