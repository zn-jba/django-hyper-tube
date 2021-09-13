apartments_per_street = House.objects.values("street").annotate(sum=Sum("apartments"))
