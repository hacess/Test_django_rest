from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from polls.views import QuestionViewSet, ChoiceViewSet



router = routers.DefaultRouter()
router.register(r'question', QuestionViewSet)



urlpatterns = [
	url(r'^polls/', include('polls.urls')),
	url(r'^login/',include('login.urls')),
	url(r'^admin/', admin.site.urls),
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls'))
]