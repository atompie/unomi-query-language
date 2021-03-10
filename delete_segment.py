import json

from unomi_query_language.query.parser import Parser
from unomi_query_language.query.grammar.grammars import delete
from pprint import pprint
from unomi_query_language.query.transformers.delete_transformer import DeleteTransformer

p = Parser(delete(), start='delete')
t = p.parse(
    "delete scope \"kuptoo\""
)

print(t)
r = DeleteTransformer().transform(t)
pprint(r)
print(json.dumps(r[2]))
