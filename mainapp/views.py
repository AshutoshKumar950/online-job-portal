from django.shortcuts import render, redirect
from .models import LoginInfo, JobSeeker, Enquiry
from django.contrib import messages
import datetime



# ==========================
# HOME PAGE
# ==========================

def index(request):

    return render(request, 'index.html')





# ==========================
# ABOUT PAGE
# ==========================

def about(request):

    return render(request, 'about.html')






# ==========================
# CONTACT PAGE
# ==========================

def contact(request):

    if request.method == "POST":


        name = request.POST.get("name")

        contactno = request.POST.get("contactno")

        email = request.POST.get("email")

        enquirytext = request.POST.get("Enquirytext")

        posteddate = datetime.datetime.today().strftime("%d/%m/%Y")



        enq = Enquiry(

            name=name,

            contactno=contactno,

            emailaddress=email,

            EnquiryText=enquirytext,

            posteddade=posteddate

        )


        enq.save()


        messages.success(
            request,
            "Enquiry is saved successfully"
        )


        return redirect("contact")



    return render(request, 'contact.html')








# ==========================
# JOB SEEKER REGISTER
# ==========================


def register(request):


    if request.method == "POST":


        name = request.POST.get("name")

        gender = request.POST.get("gender")

        contactno = request.POST.get("contactno")

        emailaddress = request.POST.get("emailaddress")

        qualification = request.POST.get("qualification")

        experience = request.POST.get("experience")

        keyskill = request.POST.get("keyskill")

        address = request.POST.get("address")

        password = request.POST.get("password")

        confirm_password = request.POST.get("confirm_password")





        # PASSWORD CHECK

        if password != confirm_password:


            messages.error(
                request,
                "Password and Confirm Password do not match"
            )


            return redirect("register")







        # DUPLICATE EMAIL CHECK


        if LoginInfo.objects.filter(
            username=emailaddress
        ).exists():


            messages.error(
                request,
                "Email already registered"
            )


            return redirect("register")







        # SAVE JOB SEEKER DETAILS


        js = JobSeeker(

            name=name,

            gender=gender,

            contactno=contactno,

            emailaddress=emailaddress,

            qualification=qualification,

            experience=experience,

            keyskill=keyskill,

            address=address

        )


        js.save()







        # SAVE LOGIN DETAILS


        li = LoginInfo(

            usertype="jobseeker",

            username=emailaddress,

            password=password

        )


        li.save()






        messages.success(
            request,
            "Registration is done successfully"
        )


        return redirect("login")





    return render(request,'register.html')









# ==========================
# LOGIN
# ==========================


def login(request):


    if request.method == "POST":


        username = request.POST.get("username")

        password = request.POST.get("password")



        try:


            user = LoginInfo.objects.get(

                username=username,

                password=password

            )




            if user.usertype == "admin":



                messages.success(
                    request,
                    "Welcome Admin"
                )


                request.session["adminid"] = user.username


                return redirect("admindash")







            elif user.usertype == "jobseeker":



                messages.success(
                    request,
                    "Welcome Job Seeker"
                )


                request.session["userid"] = user.username


                return redirect("userdash")







        except LoginInfo.DoesNotExist:


            messages.error(
                request,
                "Invalid username or password"
            )


            return redirect("login")





    return render(request,'login.html')

