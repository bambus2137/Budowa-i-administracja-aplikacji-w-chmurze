from Models.task import Task

class TaskRepository:

    @staticmethod
    def get_all():
        return Task.objects.all()

    @staticmethod
    def get_by_id(task_id):
        return Task.objects.get(id=task_id)

    @staticmethod
    def create(data):
        return Task.objects.create(**data)

    @staticmethod
    def delete(task):
        task.delete()
