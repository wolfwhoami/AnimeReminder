from rest_framework import serializers
from models import Anime, Subscription, User, Season, Track


# Season serializers
class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ('id', 'name', 'cover', 'default', 'season_id', 'anime', 'count')


class SeasonOfSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ('id', 'name', 'cover', 'default', 'season_id', 'count')


# Anime serializers
class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ('id', 'aid', 'name', 'description', 'is_end', 'episode', 'poster_link', 'updated_time')


class AnimeOfSubscriptionSerializer(serializers.ModelSerializer):
    seasons = SeasonOfSubscriptionSerializer(many=True)

    class Meta:
        model = Anime
        fields = ('id', 'aid', 'name', 'description', 'is_end', 'episode', 'poster_link', 'updated_time', 'seasons')


# Subscription serializers
class SubscriptionSerializer(serializers.ModelSerializer):
    anime = AnimeOfSubscriptionSerializer()

    class Meta:
        model = Subscription
        fields = ('id', 'anime', 'currently_watched', 'status', 'season')


class SubscriptionCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class SubscriptionUpdateSerializer(serializers.ModelSerializer):
    def get_fields(self):
        fields = super(SubscriptionUpdateSerializer, self).get_fields()
        # filter seasons of the anime
        if not self.instance:
            fields['season'].queryset = None
            return fields
        fields['season'].queryset = Season.objects.filter(anime=self.instance.anime)
        return fields

    class Meta:
        model = Subscription
        fields = ('id', 'anime', 'currently_watched', 'status', 'season')
        read_only_fields = ('user', 'anime')


# Track Serializer
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('subscription', 'date_watched', 'status', 'message')


# User serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'date_joined', 'is_staff', 'last_login', 'email', 'username')
        read_only_fields = ('date_joined', 'is_staff', 'last_login', 'username')


class UserProfileSerializer(serializers.ModelSerializer):
    track = TrackSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'date_joined', 'is_staff', 'last_login', 'username', 'track')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', )


# Others
class SearchSerializer(serializers.Serializer):
    aid = serializers.IntegerField()
    season_id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    episode = serializers.IntegerField()
    poster_link = serializers.URLField()
    updated_time = serializers.DateTimeField()