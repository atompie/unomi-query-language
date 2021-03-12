# Unomi Query Language

Unomi Query Language(UQL) is a library for managing Apache Unomi with easy to use query language. It connects to unomi API and performs actions described in UQL.

Currently it has implemented the following query types:

* SELECT
* CREATE
* DELETE

## SELECT query statement

Optional parts of the statement are in square brackets []. Multiple choice but required statement parts are in round brackets ().

```
    SELECT 
    [FRESH] 
    (EVENT | RULE | SEGMENT | PROFILE)
        [WHERE where condition]
        [OFFSET integer]
        [LIMIT integer]
```

# SELECT statement examples

With select query you can search the following data types:

* EVENT
* PROFILE
* RULE
* SEGMENT

The simplest example of SELECT query looks like this:

```
    SELECT PROFILE
```

It finds all profiles in the Unomi storage. 

```
    SELECT PROFILE OFFSET 100 LIMIT 20
```

limits the results to 20 records and skips first 100 records

```
    SELECT EVENT WHERE type=”view”
```

finds events with eventType equal to view. 

```
    SELECT EVENT 
        WHERE type=”view” 
            AND (scope=”my-site-1” OR scope=”my-site-2”) 
            AND properties.target.pageInfo=”page-info’
```

finds view events that are in scope “my-site-1” OR  “my-site-2”  and target has property pageInfo that equals “page -info”.  You can limit or offset results with LIMIT and OFFSET as in the above example.


## WHERE|WHEN condition statement

The following grammar rules define expression syntax in UQL.
```
expr:
  | expr OR (expr AND expr)
  | expr AND (expr OR expr)
```

that means that expressions with similar operations e.g. OR must be in brackets.
The following where statement is forbidden:

```
field1=1 AND field2=2 OR field3=3
```
correct statement is either:
```
field1=1 AND (field2=2 OR field3=3)
```
or 
```
(field1=1 AND field2=2) OR field3=3
```
There is no auto resolution of priority operations

###Available operations mappings

Unomi operator maps to UQL where condition statement in the following way 

    * exists -> field EXISTS
    * between -> BETWEEN number AND number
    * equals -> filed EQUALS
    * notEquals -> field != string|number
    * greaterThanOrEqualTo -> field >= number
    * lessThanOrEqualTo -> field <= number
    * greaterThan -> field > number
    * lessThan -> field < number
    * missing -> field NOT EXISTS
    * contains -> CONTAINS

# CREATE statement

Create statements can be used to create rules and segments.
```
    CREATE (RULE|SEGMENT)
        [READONLY]
        [DISABLED]
        [HIDDEN]
    [WITH TAGS [tag1, tag2, ...]]
    "rule or segment name"
    [DESCRIBE "rule or segment description"]
    IN SCOPE "scope"
    WHEN where condition
    [THEN prefindedAction(), …]
```

When using CREATE SEGMENT statement there is no THEN part of statement.

Example of CREATE STATEMENT
```
    CREATE SEGMENT
        WITH TAGS ["important"]
        "At least 1 visit"
        DESCRIBE "First time visitor"
        IN SCOPE \"site-1\"
        WHEN profile:properties.nbOfVisits>=1
```

Example of CREATE RULE

```
    CREATE RULE 
        "if identify event then copy event properties to profile" 
        DESCRIBE "Copies user data from events target properties to profile"
        IN SCOPE "my-site" 
        WHEN event:type="identify" AND event:scope = "my-site"  
        THEN CopyEventsToProfileProperties()
```

# DELETE statement
```
DELETE 
(RULE|SEGMENT|PROFILE) 
“rule or segment or profile id”
```
Example of delete rule statement:
```
DELETE RULE “my-rule-id” 
```

# Python usage example

```python
import json

from unomi_query_language.query.dispatcher import Host, Dispatcher
from unomi_query_language.query.parser import Parser
from unomi_query_language.query.grammar.grammars import read
from pprint import pprint

from unomi_query_language.query.transformers.select_transformer import SelectTransformer

// Parse select statement 

p = Parser(read('uql_select.lark'), start='select')
t = p.parse(
    """
    SELECT EVENT WHERE type="click"
    """
)

query = SelectTransformer().transform(t)

// Connect to unomi

host = Host('localhost', port=8181, protocol='http').credentials('karaf','karaf')
dispatcher = Dispatcher(host)
response = dispatcher.fetch(query)

// Read response

if response.status_code == 200:
    pprint(json.loads(response.content))
else:
    print(response.content)
```