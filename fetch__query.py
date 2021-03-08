import json

import lark

from app.query.dispatcher import Dispatcher, Host
from app.query.parser import SelectParser
from app.query.transformer import SelectTransformer
from pprint import pprint

uql = "SELECT EVENT WHERE target.type =\"session\" OFFSET 0 LIMIT 100 -- comment"


host = Host('localhost', port=9443, protocol='https').credentials('karaf','karaf')
dispatcher = Dispatcher(host)
print("connected to {}".format(host))

while True:
    uql = input('uql>')
    try:
        p = SelectParser()
        tree = p.parse(uql)

        query = SelectTransformer().transform(tree)
        uri, method, body = query
        print(f"Fetching {uql} from {method} {host}{uri}")
        response = dispatcher.fetch(query)
        if response.status_code == 200:
            pprint(json.loads(response.content))
        else:
            print(response.content)
    except lark.exceptions.UnexpectedCharacters as e:
        print(str(e))