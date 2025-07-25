from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], depretated="auto")

fake_users_db = {
    "admin":{
        "username": "admin",
        "hashed_password": pwd_context.hash("1234"),
        "roles":["admin"]
    },
    "user1":{
        "username": "user1",
        "hashed_password": pwd_context.hash("1234"),
        "roles": ["user"]
    }
}