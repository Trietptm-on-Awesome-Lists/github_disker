# -*- coding: utf-8 -*-

"""
github repo manager

!+ with UI, so user can easily look through these repos +!

其他的repo:
    https://github.com/git-cola/git-cola
    https://github.com/jacogr/atom-git-control
    https://github.com/kaisellgren/Git-GUI
    https://github.com/gyim/stupidgit
    https://github.com/pitaj/wengit
    https://github.com/joeferner/node-gitgui
    https://github.com/techwizrd/GitKraken

    https://github.com/demian85/git-watcher
    https://github.com/jasonim/github-guide

先说我们不做什么：

1. repo的changes、history、diff、branch等
2. 自己repo的创建等


那么，我们需要用这个东西来做什么？

1. 多种"整合"方式:
   a. 直接输入URL
   b. 比较磁盘新增加的repo
   c. 磁盘上的repo可以在多个目录中

2. repo的浏览:
   方便的浏览所有的repo，给自己"提醒"，不要忘掉好东西
   my_desc

3. repo的本地搜索:
   搜索代码，用作coding的参考
   my_tag

4. repo的github站内搜素:
   搜索tag、keyword，与本地的匹配，直接clone到本地，可以同时添加tag_my等

5. repo的外站搜索:
   从n0where.com等网站搜索


一些肯定要实现的公共功能:

1. 更新

2. 用subl、VS、Explorer、IE、Git打开

3. pin

4. 内置的文件和代码浏览器
"""

import os
import inspect

file_path = os.path.abspath(inspect.getsourcefile(lambda: 0))
file_dir = os.path.dirname(inspect.getsourcefile(lambda: 0))


# ---------------------------------------------------------------------------
# global var
v_github_username = ""
v_github_password = ""


# ---------------------------------------------------------------------------
# dat

def load_repo_basic_dat():
    """
        load basic repo info from disk

        file name: "_repo_baisc.csv", under same dir with script file.
        this file is exported by _git.xlsx, things we gathered manually.
    """
    pass


def save_repo_basic_dat():
    pass


def load_repo_dat():
    pass


def save_repo_dat():
    """
        save repo info as dat file in v_disk_root
    """
    pass


# ---------------------------------------------------------------------------
# disk
def load_repo_disk():
    """
        load repos from disk

        file name: "_repo_details.dat", under same dir with this script file
    """
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

    load_repo_disk()
    exit(1)

    from github import Github

    # First create a Github instance:
    g = Github("763090709@qq.com", "U1B3g5P9")

    # Then play with your Github objects:
    for repo in g.get_user().get_repos():
        print repo.name
