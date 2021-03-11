from unomi_query_language.query.transformers.transformer_namespace import TransformerNamespace


class CommonTransformer(TransformerNamespace):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def ESCAPED_STRING(self, args):
        return 'ESCAPED_STRING', args.value

    def NUMBER(self, args):
        return 'NUMBER', args.value