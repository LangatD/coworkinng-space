# CoWork Finder - Django REST API

## Setup

1. Clone the repo
   git clone https://github.com/yourusername/coworkinng-space.git

2. Create and activate virtual environment
   python -m venv venv
   source venv/bin/activate

3. Install dependencies
   pip install django djangorestframework

4. Run migrations
   python manage.py makemigrations
   python manage.py migrate

5. Start the server
   python manage.py runserver



## API Endpoints


- GET /api/spaces/ - list all spaces
- POST /api/spaces/ - create a space
- GET /api/spaces/1/ - get a single space
- PUT /api/spaces/1/ - update a space
- DELETE /api/spaces/1/ - delete a space

## Tech Stack
- Django
- Django REST Framework
- SQLite