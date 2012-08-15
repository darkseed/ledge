ledge
=====

Simple serialized persistence for Python dictionaries. With backends for Amazon S3 and the filesystem.

Pre-alpha quality, probably not a good idea to use this yet.

```pycon
>>> my_ledge = Ledge('my_ledge', backend=S3('some-bucket', 'some-key'))
>>> my_ledge['name'] = 'my_ledge'
>>> my_ledge['age'] = 42
>>> my_ledge.sync()
>>>
>>> # ... time passes
>>>
>>> my_ledge = Ledge('my_ledge', backend=S3('some-bucket', 'some-key'))
>>> print my_ledge['name']
"my_ledge"
```
