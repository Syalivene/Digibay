from django import forms
from django.core.validators import MaxLengthValidator
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
INPUT_CLASSE_IMAGE = 'w-full py-4 px-6 rounded-xl border bg-white'
INPUT_CLASSES_B = 'w-2/3 py-2 px-3 rounded-xl border'

class NewItemForm(forms.ModelForm):
    name = forms.CharField(validators=[MaxLengthValidator(20)], widget=forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'Name of item (max 18 letters)',
            }))

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'price2', 'image',)

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'required': True
            }),

            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'rows': 3,
                'cols': 40,
                'placeholder': 'eg. local hen with good culinary properties and disease-resistant breed...'
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'eg. 15'
            }),
            'price2': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'eg. 14'
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSE_IMAGE,
                'required': True
            }),
        }

        help_texts = {
            'image': '<span class="text-teal-500 text-sm">Upload main image (mandatory)</span>',
            'price': '<span class="text-teal-500 text-sm">Current price of item</span>',
            'price2': '<span class="text-teal-500 text-sm">Discounted price of item</span>',
            'category': '<span class="text-teal-500 text-sm">Select category of item</span>',
            'description': '<span class="text-teal-500 text-sm">Describe your item</span>',
        }



class NewItemFormPremium(forms.ModelForm):
    name = forms.CharField(validators=[MaxLengthValidator(20)], widget=forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'Name of item (max 18 letters)',
            }))

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'price2', 'image', 'image2', 'image3', 'status', 'stock',)

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'required': True
            }),

            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'rows': 3,
                'cols': 40,
                'placeholder': 'eg. local hen with good culinary properties and disease-resistant breed...'
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'eg. 15'
            }),
            'price2': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'eg. 14'
            }),
            'status': forms.Select(attrs={
                'class': INPUT_CLASSES_B,
                'required': True
            }),
            'stock': forms.Select(attrs={
                'class': INPUT_CLASSES_B,
                'required': True
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSE_IMAGE,
                'required': True
            }),
            'image2': forms.FileInput(attrs={
                'class': INPUT_CLASSE_IMAGE,
            }),
            'image3': forms.FileInput(attrs={
                'class': INPUT_CLASSE_IMAGE,
            }),
        }

        help_texts = {
            'image': '<span class="text-teal-500 text-sm">Upload main image (mandatory)</span>',
            'image2': '<span class="text-teal-500 text-sm">Upload second image (optional)</span>',
            'image3': '<span class="text-teal-500 text-sm">Upload brand image (optional)</span>',
            'price': '<span class="text-teal-500 text-sm">Current price of item</span>',
            'price2': '<span class="text-teal-500 text-sm">Discounted price of item</span>',
            'category': '<span class="text-teal-500 text-sm">Select category of item</span>',
            'description': '<span class="text-teal-500 text-sm">Describe your item</span>',
        }


class EditItemForm(forms.ModelForm):
    name = forms.CharField(validators=[MaxLengthValidator(20)], widget=forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'Name of item (max 18 letters)',
            }))

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'price2', 'image', 'is_sold',)

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'required': True
            }),

            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'rows': 3,
                'cols': 40
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'eg. 15'
            }),
            'price2': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'eg. 14'
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
                'required': True
            }),
        }

        help_texts = {
            'image': '<span class="text-teal-500 text-sm">Upload main image (mandatory)</span>',
            'price': '<span class="text-teal-500 text-sm">Current price of item</span>',
            'price2': '<span class="text-teal-500 text-sm">Discounted price of item</span>',
            'category': '<span class="text-teal-500 text-sm">Select category of item</span>',
            'description': '<span class="text-teal-500 text-sm">Describe your item</span>',
        }




class EditItemFormPremium(forms.ModelForm):
    name = forms.CharField(validators=[MaxLengthValidator(20)], widget=forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'Name of item (max 18 letters)',
            }))

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'price2', 'image', 'image2', 'image3', 'status', 'stock',)

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'required': True
            }),

            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'rows': 3,
                'cols': 40,
                'placeholder': 'eg. local hen with good culinary properties and disease-resistant breed...'
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'eg. 15'
            }),
            'price2': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'eg. 14'
            }),
            'status': forms.Select(attrs={
                'class': INPUT_CLASSES_B,
                'required': True
            }),
            'stock': forms.Select(attrs={
                'class': INPUT_CLASSES_B,
                'required': True
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSE_IMAGE,
                'required': True
            }),
            'image2': forms.FileInput(attrs={
                'class': INPUT_CLASSE_IMAGE,
            }),
            'image3': forms.FileInput(attrs={
                'class': INPUT_CLASSE_IMAGE,
            }),
        }

        help_texts = {
            'image': '<span class="text-teal-500 text-sm">Upload main image (mandatory)</span>',
            'image2': '<span class="text-teal-500 text-sm">Upload second image (optional)</span>',
            'image3': '<span class="text-teal-500 text-sm">Upload brand image (optional)</span>',
            'price': '<span class="text-teal-500 text-sm">Current price of item</span>',
            'price2': '<span class="text-teal-500 text-sm">Discounted price of item</span>',
            'category': '<span class="text-teal-500 text-sm">Select category of item</span>',
            'description': '<span class="text-teal-500 text-sm">Describe your item</span>',
        }
