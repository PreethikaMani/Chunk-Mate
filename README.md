# Chunk-Mate

**Chunk-Mate** is a web-based document chunking tool designed for Generative AI workflows. It allows users to upload documents (md files), split them into manageable chunks,
and store the data for downstream processing using machine learning or AI models.

🚀 Features

- Upload and preview documents
- Intelligent document chunking
- View and manage extracted chunks
- RESTful API backend
- React-based dynamic frontend
- MySQL database integration with Django ORM
- Styled Components for modern UI design

🛠️ Tech Stack

 Frontend
- React.js
- Vite
- Styled Components

 Backend
- Django
- Django REST Framework
- MySQL

 Others
- Axios (API calls)
- React Dropzone or FilePond (for file uploads)
- Python PDF parsing libraries (e.g., PyMuPDF or pdfminer)

---

📂 Project Structure

chunk-mate/
│
├── backend/
│ ├── manage.py
│ ├── chunkmate/ # Django project
│ ├── documents/ # App: Models, Views, Serializers, APIs
│ ├── media/ # Uploaded files
│ └── requirements.txt
│
├── frontend/
│ ├── index.html
│ ├── vite.config.js
│ ├── src/
│ │ ├── components/ # Reusable components
│ │ ├── pages/ # Page components
│ │ ├── api/ # Axios API functions
│ │ ├── App.jsx
│ │ └── main.jsx
│ └── package.json
