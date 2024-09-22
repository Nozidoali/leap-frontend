from lark import Transformer, v_args
from ...modules import *
from .larkUtils import *


class EventTransformer(Transformer):

    def always_block(self, items):
        event_condition: DFGNode = items[0]
        assert isinstance(event_condition, DFGNode)
        return [x.setEvent(event_condition) for x in items[1]]

    def initial_block(self, items):
        event_condition: DFGNode = InitEvent()
        assert isinstance(event_condition, DFGNode)
        return [x.setEvent(event_condition) for x in items[0]]

    def combinational_event_expression(self, _):
        return EmptyEvent()

    def posedge_event_expression(self, items):
        return OPNode("posedge", OPType.EVENT_POSEDGE, items[0])

    def negedge_event_expression(self, items):
        return OPNode("negedge", OPType.EVENT_NEGEDGE, items[0])

    def event_or(self, items):
        return OPNode("or", OPType.EVENT_OR, items)

    def event_and(self, items):
        return OPNode("and", OPType.EVENT_AND, items)
