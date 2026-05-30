import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_V3O2AwrdmlTW@ep-shy-brook-apa1hz8f-pooler.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

class Config:
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")
