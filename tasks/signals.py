from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from tasks.models import TodoItem, Category, Priority
from collections import Counter


@receiver(post_save, sender=TodoItem)
def task_cats_added(sender, **kwargs):
    # if action == "post_add" or action == "post_remove" or action == "post_clear" :
    for category in Category.objects.all():
        Category.objects.filter(name=category.name).update(todos_count=TodoItem.objects.filter(category=category).count())

    for priority in Priority.objects.all():
        Priority.objects.filter(prior=priority.prior).update(todos_count=TodoItem.objects.filter(priority=priority).count())
        




        # new_count = 0
        # for task in TodoItem.objects.all():
        #     new_count += task.category.filter(name=name).count()

        # Category.objects.filter(name=name).update(todos_count=new_count)


# @receiver(m2m_changed, sender=TodoItem.category.through)
# def task_cats_removed(sender, instance, action, model, **kwargs):
#     if action != "post_remove":
#         return

#     cat_counter = Counter()
#     for task in TodoItem.objects.all():
#         for cat in task.category.all():
#             cat_counter[cat.slug] += 1

#     for slug, new_count in cat_counter.items():
#         Category.objects.filter(slug=slug).update(todos_count=new_count)

