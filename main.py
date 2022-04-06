
from ev_setting import app as fastApp
from address import views as address_views
fastApp.include_router(address_views.router,
                    tags=["address"],
                       prefix="/address",
                    responses={404: {"error": "address router missing"}},
)