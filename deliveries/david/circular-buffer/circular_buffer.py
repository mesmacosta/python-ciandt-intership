class BufferFullException(Exception):
    def __init__(self, msg):
        self.msg = msg

class BufferEmptyException(Exception):
    def __init__(self, msg):
        self.msg = msg

class CircularBuffer:
    def __init__(self, capacity):
        self.list_circulator = list()

        self.list_circulator.append(','.join(str(capacity)))

    def read(self):
       if self.list_circulator == None:
           return BufferEmptyException("Empty")
       else:
           for items in self.list_circulator:
               return items

    def write(self, data):
        pass


    def overwrite(self, data):
        pass

    def clear(self):
        pass
