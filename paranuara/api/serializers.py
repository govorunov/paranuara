from rest_framework import serializers
from api.models import Companies, People, Tags, Vegetables, Fruits


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('index',)


class CompaniesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Companies
        fields = ("index", "company")


class PeopleSerializer(serializers.ModelSerializer):
    friends = FriendsSerializer(many=True)
    tags = serializers.StringRelatedField(many=True)
    favorite_fruits = serializers.StringRelatedField(many=True)
    favorite_vegetables = serializers.StringRelatedField(many=True)

    class Meta:
        model = People
        fields = ("_id", "index", "guid", "has_died", "balance", "picture",
                  "age", "eyeColor", "name", "gender", "company_id", "email",
                  "phone", "address", "about", "registered", "greeting")

    def create(self, validated_data):
        friends_list = validated_data.pop('friends')
        favorite_food = validated_data.pop('favouriteFood')
        tags = validated_data.pop('tags')
        person = People.objects.create(**validated_data)
        company_id = validated_data.pop('company_id')
        person.company = Companies.objects.get_or_create(index=company_id)
        person.save()
        for friend_data in friends_list:
            friend = People.objects.get_or_create(friend_data)
            person.friends.add(friend)
        person.save()
        return person
