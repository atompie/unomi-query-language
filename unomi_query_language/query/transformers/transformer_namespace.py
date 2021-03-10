from lark import Transformer


class TransformerNamespace(Transformer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._namespace = None
        self._namespace_size = 0
        self.transformer = None

    def namespace(self, namespace, transformer):
        self.transformer = transformer

        if not isinstance(namespace, str):
            raise ValueError("Namespace parameter is not string")

        self._namespace = namespace
        self._namespace_size = len(namespace) if namespace else 0

    def __getattr__(self, item):
        if self._namespace and item[:self._namespace_size] == self._namespace:
            method = item[self._namespace_size:]
            method = getattr(self.transformer, method)
            if callable(method):
                return method
        raise AttributeError("Attribute {} does not exist in class {}".format(item, type(self).__name__))
