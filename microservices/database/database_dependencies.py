import microservices.database.database as db

def get_db_session():
    return db.SessionLocal()


def get_db():
    try:
        db = get_db_session()
        yield db
    finally:
        db.close()