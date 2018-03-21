"""
Class to model an object in a category. 
Note that axiomatically, an object is an undefined term 
Therefore, we endow it with only a name
"""


class object:
    def __init__(self, name: str):
        self.name = name 

    def __str__(self):
        return self.name 

    def __repr__(self):
        return "object in a category with name" + self.name



def main():
    A = object('A')
    print(A)


if __name__=="__main__":
    main()
