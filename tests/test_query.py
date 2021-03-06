from hiku.query import merge, Node, Field, Link

from .base import reqs_eq_patcher


def test():
    q1 = Node([Field('a1'), Field('a2'),
              Link('b', Node([Field('b1'), Field('b2')]))])
    q2 = Node([Field('a2'), Field('a3'),
              Link('b', Node([Field('b2'), Field('b3')]))])
    query = merge([q1, q2])
    expected = Node([Field('a1'), Field('a2'), Field('a3'),
                     Link('b', Node([Field('b1'), Field('b2'), Field('b3')]))])
    with reqs_eq_patcher():
        assert query == expected
