new_priority = 100_500
Task.objects.filter(description="call mom").update(priority=new_priority)
