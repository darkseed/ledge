import json


class JSON(object):

    def serialize(self, obj):
        return json.dumps(obj)

    def deserialize(self, raw):
        return json.loads(raw)
