import sys
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# Load biến môi trường từ .env
load_dotenv()

# thêm path để import app
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.config.database import Base
import app.models  # load toàn bộ models

# cấu hình logging
fileConfig(context.config.config_file_name)

target_metadata = Base.metadata

def run_migrations_offline():
    """Chạy migration ở chế độ offline"""
    url = os.getenv("DATABASE_URL")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Chạy migration ở chế độ online (kết nối DB)"""
    configuration = context.config.get_section(context.config.config_ini_section)
    configuration["sqlalchemy.url"] = os.getenv("DATABASE_URL")

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
