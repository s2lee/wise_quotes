from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import WiseQuotesSerializer

from .models import WiseQuotes

	
@api_view(['GET'])
def get_wise_quotes_list(request):
	wisequotes = WiseQuotes.objects.all().order_by('-id')[:7]	
	serializer = WiseQuotesSerializer(wisequotes, many=True)
	return Response(serializer.data)

	
@api_view(['GET'])
def get_recommend_list(request):
	wisequotes = WiseQuotes.objects.all().order_by('-like','-id')[:7]
	serializer = WiseQuotesSerializer(wisequotes, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def detail_wise_quotes(request, pk):
	wisequotes = WiseQuotes.objects.get(id=pk)
	serializer = WiseQuotesSerializer(wisequotes, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def create_wise_quotes(request):
	serializer = WiseQuotesSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def update_wise_quotes(request, pk):
	wisequotes = WiseQuotes.objects.get(id=pk)
	serializer = WiseQuotesSerializer(instance=wisequotes, data=request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def delete_wise_quotes(request, pk):
	wisequotes = WiseQuotes.objects.get(id=pk)
	wisequotes.delete()

	return Response('Wise Quotes succsesfully delete!')


@api_view(['POST'])
def recommend_wise_quotes(request, pk):
	wisequotes = WiseQuotes.objects.get(id=pk)
	wisequotes.like += 1
	wisequotes.save()
	serializer = WiseQuotesSerializer(instance=wisequotes, data=request.data)
	if serializer.is_valid():		
		serializer.save()

	return Response(serializer.data)