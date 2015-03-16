from django.db import models
import uuid

# Create your models here.
class verifiable():
	verified = False
	flagged = False

	def isVerified(self):
		return verified

	def isFlagged(self):
		return flagged

	def setFlagged(self,flag):
		flagged = flag

	def verify(self,verification):
		verified = verification
		flagged = False

class Profile(verifiable, models.Model):
	uid = models.CharField(default=uuid.uuid4)
	name = models.CharField(max_length=128)
	website = models.URLField()
	ownedcontent = []
	followers = []

	def __init__(self):
		uid = uuid.uuid4()

	def __init__(self, uid):
		uid = uid

	def getId(self):
		return uid

	def getName(self):
		return name

	def setName(self, n):
		name = n

	def getWebsite(self):
		return website

	def setWebsite(self, site):
		website = site

	def addContent(self, content):
		if content not in ownedcontent:
			ownedcontent.append(content)

	def removeContent(self, content):
		if content in ownedcontent:
			ownedcontent.remove(content)

	def getContent(self):
		return ownedcontent

	def addFollower(self, user):
		if user not in followers:
			followers.append(user)

	def removeFollower(self, user):
		if user in followers:
			followers.remove(user)

	def getFollowers(self):
		return followers

class UserModel(Profile):
	email = models.EmailField()
	passwordHash = models.CharField(max_length=256)
	favorites = []
	garages = []
	following = []
	admin = False

	def getEmail(self):
		return email

	def setEmail(self, address):
		email = address

	def getPasswordHash(self):
		return passwordHash

	def setPasswordHash(self,passhash):
		passwordHash = passhash

	def addFavorite(self, content):
		if content not in favorites:
			favorites.append(content)

	def removeFavorite(self, content):
		if content in favorites:
			favorites.remove(content)

	def getFavorites(self):
		return favorites

	def addGarage(self,garage):
		if garage not in garages:
			garages.append(garage)

	def removeGarage(self,garage):
		if garage in garages:
			garages.remove(garage)

	def getGarages(self):
		return garages

	def addFollowing(self, user):
		if user not in following:
			following.append(user)

	def removeFollowing(self, user):
		if user in following:
			following.remove(user)

	def getFollowing(self):
		return following

	def isAdmin(self):
		return admin

	def setAdmin(self, a):
		admin = a

class ContentModel():
	uid = models.CharField(default=uuid.uuid4)
	title = models.CharField(max_length=128)
	artist = models.charField(max_length=128)
	genre = models.charField(max_length=128)
	description = models.charField(max_length=128)
	album = models.charField(max_length=128)	
	website = models.URLField()
	favoritedBy = []
	comments = []

	def __init__(self):
		uid = uuid.uuid4()

	def __init__(self, uid):
		uid = uid

	def getId(self):
		return uid

	def getTitle(self):
		return title

	def setTitle(self, n):
		title = n

	def getArtist(self):
		return artist

	def setArtist(self, profile):
		artist = profile

	def getGenre(self):
		return genre 

	def setGenre(self, n):
		genre = n

	def getDescription(self):
		return description

	def setDescription(self, n):
		description = n 

	def getAlbum(self):
		return album

	def setAlbum(self, n):
		album = name

	def getMedia(self):
		return media

	def setMedia(self, n):
		media = n

	def addFavoritedBy(self, user):
		if user not in FavoritedBy:
			favoritedBy.append(user)

	def removeFavoritedBy():
		if user in FavoritedBy:
			favoritedBy.remove(user)

	def getFavoritedBy():
		return favoritedBy

	def addComment(comment):
		if comment not in comments:
			comments.append(comment)

	def removeComment():
		if comment in comments:
			comments.remove(comment)

	def getComments(self):
		return comments


class GarageModel(Profile):
	members = []

	def addMember(self, user):
		if user not in members:
			members.append(user)

	def removeMember(self, user):
		if user in members:
			members.remove(user)

	def getMembers(self):
		return members

# stream
class StreamModel(models.Model):
 	NEWEST = "0"
 	FEATURED = "1"
 	SORTBY_CHOICES = (
 		(NEWEST: "Newest"),
 		(FEATURED: "Featured"),
 	)

 	content = []
 	sortBy = models.CharField(max_length=1, choices=SORTBY_CHOICES, default=NEWEST)

 	def getContent(self):
 		return content

 	def sort(self, value):
 		sortBy = value

