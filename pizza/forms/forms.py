from django import forms


class BuyForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'name': 'email',
                'type': 'email',
                'class': 'form-control',
                'required': True
            }
        )
    )

    phone = forms.IntegerField(
        label='Телефон',
        widget=forms.TextInput(
            attrs={
                'name': 'phone',
                'type': 'tel',
                'class': 'form-control',
                'required': True
            }
        )
    )

    name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={
                'name': 'name',
                'class': 'form-control',
                'required': True
            }
        )
    )

    summary_price = forms.CharField(
        label='Итоговая цена($)',
        widget=forms.TextInput(
            attrs={
                'name': 'summary_price',
                'class': 'form-control',
                'disabled': 'true'
            }
        )
    )
