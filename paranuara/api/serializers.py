from rest_framework import serializers
from paranuara.api.models import Companies, People


class CompaniesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Companies
        fields = ("index", "company")


class StringListField(serializers.ListField):
    child = serializers.CharField()


class PeopleSerializer(serializers.Serializer):
    index = serializers.IntegerField(min_value=0, required=True)
    name = serializers.CharField(max_length=128, allow_blank=True, required=False)
    _id = serializers.CharField(max_length=64, allow_blank=True, required=False)
    guid = serializers.CharField(max_length=64, allow_blank=True, required=False)
    has_died = serializers.BooleanField(default=False, required=False)
    balance = serializers.CharField(max_length=64, allow_blank=True, required=False)
    picture = serializers.CharField(max_length=256, allow_blank=True, required=False)
    age = serializers.IntegerField(min_value=0, required=False)
    eyeColor = serializers.CharField(max_length=32, allow_blank=True, required=False)
    gender = serializers.CharField(max_length=16, allow_blank=True, required=False)
    email = serializers.EmailField(max_length=64, allow_blank=True, required=False)
    phone = serializers.CharField(max_length=32, allow_blank=True, required=False)
    address = serializers.CharField(max_length=256, allow_blank=True, required=False)
    about = serializers.CharField(allow_blank=True, required=False)
    registered = serializers.DateTimeField(input_formats=[
        'YYYY-MM-DDThh:mm[:ss[.uuuuuu]] [+HH:MM|-HH:MM|Z]',
        '%Y-%m-%dT%H:%M:%S %z',
        'iso-8601'], required=False)
    greeting = serializers.CharField(allow_blank=True, required=False)
    company_id = serializers.IntegerField(required=False)
    favourite_fruits = StringListField(required=False)
    favourite_vegetables = StringListField(required=False)
    tags = StringListField(required=False)
    friends = serializers.ListField(required=False)

    favouriteFood = StringListField(required=False)

    def create(self, validated_data):
        friends_list = None
        favorite_food = None
        company_id = None
        if 'friends' in validated_data:
            friends_list = validated_data.pop('friends')
        if 'favouriteFood' in validated_data:
            favorite_food = validated_data.pop('favouriteFood')
        if 'company_id' in validated_data:
            company_id = validated_data.pop('company_id')
        person, created = People.objects.update_or_create(index=validated_data['index'], defaults=validated_data)
        person.save()
        if company_id:
            company, created = Companies.objects.get_or_create(index=company_id)
            if created:
                company.save()
            person.company = company
        for friend_data in friends_list:
            friend, created = People.objects.get_or_create(**friend_data)
            if created:
                friend.save()
            if person.index != friend.index:
                person.friends.add(friend)
        person.save()
        return person

    def update(self, instance, validated_data):
        pass
