import requests
requests.packages.urllib3.disable_warnings()


class Credentials:

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def __str__(self):
        return f"{self.user}:{self.password}"


class Host:

    def __init__(self, host, port=80, protocol='http'):
        self.protocol = protocol
        self.port = port
        self.host = host
        self._credentials = None
        self._uri = None

    def credentials(self, user, password):
        self._credentials = Credentials(user, password)
        return self

    def uri(self, uri):
        self._uri = uri
        return self

    def __str__(self):
        if self._credentials:
            url = f"{self.protocol}://{self._credentials}@{self.host}:{self.port}/"
        else:
            url = f"{self.protocol}://{self.host}:{self.port}/"

        if self._uri:
            url += self._uri

        return url


class RequestData:
    def __init__(self, uri, method, body):
        self.uri = uri
        self.method = method
        self.body = body


class Dispatcher:

    def __init__(self, host: Host):
        self._host = host

    def fetch(self, query):
        _request = RequestData(*query)
        _host = str(self._host.uri(_request.uri))

        if _request.method == "GET":
            return requests.get(_host, verify=False)
        elif _request.method == "POST":
            return requests.post(_host, json=_request.body, verify=False)
        else:
            raise ValueError("Unknown method {}".format(_request.method))
