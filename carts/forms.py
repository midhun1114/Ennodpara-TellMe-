from django import forms
from .models import cart



# class cartsCreateForm(forms.ModelForm):
    # title = forms.CharField(label='Name',
    #                         widget=forms.TextInput(attrs={"class" :"form-control ","placeholder": "Your title"}))
    # description = forms.CharField(
    #
    #     widget=forms.Textarea(
    #         attrs={"class" :"form-control ",
    #             "placeholder": "Your description",
    #             "class": "new-class-name two",
    #             "id": "my-id-for-textarea",
    #             "rows": 20,
    #             'cols': 120
    #         }
    #     )
    # )
    # song = forms.CharField(label='Song',required=False,
    #                         widget=forms.TextInput(attrs={"class" :"form-control ","placeholder": "Song Name"}))
    # name2 = forms.CharField(label='', required=False,
    #                         widget=forms.TextInput(attrs={"class" :"form-control ","placeholder": "Your title"}))
    #
    # class Meta:
    #     model = cart
    #     fields = [
    #         'title',
    #         'description',
    #         'song',
    #         'name2'
    #     ]

class RawCartForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField( required=True , widget=forms.Textarea)
    song = forms.CharField(max_length=256 , required=False)
    name2 = forms.CharField(max_length=100,required=False)


    # title = forms.CharField(label='Name',
    #                         widget=forms.TextInput(attrs={"class" :"form-control ","placeholder": "Your title"}))
    # description = forms.CharField(
    # #
    #     widget=forms.Textarea(
    #         attrs={"class" :"form-control ",
    #             "placeholder": "Your description",
    #             "class": "new-class-name two",
    #             "id": "my-id-for-textarea",
    #             "rows": 20,
    #
    #         }
    #     )
    # )
    # song = forms.CharField(label='Song', required=False,
    #                        widget=forms.TextInput(attrs={"class" :"form-control ","placeholder": "Song Name"}))
    # name2 = forms.CharField(label='', required=False,
    #                         widget=forms.TextInput(attrs={"class" :"form-control ","placeholder": "Your title"}))
