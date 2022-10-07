from stock import Stock

s = Stock()
print('-' * 20 + 'The Menu' + '-' * 20)
print('1.Add your product\n2.Delete product\n3.Search for one product\n4.List all the product in stock\n5.Exit')
while True:
    try:
        info = eval(input('Please select the service you would like：'))
        if info == 1:
            s.UserAdd()
        elif info == 2:
            s.UserDelete()
        elif info == 3:
            s.Search()
        elif info == 4:
            s.ListAll()
        elif info == 5:
            print('Thanks for using!')
            break
        else:
            print("Error for input!")
    except NameError:
        print("Error for input!")
