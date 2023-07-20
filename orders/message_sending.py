from django.core.mail import send_mail


def message_sending(order):
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
