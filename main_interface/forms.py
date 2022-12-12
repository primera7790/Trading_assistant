from django import forms


class BalanceForm(forms.Form):
    value = forms.CharField(max_length=12)