from rest_framework import serializers
from .models import Category, Blog

class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    blog_name = serializers.CharField()
    desc = serializers.CharField()
    image = serializers.ImageField()
    homepage = serializers.BooleanField()

    def create(self, validated_data):
        print(validated_data)
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.blog_name = validated_data.get('blog_name', instance.blog_name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.image = validated_data.get('image', instance.image)
        instance.homepage = validated_data.get('homepage', instance.homepage)
        instance.save()

        return instance
