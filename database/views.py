from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import User,Stain, Tissue, Slide,Gender,System, Diagnosis, Comment,Title
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def tissue_filter(request, system):
    print(system)
    if system == "all":
        system_selected = Tissue.objects.all()
    else:
        system_id = System.objects.get(system_type = system)
        system_selected = Tissue.objects.filter(system = system_id).order_by('tissue_type')
    return JsonResponse([each_entry.serialize() for each_entry in system_selected], safe=False)

@csrf_exempt
def comment(request, slide_id):
    comment_user = User.objects.get(id = request.user.id)
    comment_slide = Slide.objects.get(id = slide_id)
    data = json.loads(request.body)
    comment_body = data.get("comment", "")
    if comment_body != "": 
        new_comments = Comment.objects.create(person= comment_user, slide=comment_slide, comment = comment_body)    
    comments = Comment.objects.filter(slide = slide_id).order_by("-id")
    return JsonResponse([comment.serialize() for comment in comments], safe=False)

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        id_max = Slide.objects.all().count()
        gender_options = Gender.objects.all()
        stain_options = Stain.objects.all().order_by("stain_type")
        tissue_options = Tissue.objects.all().order_by("tissue_type")
        systems_options = System.objects.all().order_by("system_type")
        diagnosis_options = Diagnosis.objects.all().order_by("WHO_diagnosis")
        filter_results = ""
        #search algorith boi
        filter_list ={}
        try:
            id = request.GET["id"]
            if id != '':
                int_id = int(id)
                filter_list['id'] = int_id

            min = request.GET['min_age']
            if min != '':
                filter_list['age__gte'] = min
            
            max = request.GET['max_age']
            if max != '':
                filter_list['age__lte'] = max

            gender = request.GET["gender"]
            if gender != 'all':
                filter_list['gender'] = Gender.objects.get(gender_type = gender)

            stain = request.GET["stain"]
            if stain != 'all':
                filter_list['stain'] = Stain.objects.get(stain_type = stain)

            tissue = request.GET["tissue"]
            if tissue != 'all':
                filter_list['tissue'] = Tissue.objects.get(tissue_type = tissue)
            else:
                system = request.GET["system"]  
                if system != 'all':
                    system_selected = System.objects.get(system_type = system)
                    tissues_in_system = Tissue.objects.filter(system = system_selected)
                    tissue_list = []
                    for each_tissue in tissues_in_system:
                        tissue_list.append(each_tissue)
            try:
                # with tissue and system search
                filter_results = Slide.objects.filter(**filter_list).filter(tissue__in=tissue_list).order_by('-id')
            except:
                # without
                filter_results = Slide.objects.filter(**filter_list).order_by('-id')

        finally:
            return render(request, "database/index.html",
            {
            "id_max":id_max, 
            "gender_options":gender_options,
            "stain_options":stain_options,
            "system_options":systems_options,
            "tissue_options":tissue_options,
            "diagnosis_options":diagnosis_options,
            "results": filter_results
            })
    else:
        #return HttpResponseRedirect(reverse("login"))
        return render(request, "database/login.html")

def image_page(request,id):
    slide = Slide.objects.get(pk = id)
    comments = Comment.objects.filter(slide = slide).order_by("-id")
    return render(request, "database/image.html",{"image":slide,"comments":comments})

def profile_page(request,id):
    person = User.objects.get(id = id)
    titles = Title.objects.all()
    if request.method == "POST":
        message = ""
        if "username" in request.POST:
            username = request.POST["username"]
            title = request.POST["title"]
            title_id = Title.objects.get(title_type = title)
            firstname = request.POST["firstname"]
            surname = request.POST["surname"]
            email = request.POST["email"]
            update = User.objects.filter(id = id).update(username=username, title = title_id, first_name = firstname, last_name = surname, email = email)
            message = f"Details for {username} updated"
            person.refresh_from_db()
            return render(request, "database/profile.html",{"person":person, "titles":titles, "message":message})
        elif "passone" in request.POST:
            passone = request.POST["passone"]
            passtwo = request.POST["passtwo"]
            if passone != passtwo:
                message = "NO CHANGES SAVED AS PASSWORDS DIFFERENT"
                return render(request, "database/profile.html",{"person":person, "titles":titles, "message":message})
            else:
                new_pword = User.objects.get(id=id)
                new_pword.set_password(passone)
                new_pword.save()
                message = f"Password for {new_pword} has sucessfully been changed"
                return render(request, "database/login.html", {'login_message':message})
        person.refresh_from_db()
        return render(request, "database/profile.html",{"person":person, "titles":titles, "message":message})
        #return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "database/profile.html",{"person":person, "titles":titles})

def signup(request):
    titles = Title.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        passone = request.POST["passone"]
        passtwo = request.POST["passtwo"]
        already_in_db = User.objects.filter(username= username)
        if len(already_in_db) > 0:
            message = f"Username '{username}' already taken, please use another userneame"
            return render(request, "database/signup.html", {"titles":titles, "message":message})
        elif passone != passtwo:
            message = "NO CHANGES SAVED AS PASSWORDS DIFFERENT"
            return render(request, "database/signup.html", {"titles":titles, "message":message})
        else:
            title = request.POST["title"]
            title_id = Title.objects.get(title_type = title)
            firstname = request.POST["firstname"]
            surname = request.POST["surname"]
            email = request.POST["email"]
            sign_up = request.POST["sign_up"]
            #create_user sorts password hashing
            new_user = User.objects.create_user(username=username, password=passone,title=title_id, 
                                                first_name=firstname, last_name=surname, 
                                                email=email, signup=sign_up)
            new_user.save()
            message = f"User {username} successfully signed up to HistoSearch"
            return render(request, "database/signup.html", {"titles":titles, "message":message})
    else:
        return render(request, "database/signup.html", {"titles":titles})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            message = "Username or Password incorrect"
            return render(request, "database/login.html", {'login_message':message})
    # if just get request
    else:
        return render(request, "database/login.html")

def logout_view(request):
    logout(request)
    message = "You have sucessfully logged out"
    return render(request, "database/login.html", {'login_message':message})

