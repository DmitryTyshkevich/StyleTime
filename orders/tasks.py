from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def message_sending(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Онлайн-магазин "StyleTime"'
    message = f'Уважаемый {order.first_name}! \
            \nВы успешно разместили заказ! \
            \nВаш заказ №{order.id} \
            \nСпасибо за покупку, мы свяжемся с Вами в ближайшее время!'

    mail_sent = send_mail(
        subject,
        message,
        'tyshkevich.dima@mail.ru',
        [order.email]
    )
    return mail_sent
