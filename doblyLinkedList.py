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
    def insert_at_begnning(self,data):
        new_node=node(data,self.head)
        self.head=new_node
        self.head.next=self.head.prev
        
    
if __name__=='__main__':
    dl=doublyLinkedList()
    dl.insert_at_begnning(10)
    dl.insert_at_begnning(20)
    dl.insert_at_begnning(30)
    dl.insert_at_begnning(300)
    dl.print_dl()
        
        
