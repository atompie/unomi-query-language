from unomi_query_language.query.parser import Parser
from unomi_query_language.query.grammar.grammars import read
from pprint import pprint

from unomi_query_language.query.transformers.select_transformer import SelectTransformer

p = Parser(read('uql_select.lark'), start='select')
t = p.parse(
    "SELECT FRESH EVENT WHERE properties.name=\"asasas\" AND id=14.3 AND id BETWEEN 1 AND 2"
)

print(t)
pprint(SelectTransformer().transform(t))
