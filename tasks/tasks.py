from __future__ import absolute_import

import time

from celery import shared_task


@shared_task('task_list_1')
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True


@shared_task('task_list_2')
def test_app(a):
    print(a)
    return True


@shared_task('task_list_1')
def test_app2(a):
    print(a)
    return True
