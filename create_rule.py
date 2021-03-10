import json

from unomi_query_language.query.parser import Parser
from unomi_query_language.query.grammar.grammars import create_rule, read
from pprint import pprint

from unomi_query_language.query.transformers.create_rule_transformer import CreateRuleTransformer

p = Parser(read('uql_create_rule.lark'), start='create_rule')
t = p.parse(
    """
    
    CREATE RULE "if identify the event properties to profile" 
    // DESCRIBE "Copies user data from events target properties to profile"
    IN SCOPE "kuptoo" 
    WHEN event:type="identify" AND event:scope BETWEEN 1 AND 2 and event:scope is null and event:scope = [1,2.3]
    THEN copyEventsToProfileProperties(), setProfilePropertyFromEvent("x","lastName")
    
    """
)

print(t)
r = CreateRuleTransformer().transform(t)
pprint(r)
print(json.dumps(r[2]))

