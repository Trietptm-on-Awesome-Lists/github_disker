# -*- coding: utf-8 -*-

"""
github repo manager

!+ with UI, so user can easily look through these repos +!
"""

# ---------------------------------------------------------------------------
# global var
v_disk_root = ""
v_github_username = ""
v_github_password = ""


# ---------------------------------------------------------------------------
# repo_info
class repo_info:

    def __init__(self, name, url, desc, disk_path, topics=[], programming_lan=[]):
        self.name = name
        self.url = url
        self.desc = desc
        self.disk_path = disk_path

        self.topics = topics
        self.programming_lan = programming_lan

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
    def add_topics(self, topics):
        pass

    def set_programming_lan(self, lan):
        pass

    # ---------------------------------------------------------------------------
    # get
    def check_topics(self, topics):
        pass


# ---------------------------------------------------------------------------
# csv
def load_repo_csv():
    pass


def save_repo_csv():
    """
        save repo info as csv file in v_disk_root
    """
    pass


# ---------------------------------------------------------------------------
# disk
def load_repo_disk():
    pass

# ---------------------------------------------------------------------------
# search


def search_repo_by_topic():
    pass

# ---------------------------------------------------------------------------
# main

#
# supposed usages:
#   1. update repos(might by some filter)
#      check latest pull
#      check disk has repo
#   2. search repos
#   3. update disk
#


def diff_repo_csv_disk():
    pass


if __name__ == "__main__":
    pass
