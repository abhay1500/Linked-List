class node: #ye sirf ek node banata hai
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class linkedlist: #ye nodes ko connect krta hai
    def __init__(self):
        self.head=None
        
    def print_ll(self):
        if self.head==None:
            print("empty linked list")
            return
        else:
            n=self.head
            while n!=None:
                print(n.data,"--->",end="")
                n=n.next
    def insert_at_begnning(self,data):
        new_node=node(data,self.head)
        #new_node.next=self.head
        self.head=new_node
    def insert_at_end(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node
        else:
            n=self.head
            while n.next!=None:
                n=n.next
            n.next=new_node
    def after_node(self,data,x):
        n=self.head
        while n!=None:
            if x==n.data:
                break
            n=n.next
        if n==None:
            print("Node is not present in linked list.")
        else:
            new_node=node(data)
            new_node.next=n.next
            n.next=new_node
    def before_node(self,data,x):
        if self.head==None:
            print("liked list is empty.")
            return
        if self.head.data==x:
            new_node=node(data)
            new_node.next=self.head
            self.head=new_node
            return
        n=self.head
        while n.next!=None:
            if n.next.data==x:
                break
            n=n.next
        if n.next==None:
            print("linked list is not found.")
        else:
            new_node=node(data)
            new_node.next=n.next
            n.next=new_node
    def empty(self,data):
        if self.head!=None:
            print("linked list is not empty.")
            return 
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    def del_begining(self):
        if self.head==None:
            print("linked list is empty,can't delete it.")
        else:
            z=self.head.data
            self.head=self.head.next  
            print("The first delete data is:",z)
    def del_end(self):
        if self.head is None:
            print("Linked list is empty,can't delete it.")
        elif self.head.next==None:
            self.head=None
        else:
            n=self.head
            while n.next.next!=None:
                n=n.next
            z=n.next.data
            n.next=None
            print("The last deleted data is:",z)
     def del_by_value(self,x):
        if self.head==None:
            print("can't delete the element ,linked list is empty.")
            return
        if x==self.head.data:
            self.head=self.head.next
            return
        n=self.head
        while(n.next!=None):
            if x==n.next.data:
                break
            n=n.next
        if n.next==None:
            print("note is not present.")
        else:
            n.next=n.next.next
        print("The delted node is:",x)
              

          
if __name__=='__main__':
    ll=linkedlist() 
    ll.insert_at_begnning(10)
    #ll.empty(10)
    #ll.insert_at_end(50)
    """ll.insert_at_begnning(20)
    ll.insert_at_begnning(30)
    ll.insert_at_begnning(40)
    ll.del_begining()"""
    #ll.del_by_value(20)
    ll.del_end()
    #ll.before_node(1,200)
    ll.print_ll()
