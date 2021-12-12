from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'



class ProjectSerializer(serializers.ModelSerializer):
    
    # deal with mested serializers:
    # to fully display those FK field (not only show the id of FK field):
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)

    # method field (to get child field or any calculated results)
    reviews = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = '__all__'
    
    def get_reviews(self, obj):   # method field must start with get_. obj here is the model in class, i.e. project
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data