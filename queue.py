from heapq import heappush, heappop


class Queue:
    def __init__(self):
        self.beginning = 0
        self.end = 0
        self.queue = []

    def add_user(self):
        self.end += 1
        heappush(self.queue, (1, self.end))
        return self.end

    def add_vip(self):
        self.end += 1
        heappush(self.queue, (0, self.end))
        return self.end

    def remove_user(self):
        if self.beginning < self.end:
            self.beginning += 1
            removed = heappop(self.queue)
            return removed[1]
        else:
            return

