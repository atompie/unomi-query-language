import os
from lark import Lark

_local_dir = os.path.dirname(__file__)


class Parser:

    def __init__(self, grammar, start, parser='earley', transformer=None):
        import_paths = [
            'unomi_query_language/query/grammar'
        ]
        self.base_parser = Lark(grammar, start=start, transformer=transformer,
                                import_paths=import_paths)

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
