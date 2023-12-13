from abc import ABC, abstractmethod

class ISource(ABC):
    @abstractmethod
    def read_char(self):
        """Method to read a character from the source."""
        pass

class IDestination(ABC):
    @abstractmethod
    def write_char(self, char):
        """Method to write a character to the destination."""
        pass

class Copier:
    def __init__(self, source, destination):
        if source is None or destination is None:
            raise ValueError("Source and destination cannot be None")
        self._source = source
        self._destination = destination

    def copy(self):
        """Copy characters from source to destination until newline is encountered."""
        next_char = self._source.read_char()
        while next_char != '\n':
            self._destination.write_char(next_char)
            next_char = self._source.read_char()

class StringSource(ISource):
    def __init__(self, string):
        self._string = iter(string)

    def read_char(self):
        """Read the next character or return newline if end of string."""
        return next(self._string, '\n')

class BufferDestination(IDestination):
    def __init__(self):
        self.buffer = []  # Initialize an empty buffer

    def write_char(self, char):
        """Append character to the buffer."""
        self.buffer.append(char)

    def get_content(self):
        """Return the content of the buffer as a string."""
        return ''.join(self.buffer)


