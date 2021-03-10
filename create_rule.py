import json

from unomi_query_language.query.parser import Parser
from unomi_query_language.query.grammar.grammars import create_rule
from pprint import pprint

from unomi_query_language.query.transformers.create_rule_transformer import CreateRuleTransformer

p = Parser(create_rule(), start='create_rule')
t = p.parse(
    """
    
    CREATE RULE "if identify the event properties to profile" 
    // DESCRIBE "Copies user data from events target properties to profile"
    IN SCOPE "kuptoo" 
    WHEN event:type="identify" 
    THEN copyEventsToProfileProperties(), setProfilePropertyFromEvent("x","lastName")
    
    """
)

pprint(t)
r = CreateRuleTransformer().transform(t)
pprint(r)
print(json.dumps(r[2]))

