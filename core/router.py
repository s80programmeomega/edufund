from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from school.views import (FundingCampaignViewSet, RepresentativeViewSet,
                          SchoolDocumentViewSet, SchoolImageViewSet,
                          SchoolViewSet, StudentViewSet)
from sponsor.views import (AnonymousDonationViewSet, DonationViewSet,
                           SponsorRepresentativeViewSet, SponsorViewSet)
from users.views import UserViewSet

router = DefaultRouter()

# users routes
router.register("users", UserViewSet, basename="users")

# school routes
router.register("school", SchoolViewSet, basename="school")
router.register("representative", RepresentativeViewSet,
                basename="representative")
router.register("student", StudentViewSet, basename="student")
router.register("funding-campaign", FundingCampaignViewSet,
                basename="funding-campaign")
router.register("school-document", SchoolDocumentViewSet,
                basename="school-document")
router.register("school-image", SchoolImageViewSet, basename="school-image")

# sponsor routes
router.register("sponsor", SponsorViewSet, basename="sponsor")
router.register(
    "sponsor-representative",
    SponsorRepresentativeViewSet,
    basename="sponsor-representative",
)
router.register("donation", DonationViewSet, basename="donation")
router.register("anonymous-donation", AnonymousDonationViewSet,
                basename="anonymous-donation")


# Create a list of additional URL patterns for JWT
jwt_patterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]


drf_spectacular_urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
from users.views import LoginView, LogoutView
auth_urlpatterns = [
    path('login/', view=LoginView.as_view(), name="login"),
    path('logout/', view=LogoutView.as_view(), name="logout"),
    # restframework auth views
    path('auth/', include('rest_framework.urls')),
]

# Combine router URLs and JWT URLs
urlpatterns = router.urls + jwt_patterns + drf_spectacular_urlpatterns + auth_urlpatterns
