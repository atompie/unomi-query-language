import json

from unomi_query_language.query.dispatcher import Host, Dispatcher
from unomi_query_language.query.parser import Parser
from unomi_query_language.query.grammar.grammars import read
from pprint import pprint

from unomi_query_language.query.transformers.create_rule_transformer import CreateRuleTransformer

p = Parser(read('uql_create_rule.lark'), start='create_rule')
t = p.parse(
    """
    
    # CREATE RULE 
    #     // WITH TAGS ["długa","bśćółęńć-"] 
    #     "if identify the event properties to profile" 
    #     # DESCRIBE "Copies user data from events target properties to profile"
    #     IN SCOPE "kuptoo" 
    #     WHEN event:type="identify" AND event:scope BETWEEN 1 AND 2  
    #         AND event:scope IS NULL AND event:scope = [1,2.3]
    #     THEN 
    #         CopyEventsToProfileProperties(), SetProfilePropertyFromEvent("1","lastName")
    
    # CREATE RULE 
    #     # WITH TAGS ["analytics"] 
    #     "Number of views" 
    #     DESCRIBE "Increment view property in profile with every view event"
    #     IN SCOPE "kuptoo" 
    #     WHEN event:type="click"
    #     THEN SetProfilePropertyFromEvent("nbOfViews","nbOfViews")
        
     # CREATE RULE 
     #    WITH TAGS ["analytics"] 
     #    "Number of views" 
     #    DESCRIBE "Increment view property in profile with every view event"
     #    IN SCOPE "kuptoo" 
     #    WHEN event:type="click"
     #    THEN EventToProfileProperty("nbOfViews","nbOfViews1")
        
     # CREATE RULE 
     #    # WITH TAGS ["analytics"] 
     #    "Number of views new" 
     #    DESCRIBE "NEW Increment view property in profile with every view event"
     #    IN SCOPE "kuptoo" 
     #    WHEN event:type="view"
     #    THEN IncrementProfileProperty("nbOfViews1")
        
    # CREATE RULE 
    #     "if identify event then copy event properties to profile" 
    #     DESCRIBE "Copies user data from events target properties to profile"
    #     IN SCOPE "my-site" 
    #     WHEN event:type="identify" AND event:scope = "my-site"  
    #     THEN CopyEventsToProfileProperties()
        
    CREATE RULE " points with every purchase" 
    DESCRIBE "Add points to loyalty cat with every purchase" 
    IN SCOPE "site-1" 
    WHEN  (scope="my-site1" OR scope="my-site2") AND event:type="view" 
    THEN CopyEventsToProfileProperties(), CopyEventsToProfileProperties()

        
    """
)

query = CreateRuleTransformer().transform(t)
pprint(query)

host = Host('localhost', port=8181, protocol='http').credentials('karaf','karaf')
dispatcher = Dispatcher(host)
response, _ = dispatcher.fetch(query)
if response.status_code == 200:
    pprint(json.loads(response.content))
else:
    print(response.content)
print(response.status_code)
