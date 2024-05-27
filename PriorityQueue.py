class PriorityQueue:
    def __init__(self):
        self.heap = []
 
    def insert(self, val):
        self.heap.append(val)

        i = len(self.heap) - 1
        while i > 0:
            parent_i = (i - 1) // 2
            if self.heap[i] > self.heap[parent_i]:
                self.heap[i], self.heap[parent_i] = self.heap[parent_i], self.heap[i]
                i = parent_i
            else:
                break
    
 
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        val = self.heap[0]
        self.heap[0] = self.heap.pop()
        
        i = 0
        left_child_i = i * 2 + 1

        while left_child_i < len(self.heap):
            if right_child_i < len(self.heap) and self.heap[right_child_i] > self.heap[left_child_i]:
                largest_child_i = right_child_i
            else:
                largest_child_i = left_child_i

            if self.heap[i] < self.heap[largest_child_i]:
                self.heap[i], self.heap[largest_child_i] = self.heap[largest_child_i], self.heap[i] # swap
                i = largest_child_i
            else:
                break
            left_child_i = i * 2 + 1
            right_child_i = i * 2 + 2
        return val