from unomi_query_language.query.parser import Parser
from unomi_query_language.query.grammar.grammars import read
from pprint import pprint

from unomi_query_language.query.transformers.condition_transformer import ConditionTransformer

p = Parser(read('uql_expr.lark'), start='expr')
t = p.parse(
    "properties.name=\"asasas\" and id=14.3 and id between 1 and 2"
)

print(t)
pprint(ConditionTransformer().transform(t))
