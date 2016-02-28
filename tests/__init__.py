# -*- coding: utf-8 -*-

import types


def is_instance_method(obj):
    """

    Checks if an object is a bound method on an instance.

    from http://stackoverflow.com/a/1260881

    @type  obj: object
    @param obj: the object to check if is an instance method or not

    @rtype:  bool
    @return: whether the object is an instance method or not

    """
    # not a method
    if not isinstance(obj, types.MethodType):
        return False
    # method is not bound
    if obj.im_self is None:
        return False
    # method is a classmethod
    if issubclass(obj.im_class, type) or isinstance(obj.im_class, types.ClassType):
        return False
    return True
