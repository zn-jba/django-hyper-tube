elm_street_houses = House.objects.filter(street__contains="Elm st.").order_by("house_number")
