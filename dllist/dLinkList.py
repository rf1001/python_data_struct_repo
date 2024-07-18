class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DLList:
    def __init__(self, data) -> None:
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return self
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
    
    def print_reverse(self):
        temp = self.tail
        while temp is not None:
            print (temp.data)
            temp = temp.prev
    
    def get_length(self):
        return self.length
    
    def append_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return self
    def insert(self, index, data):
        new_node = Node(data)
        if index == 0 :
            append_first(self, data)
        elif index == self.length:
            append_last(self, data)
        else:
            temp = self.head
            count = 0
            while count < index:
                temp = temp.next
                count += 1
            new_node.next = temp
            new_node.prev = temp.prev
            temp.prev.next = new_node
    def delet_list(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.length:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            temp = self.head
            count = 0
            while count < index:
                temp = temp.next
                count += 1
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
        self.length -= 1
    
    
    
            
    
                        
def main():
    my_dll = DLList(10)
    my_dll.append_last(20)
    my_dll.append_last(30)
    my_dll.append_last(40)
    my_dll.print_list()
    print("Reverse the order")
    my_dll.print_reverse()
    print("after delete")
    my_dll.delet_list(2)
    my_dll.print_list()
    
    
if __name__ == "__main__":
    main()        
            
        
    