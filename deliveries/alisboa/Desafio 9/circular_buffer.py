class BufferFullException(Exception):
    def __init__(self, msg):
        self.msg = msg


class BufferEmptyException(Exception):
    def __init__(self, msg):
        self.msg = msg


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.actual_index_read = 0
        self.actual_index_write = 0
        self.buffer = []
        for index in range(self.capacity):
            self.buffer.append('|||')

    def read(self):
        if all([element == '|||' for element in self.buffer]):
            raise BufferEmptyException("Buffer empty")
        value_to_return = self.buffer[self.actual_index_read]
        self.buffer[self.actual_index_read] = '|||'
        self.actual_index_read = (self.actual_index_read + 1) % self.capacity
        return value_to_return

    def __is_buffer_full(self):
        return all([element != '|||' for element in self.buffer])

    def write(self, data):
        if self.__is_buffer_full():
            raise BufferFullException("Buffer full")
        self.__force_write(data)

    def __force_write(self, data):
        self.buffer[self.actual_index_write] = data
        self.actual_index_write = (self.actual_index_write + 1) % self.capacity

    def overwrite(self, data):
        if self.__is_buffer_full():
            self.buffer[self.actual_index_read] = data
            self.actual_index_read = (self.actual_index_read + 1) % self.capacity
        else:
            self.__force_write(data)

    def clear(self):
        try:
            while 1:
                self.read()
        except BufferEmptyException:
            # All cleared
            pass
