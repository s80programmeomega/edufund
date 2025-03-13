from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from school.views import (
    FundingCampaignViewSet,
    RepresentativeViewSet,
    SchoolDocumentViewSet,
    SchoolImageViewSet,
    SchoolViewSet,
    StudentViewSet,
)
from users.views import UserViewSet

from sponsor.views import SponsorViewSet, SponsorRepresentativeViewSet, DonationViewSet

router = DefaultRouter()

# users routes
router.register("users", UserViewSet, basename="users")

# school routes
router.register("school", SchoolViewSet, basename="school")
router.register("representative", RepresentativeViewSet, basename="representative")
router.register("student", StudentViewSet, basename="student")
router.register("funding-campaign", FundingCampaignViewSet, basename="funding-campaign")
router.register("school-document", SchoolDocumentViewSet, basename="school-document")
router.register("school-image", SchoolImageViewSet, basename="school-image")

# sponsor routes
router.register("sponsor", SponsorViewSet, basename="sponsor")
router.register("sponsor-representative", SponsorRepresentativeViewSet, basename="sponsor-representative")
router.register("donation", DonationViewSet, basename="donation")


# Create a list of additional URL patterns for JWT
jwt_patterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]

# Combine router URLs and JWT URLs
urlpatterns = router.urls + jwt_patterns
