import json

from unomi_query_language.query.dispatcher import Dispatcher, Host
from unomi_query_language.query.parser import Parser
from pprint import pprint

from unomi_query_language.query.transformers.select_transformer import SelectTransformer

uql = "SELECT EVENT"

p = Parser()
t = p.parse(
    uql
)
print(uql)
query = SelectTransformer().transform(t)
print(query)
host = Host('localhost', port=8181, protocol='http').credentials('karaf','karaf')
dispatcher = Dispatcher(host)
response = dispatcher.fetch(query)
if response.status_code == 200:
    pprint(json.loads(response.content))
else:
    print(response.content)
