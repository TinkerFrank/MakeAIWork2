#---------------------------------
class Button: #conventie classes met hoofdletter
    def __init__(self, bgColor,txt):

        self.backgroundColor = bgColor
        self.text = txt

    def click(self): #self refereert naar het object/instantie dat in het geheugen zit waar je nu mee bezig bent
        print(f'{self.text}')

#---------------------------------

btn1 = Button('red','click me')

btn2 = Button('blue','dont click')

btn2.backgroundColor= 'orange'

#---------------------------------

btn1.click()
btn2.click()

#---------------------------------

class ConfusedAdd:
    def __init__(self,a):
        self.a = a
    
    def __add__(self, U):
        return(self.a*U)
    

x = ConfusedAdd(5)

print(x+5)  # == x.__add__(5)



