from rest_framework import serializers
from api.models import Companies, People, Tags, Vegetables, Fruits


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('index',)


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('name',)


class FruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruits
        fields = ('name',)


class VegetablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegetables
        fields = ('name',)


class CompaniesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Companies
        fields = ("index", "company")


class PeopleSerializer(serializers.ModelSerializer):
    friends = FriendsSerializer(many=True, required=False)
    tags = TagsSerializer(many=True, required=False)
    favorite_fruits = FruitsSerializer(many=True, required=False)
    favorite_vegetables = VegetablesSerializer(many=True, required=False)
    favoriteFood = serializers.CharField(required=False, allow_blank=True, max_length=256)
    registered = serializers.DateTimeField(input_formats=[
        'YYYY-MM-DDThh:mm[:ss[.uuuuuu]] [+HH:MM|-HH:MM|Z]',
        '%Y-%m-%dT%H:%M:%S %z',
        'iso-8601'])

    class Meta:
        model = People
        fields = ("_id", "index", "guid", "has_died", "balance", "picture",
                  "age", "eyeColor", "name", "gender", "company_id", "email",
                  "phone", "address", "about", "registered", "greeting", "friends", "tags",
                  "favorite_fruits", "favorite_vegetables", "favoriteFood")

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
