from flask import Flask,render_template,request, flash,redirect, url_for, jsonify,send_file
from config_file import client
from models import *
import secrets
import datetime
from bson import ObjectId
# from datetime import datetime
from random import randint
import os

import json

app = Flask(__name__)

app.secret_key='my_key'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','mp4','csv','xlsx'}




UPLOAD_NOMINATE_PIC = 'static/images/online_voting/nominates_pics'
app.config['UPLOAD_NOMINATE_PIC']=UPLOAD_NOMINATE_PIC

@app.route('/online_voting/nominates_pics/<filename>')
def send_uploaded_file_nominate_profile_pic(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["UPLOAD_NOMINATE_PIC"], filename)


@app.route("/",methods=['POST','GET'])
def onlineVotingPage():
    emailId = request.form.get('emailId')
    password = request.form.get('password')

    if emailId and password and request.method=='POST':
        try:
            get_logins = VotingAdminDetails.objects.get(emailId__iexact=emailId,password__exact=password,status__in=[1])
            if get_logins:
                votingAdminRefLink = get_logins.votingAdminRefLink
                return redirect(url_for('onlineVotingDashboardPage',votingAdminRefLink=votingAdminRefLink))
            else:
                flash("Invalid Credentials!!!")
                return render_template("online_voting/voting_admin_login.html")
        except VotingAdminDetails.DoesNotExist as e:
            flash("Invalid Credentials!!!")
            return render_template("online_voting/voting_admin_login.html")

    return render_template('online_voting/voting_admin_login.html')

@app.route("/votingAdminRegister",methods=['POST','GET'])
def votingAdminRegisterPage():
    fullName = request.form.get("fullName")
    emailId = request.form.get("emailId")
    phoneNumber = request.form.get("phoneNumber")
    password = request.form.get("password")
    votingAdminRefLink = secrets.token_urlsafe()
    createdOn = datetime.datetime.now()
    status = 1

    if request.method == 'POST':
        voting_admin = VotingAdminDetails(
            fullName=fullName,
            emailId=emailId,
            phoneNumber=phoneNumber,
            password=password,
            votingAdminRefLink=votingAdminRefLink,
            createdOn=createdOn,
            status=status
            )
        voting_admin_details = voting_admin.save()
        if voting_admin_details:
            flash("Successfully Admin Added !!!")
            return redirect(url_for('onlineVotingPage'))
        else:
            flash("Required fields are missing !")
            return render_template('online_voting/voting_admin_register.html')
    else:
        return render_template('online_voting/voting_admin_register.html')


