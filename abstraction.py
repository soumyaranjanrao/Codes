#To create a abstarction
class admin:
    def __init__(self):
        self.name = 'Soumya Ranjan Rao'
        self.id = 24
        self.__sal = 44000
        self.addr = 'Hyderabad,Ameerpet'

    def display(self):
        print('Name is:', self.name)
        print('Id is:', self.id)
        print('Address is:', self.addr)

a = admin()
a.display()
print('Salary is:', a._admin__sal)
