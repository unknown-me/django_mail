from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from mail.api.serializers import SendMyMailSerializer
from mail.models import MyMailConfig, MyMailContent


class SendMyMail(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = SendMyMailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            mail_attachment = request.FILES.get('mail_attachment')
            try:
                if mail_attachment:
                    mail_attachment = request.FILES.get('mail_attachment')
                    mail_content_obj = MyMailContent.objects.create(mail_to=data['mail_to'],
                                                                    mail_content=data['mail_content'],
                                                                    mail_subject=data['mail_subject'],
                                                                    mail_attachment=mail_attachment)
                else:
                    mail_content_obj = MyMailContent.objects.create(mail_to=data['mail_to'],
                                                                    mail_content=data['mail_content'],
                                                                    mail_subject=data['mail_subject'])
            except Exception as e:
                return Response({'message': 'Exception ' + str(e)})
            my_config_obj = MyMailConfig.objects.all()[0]
            to = mail_content_obj.mail_to
            plain_message = None
            from_email = my_config_obj.email_id
            subject = mail_content_obj.mail_subject
            if mail_attachment:
                message_text = render_to_string('send_my_mail_attachment.html', {
                    'mail_to': mail_content_obj.mail_to,
                    'user': my_config_obj.email_id,
                    'content': mail_content_obj.mail_content,
                    'url': mail_content_obj.mail_attachment.url
                })
            else:
                message_text = render_to_string('send_my_mail.html', {
                    'mail_to': mail_content_obj.mail_to,
                    'user': my_config_obj.email_id,
                    'content': mail_content_obj.mail_content
                })
            send_mail(subject, plain_message, from_email, [to], html_message=message_text,
                      auth_user=my_config_obj.email_id,
                      auth_password=my_config_obj.email_password)
            return Response({'message': 'Mail sent successfully'})
