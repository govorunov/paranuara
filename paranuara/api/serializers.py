from rest_framework import serializers
from .models import Companies, People

FRUITS_SET = {'apple', 'apricot', 'banana', 'bilberry', 'blackberry', 'blackcurrant',
              'blueberry', 'coconut', 'currant', 'cherry', 'cherimoya', 'clementine',
              'cloudberry', 'date', 'damson', 'durian', 'elderberry', 'fig', 'feijoa',
              'gooseberry', 'grape', 'grapefruit', 'huckleberry', 'jackfruit', 'jambul',
              'jujube', 'kiwifruit', 'kumquat', 'lemon', 'lime', 'loquat', 'lychee', 'mango',
              'melon', 'cantaloupe', 'honeydew', 'watermelon', 'rock', 'melon', 'nectarine',
              'orange', 'passionfruit', 'peach', 'pear', 'plum', 'plumcot', 'prune',
              'pineapple', 'pomegranate', 'pomelo', 'purple', 'mangosteen', 'raisin',
              'raspberry', 'rambutan', 'redcurrant', 'satsuma', 'strawberry', 'tangerine',
              'tomato', 'ugli', 'fruit'}

VEGETABLES_SET = {'artichoke', 'asparagus', 'aubergine', 'beet', 'beetroot', 'bell pepper',
                  'broccoli', 'brussels sprout', 'cabbage', 'carrot', 'cauliflower', 'celery',
                  'corn', 'courgette', 'cucumber', 'eggplant', 'green bean', 'green onion',
                  'leek', 'lettuce', 'mushroom', 'onion', 'pea', 'pepper', 'potato', 'pumpkin',
                  'radish', 'spring onion', 'squash', 'sweet potato', 'tomato', 'zucchini'}


class CompaniesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Companies
        fields = ('index', 'company')


class PeopleSerializer(serializers.ModelSerializer):
    tags = serializers.ListField()
    favourite_fruits = serializers.ListField()
    favourite_vegetables = serializers.ListField()

    class Meta:
        model = People
        fields = '__all__'


class PeopleBriefSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = ('index', 'name', 'age', 'address', 'phone',)


class CompaniesEmployeesSerializer(serializers.ModelSerializer):
    employees = PeopleBriefSerializer(many=True, read_only=True)

    class Meta:
        model = Companies
        fields = ('index', 'company', 'employees', )


class TwoPeopleSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        return {
            'person1': PeopleBriefSerializer(obj['person1']).data,
            'person2': PeopleBriefSerializer(obj['person2']).data,
            'common_friends': PeopleBriefSerializer(obj['common_friends'], many=True).data,
        }


class StringListField(serializers.ListField):
    child = serializers.CharField()


class PeopleImportSerializer(serializers.Serializer):
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
        if person.favourite_vegetables is None:
            person.favourite_vegetables = []
        if person.favourite_fruits is None:
            person.favourite_fruits = []
        # if created:
        #     person.save()
        if company_id:
            company, created = Companies.objects.get_or_create(index=company_id)
            if created:
                company.save()
            person.company = company
        for food in favorite_food:
            if food.strip(',. ').lower() in VEGETABLES_SET:
                person.favourite_vegetables.append(food)
            else:
                person.favourite_fruits.append(food)
        for friend_data in friends_list:
            friend, created = People.objects.get_or_create(**friend_data)
            if created:
                friend.save()
            if person.index != friend.index:
                person.friends.add(friend)
        person.save()
        return person

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class FruitsVegetablesSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='name')
    fruits = serializers.ListField(source='favourite_fruits')
    vegetables = serializers.ListField(source='favourite_vegetables')

    class Meta:
        model = People
        fields = ('username', 'age', 'fruits', 'vegetables',)
        read_only_fields = ('username', 'age', 'fruits', 'vegetables',)
