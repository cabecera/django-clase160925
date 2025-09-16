# Documentacion Django proyecto

1. Buscar un template que nos gusta y descargamos: 
	-  https://startbootstrap.com/theme/clean-blog
2.  Abrir visual studio:
	- Iniciamos un proyecto
		- Agregamos core 
		- Agregamos foro 
	- Migramos 
	
```
		django-admin startproject nombreproyecto
		python manage.py startapp core
		python manage.py startapp foro
		python manage.py runserver
```

3. En core agregar: 
	- templates/core
	- static/core
4. En static/core poner los archivos estáticos del template que descargamos:
	- css
	- js
	- assets
5. En templates/core agregar la base.html e index.html
6. En base.html agregar el codigo de la base del template(index.html)
7. configurar lo que queremos que se muestre con:
	{% block content %}{% endblock %} : en este proyecto se usó antes de llegar al footer
8.  En index agregar la base:
```
{% extends 'core/base.html' %}
    {% block content %}
    
    
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima eligendi aliquam quaerat, maiores labore quisquam officiis, impedit ex libero autem at hic voluptatum repudiandae quidem beatae provident voluptas quo adipisci?</p>

    {% endblock %}
```
9.  Configurar: 

settings: agregamos core y foro a installed_apps
views: creamos una nueva vista para index.html
```
# Create your views here.

def index(request):
    return render(request,"core/index.html")
```
url:
```
from core import views as views_core

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_core.index,name="index"),
]
```



