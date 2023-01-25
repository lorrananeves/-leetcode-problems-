class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current_node_l1 = l1
        current_node_l2 = l2
        str_l1 = []
        str_l2 = []
        while current_node_l1:
            str_l1.append(str(current_node_l1.val))
            current_node_l1 = current_node_l1.next
        while current_node_l2:
            str_l2.append(str(current_node_l2.val))
            current_node_l2 = current_node_l2.next
        l1_int = int("".join(reversed(str_l1)))
        l2_int = int("".join(reversed(str_l2)))
        sum_num = l1_int + l2_int
        final_node = None
        current_node = None
        for num in reversed(str(sum_num)):
            if current_node is None:
                current_node = ListNode(int(num))
                final_node = current_node
            else:
                current_node.next = ListNode(int(num))
                current_node = current_node.next
        return final_node
            
