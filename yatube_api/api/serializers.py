from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import CurrentUserDefault
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field='username', read_only=True, default=CurrentUserDefault()
    )
    following = SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=("user", "following"),
                message="Ошибка валидации. Вы уже подписаны."
            )
        ]

    def validate(self, data):
        if data['following'] == self.context['request'].user:
            raise serializers.ValidationError(
                'Ошибка валидации. Вы не можете подписаться на самого себя.'
            )
        return data
