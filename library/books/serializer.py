from rest_framework import serializers

class Serializer(serializers.Serializer):
	id = serializers.IntegerField()
	name_book = serializers.CharField(max_length=50)
	autor = serializers.CharField()
	date = serializers.DateField()
	category_id = serializers.IntegerField()