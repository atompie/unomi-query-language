from app.query.parser import SelectParser
from app.query.transformer import SelectTransformer
from pprint import pprint

p = SelectParser()
t = p.parse(
    "SELECT RULE WHERE profile.id=\"form\" -- comment"
)

print(t)
pprint(SelectTransformer().transform(t))
