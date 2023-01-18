from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from annomalies import models, serializers
from rest_framework import status


# Create your views here.

class issues(APIView):
    def get(self, request):
        all_issues=models.issues.objects.all()
        serializer=serializers.issuesSerializer(all_issues,many=True)
        return Response(serializer.data)

    def post(self, request):
        
        serializer=serializers.issuesSerializer(data=request.data)
        if serializer.is_valid():
            
            if models.issues.objects.filter(issue=request.data.get('issue')).exists():
                return Response ('The Annomaly issue already exists ')
            else:

                serializer.save()
                return Response('Annomalie Issue Saved Successfuly',status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        issue=models.issues.objects.get(pk=pk)
        serializer=serializers.issuesSerializer(issue,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ('Record updated successfuly', status=status.HTTP_200_OK)

        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        issue=models.issues.objects.get(pk=pk)
        issue.delete()
        return Response ('Entry deleted', status=status.HTTP_204_NO_CONTENT)

class parcel(APIView):
    def get(self, request):
        parcel=models.parcel.objects.all()
        serializer=serializers.parcelSerializer(parcel,many=True)
        return Response(serializer.data)

    def post(self, request):
        
        serializer=serializers.parcelSerializer(data=request.data)
        if serializer.is_valid():           

            if models.parcel.objects.filter(survey_parcel_no=request.data.get('survey_parcel_no')).exists():
                return Response ('The parcel already exists ')

            else :

                serializer.save()
                return Response('Parcel Saved Successfuly',status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        issue=models.parcel.objects.get(pk=pk)
        serializer=serializers.parcelSerializer(issue,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ('Parcel details updated successfuly', status=status.HTTP_200_OK)
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        issue=models.parcel.objects.get(pk=pk)
        issue.delete()
        return Response ('Entry deleted', status=status.HTTP_204_NO_CONTENT)


class issue_details(APIView):
    def get(self, request,pk):
        parcel=models.parcel.objects.filter(id=pk).first()
        parcel_info_serializer=serializers.parcelSerializer(parcel)
        parcel_detail=models.issue_details.objects.filter(parcel_id=pk)
        serializer=serializers.issueDetailsSerializer(parcel_detail,many=True)

        parcel_info=parcel_info_serializer.data
        parcel_info["issues"] = serializer.data
                
        data=[parcel_info]        
        
        return Response(data)

    def post(self, request):
        
        serializer=serializers.issueDetailsSerializer(data=request.data)
        if serializer.is_valid():            
            serializer.save()
            return Response('Anomally Saved Successfuly',status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        issue=models.issue_details.objects.get(pk=pk)
        serializer=serializers.issueDetailsSerializer(issue,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response ('Anomally details updated successfuly', status=status.HTTP_200_OK)

        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        issue=models.issue_details.objects.get(pk=pk)
        issue.delete()
        return Response ('Anomally Entry deleted', status=status.HTTP_204_NO_CONTENT)