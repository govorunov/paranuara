from rest_framework import serializers
from api.models import Companies, People
from django.core.validators import MinValueValidator


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('index',)


class CompaniesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Companies
        fields = ("index", "company")


class PeopleSerializer(serializers.ModelSerializer):
    friends = FriendsSerializer(many=True, required=False)
    favouriteFood = serializers.ListField(required=False)
    registered = serializers.DateTimeField(input_formats=[
        'YYYY-MM-DDThh:mm[:ss[.uuuuuu]] [+HH:MM|-HH:MM|Z]',
        '%Y-%m-%dT%H:%M:%S %z',
        'iso-8601'])
    tags = serializers.ListField(required=False)
    favourite_fruits = serializers.ListField(required=False)
    favourite_vegetables = serializers.ListField(required=False)

    class Meta:
        model = People
        fields = ("_id", "index", "guid", "has_died", "balance", "picture",
                  "age", "eyeColor", "name", "gender", "company_id", "email",
                  "phone", "address", "about", "registered", "greeting", "friends", "tags",
                  "favourite_fruits", "favourite_vegetables", "favouriteFood")
        extra_kwargs = {
            'index': {
                'validators': [],
            }
        }

    def create(self, validated_data):
        friends_list = validated_data.pop('friends')
        favorite_food = validated_data.pop('favouriteFood')
        # tags = validated_data.pop('tags')
        person, created = People.objects.update_or_create(**validated_data)
        if 'company_id' in validated_data:
            company_id = validated_data.pop('company_id')
            company, created = Companies.objects.get_or_create(index=company_id)
            if created:
                company.save()
            person.company = company
        person.save()
        for friend_data in friends_list:
            friend, created = People.objects.get_or_create(friend_data)
            if created:
                friend.save()
            person.friends.add(friend)
        person.save()
        return person

    def update(self, instance, validated_data):
        instance.index = validated_data.get('index', instance.index)
        instance.save()
        return instance
