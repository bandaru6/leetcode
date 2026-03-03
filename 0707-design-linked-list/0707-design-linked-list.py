class Node:
    def __init__(self, val=None, prev=None, nxt=None):
        self.val = val
        self.next = nxt
        self.prev = prev
        
class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, index: int) -> int:
        curr = self.head.next
        for x in range(index):
            if curr != None:
                curr = curr.next
        return curr.val if curr else -1
    
    def iterator(self, index: int) -> int:
        curr = self.head.next
        for x in range(index):
            if curr != None:
                curr = curr.next
        return curr if curr else None
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val=val)
        newNode_next = self.head.next
        self.head.next = newNode
        newNode.next = newNode_next
        newNode.prev = self.head
        newNode_next.prev = newNode
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val=val)
        newNode_prev = self.tail.prev
        self.tail.prev = newNode
        newNode.next = self.tail
        newNode.prev = newNode_prev
        newNode_prev.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        
        curr = self.iterator(index)
        curr = curr.prev if curr != None else curr
        if curr:
            newNode = Node(val=val)
            newNode_next = curr.next
            curr.next = newNode
            newNode.next = newNode_next
            newNode.prev = curr
            newNode_next.prev = newNode

    def deleteAtIndex(self, index: int) -> None:
        
        curr = self.iterator(index)

        if curr != None and curr != self.head and curr != self.tail:
            ahead = curr.next
            behind = curr.prev
            
            behind.next = ahead
            ahead.prev = behind

            curr.next = None
            curr.prev = None
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)