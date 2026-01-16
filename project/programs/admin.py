from django.contrib import admin
from .models import Programs, Exercise, Photo

from django.urls import path
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages


# class CsvImportForm(forms.Form):
#     csv_uploader = forms.FileField()
#
# class ProgramsAdmin(admin.ModelAdmin):
#     def get_urls(self):
#         urls = super().get_urls()
#         new_urls = [path("upload-csv/", self.upload_csv)]
#         return new_urls + urls
#
#     def upload_csv(self, request):
#         if request.method == "POST":
#             csv_file = request.FILES["csv_uploader"]
#
#             if not csv_file.name.endswith('.csv'):
#                 messages.warning(request, "Ошибочный тип файла")
#                 return redirect('.')
#
#             file_data = csv_file.read().decode("utf-8")
#             csv_data = file_data.split("\n")
#
#             for x in csv_data:
#                 fields = x.split(",")
#                 Programs.objects.update_or_create(
#                     id=fields[0],
#                     name=fields[1],
#                     description=fields[2]
#                 )
#
#             return redirect('admin:index')
#
#         form = CsvImportForm()
#         data = {"form": form}
#         return render(request, 'admin/csv_uploader.html', data)

class PhotoAdd(admin.StackedInline):
    model = Photo
    fields = ('exercise', 'add_photo')
    extra = 0

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_display_links = ('id', 'name')
    inlines = [PhotoAdd]

    # def get_urls(self):
    #     urls = super().get_urls()
    #     new_urls = [path("upload-csv-exercise/", self.upload_csv)]
    #     return new_urls + urls
    #
    # def upload_csv(self, request):
    #     if request.method == "POST":
    #         csv_file = request.FILES["csv_uploader"]
    #
    #         if not csv_file.name.endswith('.csv'):
    #             messages.warning(request, "Ошибочный тип файла")
    #             return redirect('.')
    #
    #         file_data = csv_file.read().decode("utf-8")
    #         csv_data = file_data.split("\n")
    #
    #         for x in csv_data:
    #             fields = x.split(",")
    #             Exercise.objects.update_or_create(
    #                 id=fields[0],
    #                 name=fields[1],
    #                 image=fields[2],
    #                 description=fields[3],
    #                 short_description=fields[4],
    #                 category=Programs(fields[5][0])
    #             )
    #
    #         return redirect('admin:index')
    #
    #     form = CsvImportForm()
    #     data = {"form": form}
    #     return render(request, 'admin/csv_uploader.html', data)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'add_photo')

    # def get_urls(self):
    #     urls = super().get_urls()
    #     new_urls = [path("upload-csv-photo/", self.upload_csv)]
    #     return new_urls + urls
    #
    # def upload_csv(self, request):
    #     if request.method == "POST":
    #         csv_file = request.FILES["csv_uploader"]
    #
    #         if not csv_file.name.endswith('.csv'):
    #             messages.warning(request, "Ошибочный тип файла")
    #             return redirect('.')
    #
    #         file_data = csv_file.read().decode("utf-8")
    #         csv_data = file_data.split("\n")
    #
    #         for x in csv_data:
    #             fields = x.split(",")
    #             print(fields)
    #             Photo.objects.update_or_create(
    #                 id=fields[0],
    #                 product=Programs(fields[1]),
    #                 add_photo=fields[2][:-1]
    #             )
    #         return redirect('admin:index')
    #
    #     form = CsvImportForm()
    #     data = {"form": form}
    #     return render(request, 'admin/csv_uploader.html', data)

admin.site.register(Programs)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Photo, PhotoAdmin)