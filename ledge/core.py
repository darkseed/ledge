from ledge.serializers import JSON
from ledge.exceptions import ReadOnlyError

class Ledge(dict):

    def __init__(self, backend, serializer=None, readonly=True):
        self.backend = backend
        self.serializer = serializer or JSON()
        self.readonly = readonly

        raw = self.backend.load()
        deserialized = self.serializer.deserialize(raw)
        self.update(**deserialized)

    def sync(self):
        if self.readonly:
            raise ReadOnlyError('This ledge is not writable')
        raw = self.serializer.serialize(self)
        self.backend.store(raw)
