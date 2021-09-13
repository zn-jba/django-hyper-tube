def get_cleaned_data(raw_data):
    form = PromoCodeForm(raw_data)
    return form.cleaned_data if form.is_valid() else dict()
