from api import user
from schema import schemas
from database.session import SessionLocal


def init() -> None:
    db = SessionLocal()
    user.create(
        request= schemas.User(
            first_name="John",
            last_name = "Doe",
            email = "JohnDoe@gmail.com",
            password = "qwerty",
        ),
        db=db
    )

if __name__ == "__main__":
    print("Creating user John Doe")
    init()
    print("User created")