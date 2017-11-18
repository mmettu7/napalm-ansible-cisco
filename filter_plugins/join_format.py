from jinja2 import Environment, FileSystemLoader
from ansible import errors
from itertools import groupby, count

def join_format(*args):
    clustered = [list(v) for _,v in groupby(sorted(*args), lambda n, c=count(): n-next(c))]
    out = ",".join(["{0}-{1}".format(k[0], k[-1]) if len(k) > 1 else "{0}".format(k[0]) for k in clustered])
    return out

class FilterModule(object):
    def filters(self):
        return {
            'join_format': join_format
        }
