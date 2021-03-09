import json

from app.query.parser import Parser
from app.query.rules.grammars import delete
from pprint import pprint
from app.query.transformers.delete_transformer import DeleteTransformer

p = Parser(delete(), start='delete')
t = p.parse(
    "delete scope \"kuptoo\""
)

print(t)
r = DeleteTransformer().transform(t)
pprint(r)
print(json.dumps(r[2]))
