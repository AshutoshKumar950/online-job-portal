from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.cache import cache_control
from mainapp.models import JobSeeker, LoginInfo
from adminapp.models import JobInfo
from .models import Response
import datetime


# ==========================
# USER DASHBOARD
# ==========================
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def userdash(request):
    try:
        if request.session['userid']:

            js = JobSeeker.objects.get(
                emailaddress=request.session['userid']
            )

            context = {
                "js": js,
                "total_jobs": JobInfo.objects.count(),
                "responses": Response.objects.filter(
                    contactno=js.contactno
                ).count(),
            }

            return render(request, "userdash.html", context)

    except KeyError:
        messages.error(request, "Please login first!!")
        return redirect("login")


# ==========================
# USER LOGOUT
# ==========================
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def userlogout(request):
    try:
        if request.session['userid']:
            del request.session['userid']
            messages.success(request, "Logged out successfully.")
            return redirect("login")

    except KeyError:
        messages.error(request, "Please login first!!")
        return redirect("login")


# ==========================
# VIEW JOBS
# ==========================
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewjobs(request):
    try:
        if request.session['userid']:

            js = JobSeeker.objects.get(
                emailaddress=request.session['userid']
            )

            ji = JobInfo.objects.all()

            return render(request, "viewjobs.html", {
                "js": js,
                "ji": ji
            })

    except KeyError:
        messages.error(request, "Please login first!!")
        return redirect("login")


# ==========================
# VIEW PROFILE
# ==========================
# ==========================
# VIEW PROFILE
# ==========================
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewprofile(request):
    try:
        if request.session['userid']:

            js = JobSeeker.objects.get(
                emailaddress=request.session['userid']
            )

            if request.method == "POST":

                js.name = request.POST.get("name")
                js.fathername = request.POST.get("fathername")
                js.gender = request.POST.get("gender")
                js.contactno = request.POST.get("contactno")
                js.qualification = request.POST.get("qualification")
                js.address = request.POST.get("address")

                js.save()

                messages.success(request, "Profile updated successfully.")

                return redirect("viewprofile")

            return render(request, "viewprofile.html", {
                "js": js
            })

    except JobSeeker.DoesNotExist:
        messages.error(request, "Profile not found.")
        return redirect("userdash")

    except KeyError:
        messages.error(request, "Please login first!!")
        return redirect("login")


# ==========================
# VIEW RESPONSE
# ==========================
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewresponse(request):
    try:
        if request.session['userid']:

            js = JobSeeker.objects.get(
                emailaddress=request.session['userid']
            )

            res = Response.objects.filter(
                contactno=js.contactno
            )

            return render(request, "viewresponse.html", {
                "res": res,
                "js": js
            })

    except KeyError:
        messages.error(request, "Please login first!!")
        return redirect("login")


# ==========================
# CHANGE PASSWORD
# ==========================
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def changeuserpwd(request):
    try:
        if request.session['userid']:

            if request.method == "POST":

                oldpassword = request.POST.get("oldpassword")
                newpassword = request.POST.get("newpassword")
                confirmpassword = request.POST.get("confirmpassword")

                if newpassword != confirmpassword:
                    messages.error(request, "Passwords do not match.")
                    return redirect("changeuserpwd")

                try:
                    LoginInfo.objects.get(
                        username=request.session['userid'],
                        password=oldpassword
                    )

                    LoginInfo.objects.filter(
                        username=request.session['userid']
                    ).update(password=newpassword)

                    messages.success(request, "Password changed successfully.")
                    return redirect("userlogout")

                except LoginInfo.DoesNotExist:
                    messages.error(request, "Old password is incorrect.")
                    return redirect("changeuserpwd")

            return render(request, "changeuserpwd.html")

    except KeyError:
        messages.error(request, "Please login first!!")
        return redirect("login")


# ==========================
# GIVE RESPONSE
# ==========================
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def giveresponse(request):
    try:
        if request.session['userid']:

            js = JobSeeker.objects.get(
                emailaddress=request.session['userid']
            )

            if request.method == "POST":

                responsetype = request.POST.get("responsetype")
                subject = request.POST.get("subject")
                responsetext = request.POST.get("responsetext")

                Response.objects.create(
                    name=js.name,
                    contactno=js.contactno,
                    responsetype=responsetype,
                    subject=subject,
                    responsetext=responsetext,
                    posteddate=datetime.datetime.today().strftime("%d/%m/%Y")
                )

                messages.success(request, "Response submitted successfully.")
                return redirect("giveresponse")

            return render(request, "giveresponse.html", {
                "js": js
            })

    except KeyError:
        messages.error(request, "Please login first!!")
        return redirect("login")