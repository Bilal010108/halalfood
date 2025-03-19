from .models import Product, Store, Category
from modeltranslation.translator import TranslationOptions,register

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('description',)



@register(Store)
class StoreTranslationOptions(TranslationOptions):
    fields = ('store_description',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)