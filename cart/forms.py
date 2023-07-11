from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductFormV1(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int, label=''
    )
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CartAddProductFormV2(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label='',
        widget=forms.Select(attrs={'hidden': 'true'})
    )
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
