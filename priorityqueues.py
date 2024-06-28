import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def insert(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def delete(self):
        return heapq.heappop(self.elements)[1]

    def peek(self):
        return self.elements[0][1]

    def is_empty(self):
        return len(self.elements) == 0

# Example usage:
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert('Task 1', 3)
    pq.insert('Task 2', 1)
    pq.insert('Task 3', 2)

    while not pq.is_empty():
        print(pq.delete())
