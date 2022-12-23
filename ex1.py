from rest_framework import serializers


class Author:
    def __init__(self, name, year):
        self.name = name
        self.year = year


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    year = serializers.IntegerField()

    def validate_year(self, value):
        if value < 0:
            print('Год рождения не может быть отрицательным')
            raise serializers.ValidationError()

        return value

    def create(self, validated_data):
        return Author(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.year = validated_data.get('year', instance.year)
        return instance


data = {'name': 'Грин', 'year': 1880}
serializer = AuthorSerializer(data=data)
serializer.is_valid()
author = serializer.save()
print(author.__dict__)

new = {'name': 'babka'}
serializer = AuthorSerializer(author, data=new, partial=True)
serializer.is_valid()
author = serializer.save()
print(author.__dict__)
