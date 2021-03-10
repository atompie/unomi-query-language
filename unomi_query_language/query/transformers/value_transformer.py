from lark import Transformer, Token
from unomi_query_language.query.mappers.operation_mapper import operation_mapper


class ValueTransformer(Transformer):

    def __init__(self):
        super().__init__()

    def value(self, args):
        token = args[0]  # type: Token
        if isinstance(token, Token):
            return token.value
        else:
            return token

    def BOOL(self, args):
        return {
            'value': {
                'token': args,
                'type': 'bool',
                "unomi-type": 'propertyValue',
                'value': True if args.value.lower() == 'true' else False
            }
        }

    def INTEGER(self, args):
        return {
            'value': {
                'token': args,
                'type': 'number',
                "unomi-type": 'propertyValueInteger',
                'value': int(args.value)
            }
        }

    def FLOAT(self, args):
        return {
            'value': {
                'token': args,
                'type': 'number',
                "unomi-type": 'propertyValueInteger',
                'value': float(args.value)
            }
        }

    def STRING(self, args):
        string = str(args.value.strip('"'))
        string = string.replace('(', "\"")

        return {
            'value': {
                'token': args,
                'unomi-type': "propertyValue",
                'type': 'string',
                'value': string.replace(")", "\"")
            }

        }

    def array(self, args):
        values = [v for t, v in args]
        return {
            'value': {
                'token': args,
                "unomi-type": "propertyValues",
                'type': 'array',
                'value': values
            }
        }

    def range(self, args):
        values = [v['value']['value'] for v in args]
        return {
            'value': {
                'token': args,
                "unomi-type": "propertyValuesInteger",
                'type': 'range',
                'value': values
            }
        }

    def NULL(self, args):
        return {
            'value': {
                'token': args,
                "unomi-type": "propertyValue",
                'type': 'null',
                'value': None
            }
        }
