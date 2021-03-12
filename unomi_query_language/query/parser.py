import os
from lark import Lark

_local_dir = os.path.dirname(__file__)


class Parser:

    def __init__(self, grammar, start, parser='earley', transformer=None):
        import_paths = [
            os.path.join(_local_dir, '../../unomi_query_language/query/grammar')
        ]
        self.base_parser = Lark(grammar,
                                start=start,
                                transformer=transformer,
                                import_paths=import_paths)

    def parse(self, query):
        return self.base_parser.parse(query)
