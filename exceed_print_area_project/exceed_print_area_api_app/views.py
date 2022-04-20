from django.shortcuts import render
from os.path import basename
from .script import check_out_of_bounds
from django.conf import settings
from django.http import response
import os, glob
from os import path
from zipfile import ZipFile
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import pdf_doc_table
import shutil
import datetime
import io
import fitz
from io import BytesIO
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','POST'])
def index(request):
    if request.method == "POST" and request.FILES:
        print("yes i am here")
        try:
             shutil.rmtree(r""+settings.MEDIA_ROOT)
        except Exception as dir_del_err:
            print("Error while trying to clean media folder--->", dir_del_err)
        try:
            file = request.FILES['file']
            print("FILE TYPE---->", type(file))
            pdf_file = pdf_doc_table(docfile=file)
            pdf_file.save()
            print("-------------FILE NAME FROM IT IS GETTING SAVED-------------")
            print(pdf_file.docfile.path)
            try: 
                output_faulty_pages = check_out_of_bounds(pdf_file.docfile.path)
            except Exception as Err:
                print("------ERROR in script-------")
                print(Err)
            context = {
                "faulty_pages": output_faulty_pages
            }
            return Response({"output":context})
        except Exception as err:
            print("-------------------->",err)
            return Response({"output":err})
    else:
        return Response({"output":"We have not found any file which is attached with form data!"})

    

