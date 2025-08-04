import os
from django.shortcuts import render, redirect
from .forms import MemberForm
from django.http import HttpResponse
from django.template import loader
from django.conf import settings

# def home(request):
#     return HttpResponse("Welcome to the Gym Management System!")
#
# def main(request):
#     # Debug information
#     print("Rendering index.html")
#     print(f"Current directory: {os.getcwd()}")
#     print(f"Template exists: {os.path.exists(os.path.join(settings.BASE_DIR, 'templates', 'index.html'))}")
#
#     # Add a simple context variable to test template rendering
#     context = {
#         'debug': True,
#         'message': 'This is a test message from the view.'
#     }
#     return render(request, 'index.html', context)
# # def register_member(request):
# #     try:
# #         if request.method =='POST':
# #             form = MemberForm(request.POST)
# #             if form.is_valid():
# #                 form.save()
# #                 return redirect('register_member')
# #             else:
# #                 form = MemberForm()
# #             return render(request, 'members/register_member.html', {'form': form})
# #
# #     except Exception as e:
# #         return HttpResponse(e)


def home(request):
    context = {
        'message': 'This is a test message from the view.'
    }
    return render(request, 'index.html', context)

def register_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_member')
    else:
        form = MemberForm()

    return render(request, 'members/register_member.html', {'form': form})
