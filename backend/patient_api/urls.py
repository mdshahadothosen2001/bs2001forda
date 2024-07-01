from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views.token import MyTokenObtainPairView
from .views.register import UserRegistrationView
from .views.profile import PatientProfileView
from .views.profile_update import PatientUpdateProfileView
from .views.doctor_list import DoctorListView
from .views.specialization import SpecializationView
from .views.appointment import AppointmentListView
from .views.appointment import AppointmentListWhichRecentCreatedView
from .views.book import BookAppointmentView
from .views.appointment_detail import AppointmentDetailView
from .views.date import TodayDateView


urlpatterns = [
    # POST: localhost:8000/api/patient/register/
    path(route="register/", view=UserRegistrationView.as_view(), name="patient_register"),
    # POST: localhost:8000/api/patient/login/
    path(route="login/", view=MyTokenObtainPairView.as_view(), name="patient_login"),
    # POST: localhost:8000/api/patient/login/refresh/
    path(route="login/refresh/", view=TokenRefreshView.as_view(), name="login_refresh"),
    # GET: localhost:8000/api/patient/profile/
    path(route="profile/", view=PatientProfileView.as_view(), name="patient_profile"),
    # PATCH: localhost:8000/api/patient/profile/update/
    path(route="profile/update/", view=PatientUpdateProfileView.as_view(), name="patient_profile_update"),
    # PATCH: localhost:8000/api/patient/profile-info-update/
    path(route="profile-info-update/", view=PatientUpdateProfileView.as_view(), name="patient_profile_update"),
    # GET: localhost:8000/api/patient/doctor-list/
    path(route="doctor-list/", view=DoctorListView.as_view(), name="doctor_list"),
    # GET: localhost:8000/api/patient/specialization-list/
    path("specialization-list/", SpecializationView.as_view(), name="specializations"),
    # GET: localhost:8000/api/patient/appointment-list/
    path(route="appointment-list/", view=AppointmentListView.as_view(), name="appointment_list"),
    # GET: localhost:8000/api/patient/recent-appointment-list/
    path(route="recent-appointment-list/", view=AppointmentListWhichRecentCreatedView.as_view(), name="recent_appointment_list"),
    # POST: localhost:8000/api/patient/appointment-book/
    path(route="appointment-book/", view=BookAppointmentView.as_view(), name="appointment_book"),
    # GET: localhost:8000/api/patient/appointment-detail/2/
    path("appointment-detail/<int:pk>/", AppointmentDetailView.as_view(), name="appointment_detail"),
    # GET: localhost:8000/api/patient/today-date/
    path("today-date/", TodayDateView.as_view(), name="today_date"),
]
