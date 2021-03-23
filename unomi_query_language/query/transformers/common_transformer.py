from unomi_query_language.query.transformers.transformer_namespace import TransformerNamespace


class CommonTransformer(TransformerNamespace):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def ESCAPED_STRING(self, args):
        return 'ESCAPED_STRING', args.value

    def NUMBER(self, args):
        return 'NUMBER', args.value

    def value(self, args):

        type = args[0].type

        # remove namespace
        if '__' in type:
            type = type.split('__')[-1]

        if type == "ESCAPED_STRING":
            value = args[0].value.replace("\"", "")
        else:
            value = args[0].value
        return type, value

    def array(self, args):
        return 'ARRAY', args