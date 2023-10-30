class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DLL:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("DLL empty")
        else:
            temp=self.head
            while temp:
                print(temp.data , end=" ")
                temp=temp.next

d=DLL()
n1=Node(10)
d.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n3.prev=n2
n2.next=n3
n4=Node(40)
n4.prev=n3
n3.next=n4
n5=Node(50)
n5.prev=n4
n4.next=n5
d.display()



