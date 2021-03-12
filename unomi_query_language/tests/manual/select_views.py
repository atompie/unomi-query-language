import json

from unomi_query_language.query.dispatcher import Host, Dispatcher
from unomi_query_language.query.parser import Parser
from unomi_query_language.query.grammar.grammars import read
from pprint import pprint

from unomi_query_language.query.transformers.select_transformer import SelectTransformer

p = Parser(read('uql_select.lark'), start='select')
t = p.parse(
    """
    SELECT EVENT OFFSET 10 LIMIT 100 
    """
)

query = SelectTransformer().transform(t)
print(query)
host = Host('localhost', port=8181, protocol='http').credentials('karaf','karaf')
dispatcher = Dispatcher(host)
response, exp_code = dispatcher.fetch(query)
if response.status_code == exp_code:
    pprint(json.loads(response.content))
else:
    print(response.content)
