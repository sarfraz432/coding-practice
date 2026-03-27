# I will attempt LRU cache using a doubly linked list and a hash map

class Node:
    def __init__(self, key=0, value=0) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}
        
        # Dummy nodes to avoid null checks
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1

        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if node:
            node.value = value
            self._move_to_head(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)

            if len(self.cache) > self.capacity:
                lru = self._pop_tail()
                del self.cache[lru.key]

    def _remove_node(self, node: Node) -> None:
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

        node.prev = node.next = None


    def _add_node(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _move_to_head(self, node: Node) -> None:
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> Node:
        lru = self.tail.prev
        self._remove_node(lru)
        return lru

lru = LRUCache(2)

lru.put(1, 10)
lru.put(2, 20)
value = lru.get(1)     # returns 10
print(value)
lru.put(3, 30) # evicts key 2
print(lru.get(2))     # returns -1