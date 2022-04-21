from rest_framework.routers import DefaultRouter
from restql.rest.views import PizzaView, ToppingsView

router = DefaultRouter()

router.register('pizza', PizzaView)
router.register('toppings', ToppingsView)

urlpatterns = router.urls
