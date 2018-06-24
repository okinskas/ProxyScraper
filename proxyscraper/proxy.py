
class Proxy(object):

    def __init__(self, ip, port, code, country, anon):
        self._ip = ip
        self._port = port
        self._code = code
        self._country = country
        self._anon = anon

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
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country

    @property
    def anon(self):
        return self._anon

    @anon.setter
    def anon(self, anon):
        self._anon = anon

    def __str__(self):
        return str([self.ip, self.port, self.code, self.country, self.anon])
