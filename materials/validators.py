from rest_framework.serializers import ValidationError

links = ['http://www.youtube.com/watch?v=', 'http://www.youtube.com/watch?v=', 'http://youtu.be']
def validate_links(value):
    if value not in links:
        raise ValidationError('Ссылка должна содержать ссылку на YouTube.')