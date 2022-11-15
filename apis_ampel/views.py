from .models import AmpelGeneric, AmpelTemp, AmpelSettings
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView
from django.utils.decorators import method_decorator
# Create your views here.
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required, user_passes_test
from .fallback_settings import AMPEL_SETTINGS
from django.contrib.contenttypes.models import ContentType
from .helper_functions import get_or_create_ampel


# TODO add check for authentication

class AmpelDocsView(View):
    def get(self, request):
        template = "./ampel/ampel_documentation.html"

        return render(request, template, {})

class AmpelSettingsView(View):

    # def setup(self, request, *args, **kwargs):
    #     ampel_id = kwargs.get('ampel_id', None)
    #     self.ampel_id = ampel_id
    #     print(self.ampel_id, "ampel id")
   
    #     return super().setup(request, *args, **kwargs)

    def get(self, request):
        template = "./ampel/ampel_settings_template.html"
        rels = AMPEL_SETTINGS["relations"]
        ents = AMPEL_SETTINGS["entities"]
        #AmpelSettings.objects.all().delete()
        for el in ents+rels:
            for k,v in el.items():
                ct = ContentType.objects.get(model=k)
                a, c = AmpelSettings.objects.get_or_create(content_type=ct)
                # if c:
                #     model_class = ct.model_class()
                #     for obj in model_class.objects.all():
                #         try: 
                #             ag = AmpelGeneric.objects.create(content_type=ct, content_object=obj)
                #         except Exception as e:
                #             print(e)
                #         print("created new ampel for ", ag)
                #     print("created: ", a, c)
                #     a.active = v
                #     a.save()
        models = AmpelSettings.objects.all()
        return render(request, template, {"models":models})

    def post(self, request, **kwargs):
        instance = None
        success = False
        msg = ""

        #ampel_id = request.POST.get("ampel_id")
        ampel_id = kwargs.get("ampel_id")
        try:
            if ampel_id:
                instance = AmpelSettings.objects.get(id=ampel_id)
                instance.active = not instance.active
                instance.save()
                success = True
        except Exception as e:
            msg = str(e)
        
        return JsonResponse({"success":success, "msg":msg, "status":instance.active})


class FetchAmpelStatusView(View):
    def get(self, request):
        success = True
        msg = "success"
        ampel_pk = request.POST.get("ampel_pk")
        #status = request.POST.get("status")
        try:
            ampel = get_or_create_ampel(ampel_pk)
            ampel.status = status
            ampel.save()
        except Exception as e:
            success = False
            msg = f"something went wrong\n{e}"
        

        return JsonResponse({"success":success, "msg":msg, "status":None})


class UpdateAmpelStatusView(View):
    def post(self, request):
        success = True
        msg = "success"
        ampel_pk = request.POST.get("id")
        status = request.POST.get("status")
        try:
            ampel = get_or_create_ampel(ampel_pk, status)
            ampel.status = status
            ampel.save()
        except Exception as e:
            success = False
            msg = f"something went wrong\n{e}"
        

        return JsonResponse({"success":success, "msg":msg})


class HandleAmpelNoteView(View):

    def get(self, request, **kwargs):
        success = True
        msg = "success"
        note = ""
        try:
            ampel_pk = kwargs.get("ampel_pk")
            ampel = get_or_create_ampel(ampel_pk)
            note = ampel.note
            if not note:
                note = ""
        except Exception as e:
            success = False
            msg = f"{e}"

        return JsonResponse({"success":success, "msg":msg, "text":note})

    def post(self, request):
        print("post note called")
        success = True
        msg = "success"
        ampel_pk = request.POST.get("id")
        try:
            ampel = get_or_create_ampel(ampel_pk)
            ampel.note = request.POST.get("note_text")
            ampel.save()
        except Exception as e:
            success = False
            msg = f"{e}"
        
        return JsonResponse({"success":success, "msg":msg})

