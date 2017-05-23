from flask_mail import Mail, Message
from tcidatabase import models
from tcidatabase import db


def init_app(app):
    Postman.app = app
    Postman.mail = Mail(app)
    db.signals.post_save.connect(Postman.send_client_token,
                                 sender=models.SurveyToken)
    db.signals.post_save.connect(Postman.send_user_password,
                                 sender=models.User)


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

    @classmethod
    def send_user_password(cls, sender, document, created):
        email = document.email
        if not created or not email:
            return
        password = document.generate_password()
        msg = Message('Your TCI access', recipients=[email])
        msg.body = ('''
You can access the TCI on {url} with your email and
the following password: {pwd}'''.format(
            url=cls.app.config['TCI_PROFESSIONALS_URL'], pwd=password))
        cls.mail.send(msg)
        document.save()
