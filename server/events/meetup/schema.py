import graphene
from graphene_django.types import DjangoObjectType
from .models import Event, Group, Interest, Profile
from django.contrib.auth.models import User


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
class UserType(DjangoObjectType):
    class Meta:
        model = User

class Query(object):
    #Single Objects
    event = graphene.Field(EventType, id=graphene.Int())
    group = graphene.Field(GroupType, id=graphene.Int())
    interest = graphene.Field(InterestType, id=graphene.Int())
    profile = graphene.Field(ProfileType, id=graphene.Int())
    user = graphene.Field(UserType, id=graphene.Int())

    def resolve_event(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Event.objects.get(pk=id)
        return None

    def resolve_group(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Group.objects.get(pk=id)
        return None

    def resolve_interest(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Interest.objects.get(pk=id)
        return None

    def resolve_profile(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Profile.objects.get(pk=id)
        return None

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return User.objects.get(pk=id)
        return None

    # Bulk Objects
    all_events = graphene.List(EventType)
    all_groups = graphene.List(GroupType)
    all_interests = graphene.List(InterestType)
    all_profiles = graphene.List(ProfileType)
    all_users = graphene.List(UserType)

    def resolve_all_events(self, info, **kwargs):
        return Event.objects.all()

    def resolve_all_groups(self, info, **kwargs):
        return Group.objects.all()

    def resolve_all_interests(self, info, **kwargs):
        return Interest.objects.all()

    def resolve_all_profiles(self, info, **kwargs):
        return Profile.objects.select_related('user')

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()
