from django import forms

class NewDepartamentoForm(forms.Form):
    """NewDepartamentoForm definition."""
    name = forms.CharField(
        max_length=50,
    )
    first_name = forms.CharField(
        max_length=50,
    )
    departamento = forms.CharField(
        max_length=50,
    )
    shor_name = forms.CharField(
        max_length=20,
    )
    # TODO: Define form fields here

