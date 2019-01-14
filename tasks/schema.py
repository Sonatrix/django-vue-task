import graphene
from graphene_django.types import DjangoObjectType
from graphql_relay.node.node import from_global_id
from tasks.models import Task

class TaskType(DjangoObjectType):
	class Meta:
		model = Task

class CreateTask(graphene.Mutation):
	ok = graphene.Boolean()
	task = graphene.Field(lambda: TaskType)

	class Arguments:
		name = graphene.String()
		description = graphene.String()

	def mutate(self, info, name, description):
		task = Task(name=name, description=description, completed=False)
		task.save()

		ok = True

		return CreateTask(task, ok=ok)

class UpdateTask(graphene.Mutation):
    task = graphene.Field(lambda: TaskType)
    ok =  graphene.Boolean()

    class Arguments:
        id = graphene.String()
        completed = graphene.Boolean()
    
    def mutate(self, info, id, completed):
        task = Task.objects.get(pk=id)
        task.completed = completed
        task.save()
        ok = True
        return UpdateTask(task=task,ok=ok)


class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType)

    def resolve_tasks(self, info):
        return Task.objects.all()


class Mutations(graphene.ObjectType):
    create_task = CreateTask.Field()
    update_task = UpdateTask.Field()
    