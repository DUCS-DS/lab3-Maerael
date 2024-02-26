from llist import LList, Node, append

def length(lst):
    """return the length of a finite linked list"""
    count = 0
    node = lst.head
    while node:
        count += 1
        node = node.next
    return count

def llprint(lst):
    """print a finite linked list"""
    node = lst.head
    while node:
        print(node.val, end="")
        node = node.next
    print()

if __name__ == "__main__":
    linkList = LList()
    values = [1, 2, 4, 8, 12, 32, 64, 128, 256, 512]

    for value in values:
        append(linkList, Node(value))

    #prints the list
    llprint(linkList)

    #prints the length of the list
    print(length(linkList), "is the length of the linked list")

    #prints the length of lst from genfinite.py
    from genfinite import lst
    print(length(lst))