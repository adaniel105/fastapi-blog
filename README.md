This is a secure blog API built with 

- FastAPI, 
- PostgreSQL, 
- passlib[bcrypt] for password hashing, 
- JWT for authentication
- Alembic for data migration

## HOW TO RUN
''' bash
cd fastapi-blog
alembic revision --autogenerate
python3 initial_data.py
fastapi dev main.py
'''