@app.route("/addNominate/<votingAdminRefLink>",methods=['POST','GET'])
def addNominatePage(votingAdminRefLink):
    nominateName = request.form.get("nominateName")
    nominateClass = request.form.get('nominateClass')
    nominatePosition= request.form.get('nominatePosition')
    nominateRefLink = secrets.token_urlsafe()
    nominateGender = request.form.get('nominateGender')
    add_nominate_details=""
    file_name=""
    if request.method == 'POST':


        get_vote_admin = VotingAdminDetails.objects.get(votingAdminRefLink=votingAdminRefLink)
        nominateCode = request.form.get('nominateCode')
        if nominatePosition == "Captain":
            captainCode = nominatePosition+"-"+nominateCode
            try:
                queryset = NominateCandidateDetails.objects(nominateCode__iexact=captainCode)
                if queryset:
                    flash("Already "+captainCode+" assigned to someone!!!")
                    return render_template('/online_voting/add_nominate.html')
            except Exception as e:
                pass
            add_nominate = NominateCandidateDetails(
                nominateCode=captainCode,
                votingAdminRefLink =get_vote_admin.votingAdminRefLink,
                votingAdminFullName = get_vote_admin.fullName
                )
            add_nominate_details = add_nominate.save()
            

        elif nominatePosition == "Vice-Captain":
            viceCaptainCode = nominatePosition+"-"+nominateCode
            try:
                queryset = NominateCandidateDetails.objects(nominateCode__iexact=viceCaptainCode)
                if queryset:
                    flash("Already "+viceCaptainCode+" assigned to someone!!!")
                    return render_template('/online_voting/add_nominate.html')
            except Exception as e:
                pass
            add_nominate = NominateCandidateDetails(
                nominateCode=viceCaptainCode,
                votingAdminRefLink =get_vote_admin.votingAdminRefLink,
                votingAdminFullName = get_vote_admin.fullName
                )
            add_nominate_details = add_nominate.save()

        elif nominatePosition == "Lateral-Captain":
            lateralCaptainCode = nominatePosition+"-"+nominateCode
            try:
                queryset = NominateCandidateDetails.objects(nominateCode__iexact=lateralCaptainCode)
                if queryset:
                    flash("Already "+lateralCaptainCode+" assigned to someone!!!")
                    return render_template('/online_voting/add_nominate.html')
            except Exception as e:
                pass
            add_nominate = NominateCandidateDetails(
                nominateCode=lateralCaptainCode,
                votingAdminRefLink =get_vote_admin.votingAdminRefLink,
                votingAdminFullName = get_vote_admin.fullName
                )
            add_nominate_details = add_nominate.save()

        elif nominatePosition == "Lateral-ViceCaptain":
            lateralViceCaptainCode = nominatePosition+"-"+nominateCode
            try:
                queryset = NominateCandidateDetails.objects(nominateCode__iexact=lateralViceCaptainCode)
                if queryset:
                    flash("Already "+lateralViceCaptainCode+" assigned to someone!!!")
                    return render_template('/online_voting/add_nominate.html')
            except Exception as e:
                pass
            add_nominate = NominateCandidateDetails(
                nominateCode=lateralViceCaptainCode,
                votingAdminRefLink =get_vote_admin.votingAdminRefLink,
                votingAdminFullName = get_vote_admin.fullName
                )
            add_nominate_details = add_nominate.save()

        elif nominatePosition == "Sport-Captain":
            sportCaptainCode = nominatePosition+"-"+nominateCode
            try:
                queryset = NominateCandidateDetails.objects(nominateCode__iexact=sportCaptainCode)
                if queryset:
                    flash("Already "+sportCaptainCode+" assigned to someone!!!")
                    return render_template('/online_voting/add_nominate.html')
            except Exception as e:
                pass
            add_nominate = NominateCandidateDetails(
                nominateCode=sportCaptainCode,
                votingAdminRefLink =get_vote_admin.votingAdminRefLink,
                votingAdminFullName = get_vote_admin.fullName
                )
            add_nominate_details = add_nominate.save()
            
        elif nominatePosition == "Sport-ViceCaptain":
            sportViceCaptainCode = nominatePosition+"-"+nominateCode
            try:
                queryset = NominateCandidateDetails.objects(nominateCode__iexact=sportViceCaptainCode)
                if queryset:
                    flash("Already "+sportViceCaptainCode+" assigned to someone!!!")
                    return render_template('/online_voting/add_nominate.html')
            except Exception as e:
                pass
            add_nominate = NominateCandidateDetails(
                nominateCode=sportViceCaptainCode,
                votingAdminRefLink =get_vote_admin.votingAdminRefLink,
                votingAdminFullName = get_vote_admin.fullName
                )
            add_nominate_details = add_nominate.save()
            
        elif nominatePosition == "Cultural-Captain":
            culturalCaptainCode = nominatePosition+"-"+nominateCode
            try:
                queryset = NominateCandidateDetails.objects(nominateCode__iexact=culturalCaptainCode)
                if queryset:
                    flash("Already "+culturalCaptainCode+" assigned to someone!!!")
                    return render_template('/online_voting/add_nominate.html')
            except Exception as e:
                pass
            add_nominate = NominateCandidateDetails(
                nominateCode=culturalCaptainCode,
                votingAdminRefLink =get_vote_admin.votingAdminRefLink,
                votingAdminFullName = get_vote_admin.fullName
                )
            add_nominate_details = add_nominate.save()
            
        elif nominatePosition == "Cultural-ViceCaptain":
            culturalViceCaptainCode = nominatePosition+"-"+nominateCode
            try:
                queryset = NominateCandidateDetails.objects(nominateCode__iexact=culturalViceCaptainCode)
                if queryset:
                    flash("Already "+culturalViceCaptainCode+" assigned to someone!!!")
                    return render_template('/online_voting/add_nominate.html')
            except Exception as e:
                pass
            add_nominate = NominateCandidateDetails(
                nominateCode=culturalViceCaptainCode,
                votingAdminRefLink =get_vote_admin.votingAdminRefLink,
                votingAdminFullName = get_vote_admin.fullName
                )
            add_nominate_details = add_nominate.save()
        elif nominatePosition == "None":
            add_nominate = NominateCandidateDetails(
                nominateCode=None,
                votingAdminRefLink =get_vote_admin.votingAdminRefLink,
                votingAdminFullName = get_vote_admin.fullName
                )
            add_nominate_details = add_nominate.save()
        if add_nominate_details:
            updated_nominate = add_nominate_details.update(
                nominateName = nominateName,
                nominateClass = nominateClass,
                nominatePosition = nominatePosition,
                nominateRefLink = nominateRefLink,
                nominateGender = nominateGender,
                createdOn = datetime.datetime.now(),
                status = 1
                )


        nominate_id = str(add_nominate_details.id)
        if nominate_id:
            nominateProfilePic = request.files['nominateProfilePic']
            if nominateProfilePic.filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS:
                ext = nominateProfilePic.filename.rsplit('.',1)[1].lower()
                file_name = str(nominate_id)+"."+ext
                if not os.path.exists(app.config['UPLOAD_NOMINATE_PIC']):
                    os.mkdir(app.config['UPLOAD_NOMINATE_PIC'])
                nom_profile = app.config['UPLOAD_NOMINATE_PIC']
                nominateProfilePic.save(os.path.join(nom_profile,file_name))
            add_nominate_details.update(nominateProfilePic=file_name)
        if add_nominate_details:
            # flash("Successfully Added Nominated Person !")
            return redirect(url_for('viewNominatePage',votingAdminRefLink=votingAdminRefLink))
    return render_template('/online_voting/add_nominate.html')

@app.route("/viewNominates/<votingAdminRefLink>",methods=['POST','GET'])
def viewNominatePage(votingAdminRefLink):
    nominate_dict={}
    nominate_list=[]
    get_nominate_details = NominateCandidateDetails.objects(status__in=[1]).all()
    if get_nominate_details:
        for nd in get_nominate_details:
            nominate_dict={
                "nominateName":nd.nominateName,
                "nominateCode":nd.nominateCode,
                "nominateClass":nd.nominateClass,
                "nominatePosition":nd.nominatePosition,
                "nominateRefLink":nd.nominateRefLink,
                "nominateGender":nd.nominateGender,
                "nomProPic":nd.nominateProfilePic
            }
            nominate_list.append(nominate_dict)

    return render_template('/online_voting/nominates_view.html',nominate_list=nominate_list)


@app.route("/viewVotersList/<votingAdminRefLink>",methods=['POST','GET'])
def viewVotersListPage(votingAdminRefLink):
    voter_list = []
    voter_dict = {}
    get_voters = VotersDetails.objects(status__in=[1],voterStatus__in=[0,1]).all()
    count=0
    if get_voters:
        for gv in get_voters:
            count=count+1
            voter_dict ={
                "sno":count,
                "fullName":gv.fullName,
                "emailId" :gv.emailId,
                "phoneNumber":gv.phoneNumber,
                "className":gv.className,
                "voterId":gv.voterId,
                "voterStatus":gv.voterStatus,
                # "votedDate":gv.votedOn.strftime("%m/%d/%Y"),
                # "votedTime":gv.votedOn.strftime("%H:%M:%S")
            }
            voter_list.append(voter_dict)
    return render_template("/online_voting/voters_list.html",voter_list=voter_list)

@app.route("/viewVotersCastList/<votingAdminRefLink>",methods=['POST','GET'])
def viewVotersCastListPage(votingAdminRefLink):
    voter_cast_list = []
    voter_cast_dict = {}
    get_cast_voters = VotersDetails.objects(status__in=[1],voterStatus__in=[1]).all()
    count=0
    
    if get_cast_voters:

        for gv in get_cast_voters:
            count=count+1
            voter_cast_dict ={
                "sno":count,
                "fullName":gv.fullName,
                "emailId" :gv.emailId,
                "phoneNumber":gv.phoneNumber,
                "className":gv.className,
                "voterId":gv.voterId,
                "voterStatus":gv.voterStatus,
                "votedDate":gv.votedOn.strftime("%m/%d/%Y"),
                "votedTime":gv.votedOn.strftime("%H:%M:%S")
            }
            voter_cast_list.append(voter_cast_dict)

    return render_template("/online_voting/voters_cast_list.html",voter_cast_list=voter_cast_list)

