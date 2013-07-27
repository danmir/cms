#-*- coding: utf-8 -*-
__author__ = 'apple'
from django.contrib import admin
from search.models import SearchKeyord
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

#При редактировании FlatPage можем добавить keywords
class SearchKeywordInLine(admin.StackedInline):
    model = SearchKeyord

class FlatPageAdminWithKeywords(FlatPageAdmin):
    inlines = [SearchKeywordInLine]

class SearchKeywordAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminWithKeywords)
admin.site.register(SearchKeyord, SearchKeywordAdmin)