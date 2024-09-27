import heapq


class PriorityQueue:
    """
    Implements a priority queue data structure. Each inserted item
    has a priority associated with it and the client is usually interested
    in quick retrieval of the lowest-priority item in the queue. This
    data structure allows O(1) access to the lowest-priority item.
    """

    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        """
        Pushes an element to the queue.

        Arguments:
            item: the item to push
            priority: the priority of the item
        """
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        """
        Returns the element of the queue with the lowest priority.

        Returns: a tuple (priority, item)
        """
        (priority, _, item) = heapq.heappop(self.heap)
        return (priority, item)

    def isEmpty(self):
        """
        Returns a boolean, True is the queue is empty.
        """
        return len(self.heap) == 0

    def update(self, item, priority):
        # If item already in priority queue with higher priority,
        # update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority,
        # do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)


class PriorityQueueWithFunction(PriorityQueue):
    """
    A priority queue that computes the priority of the items automatically.

    Arguments:
        priorityFunction: the function to use to determine the priority of
            the items
    """

    def __init__(self, priorityFunction):
        self.priorityFunction = priorityFunction
        PriorityQueue.__init__(self)

    def push(self, item):
        """
        Pushes an item to the queue.

        Arguments:
            item: the item to push
        """
        PriorityQueue.push(self, item, self.priorityFunction(item))
