from celery import current_app
from django.shortcuts import render

# Create your views here.
from django.views import View

from django_docker.tasks.tasks import test_app2, create_task


class TaskView(View):
    def get(self):
        pass

    @staticmethod
    def test_task(value='wasim'):
        create_task.delay('10')
        # current_app.send_task(
        #     'task_list_2',
        #     args=(value,),
        #     queue='default'
        # )