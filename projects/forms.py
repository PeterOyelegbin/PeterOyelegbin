from django import forms


class ContactRequestForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "class": "w-full bg-slate-900 border border-slate-800 rounded p-2.5 text-slate-200 focus:outline-none focus:border-emerald-500",
            "placeholder": "John Doe",
        }),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "w-full bg-slate-900 border border-slate-800 rounded p-2.5 text-slate-200 focus:outline-none focus:border-emerald-500",
            "placeholder": "john@company.com",
        }),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "w-full bg-slate-900 border border-slate-800 rounded p-2.5 text-slate-200 focus:outline-none focus:border-emerald-500",
            "rows": 3,
            "placeholder": "Tell me about your API or deployment needs...",
        }),
    )
