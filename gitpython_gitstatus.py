#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import git

tracking_name = ''
repo = git.Repo(search_parent_directories=True)
if repo.head.is_detached:
    hexsha, branch = repo.head.object.name_rev.split(' ')
    if branch[len('tags/'):] in repo.tags:
        status_name = branch
    else:
        status_name = hexsha[:7]
else:
    hexsha = repo.head.object.hexsha
    branch = repo.active_branch.name
    tracking = repo.active_branch.tracking_branch()
    if tracking:
        tracking_name = tracking.name
    status_name = branch

untracking_files = len(repo.untracked_files)
modified_files = len(repo.index.diff(None))
conflict_files = len(repo.index.unmerged_blobs())
staged_files = len(repo.index.diff('HEAD'))

print('status_name:', status_name)
print('tracking_name:', tracking_name)
print('untracking_files:', untracking_files)
print('modified_files:', modified_files)
print('staged_files:', staged_files)
