# -*- coding: utf-8 -*-

"""
"""


# ---------------------------------------------------------------------------


class repo_basic:
    def __init__(self):
        pass


class repo_new:
    def __init__(self, url, my_desc="", my_tags=[]):
        pass


class repo_disk:

    def __init__(self, author, name, url, disk_path, desc, my_desc, tags, my_tags, lang_list):
        """
            @param: author :
            @param: name   :
            @param: url    :
            @param: disk_path :
            @param: desc   :
            @param: my_desc :
            @param: tags   :
            @param: my_tags :
            @param: lang   :
        """
        self.author = author
        self.name = name
        self.url = url
        self.desc = desc
        self.disk_path = disk_path

        self.tags = tags
        self.lang_list = lang_list

    def init_wsf(self, watch, star, fork):
        self.watch = watch
        self.star = star
        self.fork = fork

    def init_lp(self, last_pull_info):
        self.last_pull_info = last_pull_info

    def init_arch(self, arch):
        self.arch = arch

    """
    self.my_cmnt
    """

    # ---------------------------------------------------------------------------
    # github functionality
    def watch(self):
        pass

    def unwatch(self):
        pass

    def clone(self, path):
        pass

    def retrive_info_wsf(self):
        """
            retrive repo info: watch, star, fork
        """
        pass

    def retrive_info_lp(self):
        pass

    # ---------------------------------------------------------------------------
    # set
    def add_tags(self, tags):
        pass

    def set_programming_lan(self, lan):
        pass

    # ---------------------------------------------------------------------------
    # get
    def check_tags(self, tags):
        pass


def repo_new_to_repo_disk(r_new):
    pass
