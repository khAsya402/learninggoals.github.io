class Node:
    """ 
    Node object includes 
    data(int)
    next_id(id())
    """
    def __init__(self, data = None, next_id = None):
        self.data = data
        self.next_id = next_id


class LinkedList:

    def __init__(self, *args):
        self.len_args = len(args)
        self.nodes = args

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self): 
        if self.n < self.len_args:
            self.node = self.nodes[self.n]
            self.next_id = id(self.node.data)
            self.node = Node(self.node.data, self.next_id)
            self.n += 1
            if self.n == self.len_args:
                self.node.next_id = None
            return self.node
        else:
            raise StopIteration

    def add(self, x):                                   
        if x.data is not None:
            last_node = self.nodes[-1]
            last_node.next_id = id(last_node.data)
            new_node = Node(x.data, None)
            self.node = new_node
            self.len_args += 1 
            self.nodes += (self.node,)
            self.__next__()
            return self

    def get(self):                                            # TO DO
        pass

    def size(self):
        count = 0
        for i in self.__iter__():
            count += 1                                 
        return count

    def remove(self, node = Node()): 
        nodes = []
        for j in self.__iter__():
            if j.data == node.data:
                continue
            else:
                nodes.append(j)
        self.nodes = tuple(nodes)
        self.nodes[-1].next_id = None
        self.len_args = len(nodes)
        return self

node1 = Node(5)
node2 = Node(2)
node3 = Node(4)

l = LinkedList(node1, node2, node3)
L = iter(l)

l = l.add(Node(1))
for i in L:
    print((i.data,i.next_id))

print(l.size())

l = l.remove(Node(2))

for i in iter(l):
    print((i.data,i.next_id))
