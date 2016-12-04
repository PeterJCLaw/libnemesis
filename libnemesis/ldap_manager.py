
class LDAPObjectManager(object):
    def __init__(self):
        self._cache = {}

    def get(self, cls, name):
        class_cache = self._cache.setdefault(cls, {})

        try:
            inst = class_cache[name]
        except KeyError:
            class_cache[name] = inst = cls(name, ldap_manager=self)

        return inst

    def has_cached(self, cls, name):
        try:
            self._cache[cls][name]
            return True
        except KeyError:
            return False

    def preload(self, cls, name):
        self.get(cls, name)
