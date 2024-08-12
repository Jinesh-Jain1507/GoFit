import requests
import json
from django.shortcuts import render, redirect
from .forms import RegistrationForm, CustomAuthenticationForm, PromptForm, ExerciseForm, DateSelectionForm, UserProfileForm
from .models import Exercise, UserProfile
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from dotenv import load_dotenv
import os
import openai
from django.utils.timezone import now

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def workout_redirect(request):
    date = now().date()
    return redirect('workouts', date)

def workouts(request, date):
    if request.method == 'POST':
        eform = ExerciseForm(request.POST)
        if eform.is_valid():
            exercise = eform.save(commit=False)
            exercise.user = request.user
            exercise.save()
            return redirect('workout')
    else:
        dform = DateSelectionForm()
        eform = ExerciseForm()
        workouts = Exercise.objects.filter(date=date, user=request.user)
        if date == str(now().date()):
            add = True
        else:
            add = False
    return render(request, 'core/workouts.html', {'eform': eform,'dform': dform, 'workouts': workouts, 'add': add})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'core/register.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                user_login(request, user)
                # Redirect to a success page
                return redirect('home')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'core/login.html', {'form': form})

def logout(request):
    user_logout(request)
    return redirect('home')

def yoga(request):
    response = requests.get("https://yoga-api-nzy4.onrender.com/v1/poses")
    if response.status_code == 200:
        poses = response.json()
        return render(request, 'core/yogahome.html', {"poses":poses})

def yogaasana(request, id):
    response = requests.get(f"https://yoga-api-nzy4.onrender.com/v1/poses?id={id}")
    if response.status_code == 200:
        pose = response.json()
        pose['pose_benefits'] = [benefit.strip() for benefit in pose['pose_benefits'].strip('.').split('.')]
        return render(request, 'core/yoga.html', {"pose":pose})

def calories(request):
    if request.method == 'POST':
        load_dotenv()
        API_KEY = os.getenv("API_KEY", None)
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': API_KEY})
        print(query)
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception:
            api = "oops! There was an error"
        return render(request, 'core/calories.html', {'api': api})
    else:
        return render(request, 'core/calories.html', {'query': 'Enter a valid query'})
    
def chat(request):
    form = PromptForm(request.POST or None)
    response, prompt = None, None
    if request.method == 'POST' and form.is_valid():
        prompt = form.cleaned_data['prompt']
        response = get_openai_response(prompt)
        form = PromptForm()
    return render(request, 'core/chat.html', {'form': form, 'response': response, 'prompt': prompt})

def get_openai_response(prompt):
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY", None)
    openai.api_key = API_KEY
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()

def faq(request):
    return render(request, 'core/faq.html')

def contact(request):
    return render(request, 'core/contact.html')

def profile(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form =UserProfileForm(request.POST)
            if form.is_valid():
                details = form.save(commit=False)
                details.user = request.user
                details.save()
                profile = UserProfile.objects.filter(user = id)
                return redirect('profile', request.user)
            else:
                print("error")
        else:
            form = UserProfileForm()
            profile = UserProfile.objects.filter(user = id)
            print(profile[0])
        return render(request, 'core/profile.html', {'form': form, 'profile': profile[0]})
    else:
        return redirect('login')
    
def delete(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Exercise.objects.get(pk=id)
            pi.delete()
            id = request.user.id
            return redirect('workout')
        else:
            return redirect('home')

    else:
        return redirect('login')