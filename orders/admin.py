from django.contrib import admin
from .models import Order, OrderItem, CartItem

# Užsakymo prekės inline klasė
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['order']
    extra = 0

# Užsakymo administravimo klasė
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'updated_at', 'is_paid', 'get_total_cost']
    list_filter = ['is_paid', 'created_at', 'updated_at']
    search_fields = ['user__username', 'id']
    inlines = [OrderItemInline]
    ordering = ['-created_at']

    # Metodas, kuris grąžina bendrą užsakymo kainą
    def get_total_cost(self, obj):
        return obj.get_total_cost()

    # Nustatome stulpelio pavadinimą administravimo panelėje
    get_total_cost.short_description = 'Bendra kaina'

# Užsakymo prekės administravimo klasė
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', 'get_cost']
    list_filter = ['order']
    search_fields = ['product', 'order__user__username']

    def get_cost(self, obj):
        return obj.get_cost()
    get_cost.short_description = 'Prekės kaina'

# Krepšelio prekės administravimo klasė
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'user', 'quantity', 'date_added')
    search_fields = ('user__username', 'product_name')
    list_filter = ('date_added', 'user')

    def product_name(self, obj):
        return obj.product.name

    product_name.short_description = 'Prekė'

# Registruojame modelius administravimo panelėje
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(CartItem, CartItemAdmin)