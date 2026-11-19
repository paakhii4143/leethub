
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Calculate length and find last node
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Remove unnecessary rotations
        k = k % length

        if k == 0:
            return head

        # Make linked list circular
        tail.next = head

        # Find new tail
        steps = length - k - 1
        newTail = head

        for i in range(steps):
            newTail = newTail.next

        # Find new head and break the circle
        newHead = newTail.next
        newTail.next = None

        return newHead
