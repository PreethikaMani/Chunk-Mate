from rest_framework import serializers
from .models import Document, Chunk

class ChunkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chunk
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    chunks = ChunkSerializer(many=True, read_only=True)

    class Meta:
        model = Document
        fields = ['id', 'title', 'file', 'uploaded_at', 'chunks']
