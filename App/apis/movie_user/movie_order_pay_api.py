from alipay import AliPay
from flask_restful import Resource

from App.apis.api_constant import HTTP_OK
from App.apis.movie_user.utils import login_required
from App.settings import ALIPAY_APPID, APP_PRIVATE_KEY, ALIPAY_PUBLIC_KEY


class MovieOrderPayResource(Resource):
    @login_required
    def get(self, order_id):
        alipay_client = AliPay(
            appid=ALIPAY_APPID,
            app_notify_url=None,
            app_private_key_string=APP_PRIVATE_KEY,
            alipay_public_key_string=ALIPAY_PUBLIC_KEY,
            sign_type="RSA",
            debug=False
        )

        subject = "i9 20核系列 RTX2080"

        order_string = alipay_client.api_alipay_trade_page_pay(
            out_trade_no="110",
            total_amount=10000,
            subject=subject,
            return_url="http://www.1000phone.com",
            notify_url="http://www.1000phone.com"
        )
        pay_url = "https://openapi.alipaydev.com/gateway.do?" + order_string
        data = {
            "msg": "ok",
            "status": HTTP_OK,
            "data": {
                "pay_url": pay_url,
                "order_id": order_id
            }
        }
        return data
