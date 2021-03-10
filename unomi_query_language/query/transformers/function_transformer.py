from unomi_query_language.query.transformers.transformer_namespace import TransformerNamespace


class FunctionTransformer(TransformerNamespace):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def function(self, args):
        return 'FUNCTION', args

    def FUNCTION_NAME(self, args):
        return 'FUNCTION_NAME', args.value

    def params(self, args):
        return 'PARAMS', args

    def param(self, args):
        type = args[0].type
        if type == "ESCAPED_STRING":
            value = args[0].value.replace("\"", "")
        else:
            value = args[0].value
        return type, value
