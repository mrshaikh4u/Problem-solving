from Utils import LinkedListUtils
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next

obj = Solution()
input_list =LinkedListUtils.prepareList()
temp = input_list
print('before list : ')
LinkedListUtils.printList(temp)
while temp.val != 5:
    temp=temp.next

obj.deleteNode(temp)
# print(temp.val)
print('after list : ')
LinkedListUtils.printList(input_list)
