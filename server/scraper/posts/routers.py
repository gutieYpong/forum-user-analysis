from rest_framework.routers import SimpleRouter

from .viewsets import LihkgSonListRetrieveViewSet, PostListRetrieveViewSet, CommentListRetrieveViewSet


router = SimpleRouter()

# POSTS
router.register(r'users', LihkgSonListRetrieveViewSet, basename='users')
router.register(r'posts', PostListRetrieveViewSet, basename='posts')
router.register(r'comments', CommentListRetrieveViewSet, basename='comments')

urlpatterns = [
    *router.urls
]
