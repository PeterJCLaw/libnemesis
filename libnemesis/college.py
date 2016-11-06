import srusers

import user

class College:
    @classmethod
    def all_college_names(cls):
        all_groups = srusers.groups.list()
        return [g for g in all_groups if College.is_valid_college_name(g)]

    @classmethod
    def is_valid_college_name(cls, string):
        return string.startswith(srusers.constants.COLLEGE_PREFIX)

    def __init__(self, group_name):
        self._group = srusers.group(group_name)
        self.group_name = group_name

    @property
    def name(self):
        return self._group.desc

    @property
    def teams(self):
        teams = set()
        for user_object in self.users:
            # Only allow teams which team-leaders or students are members
            # of to count. Blueshirts are likely to be added to many teams
            # and colleges but we don't want that to affect the teams
            # which are actually related to the colleges.
            if user_object.is_teacher or user_object.is_student:
                teams.update(user_object.teams)

        return teams

    @property
    def users(self):
        return [user.User.create_user(username=un) for un in self._group.members]

    def __eq__(self, other):
        if isinstance(other, College):
            return self.group_name == other.group_name
        elif isinstance(other, basestring):
            return self.group_name == other
        else:
            return False

    def __neq__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.group_name)

    def __unicode__(self):
        return self.group_name

    def __str__(self):
        return self.group_name
