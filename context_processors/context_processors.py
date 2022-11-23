from core.models import Topic
from core.models import Message



def topics(request):
    topic = Topic.objects.all()
    return {'topics': topic}


def recent_activities(request):
    message = Message.objects.filter(status=True)
    return {'messages': message}    