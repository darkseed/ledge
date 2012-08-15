try:
    import boto
except ImportError:
    boto = None


class File(object):

    def __init__(self, path):
        self.path = path

    def store(self, data):
        file = open(self.path, 'w')
        file.write(data)
        file.close()

    def load(self):
        try:
            file = open(self.path, 'r')
            return file.read()
        except IOError:
            return u'{}'


class S3(object):

    def __init__(self, bucket, key, *args, **kwargs):
        conn = boto.connect_s3(*args, **kwargs)
        bucket = conn.create_bucket(bucket)
        self.key = boto.s3.key.Key(bucket)
        self.key.key = key

    def store(self, data):
        self.key.set_contents_from_string(data)

    def load(self):
        try:
            return self.key.get_contents_as_string()
        except boto.exception.S3ResponseError:
            return u'{}'
