from rest_framework import serializers
from .models import Tuitions, Subjects, Reviews

class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = "__all__"

# class TuitionSerializer(serializers.ModelSerializer):
#     subjects = SubjectSerializers(many=True, read_only=True)

#     subject_ids = serializers.PrimaryKeyRelatedField(
#         queryset=Subjects.objects.all(), source='subjects', many=True, write_only=True
#     )
#     class Meta:
#         model = Tuitions
#         fields = "__all__"
class TuitionSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializers(many=True, read_only=True)
    subject_ids = serializers.PrimaryKeyRelatedField(
        queryset=Subjects.objects.all(), source='subjects', many=True, write_only=True
    )

    class Meta:
        model = Tuitions
        fields = "__all__"

    def create(self, validated_data):
        subjects_data = validated_data.pop('subjects', [])

        tuition = Tuitions.objects.create(**validated_data)
        
        if subjects_data:
            tuition.subjects.set(subjects_data)
        
        return tuition

    def update(self, instance, validated_data):
        subjects_data = validated_data.pop('subjects', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        if subjects_data:
            instance.subjects.set(subjects_data)
        
        return instance
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__" 