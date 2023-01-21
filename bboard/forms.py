from django.forms import ModelForm
from .models import Bb, AdditionalImage
from django.forms import inlineformset_factory
from image_uploader_widget.widgets import ImageUploaderWidget


class AdditionalImageForm(ModelForm):
    class Meta:
        model = AdditionalImage
        fields = '__all__'
        widgets = {'image': ImageUploaderWidget(empty_text = "перетащите сюда фото или нажмите для выбора...", drop_text = "перетащите фото сюда")}

class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = '__all__'
        widgets = {'image': ImageUploaderWidget(empty_text = "перетащите сюда фото или нажмите для выбора...", drop_text = "перетащите фото сюда")}
        inlines = [AdditionalImageForm]

#class BaseChildrenFormSet(BaseInlineFormSet):
#    class Meta:
#        model = AdditionalImage
#        fields = '__all__'
#        widgets = {'image': ImageUploaderWidget(empty_text = "перетащите сюда фото или нажмите для выбора...", drop_text = "перетащите фото сюда")}


AIFormSet = inlineformset_factory(Bb, AdditionalImage, fields='__all__', localized_fields='__all__', extra=3, widgets = {'image': ImageUploaderWidget(empty_text = "перетащите сюда фото или нажмите для выбора...", drop_text = "перетащите фото сюда")}) #

