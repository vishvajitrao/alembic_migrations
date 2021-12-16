from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine


class Config(object):
    DATABASE_URI = "postgresql://root:Movtek,123@localhost/callnotes"


dbEngine = create_engine(
    Config.DATABASE_URI, pool_size=20, isolation_level="READ COMMITTED"
)
dbEngine.echo = False
dbEngine.pool_pre_ping = True
session_factory = sessionmaker(bind=dbEngine, autoflush=True)
dbSession = scoped_session(session_factory)

# Connect to database session
DB = dbSession()
