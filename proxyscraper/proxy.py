
class Proxy(object):

    def __init__(self, ip, port, code, anonymity):
        self._ip = ip
        self._port = port
        self._code = code
        self._anonymity = anonymity

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, ip):
        self._ip = ip

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def anonymity(self):
        return self._anonymity

    @anonymity.setter
    def anonymity(self, anonymity):
        self._anonymity = anonymity
