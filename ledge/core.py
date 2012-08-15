from ledge.serializers import JSON


class Ledge(dict):

    def __init__(self, backend, serializer=None):
        self.backend = backend
        self.serializer = serializer or JSON()

        raw = self.backend.load()
        deserialized = self.serializer.deserialize(raw)
        self.update(**deserialized)

    def sync(self):
        raw = self.serializer.serialize(self)
        self.backend.store(raw)
