# -------------------------------
# کلاس گره (Node)
# -------------------------------
class Node:
    def __init__(self, data):
        self.Data = data
        self.next = None

# -------------------------------
# کلاس لیست پیوندی
# -------------------------------
class LinkedList:
    def __init__(self):
        self.head = None

    # درج در ابتدا
    def insert_first(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    # درج در انتها
    def insert_last(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # درج بعد از گره دارای مقدار x
    def insert_after(self, x, y):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current:
            if current.Data == x:
                new_node = Node(y)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Not found")

    # درج قبل از گره دارای مقدار x
    def insert_before(self, x, y):
        if self.head is None:
            print("List is empty")
            return
        if self.head.Data == x:  # اگر اولین گره هدف باشد
            self.insert_first(y)
            return
        prev = self.head
        current = self.head.next
        while current:
            if current.Data == x:
                new_node = Node(y)
                new_node.next = current
                prev.next = new_node
                return
            prev = current
            current = current.next
        print("Not found")

    # نمایش لیست
    def display(self):
        current = self.head
        while current:
            print(current.Data, end=" -> ")
            current = current.next
        print("None")

# -------------------------------
# نمونه استفاده
# -------------------------------
ll = LinkedList()
ll.insert_first(10)
ll.insert_last(20)
ll.insert_last(30)
ll.insert_after(20, 25)
ll.insert_before(10, 5)

print("لیست پیوندی:")
ll.display()