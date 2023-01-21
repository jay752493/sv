from django.contrib import admin
from .forms import BbForm

from .models import Bb, Rubric, AdditionalImage
from image_uploader_widget.admin import ImageUploaderInline
# Register your models here.

admin.site.register(Rubric)

class AdditionalImageInline(ImageUploaderInline):
    model = AdditionalImage
    add_image_text = "добавить фото"
    empty_text = "перетащите сюда фото или нажмите для выбора..."
    drop_text = "перетащите фото сюда"

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'kind', 'content', 'image','published')
    fields = (('rubric'), 'title', 'content', 'image', 'kind')
    search_fields = ('title', 'content')
    inlines = (AdditionalImageInline,)
    form = BbForm

admin.site.register(Bb, BbAdmin)

#class InlineEditor(ImageUploaderInline):
#    model = AdditionalImage

#@admin.register(models.Inline)
#class InlineAdmin(admin.ModelAdmin):
#    inlines = [InlineEditor]
