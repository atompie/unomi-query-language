from app.query.parser import SelectParser
from app.query.transformer import SelectTransformer
from pprint import pprint

p = SelectParser()
t = p.parse(
    "SELECT EVENT WHERE profile.id=\"form\" not exists -- comment"
)

print(t)
pprint(SelectTransformer().transform(t))
