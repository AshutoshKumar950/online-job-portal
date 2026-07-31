from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.cache import cache_control
import datetime


from mainapp.models import JobSeeker, LoginInfo, Enquiry
from .models import JobInfo
from userapp.models import Response


# ==========================
# ADMIN DASHBOARD
# ==========================
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admindash(request):
    try:
        if request.session['adminid']:

            context = {
                "total_jobseekers": JobSeeker.objects.count(),
                "total_jobs": JobInfo.objects.count(),
                "posted_jobs": JobInfo.objects.count(),
                "enquiries": Enquiry.objects.count(),
                "feedback": Response.objects.filter(responsetype="feed").count(),
                "complaints": Response.objects.filter(responsetype="comp").count(),
            }

            return render(request, "admindash.html", context)

    except KeyError:
        messages.error(request, "Please login first!!")
        return redirect("login")


# ==========================
# ADMIN LOGOUT
# ==========================
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminlogout(request):
    try:
        if request.session['adminid']:
            del request.session['adminid']
            messages.success(request, "You have logged out successfully.")
            return redirect("login")

    except KeyError:
        messages.error(request, "Please login first!!")
        return redirect("login")


# ==========================
# JOB SEEKERS
# ==========================
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def jobseeker(request):
    try:
        if request.session['adminid']:
            js = JobSeeker.objects.all()
            return render(request, "jobseeker.html", {"js": js})

    except KeyError:
        messages.error(request, "Please login first!!")
        return redirect("login")


# ==========================
# POST JOB
# ==========================
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def postjob(request):
    try:
        if request.session['adminid']:

            if request.method == "POST":

                title = request.POST.get("title")
                description = request.POST.get("description")
                location = request.POST.get("location")
                salary = request.POST.get("salary")
                jobtype = request.POST.get("jobtype")
                lastdate = request.POST.get("lastdate")

                posteddate = datetime.date.today().strftime("%d/%m/%Y")

                JobInfo.objects.create(
                    title=title,
                    description=description,
                    location=location,
                    salary=salary,
                    jobtype=jobtype,
                    lastdata=lastdate,
                    posteddate=posteddate,
                )

                messages.success(request, "Job posted successfully.")
                return redirect("postjob")

            return render(request, "postjob.html")

    except KeyError:
        messages.error(request, "Please login first!!")
        return redirect("login")


# ==========================
# POSTED JOBS
# ==========================
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def postedjob(request):
    try:
        if request.session['adminid']:
            ji = JobInfo.objects.all()
            return render(request, "postedjob.html", {"ji": ji})

    except KeyError:
        messages.error(request, "Please login first!!")
        return redirect("login")


# ==========================
# ENQUIRIES
# ==========================
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def enquiries(request):
    try:
        if request.session['adminid']:
            enq = Enquiry.objects.all()
            return render(request, "enquiries.html", {"enq": enq})

    except KeyError:
        messages.error(request, "Please login first!!")
        return redirect("login")


# ==========================
# CHANGE PASSWORD
# ==========================
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def changeadminpwd(request):
    try:
        if request.session['adminid']:

            if request.method == "POST":

                oldpassword = request.POST.get("oldpassword")
                newpassword = request.POST.get("newpassword")
                confirmpassword = request.POST.get("confirmpassword")

                if newpassword != confirmpassword:
                    messages.error(request, "New Password and Confirm Password do not match.")
                    return redirect("changeadminpwd")

                try:
                    LoginInfo.objects.get(
                        username=request.session['adminid'],
                        password=oldpassword
                    )

                    LoginInfo.objects.filter(
                        username=request.session['adminid']
                    ).update(password=newpassword)

                    messages.success(request, "Password changed successfully.")
                    return redirect("adminlogout")

                except LoginInfo.DoesNotExist:
                    messages.error(request, "Old password is incorrect.")
                    return redirect("changeadminpwd")

            return render(request, "changeadminpwd.html")

    except KeyError:
        messages.error(request, "Please login first!!")
        return redirect("login")


# ==========================
# FEEDBACK
# ==========================
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewfeedback(request):
    try:
        if request.session['adminid']:
            res = Response.objects.filter(responsetype="feed")
            return render(request, "viewfeedback.html", {"res": res})

    except KeyError:
        messages.error(request, "Please login first!!")
        return redirect("login")


# ==========================
# COMPLAINTS
# ==========================
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewcomplaint(request):
    try:
        if request.session['adminid']:
            res = Response.objects.filter(responsetype="comp")
            return render(request, "viewcomplaint.html", {"res": res})

    except KeyError:
        messages.error(request, "Please login first!!")
        return redirect("login")


# ==========================
# DELETE ENQUIRY
# ==========================
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deleteenq(request, id):
    try:
        if request.session['adminid']:
            enq = Enquiry.objects.get(id=id)
            enq.delete()
            messages.success(request, "Enquiry deleted successfully.")
            return redirect("enquiries")

    except KeyError:
        messages.error(request, "Please login first!!")
        return redirect("login")