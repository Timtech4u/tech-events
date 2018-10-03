import graphene
from graphene_django.types import DjangoObjectType
from .models import Event, Group, Interest, Profile

class EventType(DjangoObjectType):
    class Meta:
        model = Event

class GroupType(DjangoObjectType):
    class Meta:
        model = Group

class InterestType(DjangoObjectType):
    class Meta:
        model = Interest

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


class Query(object):
    all_events = graphene.List(EventType)
    all_groups = graphene.List(GroupType)
    all_interests = graphene.List(InterestType)
    all_profiles = graphene.List(ProfileType)

    def resolve_all_events(self, info, **kwargs):
        return Event.objects.all()

    def resolve_all_groups(self, info, **kwargs):
        return Group.objects.all()

    def resolve_all_interests(self, info, **kwargs):
        return Interest.objects.all()

    def resolve_all_profiles(self, info, **kwargs):
        return Profile.objects.all()