from django.core import serializers


def dump_json(object):
    if object is None:
        return {}
    elif type(object) == type([]):
        object = serializers.serialize('json', object)
    else:
        object = serializers.serialize('json', [object])
    return object[1:-1]
