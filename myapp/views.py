from django.shortcuts import render,redirect
from . models import Courses,Student,Teacher
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(req):
    return render(req,'home.html')


def about(req):
    return render(req,'about.html')


def services(req):
    return render(req,'services.html')

@login_required(login_url='login')
def teachers(req):
    teach = Teacher.objects.all()
    return render(req,'teachers.html',{'teach':teach})

@login_required(login_url='login')
def student_list(req):
    stud = Student.objects.all()
    return render(req,'stud_list.html',{'stud':stud})

@login_required(login_url='login')
def teacher(req):
    uid = req.user.id
    print(uid)
    teach = Teacher.objects.get(user=uid)
    print(teach)
    return render(req,'teacher.html',{'teach':teach})

def login(req):
    if req.method == "POST":    
        username = req.POST['uname'] 
        password = req.POST['password']
        user = auth.authenticate(username=username,password = password)
        if user is not None:
            
            auth.login(req,user)
            
            return redirect('home')
        else:
           
            return redirect('login')
    return render(req,'login.html')
def register(req):
    cor = Courses.objects.all()
    return render(req,'register.html',{'cor':cor})

def logout(req):
    auth.logout(req)
    return redirect('home')

def course(req):
    return render(req,'course.html')

def coursedb(req):
    if req.method == "POST":
        cname = req.POST['cname']    
        cfee = req.POST['cfee'] 
        cor = Courses(Course_Name=cname,Course_Fee=cfee)
        cor.save()
        return redirect('home')
    return render(req,'course.html')

def students(req):
    cour = Courses.objects.all()
    if req.method == "POST":
        fname = req.POST['fname']    
        lname = req.POST['lname']     
        age = req.POST['age']     
        email = req.POST['email']    
        number = req.POST['number']     
        address = req.POST['addr']    
        id = req.POST['sel']    
        cor = Courses.objects.get(id=id)
        stud = Student(Stu_Lname = lname,Stu_Fname = fname,Stu_Age = age,Stu_Email = email,Stu_Number = number,Stu_Address = address,Stu_Course = cor)
        stud.save()
        return redirect('student_list')
    return render(req,'student.html',{'cor':cour})

def registerdb(req):
    if req.method == "POST":
        fname = req.POST['fname']    
        lname = req.POST['lname']    
        uname = req.POST['uname']    
        age = req.POST['age']    
        password = req.POST['password']    
        email = req.POST['email']    
        number = req.POST['number']    
        image = req.FILES['image']    
        password = req.POST['password']    
        cpassword = req.POST['cpassword']
        address = req.POST['addr']    
        id = req.POST['sel']    
        cor = Courses.objects.get(id=id) 
        if password == cpassword:
            auser = User.objects.create_user(first_name = fname,last_name = lname,password = password,username = uname,email = email,)
            auser.save()
            print(auser.username)
            t_user = User.objects.get(username = uname)
            teacher = Teacher(user = t_user,course = cor,Teach_Age = age,Teach_Number = number,Teach_Address = address,Teach_Image =image)
            print("saved")    
            teacher.save()
        
            return redirect('home')
    return render(req,'register.html')

def stud_edit(req,id):
    cour = Courses.objects.all()
    stud = Student.objects.get(id=id)
    if req.method == "POST":
        stud.Stu_Fname = req.POST['fname']    
        stud.Stu_Lname = req.POST['lname']     
        stud.Stu_Age = req.POST['age']     
        stud.Stu_Email = req.POST['email']    
        stud.Stu_Number = req.POST['number']     
        stud.Stu_Address = req.POST['addr']    
        id = req.POST['sel']    
        stud.Stu_Course = Courses.objects.get(id=id)
        stud.save()
        return redirect('student_list')
    return render(req,'editstud.html',{'cor':cour,'s':stud})

def edit(req,id):
    cor = Courses.objects.all()
    teach = Teacher.objects.get(user=id)
    u = User.objects.get(id=id)
    if req.method == 'POST':
        u.first_name = req.POST['fname']    
        u.last_name = req.POST['lname']    
        u.username = req.POST['uname']    
        teach.Teach_Age = req.POST['age']   
        u.email = req.POST['email']    
        teach.Teach_Number = req.POST['number']    
        teach.Teach_Image = req.FILES['image']
        teach.Teach_Address = req.POST['addr']    
        cid = req.POST['sel']    
        cor = Courses.objects.get(id=cid) 
        teach.course = cor
        teach.save()
        u.save()
        return redirect('home')
    return render(req,'edit.html',{'teach':teach,'cor':cor})
    
def delete(req,id):
    teach = Teacher.objects.get(user=id)
    teach.delete()
    auth_user = User.objects.get(id=id)
    auth_user.delete()
    return redirect('teachers')

def stud_delete(req,id):
    stud = Student.objects.get(id=id)
    stud.delete()
    return redirect('student_list')