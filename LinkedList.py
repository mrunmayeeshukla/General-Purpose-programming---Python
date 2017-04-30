class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next= None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data=newdata

    def setNext(self,newnext):
        self.next=newnext


class LinkedList:
    def __init__(self):
        self.head=None

    def isEmpty(self):
        return self.head==None

    def add(self,item):
        temp= Node(item)
        temp.setNext(self.head)
        self.head= temp

    def size(self):
        current = self.head
        count=0
        while current!= None:
            count+=1
            current=current.getNext()
        return count

    def search(self,e):
        current=self.head
        count=0
        while current != None:
            count+=1
            if current.getData()==e:
                return count
            else:
                current= current.getNext()

    def remove(self, e):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == e:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def display(self):
        current = self.head
        while current != None:
            print(current.getData())
            current=current.getNext()


def main():
    l= LinkedList()
    l.add(3)
    l.add(5)
    l.add(8)
    l.add(23)

    l.display()
    l.remove(5)
    l.display()
    print(l.search(23))

main()


