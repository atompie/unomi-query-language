from lark import Token
from unomi_query_language.query.transformers.transformer_namespace import TransformerNamespace


class ValueTransformer(TransformerNamespace):

    def __init__(self):
        super().__init__()

    def op_value(self, args):
        token = args[0]  # type: Token
        if isinstance(token, Token):
            return token.value
        else:
            return token

    def OP_BOOL(self, args):
        return {
            'value': {
                'type': 'bool',
                "unomi-type": 'propertyValue',
                'value': True if args.value.lower() == 'true' else False
            }
        }

    def OP_INTEGER(self, args):
        return {
            'value': {
                'type': 'number',
                "unomi-type": 'propertyValueInteger',
                'value': int(args.value)
            }
        }

    def OP_FLOAT(self, args):
        return {
            'value': {
                'type': 'number',
                "unomi-type": 'propertyValueInteger',
                'value': float(args.value)
            }
        }

    def OP_STRING(self, args):
        string = str(args.value.strip('"'))
        string = string.replace('(', "\"")

        return {
            'value': {
                'unomi-type': "propertyValue",
                'type': 'string',
                'value': string.replace(")", "\"")
            }

        }

    def op_array(self, args):
        return {
            'value': {
                "unomi-type": "propertyValues",
                'type': 'array',
                'value': [v['value']['value'] for v in args]
            }
        }

    def op_dict(self, args):
        value = args[0] if len(args) > 0 else {}
        if len(args) > 1:
            value.update(args[1])

        return {
            'value': {
                "unomi-type": "propertyValues",
                'type': 'dict',
                'value': value
            }
        }

    def pair(self, args):
        key, value = args
        return {key['value']['value']: value['value']['value']}

    def op_range(self, args):
        values = [v['value']['value'] for v in args]
        return {
            'value': {
                "unomi-type": "propertyValuesInteger",
                'type': 'range',
                'value': values
            }
        }

    def OP_NULL(self, args):
        return {
            'value': {
                "unomi-type": "propertyValue",
                'type': 'null',
                'value': None
            }
        }
