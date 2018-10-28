class LL:
    def __init__(self):
        self.value = None
        self.next = None

def intToList(num):
    s = str(num)
    head = LL()
    curr = head
    prev = None
    for char in reversed(s):
        curr.value = int(char)
        curr.next = LL()
        prev = curr
        curr = curr.next
    prev.next = None
    return head

def printList(head):
    print(head.value)
    while (head.next):
        head = head.next
        print(head.value)
    return

def addLists(L1,L2):
    sum = 0
    place = 0
    while (L1 and L2):
        sum += (L1.value + L2.value)*(10**place)
        place += 1
        L1 = L1.next
        L2 = L2.next
    L3 = (None, (L1, L2)[not bool(L1)])[bool(L1 or L2)]
    while (L3):
        sum += (L3.value) * (10**place)
        place += 1
        L3 = L3.next
    return intToList(sum)

printList(addLists(intToList(2973),intToList(12118)))