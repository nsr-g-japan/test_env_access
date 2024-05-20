from django.shortcuts import render
from django.http import HttpResponse
import environ
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os

# Create your views here.
# # Initialize environment variables
env = environ.Env()
environ.Env.read_env()  # reads the .env file


# Load database connection details from environment variables
gl_db_server = env('HOST_SERVER_NAME')
gl_db_name = env('HOST_DB_NAME')
gl_db_username = env('HOST_DB_USERNAME')
gl_db_password = env('HOST_DB_PASSWORD')


@api_view(['GET'])
def get_record(request):

    print(gl_db_server, gl_db_username, gl_db_password, gl_db_name)
    suc_resp = {"data": [gl_db_server, gl_db_username, gl_db_password, gl_db_name]}
    return Response(suc_resp, status=200)

