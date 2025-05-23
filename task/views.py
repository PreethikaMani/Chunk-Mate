from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.core.files.storage import default_storage
from .models import Document, Chunk, Reference
from .serializers import DocumentSerializer,  ChunkSerializer
from .utils import parse_markdown_paragraphs, parse_table, extract_links

# views.py
class DocumentUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        uploaded_file = request.data['document']
        doc = Document.objects.create(file=uploaded_file)
        file_content = uploaded_file.read().decode('utf-8')  # for plain text

        chunks = chunk_markdown(file_content)

        chunk_texts = []
        for idx, chunk in enumerate(chunks):
            Chunk.objects.create(document=doc, text=chunk, chunk_index=idx)
            chunk_texts.append(chunk)

        return Response({
            'message': 'Document uploaded and chunked successfully.',
            'chunks': chunk_texts
        })
