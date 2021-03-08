import os
from lark import Lark

_local_dir = os.path.dirname(__file__)


class SelectParser:

    def __init__(self):
        with open(os.path.join(_local_dir,"rules/select.lark"), 'r') as f:
            self.base_parser = Lark(f.read(), start="select")

    def parse(self, query):
        return self.base_parser.parse(query)


class UpdateParser:

    def __init__(self):
        self.base_parser = Lark("""
            start: tags
                
            tags: [tag ("," tag)*]
            tag: FIELD OP tag_value
                | FIELD "remove"
                
            ?value: NUMBER
                | ESCAPED_STRING
                | array
                
            ?tag_value: ESCAPED_STRING
                | array

            array  : "[" [value ("," value)*] "]"
            FIELD: /\\${0,1}[#a-zA-Z0-9\\._]+/
            OP: /[+-]/

            %import common.ESCAPED_STRING
            %import common.NUMBER
            %import common.WS
            %ignore WS
        """, start="start")

    def parse(self, query):
        return self.base_parser.parse(query)



