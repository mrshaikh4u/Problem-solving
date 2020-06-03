class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 4,5,1,9
def prepareList():
    node_9 = ListNode(9)

    node_1 = ListNode(1)
    node_1.next = node_9

    node_5 = ListNode(5)
    node_5.next = node_1

    node_4 = ListNode(4)
    node_4.next = node_5

    return node_4

def printList(list : ListNode):
    original_head = list
    while list:
        print(list.val,end=' ')
        list = list.next