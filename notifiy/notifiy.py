from trycourier import Courier
import os


class CourierNotification:

    def __init__(self) -> None:
        self.courier = Courier(auth_token=os.environ.get("COURIER_AUTH_TOKEN"))

    def send_notification(self, email: str, img: str, username: str):

        return self.courier.send_message(message={
            "to": {
                "email": email,
            },
            "template": os.environ.get("COURIER_TEMPLATE_ID"),
            "data": {
                "username": username,
                "img": img,
            },
        }
        )
