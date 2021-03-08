from app.query.parser import SelectParser
from app.query.transformer import SelectTransformer
from pprint import pprint

p = SelectParser()
t = p.parse(
    "SELECT EVENT WHERE properties.name=1 and (profile.id=\"form\" or session.id>1) -- comment"
)

print(t)
pprint(SelectTransformer().transform(t))
