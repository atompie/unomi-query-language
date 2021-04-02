from lark import Tree

from query.statement_templates.sort_stmt_templates import sort_stmt
from query.transformers.sort_transformer import SortTransformer
from unomi_query_language.query.statement_templates.query_stmt_templates import create_condition_stmt, select_stmt
from unomi_query_language.query.mappers.uri_mapper import uri_mapper
from unomi_query_language.query.transformers.condition_transformer import ConditionTransformer
from unomi_query_language.query.transformers.meta_transformer import MetaTransformer
from unomi_query_language.query.transformers.transformer_namespace import TransformerNamespace


class SelectTransformer(TransformerNamespace):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.namespace('uql_expr__', ConditionTransformer())
        self.namespace('uql_sort__', SortTransformer())

    def _to_tuple(self, args):
        for data in args:
            if isinstance(data, Tree):
                yield data.data, data.children
            else:
                yield data

    def select(self, args):
        elements = {k: v for k, v in self._to_tuple(args)}

        query_data_type = elements['DATA_TYPE'] if 'DATA_TYPE' in elements else None

        key = ('select', query_data_type)
        if key in uri_mapper:
            uri, method, status = uri_mapper[key]
        else:
            raise ValueError("Unknown {} {} syntax.".format(key[0], key[1]))

        where = elements['WHERE'] if 'WHERE' in elements else None
        condition = create_condition_stmt(where, query_data_type)

        sort = elements['sort'] if 'sort' in elements else None
        sort = sort_stmt(sort, query_data_type)

        query = select_stmt(elements, condition, sort)

        return query_data_type, uri, method, query, status

    def where(self, args):
        return 'WHERE', args[0]

    def data_type(self, args):
        return 'DATA_TYPE', args[0].value.lower()

    def FRESH(self, args):
        return 'FRESH', args.value.lower()

    def limit(self, args):
        return 'LIMIT', int(args[0].value)

    def offset(self, args):
        return 'OFFSET', int(args[0].value)
