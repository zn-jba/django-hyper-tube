elm_street_apartments = House.objects.filter(street="Elm st.").aggregate(sum=Sum("apartments"))["sum"]
