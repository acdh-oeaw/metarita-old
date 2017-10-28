import zipfile
import os
from django.conf import settings
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Image
from .forms import ImageForm, UploadZipForm

MEDIA_ROOT = settings.MEDIA_ROOT


class UploadZip(FormView):
    template_name = 'images/upload_zip.html'
    form_class = UploadZipForm
    success_url = '.'

    def form_valid(self, form, **kwargs):
        context = super(UploadZip, self).get_context_data(**kwargs)
        cd = form.cleaned_data
        filepath = cd.get('filepath')
        zipped = cd.get('uploaded_zip')
        extract_path = os.path.join(MEDIA_ROOT, filepath)
        print(MEDIA_ROOT)
        context['unzip_path'] = extract_path
        zf = zipfile.ZipFile(zipped, 'r')
        extracted = zf.extractall(extract_path)
        if cd.get('link_to_class'):
            link_to_class = cd.get('link_to_class')
            model_pk = int(cd.get('object_id'))
            fetched_class = ContentType.objects.get(model=link_to_class)
            fetched_model = fetched_class.get_object_for_this_type(id=model_pk)
        else:
            fetched_model = None
        for x in zf.infolist():
            if (x.filename).endswith('.jp2'):
                print(x.filename)
                new_img = Image.objects.create(
                    directory=cd['filepath'],
                    custom_filename=x.filename)
                if fetched_model:
                    new_img.depicts_work = [fetched_model][0]
                    new_img.save()
                else:
                    pass
        context['filepath'] = filepath
        context['extract_path'] = extract_path
        context['zipped'] = zf.infolist()
        return render(self.request, self.template_name, context)


class ImageDetailView(DetailView):
    model = Image
    template_name = 'images/image_detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ImageDetailView, self).dispatch(*args, **kwargs)


class ImageListView(ListView):
    model = Image
    template_name = 'images/image_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ImageListView, self).dispatch(*args, **kwargs)


class ImageCreate(CreateView):

    model = Image
    template_name = 'images/image_create.html'
    form_class = ImageForm
