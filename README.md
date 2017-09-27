# metarita

An 'APIS' clone to caputure metadata about inventories transcribed in the project 'Reading in the Alps'


## installation

1. clone the repo `git clone https://github.com/acdh-oeaw/teihencer.git`
2. init apis-submodule `git submodule update --init`
3. create symbolic links from `metarita-webapp`, and `metarita-urls` to  `apis-core/webpage` and `apis-core/custom_urls` (on windows use  `mklink /d webpage ..\metarita-webapp`)
4. create symbolic link from `metarita-settings` to `apis-core/apis/settings`
5. Make migrations `python manage.py makemigrations entities highlighter labels metainfo relations vocabularies webpage --settings=apis.settings.dev`
