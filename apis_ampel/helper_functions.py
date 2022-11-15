from .models import AmpelTemp, AmpelSettings
from apis_core.apis_entities.models import TempEntityClass
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

# def get_ampel_color(model_class, instance_pk):
#     print("get_ampel_color called", model_class, instance_pk)
#     ct = ContentType.objects.get(model=model_class)
#     model = ct.model_class()
#     instance = model.objects.get(id=instance_pk)
#     test = AmpelGeneric.objects.filter(pk=instance_pk)
#     try:
#         if test and len(test) < 2:
#             color = test[0].status
#         else: 
#             new_instance = AmpelGeneric.objects.create(content_type=ct, content_object=instance)
#             new_instance.save()
#             color = new_instance.status
#     except Exception as e:
#         print("SOMETHING WENT WRONG", model_class, instance_pk, e)
#     return color


def get_or_create_ampel(pk, status=None):
    """
    Enables the lazy handling of the ampel: Auto-creates the ampel for a given entity or relation when it is being accessed for the first time or returns the exisiting instance.

    pk: TempEntityClass-instance primary key: Note that all entitites and relations share their primary key with the TempEntityClass they inherited from. 
        So all keys are continous and singular. Thefore, no check for the specific entity- or relation-type is needed.
    status: optional param; give an initial state or change the existing state. Expects a value of "red", "yellow" or "green".
    return: an Ampel-instance
    """
    a = AmpelTemp.objects.filter(pk=pk)

    if not status:
        if a:
            return AmpelTemp.objects.get(pk=pk)
        else: 
            a = AmpelTemp.objects.create(temp_entity=TempEntityClass.objects.get(pk=pk))
            a.save()
            return a 
    else:
        if a:
            a = AmpelTemp.objects.get(pk=pk)
            a.status = status
            a.save()
            return a
        else: 
            a = AmpelTemp.objects.create(temp_entity=TempEntityClass.objects.get(pk=pk), status=status)
            a.save()
            return a 

def is_ampel_active(model_name:str):
    """
    Checks if the display of the Ampel is enabled in the AmpelSettings for a given model. 
    model_name: name of the model to check for; like Person, Institution or PersonInstitution, etc.

    return: boolean value representing if model is active in AmpelSettings.
    
    """
    print(f"In ampel active, model name is: {model_name}")
    try: 
        as_instance = AmpelSettings.objects.get(content_type=ContentType.objects.get(model=model_name))
        return as_instance.active
    except Exception as e:
        print(e)
        return False
    

def get_ampel_color(*args, **kwargs):
    # DELETE
    pass


