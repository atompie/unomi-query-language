from app.query.parser import Parser
from app.query.rules.grammars import create, condition, select
from pprint import pprint

from app.query.transformers.condition_transformer import ConditionTransformer
from app.query.transformers.create_transformer import CreateTransformer
from app.query.transformers.select_transformer import SelectTransformer

p = Parser(create(), start='create')
t = p.parse(
    "create rule \"ala ma kota\" when properties.name=1 then properties.name=true"
)

print(t)
pprint(CreateTransformer().transform(t))
