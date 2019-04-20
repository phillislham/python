# learnlang\theapp\urls.py
# rerouting all requests that have �api� in the url to the <code>apps.core.urls
from django.conf.urls import url
from rest_framework import routers
from learnlang.theapp.views import *
 
router = routers.DefaultRouter()
router.register(r'apparray', AppArrayViewSet)
router.register(r'appexam', AppExamViewSet)
router.register(r'appexamssentences', AppExamsSentencesViewSet)
router.register(r'appexamsusers', AppExamsUsersViewSet)
router.register(r'appexamsusersevalh', AppExamsUsersEvalhViewSet)
router.register(r'appexamsusersevall', AppExamsUsersEvallViewSet)
router.register(r'appsentence', AppSentenceViewSet)
router.register(r'appsentenceimages', AppSentenceImagesViewSet)
router.register(r'appsentencesusers', AppSentencesUsersViewSet)
router.register(r'appsentencetags', AppSentenceTagsViewSet)
router.register(r'appsentencetimes', AppSentenceTimesViewSet)
router.register(r'appsentencetr', AppSentenceTrViewSet)
router.register(r'apptag', AppTagViewSet)
router.register(r'baselanguage', BaseLanguageViewSet)
router.register(r'baselanguagelang', BaseLanguageLangViewSet)
router.register(r'baseuser', BaseUserViewSet)
router.register(r'baseuserarray', BaseUserArrayViewSet)
router.register(r'template', TemplateViewSet)
router.register(r'templatearray', TemplateArrayViewSet)
router.register(r'versiondb', VersionDbViewSet)
 
urlpatterns = router.urls