from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid

class Room(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT TITLE")
    description = models.CharField(max_length=500, default="DEFAULT DESCRIPTION")
    n_to = models.IntegerField(default=0)
    s_to = models.IntegerField(default=0)
    e_to = models.IntegerField(default=0)
    w_to = models.IntegerField(default=0)
    def connectRooms(self, destinationRoom, direction):
        destinationRoomID = destinationRoom.id
        try:
            destinationRoom = Room.objects.get(id=destinationRoomID)
        except Room.DoesNotExist:
            print("That room does not exist")
        else:
            if direction == "n":
                self.n_to = destinationRoomID
            elif direction == "s":
                self.s_to = destinationRoomID
            elif direction == "e":
                self.e_to = destinationRoomID
            elif direction == "w":
                self.w_to = destinationRoomID
            else:
                print("Invalid direction")
                return
            self.save()
    def playerNames(self, currentPlayerID):
        return [p.user.username for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]
    def playerUUIDs(self, currentPlayerID):
        return [p.uuid for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currentRoom = models.IntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    def initialize(self):
        if self.currentRoom == 0:
            self.currentRoom = Room.objects.first().id
            self.save()
    def room(self):
        try:
            return Room.objects.get(id=self.currentRoom)
        except Room.DoesNotExist:
            self.initialize()
            return self.room()



@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()



'''
CREATE THE WORLD HERE


class Track:
    def __init__(self, sprint, description):
        self.sprint = sprint
        self.description = description
        self.north = None
        self.east = None
        self.south = None
        self.west = None
        self.previous = None


class Map:
    def __init__(self):
        self.start = Track('Orientation', 'Intro to Lambda')
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
    def search_map(self, sprint_name):
        data = []
        queue = []
        queue.append(self.start)
        while len(queue) != 0:
            sprint_viewed = queue.pop(0)
            data.append(sprint_viewed.sprint)
            if sprint_viewed.sprint.lower() == sprint_name.lower():
                return sprint_viewed
            if sprint_viewed.west:
                queue.append(sprint_viewed.west)
            if sprint_viewed.east:
                queue.append(sprint_viewed.east)
        return -1
        
    def insert_to_north(self, current_sprint, next_sprint, next_description):
        current_spot = self.search_map(current_sprint)
        if current_spot == -1:
            return "Sprint Not Found"
        elif current_spot != -1:
            if current_spot.north:
                return "this sprint already has a west"
            else:
                new_sprint = Track(next_sprint, next_description)
                current_spot.north = new_sprint
                new_sprint.previous = current_spot

    def insert_to_south(self, current_sprint, next_sprint, next_description):
        current_spot = self.search_map(current_sprint)
        if current_spot == -1:
            return "Sprint Not Found"
        elif current_spot != -1:
            if current_spot.south:
                return "this sprint already has a west"
            else:
                new_sprint = Track(next_sprint, next_description)
                current_spot.south = new_sprint
                new_sprint.previous = current_spot
                

    def insert_to_east(self, current_sprint, next_sprint, next_description):
        current_spot = self.search_map(current_sprint)
        if current_spot == -1:
            return "Sprint Not Found"
        elif current_spot != -1:
            if current_spot.east:
                return "this sprint already has a west"
            else:
                new_sprint = Track(next_sprint, next_description)
                current_spot.east = new_sprint
                new_sprint.previous = current_spot

    def insert_to_west(self, current_sprint, next_sprint, next_description):
        current_spot = self.search_map(current_sprint)
        if current_spot == -1:
            return "Sprint Not Found"
        elif current_spot != -1:
            if current_spot.west:
                return "this sprint already has a west"
            else:
                new_sprint = Track(next_sprint, next_description)
                current_spot.west = new_sprint
                new_sprint.previous = current_spot
'''
#web
#data science

# location = Map()
# location.insert_to_north(current_sprint='Orientation', next_sprint='web', next_description='learning web stuff')
# location.insert_to_east(current_sprint='Orientation', next_sprint='ds', next_description='learning ds stuff')
# location.insert_to_west('Orientation', 'ios', 'learning apple stuff')
# location.insert_to_west('ios', 'C#', 'learning C#')
# location.insert_to_south('Orientation', 'ux', 'learning ux stuff')
#ios
#ux


#web, data science, ios  each converge here at the northern tip
#computer science/career readiness

# track.insert_to_north('Neighbor')

# loc=Track.__class__.objects.all()
# for l in loc:
#   l.start=loc.id
#   l.save()