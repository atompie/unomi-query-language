from unomi_query_language.query.transformers.create_rule_transformer import CreateRuleTransformer
from unomi_query_language.query.transformers.create_segment_transformer import CreateSegmentTransformer
from unomi_query_language.query.transformers.delete_transformer import DeleteTransformer
from unomi_query_language.query.transformers.select_transformer import SelectTransformer
from unomi_query_language.query.transformers.transformer_namespace import TransformerNamespace


class UqlTransformer(TransformerNamespace):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.namespace('uql_select', SelectTransformer())
        self.namespace('uql_delete', DeleteTransformer())
        self.namespace('url_create_rule', CreateRuleTransformer())
        self.namespace('url_create_segment', CreateSegmentTransformer())

    def start(self, args):
        return args
