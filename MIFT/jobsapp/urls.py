from django.urls import path, include
from django.conf.urls import url
from .views import *
from django.views.generic.base import TemplateView

app_name = "jobs"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search', SearchView.as_view(), name='searh'),
    path('ngo/dashboard/', include([
        path('', DashboardView.as_view(), name='ngo-dashboard'),
        path('all-applicants', ApplicantsListView.as_view(), name='ngo-all-applicants'),
        path('applicants/<int:job_id>', ApplicantPerJobView.as_view(), name='ngo-dashboard-applicants'),
        path('mark-filled/<int:job_id>', filled, name='job-mark-filled'),
    ])),
    path('apply-job/<int:job_id>', ApplyJobView.as_view(), name='apply-job'),
    path('jobs', JobListView.as_view(), name='jobs'),
    path('jobs/<int:id>', JobDetailsView.as_view(), name='jobs-detail'),
    path('ngo/jobs/create', JobCreateView.as_view(), name='ngo-jobs-create'),
    url(r'^payment', TemplateView.as_view(template_name='jobs/payment.html'), name='jobs-payment'),
    path('jobs/<int:id>/delete', JobDeleteView.as_view(), name='jobs-delete'),
    path('jobs/<int:id>/update', JobUpdateView.as_view(), name='jobs-update'),
    path('donates/<int:id>', Donateview.as_view(), name='jobs-donate'),

]
