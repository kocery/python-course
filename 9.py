class LRUCache:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.cache = dict()

    def put(self, key, value):
        if len(self.cache) == self.capacity:
            first = list(self.cache.keys())[0]
            self.cache.pop(first)
        self.cache[key] = value

    def get(self, key):
        if key in self.cache:
            self.put(key, self.cache[key])
            return self.cache[key]
        return None


x = LRUCache()
for i in range(1, 30):
    x.put(i, i)

x.get(4)
x.put(150, 10)

print(x.cache)
