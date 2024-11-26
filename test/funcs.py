
from app.infrastructure.database.setup import create_engine, create_session_maker


engine = create_engine()

session_maker = create_session_maker(engine)