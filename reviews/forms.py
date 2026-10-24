from django.forms import ModelForm, TextInput, EmailInput, Textarea, ChoiceField, HiddenInput
from .models import Review


RATINGS = (
    ('5', '*****'), ('4', '****'), ('3', '***'),
    ('2', '**'), ('1', '*'),
)


class ReviewForm(ModelForm):
    ratings = ChoiceField(
        choices=RATINGS,
        initial="5",
        widget=HiddenInput(attrs={"id": "selectedRating"}),
    )

    class Meta:
        model = Review
        fields = ("full_name", "email", "ratings", "comment")
        widgets = {
            "full_name": TextInput(attrs={
                "class": "w-full bg-slate-950 border border-slate-800 rounded p-2.5 text-slate-200 focus:outline-none focus:border-emerald-500",
                "placeholder": "e.g. Sarah Jane",
            }),
            "email": EmailInput(attrs={
                "class": "w-full bg-slate-950 border border-slate-800 rounded p-2.5 text-slate-200 focus:outline-none focus:border-emerald-500",
                "placeholder": "you@example.com",
            }),
            "comment": Textarea(attrs={
                "class": "w-full bg-slate-950 border border-slate-800 rounded p-2.5 text-slate-200 focus:outline-none focus:border-emerald-500",
                "rows": 3,
                "placeholder": "How was the Django API delivery or cloud setup?",
            }),
        }
