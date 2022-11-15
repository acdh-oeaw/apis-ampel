from django.urls import path
from django.conf.urls import url
#from .views import HandleAmpelNoteView, UpdateAmpelStatusView
from .views import AmpelSettingsView, FetchAmpelStatusView, UpdateAmpelStatusView, HandleAmpelNoteView, AmpelDocsView

app_name = "apis_ampel"

urlpatterns = [
    url(r"ampel_page/", AmpelSettingsView.as_view(), name="ampel_settings"),
    url(r"ampel_docs/", AmpelDocsView.as_view(), name="ampel_docs"),
    url(r"ampel_settings/update/(?P<ampel_id>[0-9]+)/$", AmpelSettingsView.as_view(), name="update_ampel_view"),
   # url(r"ampel_entity/fetch_ampel_status", FetchAmpelStatusView.as_view(), name="fetch_ampel_status"),

    #url(r"entity/handle_note/get/(?P<ampel_pk>[0-9]+)/$", HandleAmpelNoteView.as_view(), name="get_note_text"),
    url(r"ampel_entity/handle_note/$", HandleAmpelNoteView.as_view(), name="update_note_text"),
    url(r"ampel_entity/update_ampel_status", UpdateAmpelStatusView.as_view(), name="update_ampel_instance"),
]