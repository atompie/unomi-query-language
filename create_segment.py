import json

from app.query.parser import Parser
from app.query.rules.grammars import create_segment, condition, select
from pprint import pprint

from app.query.transformers.condition_transformer import ConditionTransformer
from app.query.transformers.create_segment_transformer import CreateSegmentTransformer
from app.query.transformers.select_transformer import SelectTransformer

p = Parser(create_segment(), start='create_segment')
t = p.parse(
    "create segment \"At least 1 visit\" in scope \"dupa\" when profile:properties.nbOfVisits>=1"
)

print(t)
r = CreateSegmentTransformer().transform(t)
pprint(r)
print(json.dumps(r[2]))

