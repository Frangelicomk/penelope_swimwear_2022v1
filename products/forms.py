from django import forms
from .models import Product, Category, Extra_Img


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0 \
                 select form-control'


class ExtraImgForm(forms.ModelForm):

    class Meta:
        model = Extra_Img
        fields = ('img',)
