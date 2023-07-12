from mongoengine import *


class VotingAdminDetails(Document):
	fullName = StringField()
	emailId = StringField()
	phoneNumber = StringField()
	password = StringField()
	votingAdminRefLink = StringField()
	createdOn = DateTimeField()
	status = IntField(default=1)


class NominateCandidateDetails(Document):
	nominateName = StringField()
	nominateCode = StringField()
	nominateProfilePic = StringField()
	nominateClass = StringField()
	nominateRefLink = StringField()
	nominatePosition = StringField()
	nominateGender = StringField()
	votingAdminRefLink = ReferenceField('VotingAdminDetails')
	votingAdminFullName = ReferenceField('VotingAdminDetails')
	createdOn = DateTimeField()
	status = IntField(default=1)


class VotersDetails(Document):
	fullName = StringField()
	emailId = StringField()
	phoneNumber = StringField()
	password = StringField()
	className = StringField()
	voterId = StringField()
	voterRefLink = StringField()
	createdOn = DateTimeField()
	status = IntField(default=1)
	voterStatus = IntField(default=1)
	votedOn = DateTimeField()

class CastVoters(Document):
	voterName = ReferenceField('VotersDetails')
	voterRefLink = ReferenceField('VotersDetails')
	voterId = ReferenceField('VotersDetails')
	captain = StringField()
	captainCode = StringField()
	captainRefLink = StringField()
	viceCaptain = StringField()
	viceCaptainCode = StringField()
	viceCaptainRefLink = StringField()
	lateralCaptain = StringField()
	lateralCaptainCode= StringField()
	lateralCaptainRefLink = StringField()
	lateralViceCaptain = StringField()
	lateralViceCaptainCode = StringField()
	lateralViceCaptainRefLink = StringField()
	sportCaptain = StringField()
	sportCaptainCode = StringField()
	sportCaptainRefLink = StringField()
	sportViceCaptain = StringField()
	sportViceCaptainCode = StringField()
	sportViceCaptainRefLink = StringField()
	culturalCaptain = StringField()
	culturalCaptainCode = StringField()
	culturalCaptainRefLink = StringField()
	culturalViceCaptain = StringField()
	culturalViceCaptainCode = StringField()
	culturalViceCaptainRefLink = StringField()
	className = ReferenceField('VotersDetails')
	voterStatus = IntField(default=1)
	status = IntField(default=1)
	createdOn = DateTimeField()












	



