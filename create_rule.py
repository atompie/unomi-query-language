import json

from app.query.parser import Parser
from app.query.rules.grammars import create_rule
from pprint import pprint

from app.query.transformers.create_rule_transformer import CreateRuleTransformer
from app.query.transformers.select_transformer import SelectTransformer

p = Parser(create_rule(), start='create_rule')
t = p.parse(
    """
    
    CREATE RULE "if identify the event properties to profile" 
    // DESCRIBE "Copies user data from events target properties to profile"
    IN SCOPE "kuptoo" 
    WHEN event:type="identify" 
    THEN allEventToProfilePropertiesAction(param1,param2), setPropertyAction()
    
    """
)

pprint(t)
r = CreateRuleTransformer().transform(t)
pprint(r)
print(json.dumps(r[2]))

