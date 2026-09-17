class Node:
    def __intit__(self,data):
        self.data = data 
        self.next = None

if __name__ =="__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)