@app.route("/viewVotersCastNotDoneList/<votingAdminRefLink>",methods=['POST','GET'])
def viewVotersCastNotDoneListPage(votingAdminRefLink):
    voter_not_cast_list = []
    voter_not_cast_dict = {}
    get_not_cast_voters = VotersDetails.objects(status__in=[1],voterStatus__in=[0]).all()
    count=0
    
    if get_not_cast_voters:

        for gv in get_not_cast_voters:
            count=count+1
            voter_not_cast_dict ={
                "sno":count,
                "fullName":gv.fullName,
                "emailId" :gv.emailId,
                "phoneNumber":gv.phoneNumber,
                "className":gv.className,
                "voterId":gv.voterId,
                "voterStatus":gv.voterStatus,
                
            }
            voter_not_cast_list.append(voter_not_cast_dict)

    return render_template("/online_voting/voter_not_cast_done.html",voter_not_cast_list=voter_not_cast_list)

@app.route("/onlineVotingDashboard/<votingAdminRefLink>",methods=['POST','GET'])
def onlineVotingDashboardPage(votingAdminRefLink):
    get_voting_details ={}
    nominate_count = NominateCandidateDetails.objects(status__in=[1]).count()
    voters_count = VotersDetails.objects(status__in=[1],voterStatus__in=[0,1]).count()
    cast_voters = VotersDetails.objects(status__in=[1],voterStatus__in=[1]).count()
    not_cast_voters = VotersDetails.objects(status__in=[1],voterStatus__in=[0]).count()
    if request.method=='GET':
        get_voting_admin = VotingAdminDetails.objects.get(votingAdminRefLink=votingAdminRefLink)
        get_voting_details = {
            "votingAdminRefLink":get_voting_admin.votingAdminRefLink,
            "nominateCount":nominate_count,
            "votersCount":voters_count,
            "castVoteCount":cast_voters,
            "notCastCount":not_cast_voters
        }
    return render_template('/online_voting/voting_dashboard.html',get_voting=get_voting_details)

@app.route("/votersDashboard",methods=['POST','GET'])
def votersDashboardPage():
    return render_template('/online_voting/voters_dashboard.html')

@app.route("/viewNominateList",methods=['POST','GET'])
def viewNominateListPage():
    nominate_dict={}
    nominate_list=[]
    get_nominate_details = NominateCandidateDetails.objects(status__in=[1]).all()
    if get_nominate_details:
        for nd in get_nominate_details:
            nominate_dict={
                "nominateName":nd.nominateName,
                "nominateCode":nd.nominateCode,
                "nominateClass":nd.nominateClass,
                "nominatePosition":nd.nominatePosition,
                "nominateRefLink":nd.nominateRefLink,
                "nominateGender":nd.nominateGender,
                "nomProPic":nd.nominateProfilePic
            }
            nominate_list.append(nominate_dict)

    return render_template('/online_voting/nominates_view.html',nominate_list=nominate_list)

@app.route("/voterRegister",methods=['POST','GET'])
def voterRegisterPage():
    import random
    fullName = request.form.get('fullName')
    emailId = request.form.get('emailId')
    phoneNumber = request.form.get('phoneNumber')
    password = request.form.get('password')
    className = request.form.get('className')
    voterRefLink = secrets.token_urlsafe()
    voteNum = random.randint(1000,9999)
    createdOn = datetime.datetime.now()
    voterStatus = 0
    status = 1

    if request.method=='POST':
        try:
            queryset = VotersDetails.objects(emailId__iexact=emailId)
            if queryset:
                flash("Email already Exists!!!")
                return render_template("/online_voting/voter_register.html")
        except Exception as e:
            pass

        try:
            queryset = VotersDetails.objects(phoneNumber__iexact=phoneNumber)
            if queryset:
                flash("Phone Number already Exists!!!")
                return render_template("/online_voting/voter_register.html")
        except Exception as e:
            pass
        add_voters = VotersDetails(
            fullName=fullName,
            emailId=emailId,
            phoneNumber=phoneNumber,
            password=password,
            className=className,
            createdOn=createdOn,
            status=status,
            voterRefLink=voterRefLink,
            voterId='CA'+className+str(voteNum),
            voterStatus=voterStatus
            )
        add_voters_details=add_voters.save()
        if add_voters_details:
            flash("Successfully applied for vote !!")
            return redirect(url_for('voterLoginPage'))
    else:
        return render_template('/online_voting/voter_register.html')

@app.route("/voterLogin",methods=['POST','GET'])
def voterLoginPage():
    voterId = request.form.get('voterId')
    password = request.form.get('password')
    print(voterId,password)
    if voterId and password and request.method=='POST':
        try:
            get_logins = VotersDetails.objects.get(voterId__exact=voterId,password__exact=password,status__in=[1])
            if get_logins:
                voterRefLink = get_logins.voterRefLink
                return redirect(url_for('castVotePage',voterRefLink=voterRefLink))
            else:
                flash("Invalid Credentials!!!")
                return render_template("/online_voting/voter_login.html")
        except VotersDetails.DoesNotExist as e:
            flash("Invalid Credentials!!!")
            return render_template("/online_voting/voter_login.html")

    return render_template('/online_voting/voter_login.html')

