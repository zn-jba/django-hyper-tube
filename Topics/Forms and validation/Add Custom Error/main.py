def add_custom_errors(code_form):
    code_data = code_form.data.get('code')
    if code_data:
        if not code_data.startswith(f"{current_year}"):
            code_form.add_error("code", "promo code is expired")
        if not code_data.endswith("django"):
            code_form.add_error("code", "checksum is invalid")
