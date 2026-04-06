class ListNode:

    def __init__(self, key:int, value:int, next: ListNode=None):
        self.value = value
        self.key = key
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.capacity = capacity 
        self.contain = 0

    def get(self, key: int) -> int:
        
        if self.head is None:
            return -1
        
        prev = None
        temp = self.head
        value = None
        for i in range(0, self.contain):
            if temp.key == key:
                value = temp.value
                break
            else:
                prev = temp
                temp = temp.next
        
        if value is not None:
            if prev is not None:
                prev.next = temp.next
                temp.next = self.head
                self.head = temp
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.head is None:
            new_node = ListNode(key=key, value=value)
            self.head = new_node
            self.contain += 1
        
        else:
            prev = None
            temp= self.head
            found = False

            for i in range(0, self.contain):
                if temp.key == key:
                    temp.value = value
                    found = True
                    break
                else:
                    prev = temp
                    temp = temp.next
            
            if found:
                if prev:
                    prev.next = temp.next
                    temp.next = self.head
                    self.head = temp
            else:
                new_node = ListNode(key=key, value=value)
                new_node.next = self.head
                self.head = new_node

                self.contain += 1
                if self.contain > self.capacity:
                    # remain least recently used 
                    prev = None
                    temp = self.head
                    for j in range(0, self.contain - 1):
                        prev = temp
                        temp = temp.next
                    
                    prev.next = None
                    self.contain -= 1
                



        
