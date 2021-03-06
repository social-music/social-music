from django.db import models
from django.contrib.auth.models import User
import uuid

#Verifiable
class verifiable(models.Model):
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

#Profile
class Profile(verifiable):
    #Link Profile to a User model instance.
    user = models.OneToOneField(User, related_name='profile')

    #Additional attributes
    website = models.URLField(blank=True)
    ownedcontent = [] #ListField(models.ForeignKey('ContentModel'))
    followers = [] #ListField(models.ForeignKey('UserModel'))

    # Added ImageField for profile picture
    picture = models.ImageField(upload_to='profile_images', blank=True, null=True)

    #Unicode method
    def __unicode__(self):
        return self.user.username

    def addContent(self, content):
        if content not in favorites:
            favorites.append(content)

    def removeContent(self, content):
        if content in favorites:
            favorites.remove(content)

    def getContent(self):
        return favorites

    def addFollower(self, content):
        if content not in favorites:
            favorites.append(content)

    def removeFollower(self, content):
        if content in favorites:
            favorites.remove(content)

    def getFollowers(self):
        return favorites

#UserModel
class UserModel(Profile):
    favorites = [] #ListField(models.ForeignKey('ContentModel'))
    garages = [] #ListField(models.ForeignKey('GarageModel'))
    following = [] #ListField(models.ForeignKey('self'))

    # def getEmail(self):
    #   return email

    # def setEmail(self, address):
    #   email = address

    # def getPasswordHash(self):
    #   return passwordHash

    # def setPasswordHash(self,passhash):
    #   passwordHash = passhash

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

    # def isAdmin(self):
    #   return admin

    # def setAdmin(self, a):
    #   admin = a

#GarageModel
class GarageModel(Profile):
    members = [] #ListField(models.ForeignKey('UserModel'))

    def addMember(self, user):
        if user not in members:
            members.append(user)

    def removeMember(self, user):
        if user in members:
            members.remove(user)

    def getMembers(self):
        return members



# Media
class Media(models.Model):
    mediaFile = models.FileField(upload_to='mediaFiles', blank=True, null=False)

class Audio(Media):
    numPlays = models.IntegerField(default=0)

class Tab(Media):
    CHORDS = "0"
    TABS = "1"
    TYPE_CHOICES = (
        (CHORDS,"Chords"),
        (TABS,"Tabs"),
        )

    tabType = models.CharField(max_length=180, choices=TYPE_CHOICES, default=CHORDS)
    key = models.CharField(max_length=180)

class SheetMusic(Media):
    instrument = models.CharField(max_length=180)
    key = models.CharField(max_length=180)

# stream
class StreamModel(models.Model):
    NEWEST = "0"
    FEATURED = "1"
    SORTBY_CHOICES = (
        (NEWEST, "Newest"),
        (FEATURED, "Featured"),
    )

    content = []
    sortBy = models.CharField(max_length=1, choices=SORTBY_CHOICES, default=NEWEST)

    def getContent(self):
        return content

    def sort(self, value):
        sortBy = value

 #ContentModel
class ContentModel(verifiable):
    title = models.CharField(max_length=128)
    artist = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    album = models.CharField(max_length=128)    
    website = models.URLField()
    upload_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Profile, related_name="content")
    media = models.OneToOneField(Media, related_name="media")

    class Meta:
        ordering = ('upload_date', 'title')


#Comment
class CommentModel(ContentModel):
    author = UserModel()
    comment = models.CharField(max_length=140)
    timestamp = models.DateTimeField()

    def __init__(self):
        uid = uuid.uuid4()

    def __init__(self, newID):
        uid = newId

    def getId():
        return uid

    def getAuthor():
        return author

    def setAuthor(newAuthor):
        author = newAuthor

    def getComment():
        return comment

    def setComment(newComment):
        comment = newComment

    def getTimeStamp():
        return timestamp

    def setTimeStamp():
        currTime = time.time()
        timestamp = datetime.datetime.fromtimestamp(currTime).strftime('%Y-%m-%d %H:%M:%S')
