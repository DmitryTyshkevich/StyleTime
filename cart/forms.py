from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductFormV1(forms.Form):
    """
    Форма для страницы сведений конкретного товара.
    """
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label=''
    )
    # позволяет пользователю выбрать количество между 1-10
    # TypedChoiceField с coerce=int для преобразования ввода в целое число.

    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
    # Update : позволяет указать, следует ли добавлять сумму к любому
    # существующему значению в корзине для данного продукта (False) или 
    # если существующее значение должно быть обновлено с заданным 
    # значением (True). Для этого поля используется графический элемент 
    # HiddenInput, поскольку не требуется показывать его пользователю.


class CartAddProductFormV2(forms.Form):
    """
    Форма для страницы каталога.
    """
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label='',
        widget=forms.Select(attrs={'hidden': 'true'})
        # поле будет скрыто в форме
    )
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
