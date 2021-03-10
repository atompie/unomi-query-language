from unomi_query_language.query.parser import Parser
from unomi_query_language.query.grammar.grammars import select
from pprint import pprint

from unomi_query_language.query.transformers.select_transformer import SelectTransformer

p = Parser(select(), start='select')
t = p.parse(
    "select event where properties.name=\"asasas\" and id=14.3 and id between 1-2"
)

print(t)
pprint(SelectTransformer().transform(t))
