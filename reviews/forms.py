from django.forms import ModelForm, TextInput, EmailInput, Textarea, Select, ChoiceField, HiddenInput
from .models import Review


RATINGS = (
    ('5', '*****'), ('4', '****'), ('3', '***'),
    ('2', '**'), ('1', '*'),
)

class ReviewForm(ModelForm):
    ratings = ChoiceField(choices=RATINGS, widget=Select(attrs={"class":"form-control"}))

    class Meta:
        model = Review
        fields = "__all__"
        widgets = {
            "full_name": TextInput(attrs={"class":"form-control"}),
            "email": EmailInput(attrs={"class":"form-control"}),
            "comment": Textarea(attrs={"class":"form-control", "rows":3}),
            "verify": HiddenInput,
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['verify'].label = ''
