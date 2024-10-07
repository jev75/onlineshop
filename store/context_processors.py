from .models import Category

# Funkcija, kuri prideda kategorijų sąrašą į kontekstą
def categories(request):
    return {
        # Naudojame prefetch_related, kad iš anksto užkrautume susijusias subkategorijas
        'categories': Category.objects.prefetch_related('subcategory_set').all()
    }