
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article
# Create your views here.


@api_view(['GET'])
def index(request):
    article = Article.objects.all()
    
    return Response(article)
