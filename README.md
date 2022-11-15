# Apis-Ampel

Django-App for the APIS plattform. Adds status indicators to all entities that are displayed as 'traffic lights' in list, detail and edit views.

## Basics

This module consists of two parts. A settings model, which allows to turn the display of the Ampel on or off on a per module basis, i.e. Relations (PersonInstitution, PersonPlace, etc.) or Entities (Person, Event, etc.).The second part is a model that stores for each instance of a given Entity or Relation a status indicator (red, yellow or green).When the Ampel is active for a given model, the indicator will be displayed in all listviews, detail views and edit views.
There is also a special note field attached to each Ampel instance, allowing for writing and retrieving a note on the given Ampel instance.

## Usage

In detail and edit views, the Ampel indicator can be toggled, if a user is logged in. Otherwise, the indicator will be displayed, but can't be changed.
The note for a given Ampel instance can be accessed via a button; the button is blue if a note exists, otherwise it is gray.

- toggling the Ampel indicator is auto-saved in a callback – so what you see is what you get
- instances where the Ampel has not been toggled yet, will show up as red in all views
- you can filter for those instances in the listview by selecting 'default' in the dropdown
- only instances where the Ampel has been set to red will show up listed under the 'red' option
- you can also search for text segments within a given note in the listview filters
- turning the display of an existing Ampel on or off for a given model only changes the visibility, it does not change the already stored data

## Implementation

Two django-models are used: AmpelSettings – which links to the content_type of a given model, and a Ampel model.
The Ampel model links to TempEntityClass via a one-to-one-field; this field is also used as the models primary key.
Note that all Relations and Entities inherit from TempEntityClass in Apis – which means the primary key of a Entity or Relation instance
is ident to the primary key of its TempEntityClass and also with the primary key of the Ampel instance it is linked to.
As all Entities and Relations inherit their primary key field from TempEntityClass, all ids are unique, even across different Entities and Relations.
Therefore you can programmatically access a given Ampel instance by looking up the primary key of an Entity or Relation instance in the Ampel model.
The Ampel setup is lazy: you don't have to give initial values; a helper function was implemented that checks if an Ampel instance exists for a given Entity or Relation, and if not, it will be created.
So when you first try to access an Ampel instance by toggling the indicator, the actual instance will be created automatically.
That's the reason why a default display of 'red' was enabled in all views for nstances of Relations or Entities for which the Ampel has not been set yet.
You can filter for those in the listview by selecting the 'default' option in the Ampel dropdown.

## Dependencies

This module depends on apis_core version 18.3 or higher.

## Installation

### 1. Install the package

via pip:

```bash
pip install apis-ampel
```

via poetry:

```sh
poetry add apis-ampel
```

### 2. Update your settings.py file

Add "apis_ampel" to your INSTALLED_APPS settings variable.

### 3. Update your urls.py file

Add this block:

```python
if "apis_ampel" in settings.INSTALLED_APPS:
    urlpatterns.append(
        url(
            r"^apis_ampel/",
            include("apis_ampel.urls", namespace="apis_ampel"),
        )
    )
```

### 4. Update webpage/templates/base.html

Add this block within the ul-tag of your navbar element:

```html
{% if user.is_authenticated and "apis_ampel" in APPS %}
<li class="nav-item dropdown">
    <a class="nav-link"href="{% url'apis_ampel:ampel_settings' %}">Ampel`</a>`
</li>
{% endif %}
```
