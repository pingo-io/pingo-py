import sys

PY2 = sys.version_info[0] == 2
PY3 = (sys.version_info[0] >= 3)

def iteritems(obj, **kwargs):
    """replacement for six's iteritems for Python2/3 compat
       uses 'iteritems' if available and otherwise uses 'items'.
       Passes kwargs to method.
    """
    func = getattr(obj, "iteritems", None)
    if not func:
        func = obj.items
    return func(**kwargs)

def iterkeys(obj, **kwargs):
    func = getattr(obj, "iterkeys", None)
    if not func:
        func = obj.keys
    return func(**kwargs)

if PY2:
    from UserDict import UserDict
else:
    from collections import UserDict
