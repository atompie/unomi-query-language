from app.query.parser import Parser
from app.query.rules.grammars import create, condition, select
from pprint import pprint

from app.query.transformers.condition_transformer import ConditionTransformer
from app.query.transformers.create_transformer import CreateTransformer
from app.query.transformers.select_transformer import SelectTransformer

p = Parser(select(), start='select')
t = p.parse(
    "select event where properties.name=\"asasas\" and id=14.3 and id between 1-2"
)

print(t)
pprint(SelectTransformer().transform(t))
