from app.query.parser import SelectParser
from app.query.transformer import SelectTransformer
from pprint import pprint

p = SelectParser()
t = p.parse(
    "SELECT EVENT WHERE a.a=1 and (profile.id=\"form\" or session.forfile.is>1) -- comment"
)

print(t)
pprint(SelectTransformer().transform(t))