@app.route("/castVote/<voterRefLink>",methods=['POST','GET'])
def castVotePage(voterRefLink):
    nominate_list=[]
    nominate_dict={}
    voter_status=None
    cast_vote=""
    cast_vote_update =""
    get_nominate = NominateCandidateDetails.objects(status__in=[1])
    if get_nominate and request.method=='GET':    
        for gn in get_nominate:
            nominate_dict = {
                "nominateName":gn.nominateName,
                "nominateCode":gn.nominateCode,
                "nominatePosition":gn.nominatePosition
            }
            nominate_list.append(nominate_dict)
    # get_all_nominate_details = NominateCandidateDetails.objects.get(nominateCode=gn.nominateCode)
    get_voter_details = VotersDetails.objects.get(voterRefLink=voterRefLink,status__in=[1])
    if get_voter_details.voterStatus == 0:

        get_nominate_cap = NominateCandidateDetails.objects(status__in=[1],nominatePosition__in=['Captain'])
        captain = request.form.get('captain')
        
        for cc in get_nominate_cap:
            get_nominate_cap = NominateCandidateDetails.objects.get(nominateCode=cc.nominateCode,nominatePosition__in=['Captain'])
            if captain == get_nominate_cap.nominateName:
                cast_vote= CastVoters(
                    voterName = get_voter_details.fullName,
                    voterRefLink = get_voter_details.voterRefLink,
                    voterId = get_voter_details.voterId,
                    className = get_voter_details.className,
                    captain = captain,
                    captainCode = cc.nominateCode,
                    captainRefLink = cc.nominateRefLink,
                    
                    
                    )
                cast_vote_update = cast_vote.save()
        if captain == "Nota":
            cast_vote=CastVoters(
                voterName = get_voter_details.fullName,
                voterRefLink = get_voter_details.voterRefLink,
                voterId = get_voter_details.voterId,
                captain = captain,
                )
            cast_vote_update = cast_vote.save()

        get_nominate_vc = NominateCandidateDetails.objects(status__in=[1],nominatePosition__in=['Vice-Captain'])
        viceCaptain = request.form.get('viceCaptain')
        for vc in get_nominate_vc:
            get_nominate_vc = NominateCandidateDetails.objects.get(nominateCode=vc.nominateCode,nominatePosition__in=['Vice-Captain'])
            if viceCaptain == get_nominate_vc.nominateName:
                cast_vote = cast_vote_update.update(
                    viceCaptain = viceCaptain,
                    viceCaptainCode = vc.nominateCode,
                    viceCaptainRefLink = vc.nominateRefLink
                    )
        if viceCaptain == "Nota":
            cast_vote = cast_vote_update.update(
                viceCaptain = viceCaptain            
                )

        get_nominate_lc = NominateCandidateDetails.objects(status__in=[1],nominatePosition__in=['Lateral-Captain'])
        lateralCaptain = request.form.get('lateralCaptain')
        for lc in get_nominate_lc:
            get_nominate_lc = NominateCandidateDetails.objects.get(nominateCode=lc.nominateCode,nominatePosition__in=['Lateral-Captain'])
            if lateralCaptain == get_nominate_lc.nominateName:
                cast_vote = cast_vote_update.update(
                    lateralCaptain = lateralCaptain,
                    lateralCaptainCode = lc.nominateCode,
                    lateralCaptainRefLink = lc.nominateRefLink
                    )
        if lateralCaptain == "Nota":
            cast_vote = cast_vote_update.update(
                lateralCaptain = lateralCaptain            
                )

        get_nominate_lvc = NominateCandidateDetails.objects(status__in=[1],nominatePosition__in=['Lateral-ViceCaptain'])
        lateralViceCaptain = request.form.get('lateralViceCaptain')
        for lvc in get_nominate_lvc:
            get_nominate_lvc = NominateCandidateDetails.objects.get(nominateCode=lvc.nominateCode,nominatePosition__in=['Lateral-ViceCaptain'])
            if lateralViceCaptain == get_nominate_lvc.nominateName:
                cast_vote = cast_vote_update.update(
                    lateralViceCaptain = lateralViceCaptain,
                    lateralViceCaptainCode = lvc.nominateCode,
                    lateralViceCaptainRefLink = lvc.nominateRefLink
                    )
        if lateralViceCaptain == "Nota":
            cast_vote = cast_vote_update.update(
                lateralViceCaptain = lateralViceCaptain            
                )

        get_nominate_sc = NominateCandidateDetails.objects(status__in=[1],nominatePosition__in=['Sport-Captain'])
        sportCaptain = request.form.get('sportCaptain')
        
        for sc in get_nominate_sc:
            get_nominate_sc = NominateCandidateDetails.objects.get(nominateCode=sc.nominateCode,nominatePosition__in=['Sport-Captain'])
            if sportCaptain == get_nominate_sc.nominateName:
                cast_vote = cast_vote_update.update(
                    sportCaptain = sportCaptain,
                    sportCaptainCode = sc.nominateCode,
                    sportCaptainRefLink = sc.nominateRefLink
                    )

        if sportCaptain == "Nota":
            cast_vote = cast_vote_update.update(
                sportCaptain = sportCaptain            
                )



        get_nominate_svc = NominateCandidateDetails.objects(status__in=[1],nominatePosition__in=['Sport-ViceCaptain'])
        sportViceCaptain = request.form.get('sportViceCaptain')
        for svc in get_nominate_svc:
            get_nominate_svc = NominateCandidateDetails.objects.get(nominateCode=svc.nominateCode,nominatePosition__in=['Sport-ViceCaptain'])
            if sportViceCaptain == get_nominate_svc.nominateName:
                cast_vote = cast_vote_update.update(
                    sportViceCaptain = sportViceCaptain,
                    sportViceCaptainCode = svc.nominateCode,
                    sportViceCaptainRefLink = svc.nominateRefLink
                    )
        if sportViceCaptain == "Nota":
            cast_vote = cast_vote_update.update(
                sportViceCaptain = sportViceCaptain            
                )

        get_nominate_ccc = NominateCandidateDetails.objects(status__in=[1],nominatePosition__in=['Cultural-Captain'])
        culturalCaptain = request.form.get('culturalCaptain')
        for cc in get_nominate_ccc:
            get_nominate_ccc = NominateCandidateDetails.objects.get(nominateCode=cc.nominateCode,nominatePosition__in=['Cultural-Captain'])
            if culturalCaptain == get_nominate_ccc.nominateName:
                cast_vote = cast_vote_update.update(
                    culturalCaptain = culturalCaptain,
                    culturalCaptainCode = cc.nominateCode,
                    culturalCaptainRefLink = cc.nominateRefLink
                    )
        if culturalCaptain == "Nota":
            cast_vote = cast_vote_update.update(
                culturalCaptain = culturalCaptain            
                )

        get_nominate_cvc = NominateCandidateDetails.objects(status__in=[1],nominatePosition__in=['Cultural-ViceCaptain'])
        culturalViceCaptain = request.form.get('culturalViceCaptain')
        for cc in get_nominate_cvc:
            get_nominate_cvc = NominateCandidateDetails.objects.get(nominateCode=cc.nominateCode,nominatePosition__in=['Cultural-ViceCaptain'])
            if culturalViceCaptain == get_nominate_cvc.nominateName:
                cast_vote = cast_vote_update.update(
                    culturalViceCaptain = culturalViceCaptain,
                    culturalViceCaptainCode = cc.nominateCode,
                    culturalViceCaptainRefLink = cc.nominateRefLink,
                    createdOn = datetime.datetime.now(),
                    status = 1
                    )
        if culturalViceCaptain == "Nota":
            cast_vote = cast_vote_update.update(
                culturalViceCaptain = culturalViceCaptain,
                createdOn = datetime.datetime.now(),
                status = 1           
                )
        if cast_vote_update:
            update_cast_voter = get_voter_details.update(
                voterStatus=1,
                votedOn = datetime.datetime.now())
            flash("Successfully Cast Your Vote Done!!")
            return redirect(url_for('castVotePage',voterRefLink=voterRefLink))

    elif get_voter_details.voterStatus == 1:
        return render_template('/online_voting/cast_vote_done.html')
    return render_template('/online_voting/cast_vote.html',nominate_list=nominate_list,voter_status=voter_status)

