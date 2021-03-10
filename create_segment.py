import json

from unomi_query_language.query.parser import Parser
from unomi_query_language.query.grammar.grammars import create_segment, condition, select
from pprint import pprint
from unomi_query_language.query.transformers.create_segment_transformer import CreateSegmentTransformer

p = Parser(create_segment(), start='create_segment')
t = p.parse(
    "create segment \"At least 1 visit\" in scope \"dupa\" when profile:properties.nbOfVisits>=1"
)

print(t)
r = CreateSegmentTransformer().transform(t)
pprint(r)
print(json.dumps(r[2]))

