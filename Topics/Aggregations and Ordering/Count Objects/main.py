wall_street_houses_number = House.objects.filter(street__contains="Wall st.").count()
