from hiku.query import Node, Field, Link
from hiku.builder import build, Q

from .base import reqs_eq_patcher


def test():
    query = build([
        Q.tyan,
        Q.turlock[
            Q.gange
        ],
        Q.tiber(ramsons='defaces')[
            Q.decifer(botches='auxerre'),
            Q.exocet(brogues='hygiea'),
        ],
    ])
    with reqs_eq_patcher():
        assert query == Node([
            Field('tyan'),
            Link('turlock', Node([Field('gange')])),
            Link('tiber', Node([
                Field('decifer', options={'botches': 'auxerre'}),
                Field('exocet', options={'brogues': 'hygiea'}),
            ]), {'ramsons': 'defaces'}),
        ])
