from rest_framework import serializers


class SendMyMailSerializer(serializers.Serializer):
    mail_to = serializers.EmailField(error_messages={"required": "mail_to key is required", "blank": "mail_to is required"})
    mail_content = serializers.CharField(error_messages={"required": "mail_content key is required", "blank": "mail_content is required"})
    mail_subject = serializers.CharField(error_messages={"required": "mail_subject key is required", "blank": "mail_subject is required"})
