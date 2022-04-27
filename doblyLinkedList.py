class node:
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
class doublyLinkedList:
    def __init__(self):
        self.head=None
        
    def print_dl(self):
        if self.head==None:
            print("doubly linked list is empty.")
            return
        else:
            n=self.head
            while n!=None:
                print(n.data,"--->",end="")
                n=n.next
        print()
    def print_rev(self):
        if self.head==None:
            print("DOubly linked list is Empty.")
        else:
            n=self.head
            while n.next!=None:
                n=n.next
            while n!=None:
                print(n.data,"--->",end="")
                n=n.prev
                
    def insert_at_begnning(self,data):
        new_node=node(data,self.head)
        self.head=new_node
        self.head.next=self.head.prev
    def inset_at_end(self,data):
        if self.head==None:
            print("empty doubly linked list.")
            return
        n=self.head
        while(n!=None):
            n=n.next
        new_node=node(data,self.head)
        self.head.next=new_node
        new_node.prev=n
    def insert_when_empty(self,data):
        if self.head==None:
            print("Doubly Linked list is empty ,ready to insert.")
            new_node=node(data,self.head)
            self.head=new_node
        else:
            print("Doubly linked list is not Empty.")
    def insert_after_value(self,data,x):
        if self.head==None:
            print("Doubly Linked list is empty,Can't add the element.")
            return
        n=self.head
        while n!=None:
            if x==n.data:
                break
            n=n.next
        if n==None:
            print("NOde is not present.")
        else:
            new_node=node(data,self.head)
            new_node.next=n.next
            new_node.prev=n
            if n.next!=None:
                n.next.prev=new_node
            n.next=new_node
                
if __name__=='__main__':
    dl=doublyLinkedList()
    dl.insert_at_begnning(10)
    dl.insert_at_begnning(20)
    dl.insert_at_begnning(30)
    dl.insert_at_begnning(300)
    dl.insert_after_value(1,20)
    #dl.insert_when_empty(10)
    #dl.inset_at_end(1000)
    dl.print_dl()
    #dl.print_rev()
        
        
