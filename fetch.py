import json

from app.query.dispatcher import Dispatcher, Host
from app.query.parser import Parser
from app.query.transformer import SelectTransformer
from pprint import pprint

uql = "SELECT EVENT"

p = Parser()
t = p.parse(
    uql
)
print(uql)
query = SelectTransformer().transform(t)
print(query)
host = Host('localhost', port=9443, protocol='https').credentials('karaf','karaf')
dispatcher = Dispatcher(host)
response = dispatcher.fetch(query)
if response.status_code == 200:
    pprint(json.loads(response.content))
else:
    print(response.content)
