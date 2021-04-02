from lark import Tree, Token

from .common_transformer import CommonTransformer
from .transformer_namespace import TransformerNamespace


class FunctionTransformer(TransformerNamespace):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.namespace("uql_common__", CommonTransformer())

    def function(self, args):
        return 'FUNCTION', args

    def FUNCTION_NAME(self, args):
        return 'FUNCTION_NAME', args.value

    def params(self, args):
        return 'PARAMS', args

    def param(self, args):

        if isinstance(args[0], Tree):
            values = args[0].children
            return "ARRAY", values

        elif isinstance(args[0], Token):
            value = args[0]

            type = value.type

            # remove namespace
            if '__' in type:
                type = type.split('__')[-1]

            if type == "ESCAPED_STRING":
                value = args[0].value.replace("\"", "")
            else:
                value = args[0].value
            return type, value
