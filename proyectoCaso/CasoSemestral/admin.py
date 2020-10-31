from django.contrib import admin
from .models import Insumos
from .models import ImagenGaleria
from .models import ImagenSlider
from .models import QuienesSomos

class InsumosAdmin(admin.ModelAdmin):
    list_display=['nombre','precio','descripcion','stock']
    search_fields=['nombre']
    list_per_page=10

class SliderAdmin(admin.ModelAdmin):
    list_display=['imagenSlider']
    search_fields=['imagenSlider']
    list_per_page=10

class GaleriaAdmin(admin.ModelAdmin):
    list_display=['imagen']
    search_fields=['imagen']
    list_per_page=10

class QuienesAdmin(admin.ModelAdmin):
    list_display=['ident','vision','mision']
    search_fields=['ident']
    list_per_page=10


# Register your models here.

admin.site.register(Insumos,InsumosAdmin)
admin.site.register(ImagenSlider,SliderAdmin)
admin.site.register(ImagenGaleria,GaleriaAdmin)
admin.site.register(QuienesSomos,QuienesAdmin)