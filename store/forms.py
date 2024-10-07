from django import forms
from .models import Review, Clothing, Color

# Atsiliepimo formos klasė
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # Nurodome, kurie modelio laukai bus naudojami formoje
        fields = ['rating', 'comment']
        labels = {
            'rating': 'Įvertinimas',
            'comment': 'Atsiliepimas'
        }
        # Nustatome formos laukų valdiklius
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),  # Įvertinimo laukui naudojame Select valdiklį su pasirinkimais nuo 1 iki 5
            'comment': forms.Textarea(attrs={'rows': 3}),  # Atsiliepimo laukui naudojame Textarea valdiklį su 3 eilutėmis
        }

# Drabužių formos klasė
class ClothingForm(forms.ModelForm):
    class Meta:
        model = Clothing
        fields = ['name', 'category', 'genre', 'brand', 'description', 'price', 'sizes', 'colors', 'stock', 'is_on_sale', 'image']

    def __init__(self, *args, **kwargs):
        super(ClothingForm, self).__init__(*args, **kwargs)
        # Nustatome spalvų pasirinkimus
        self.fields['colors'].queryset = Color.objects.all()
        self.fields['colors'].choices = [('', '----')] + [(color.id, color.name) for color in self.fields['colors'].queryset]