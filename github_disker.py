# -*- coding: utf-8 -*-

"""
github repo manager
"""


class repo_info:

    def __init__(self, name, url, desc, disk_path, topics=[], programming_lan=[], watch=0, star=0, fork=0):
        self.name = name
        self.url = url
        self.desc = desc
        self.disk_path = disk_path

        self.topics = topics
        self.programming_lan = programming_lan

        self.watch = watch
        self.star = star
        self.fork = fork

    def watch(self):
        pass

    def unwatch(self):
        pass

    def clone(self, path):
        pass

    def add_topics(self, topics):
        pass

    def set_programming_lan(self, lan):
        pass

disk_root = ""


def load_repo_csv():
    pass


def save_repo_csv():
    pass


def load_repo_disk():
    pass


def diff_repo_csv_disk():
    pass


def search_repo_by_topic():
    pass
