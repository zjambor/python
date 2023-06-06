class QueueError(Exception):  # Choose base class for the new exception.
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Queue:
    def __init__(self):
        self.queue_list = []
        print("Your queue is ready. Use get and put methods to store or remove objects.")

    def put(self, elem):
        self.queue_list.append(elem)

    def get(self):
        if len(self.queue_list) > 0:
            elem = self.queue_list[0]
            del self.queue_list[0]
            return elem
        else:
            # print("The queue is empty.")
            raise QueueError

class SuperQueue(Queue):
    
    def __init__(self):
        super().__init__()

    def isempty(self):
        return len(self.queue_list) == 0


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