@app.route("/viewVotingResults/<votingAdminRefLink>",methods=['POST','GET'])
def viewVotingResultsPage(votingAdminRefLink):
    # caption_data = [10,20,30]
    captain_data=[]
    captains = []
    vice_captain_data =[]
    vice_captains =[]
    lateral_captain_data = []
    lateral_captains = []
    lateral_vice_captain_data = []
    lateral_vice_captains =[]
    sport_captain_data =[]
    sport_captains = []
    sport_vice_captain_data =[]
    sport_vice_captains = []
    cultural_captain_data =[]
    cultural_captains = []
    cultural_vice_captain_data =[]
    cultural_vice_captains = []

    if request.method == 'GET':
        get_captain=NominateCandidateDetails.objects.filter(nominatePosition__in=['Captain'])

        captain_count = 0        
        for cc in get_captain:
            captains.append(cc.nominateName)
            if cc.nominateCode == "Captain-01":
                get_votes_count = CastVoters.objects.filter(captainCode__in=[cc.nominateCode]).count()
                captain_data.append(get_votes_count)
            elif cc.nominateCode == "Captain-02":
                get_votes_count = CastVoters.objects.filter(captainCode__in=[cc.nominateCode]).count()
                captain_data.append(get_votes_count)
            elif cc.nominateCode == "Captain-03":
                get_votes_count = CastVoters.objects.filter(captainCode__in=[cc.nominateCode]).count()
                captain_data.append(get_votes_count)
            elif cc.nominateCode == "Captain-04":
                get_votes_count = CastVoters.objects.filter(captainCode__in=[cc.nominateCode]).count()
                captain_data.append(get_votes_count)
            elif cc.nominateCode == "Captain-05":
                get_votes_count = CastVoters.objects.filter(captainCode__in=[cc.nominateCode]).count()
                captain_data.append(get_votes_count)
            elif cc.nominateCode == "Captain-06":
                get_votes_count = CastVoters.objects.filter(captainCode__in=[cc.nominateCode]).count()
                captain_data.append(get_votes_count)
            elif cc.nominateCode == "Captain-07":
                get_votes_count = CastVoters.objects.filter(captainCode__in=[cc.nominateCode]).count()
                captain_data.append(get_votes_count)
            elif cc.nominateCode == "Captain-08":
                get_votes_count = CastVoters.objects.filter(captainCode__in=[cc.nominateCode]).count()
                captain_data.append(get_votes_count)
            elif cc.nominateCode == "Captain-09":
                get_votes_count = CastVoters.objects.filter(captainCode__in=[cc.nominateCode]).count()
                captain_data.append(get_votes_count)
            elif cc.nominateCode == "Captain-10":
                get_votes_count = CastVoters.objects.filter(captainCode__in=[cc.nominateCode]).count()
                captain_data.append(get_votes_count)

        get_vice_caption = NominateCandidateDetails.objects.filter(nominatePosition__in=['Vice-Captain'])
        vice_caption_count = 0
        for vc in get_vice_caption:
            vice_captains.append(vc.nominateName)
            if vc.nominateCode == "Vice-Captain-01":
                get_vc_votes_count = CastVoters.objects.filter(viceCaptainCode__in=[vc.nominateCode]).count()
                vice_captain_data.append(get_vc_votes_count)
            elif vc.nominateCode == "Vice-Captain-02":
                get_vc_votes_count = CastVoters.objects.filter(viceCaptainCode__in=[vc.nominateCode]).count()
                vice_captain_data.append(get_vc_votes_count)
            elif vc.nominateCode == "Vice-Captain-03":
                get_vc_votes_count = CastVoters.objects.filter(viceCaptainCode__in=[vc.nominateCode]).count()
                vice_captain_data.append(get_vc_votes_count)
            elif vc.nominateCode == "Vice-Captain-04":
                get_vc_votes_count = CastVoters.objects.filter(viceCaptainCode__in=[vc.nominateCode]).count()
                vice_captain_data.append(get_vc_votes_count)
            elif vc.nominateCode == "Vice-Captain-05":
                get_vc_votes_count = CastVoters.objects.filter(viceCaptainCode__in=[vc.nominateCode]).count()
                vice_captain_data.append(get_vc_votes_count)
            elif vc.nominateCode == "Vice-Captain-06":
                get_vc_votes_count = CastVoters.objects.filter(viceCaptainCode__in=[vc.nominateCode]).count()
                vice_captain_data.append(get_vc_votes_count)
            elif vc.nominateCode == "Vice-Captain-07":
                get_vc_votes_count = CastVoters.objects.filter(viceCaptainCode__in=[vc.nominateCode]).count()
                vice_captain_data.append(get_vc_votes_count)
            elif vc.nominateCode == "Vice-Captain-08":
                get_vc_votes_count = CastVoters.objects.filter(viceCaptainCode__in=[vc.nominateCode]).count()
                vice_captain_data.append(get_vc_votes_count)
            elif vc.nominateCode == "Vice-Captain-09":
                get_vc_votes_count = CastVoters.objects.filter(viceCaptainCode__in=[vc.nominateCode]).count()
                vice_captain_data.append(get_vc_votes_count)
            elif vc.nominateCode == "Vice-Captain-10":
                get_vc_votes_count = CastVoters.objects.filter(viceCaptainCode__in=[vc.nominateCode]).count()
                vice_captain_data.append(get_vc_votes_count)
            
        get_lateral_captain = NominateCandidateDetails.objects.filter(nominatePosition__in=['Lateral-Captain'])
        lateral_captain_count = 0
        for lc in get_lateral_captain:
            lateral_captains.append(lc.nominateName)
            if lc.nominateCode == "Lateral-Captain-01":
                get_lc_votes_count = CastVoters.objects.filter(lateralCaptainCode__in=[lc.nominateCode]).count()
                lateral_captain_data.append(get_lc_votes_count)
            elif lc.nominateCode == "Lateral-Captain-02":
                get_lc_votes_count = CastVoters.objects.filter(lateralCaptainCode__in=[lc.nominateCode]).count()
                lateral_captain_data.append(get_lc_votes_count)
            elif lc.nominateCode == "Lateral-Captain-03":
                get_lc_votes_count = CastVoters.objects.filter(lateralCaptainCode__in=[lc.nominateCode]).count()
                lateral_captain_data.append(get_lc_votes_count)
            elif lc.nominateCode == "Lateral-Captain-04":
                get_lc_votes_count = CastVoters.objects.filter(lateralCaptainCode__in=[lc.nominateCode]).count()
                lateral_captain_data.append(get_lc_votes_count)
            elif lc.nominateCode == "Lateral-Captain-05":
                get_lc_votes_count = CastVoters.objects.filter(lateralCaptainCode__in=[lc.nominateCode]).count()
                lateral_captain_data.append(get_lc_votes_count)
            elif lc.nominateCode == "Lateral-Captain-06":
                get_lc_votes_count = CastVoters.objects.filter(lateralCaptainCode__in=[lc.nominateCode]).count()
                lateral_captain_data.append(get_lc_votes_count)
            elif lc.nominateCode == "Lateral-Captain-07":
                get_lc_votes_count = CastVoters.objects.filter(lateralCaptainCode__in=[lc.nominateCode]).count()
                lateral_captain_data.append(get_lc_votes_count)
            elif lc.nominateCode == "Lateral-Captain-08":
                get_lc_votes_count = CastVoters.objects.filter(lateralCaptainCode__in=[lc.nominateCode]).count()
                lateral_captain_data.append(get_lc_votes_count)
            elif lc.nominateCode == "Lateral-Captain-09":
                get_lc_votes_count = CastVoters.objects.filter(lateralCaptainCode__in=[lc.nominateCode]).count()
                lateral_captain_data.append(get_lc_votes_count)
            elif lc.nominateCode == "Lateral-Captain-10":
                get_lc_votes_count = CastVoters.objects.filter(lateralCaptainCode__in=[lc.nominateCode]).count()
                lateral_captain_data.append(get_lc_votes_count)

        get_lateral_vice_captain = NominateCandidateDetails.objects.filter(nominatePosition__in=['Lateral-ViceCaptain'])
        lateral_vice_captain_count = 0
        for lvc in get_lateral_vice_captain:
            lateral_vice_captains.append(lvc.nominateName)
            if lvc.nominateCode == "Lateral-ViceCaptain-01":
                get_lvc_votes_count = CastVoters.objects.filter(lateralViceCaptainCode__in=[lvc.nominateCode]).count()
                lateral_vice_captain_data.append(get_lvc_votes_count)
            elif lvc.nominateCode == "Lateral-ViceCaptain-02":
                get_lvc_votes_count = CastVoters.objects.filter(lateralViceCaptainCode__in=[lvc.nominateCode]).count()
                lateral_vice_captain_data.append(get_lvc_votes_count)
            elif lvc.nominateCode == "Lateral-ViceCaptain-03":
                get_lvc_votes_count = CastVoters.objects.filter(lateralViceCaptainCode__in=[lvc.nominateCode]).count()
                lateral_vice_captain_data.append(get_lvc_votes_count)
            elif lvc.nominateCode == "Lateral-ViceCaptain-04":
                get_lvc_votes_count = CastVoters.objects.filter(lateralViceCaptainCode__in=[lvc.nominateCode]).count()
                lateral_vice_captain_data.append(get_lvc_votes_count)
            elif lvc.nominateCode == "Lateral-ViceCaptain-05":
                get_lvc_votes_count = CastVoters.objects.filter(lateralViceCaptainCode__in=[lvc.nominateCode]).count()
                lateral_vice_captain_data.append(get_lvc_votes_count)
            elif lvc.nominateCode == "Lateral-ViceCaptain-06":
                get_lvc_votes_count = CastVoters.objects.filter(lateralViceCaptainCode__in=[lvc.nominateCode]).count()
                lateral_vice_captain_data.append(get_lvc_votes_count)
            elif lvc.nominateCode == "Lateral-ViceCaptain-07":
                get_lvc_votes_count = CastVoters.objects.filter(lateralViceCaptainCode__in=[lvc.nominateCode]).count()
                lateral_vice_captain_data.append(get_lvc_votes_count)
            elif lvc.nominateCode == "Lateral-ViceCaptain-08":
                get_lvc_votes_count = CastVoters.objects.filter(lateralViceCaptainCode__in=[lvc.nominateCode]).count()
                lateral_vice_captain_data.append(get_lvc_votes_count)
            elif lvc.nominateCode == "Lateral-ViceCaptain-09":
                get_lvc_votes_count = CastVoters.objects.filter(lateralViceCaptainCode__in=[lvc.nominateCode]).count()
                lateral_vice_captain_data.append(get_lvc_votes_count)
            elif lvc.nominateCode == "Lateral-ViceCaptain-10":
                get_lvc_votes_count = CastVoters.objects.filter(lateralViceCaptainCode__in=[lvc.nominateCode]).count()
                lateral_vice_captain_data.append(get_lvc_votes_count)
        get_sport_captain = NominateCandidateDetails.objects.filter(nominatePosition__in=['Sport-Captain'])
        sport_captain_count = 0
        for scc in get_sport_captain:
            sport_captains.append(scc.nominateName)
            if scc.nominateCode == "Sport-Captain-01":
                get_scc_votes_count = CastVoters.objects.filter(sportCaptainCode__in=[scc.nominateCode]).count()
                sport_captain_data.append(get_scc_votes_count)
            elif scc.nominateCode == "Sport-Captain-02":
                get_scc_votes_count = CastVoters.objects.filter(sportCaptainCode__in=[scc.nominateCode]).count()
                sport_captain_data.append(get_scc_votes_count)
            elif scc.nominateCode == "Sport-Captain-03":
                get_scc_votes_count = CastVoters.objects.filter(sportCaptainCode__in=[scc.nominateCode]).count()
                sport_captain_data.append(get_scc_votes_count)
            elif scc.nominateCode == "Sport-Captain-04":
                get_scc_votes_count = CastVoters.objects.filter(sportCaptainCode__in=[scc.nominateCode]).count()
                sport_captain_data.append(get_scc_votes_count)
            elif scc.nominateCode == "Sport-Captain-05":
                get_scc_votes_count = CastVoters.objects.filter(sportCaptainCode__in=[scc.nominateCode]).count()
                sport_captain_data.append(get_scc_votes_count)
            elif scc.nominateCode == "Sport-Captain-06":
                get_scc_votes_count = CastVoters.objects.filter(sportCaptainCode__in=[scc.nominateCode]).count()
                sport_captain_data.append(get_scc_votes_count)
            elif scc.nominateCode == "Sport-Captain-07":
                get_scc_votes_count = CastVoters.objects.filter(sportCaptainCode__in=[scc.nominateCode]).count()
                sport_captain_data.append(get_scc_votes_count)
            elif scc.nominateCode == "Sport-Captain-08":
                get_scc_votes_count = CastVoters.objects.filter(sportCaptainCode__in=[scc.nominateCode]).count()
                sport_captain_data.append(get_scc_votes_count)
            elif scc.nominateCode == "Sport-Captain-09":
                get_scc_votes_count = CastVoters.objects.filter(sportCaptainCode__in=[scc.nominateCode]).count()
                sport_captain_data.append(get_scc_votes_count)
            elif scc.nominateCode == "Sport-Captain-10":
                get_scc_votes_count = CastVoters.objects.filter(sportCaptainCode__in=[scc.nominateCode]).count()
                sport_captain_data.append(get_scc_votes_count)
        
        get_sport_vice_captain = NominateCandidateDetails.objects.filter(nominatePosition__in=['Sport-ViceCaptain'])
        sport_vice_captain_count = 0
        for svc in get_sport_vice_captain:
            sport_vice_captains.append(svc.nominateName)
            if svc.nominateCode == "Sport-ViceCaptain-01":
                get_svc_votes_count = CastVoters.objects.filter(sportViceCaptainCode__in=[svc.nominateCode]).count()
                sport_vice_captain_data.append(get_svc_votes_count)
            elif svc.nominateCode == "Sport-ViceCaptain-02":
                get_svc_votes_count = CastVoters.objects.filter(sportViceCaptainCode__in=[svc.nominateCode]).count()
                sport_vice_captain_data.append(get_svc_votes_count)
            elif svc.nominateCode == "Sport-ViceCaptain-03":
                get_svc_votes_count = CastVoters.objects.filter(sportViceCaptainCode__in=[svc.nominateCode]).count()
                sport_vice_captain_data.append(get_svc_votes_count)
            elif svc.nominateCode == "Sport-ViceCaptain-04":
                get_svc_votes_count = CastVoters.objects.filter(sportViceCaptainCode__in=[svc.nominateCode]).count()
                sport_vice_captain_data.append(get_svc_votes_count)
            elif svc.nominateCode == "Sport-ViceCaptain-05":
                get_svc_votes_count = CastVoters.objects.filter(sportViceCaptainCode__in=[svc.nominateCode]).count()
                sport_vice_captain_data.append(get_svc_votes_count)
            elif svc.nominateCode == "Sport-ViceCaptain-06":
                get_svc_votes_count = CastVoters.objects.filter(sportViceCaptainCode__in=[svc.nominateCode]).count()
                sport_vice_captain_data.append(get_svc_votes_count)
            elif svc.nominateCode == "Sport-ViceCaptain-07":
                get_svc_votes_count = CastVoters.objects.filter(sportViceCaptainCode__in=[svc.nominateCode]).count()
                sport_vice_captain_data.append(get_svc_votes_count)
            elif svc.nominateCode == "Sport-ViceCaptain-08":
                get_svc_votes_count = CastVoters.objects.filter(sportViceCaptainCode__in=[svc.nominateCode]).count()
                sport_vice_captain_data.append(get_svc_votes_count)
            elif svc.nominateCode == "Sport-ViceCaptain-09":
                get_svc_votes_count = CastVoters.objects.filter(sportViceCaptainCode__in=[svc.nominateCode]).count()
                sport_vice_captain_data.append(get_svc_votes_count)
            elif svc.nominateCode == "Sport-ViceCaptain-10":
                get_svc_votes_count = CastVoters.objects.filter(sportViceCaptainCode__in=[svc.nominateCode]).count()
                sport_vice_captain_data.append(get_svc_votes_count)
            
        get_cultral_captain = NominateCandidateDetails.objects.filter(nominatePosition__in=['Cultural-Captain'])
        cultral_captain_count = 0
        for gcc in get_cultral_captain:
            cultural_captains.append(gcc.nominateName)
            if gcc.nominateCode == "Cultural-Captain-01":
                get_cc_votes_count = CastVoters.objects.filter(culturalCaptainCode__in=[gcc.nominateCode]).count()
                cultural_captain_data.append(get_cc_votes_count)
            elif gcc.nominateCode == "Cultural-Captain-02":
                get_cc_votes_count = CastVoters.objects.filter(culturalCaptainCode__in=[gcc.nominateCode]).count()
                cultural_captain_data.append(get_cc_votes_count)
            elif gcc.nominateCode == "Cultural-Captain-03":
                get_cc_votes_count = CastVoters.objects.filter(culturalCaptainCode__in=[gcc.nominateCode]).count()
                cultural_captain_data.append(get_cc_votes_count)
            elif gcc.nominateCode == "Cultural-Captain-04":
                get_cc_votes_count = CastVoters.objects.filter(culturalCaptainCode__in=[gcc.nominateCode]).count()
                cultural_captain_data.append(get_cc_votes_count)
            elif gcc.nominateCode == "Cultural-Captain-05":
                get_cc_votes_count = CastVoters.objects.filter(culturalCaptainCode__in=[gcc.nominateCode]).count()
                cultural_captain_data.append(get_cc_votes_count)
            elif gcc.nominateCode == "Cultural-Captain-06":
                get_cc_votes_count = CastVoters.objects.filter(culturalCaptainCode__in=[gcc.nominateCode]).count()
                cultural_captain_data.append(get_cc_votes_count)
            elif gcc.nominateCode == "Cultural-Captain-07":
                get_cc_votes_count = CastVoters.objects.filter(culturalCaptainCode__in=[gcc.nominateCode]).count()
                cultural_captain_data.append(get_cc_votes_count)
            elif gcc.nominateCode == "Cultural-Captain-08":
                get_cc_votes_count = CastVoters.objects.filter(culturalCaptainCode__in=[gcc.nominateCode]).count()
                cultural_captain_data.append(get_cc_votes_count)
            elif gcc.nominateCode == "Cultural-Captain-09":
                get_cc_votes_count = CastVoters.objects.filter(culturalCaptainCode__in=[gcc.nominateCode]).count()
                cultural_captain_data.append(get_cc_votes_count)
            elif gcc.nominateCode == "Cultural-Captain-10":
                get_cc_votes_count = CastVoters.objects.filter(culturalCaptainCode__in=[gcc.nominateCode]).count()
                cultural_captain_data.append(get_cc_votes_count)


        get_vice_cultral_captain = NominateCandidateDetails.objects.filter(nominatePosition__in=['Cultural-ViceCaptain'])
        cultral_vice_captain_count = 0
        for gcvc in get_vice_cultral_captain:
            cultural_vice_captains.append(gcvc.nominateName)
            if gcvc.nominateCode == "Cultural-ViceCaptain-01":
                get_cvc_votes_count = CastVoters.objects.filter(culturalViceCaptainCode__in=[gcvc.nominateCode]).count()
                cultural_vice_captain_data.append(get_cvc_votes_count)
            elif gcvc.nominateCode == "Cultural-ViceCaptain-02":
                get_cvc_votes_count = CastVoters.objects.filter(culturalViceCaptainCode__in=[gcvc.nominateCode]).count()
                cultural_vice_captain_data.append(get_cvc_votes_count)
            elif gcvc.nominateCode == "Cultural-ViceCaptain-03":
                get_cvc_votes_count = CastVoters.objects.filter(culturalViceCaptainCode__in=[gcvc.nominateCode]).count()
                cultural_vice_captain_data.append(get_cvc_votes_count)
            elif gcvc.nominateCode == "Cultural-ViceCaptain-04":
                get_cvc_votes_count = CastVoters.objects.filter(culturalViceCaptainCode__in=[gcvc.nominateCode]).count()
                cultural_vice_captain_data.append(get_cvc_votes_count)
            elif gcvc.nominateCode == "Cultural-ViceCaptain-05":
                get_cvc_votes_count = CastVoters.objects.filter(culturalViceCaptainCode__in=[gcvc.nominateCode]).count()
                cultural_vice_captain_data.append(get_cvc_votes_count)
            elif gcvc.nominateCode == "Cultural-ViceCaptain-06":
                get_cvc_votes_count = CastVoters.objects.filter(culturalViceCaptainCode__in=[gcvc.nominateCode]).count()
                cultural_vice_captain_data.append(get_cvc_votes_count)
            elif gcvc.nominateCode == "Cultural-ViceCaptain-07":
                get_cvc_votes_count = CastVoters.objects.filter(culturalViceCaptainCode__in=[gcvc.nominateCode]).count()
                cultural_vice_captain_data.append(get_cvc_votes_count)
            elif gcvc.nominateCode == "Cultural-ViceCaptain-08":
                get_cvc_votes_count = CastVoters.objects.filter(culturalViceCaptainCode__in=[gcvc.nominateCode]).count()
                cultural_vice_captain_data.append(get_cvc_votes_count)
            elif gcvc.nominateCode == "Cultural-ViceCaptain-09":
                get_cvc_votes_count = CastVoters.objects.filter(culturalViceCaptainCode__in=[gcvc.nominateCode]).count()
                cultural_vice_captain_data.append(get_cvc_votes_count)
            elif gcvc.nominateCode == "Cultural-ViceCaptain-10":
                get_cvc_votes_count = CastVoters.objects.filter(culturalViceCaptainCode__in=[gcvc.nominateCode]).count()
                cultural_vice_captain_data.append(get_cvc_votes_count)


    return render_template("/online_voting/final_results.html",
        captain_results=json.dumps(captain_data),
        captain_names=json.dumps(captains),
        vice_captain_results = json.dumps(vice_captain_data),
        vice_captain_names = json.dumps(vice_captains),
        lateral_captain_results = json.dumps(lateral_captain_data),
        lateral_captain_names = json.dumps(lateral_captains),
        lateral_vice_captain_results = json.dumps(lateral_vice_captain_data),
        lateral_vice_captain_names = json.dumps(lateral_vice_captains),
        sport_captain_results = json.dumps(sport_captain_data),
        sport_captain_names = json.dumps(sport_captains),
        sport_vice_captain_results = json.dumps(sport_vice_captain_data),
        sport_vice_captain_names = json.dumps(sport_vice_captains),
        cultural_captain_results = json.dumps(cultural_captain_data),
        cultural_captain_names = json.dumps(cultural_captains),
        cultural_vice_captain_results = json.dumps(cultural_vice_captain_data),
        cultural_vice_captain_names = json.dumps(cultural_vice_captains))



if __name__ == '__main__':
    # app.run(debug=True, port=4000)
    app.run(host='0.0.0.0',debug=True, port=4000)