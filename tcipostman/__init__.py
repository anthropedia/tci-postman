from flask_mail import Mail, Message
from tcidatabase import models
from tcidatabase import db


def init_app(app):
    Postman.app = app
    Postman.mail = Mail(app)
    db.signals.post_save.connect(Postman.send_client_token,
                                 sender=models.SingleToken)


class Postman:
    app = None
    mail = None

    @classmethod
    def send_client_token(cls, sender, document, created):
        recipient = document.client.email
        if recipient and created:
            msg = Message('A test is available', recipients=[recipient])
            msg.body = ('A test is pending on {}'.format(
                        cls.app.config['TCI_TEST_URL'].format(
                            token=document.key)))
            cls.mail.send(msg)
