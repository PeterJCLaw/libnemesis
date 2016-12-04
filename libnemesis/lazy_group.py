import srusers

import user
from ldap_manager import LDAPObjectManager

class LazyGroup(object):
    """A lazy wrapper around an LDAP group."""

    def __init__(self, group_name, ldap_manager=None):
        self._group_name = group_name
        self._ldap_manager = ldap_manager or LDAPObjectManager()
        self._cached_group = None
        self._cached_users = None

    @property
    def group_name(self):
        return self._group_name

    @property
    def _group(self):
        if self._cached_group is None:
            self._cached_group = srusers.group(self._group_name)

        return self._cached_group

    @property
    def users(self):
        if self._cached_users is None:
            self._cached_users = [
                self._ldap_manager.get(user.User, un)
                for un in self._group.members
            ]

        return self._cached_users

    def __repr__(self):
        return u"{0}({1})".format(self.__class__.__name__, self.group_name)
