from django import forms

class ReviewForm(forms.Form):
    stars = forms.IntegerField(label='stars')
    comment = forms.CharField(label='comment')

    def clean_stars(self):
        star = self.cleaned_data['stars']
        if star < 1:
            raise forms.ValidationError('Stars must be between 1 and 5')
        if star > 5:
            raise forms.ValidationError('Stars must be between 1 and 5')
        return star