class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        # Create 10,000 buckets.
        # Each bucket starts with a dummy ListNode.
        self.set = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        # Find which bucket this key belongs to
        cur = self.set[key % len(self.set)]

        # Go through the linked list in this bucket
        while cur.next:

            # If key already exists, don't add it again
            if cur.next.key == key:
                return

            cur = cur.next

        # Key was not found, so add it at the end
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        # Find the correct bucket
        cur = self.set[key % len(self.set)]

        # Search through the linked list
        while cur.next:

            # If the next node contains the key,
            # skip over that node to remove it
            if cur.next.key == key:
                cur.next = cur.next.next
                return

            cur = cur.next

    def contains(self, key: int) -> bool:
        # Find the correct bucket
        cur = self.set[key % len(self.set)]

        # Search through the linked list
        while cur.next:

            if cur.next.key == key:
                return True

            cur = cur.next

        return False