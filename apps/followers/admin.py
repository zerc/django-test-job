# coding: utf-8
from django.contrib import admin
from django.db.models import Count
from django import forms

from .models import Man


def make_man_admin_form(man):
    """
    Dirty trick.
    Form with reverse m2m field as FilteredSelectMultiple widget
    """
    class ManAdminForm(forms.ModelForm):
        followers = forms.ModelMultipleChoiceField(
            label="Followers", queryset=Man.objects.all(),
            initial=man.followers.all(),
            widget=admin.widgets.FilteredSelectMultiple("followers", False),
            required=False
        )

        class Meta:
            model = Man
            fields = ("name", "follow", "followers")

        def save(self, commit=True):
            instance = super(ManAdminForm, self).save(commit)
            instance.followers = self.cleaned_data.get("followers", [])
            return instance
    return ManAdminForm


class ManAdmin(admin.ModelAdmin):
    list_display = ("name", "follow_count", "followers_count")
    list_per_page = 50
    filter_horizontal = ("follow",)

    def get_form(self, request, obj=None, **kwargs):
        if obj is not None:
            self.form = make_man_admin_form(obj)
        return super(ManAdmin, self).get_form(request, obj, **kwargs)

    def follow_count(self, obj):
        return obj.follow.count()

    def followers_count(self, obj):
        return obj.followers_count

    def queryset(self, request):
        """
        Added prefetch_related and annotate for sql optimization
        """
        return super(admin.ModelAdmin, self).queryset(request)\
            .annotate(followers_count=Count("followers")).prefetch_related("follow")


admin.site.register(Man, ManAdmin)
