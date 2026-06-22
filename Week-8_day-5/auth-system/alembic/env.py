from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
import os
import sys

# ensure app package is importable when alembic runs
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

# Import the application's `Base` to provide metadata for autogenerate
try:
    from app.database import Base

    target_metadata = Base.metadata
except Exception:
    # If import fails, leave target_metadata as None; autogenerate will error.
    target_metadata = None

# Ensure all model modules are imported so their Table objects are registered
# with `Base.metadata`. If models are not imported, autogenerate won't see them.
try:
    # explicit imports register tables on Base.metadata
    import app.models.user  # noqa: F401
    import app.models.role  # noqa: F401
    import app.models.permission  # noqa: F401
    import app.models.associations  # noqa: F401
except Exception:
    # if imports fail, continue; metadata may still be populated via other means
    pass

# If the application exposes a DATABASE_URL, use it so alembic matches the app.
# Importing the app may attempt to create an Engine (and require DB drivers),
# so first try a normal import, but if that fails, fall back to parsing the
# `DATABASE_URL` value directly from the source file to avoid side effects.
try:
    from app.database import DATABASE_URL
    if DATABASE_URL:
        config.set_main_option("sqlalchemy.url", DATABASE_URL)
except Exception:
    try:
        db_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "app", "database.py")
        with open(db_file, "r", encoding="utf-8") as f:
            content = f.read()
        import re

        m = re.search(r"DATABASE_URL\s*=\s*([\'\"])(.*?)\1", content)
        if m:
            config.set_main_option("sqlalchemy.url", m.group(2))
    except Exception:
        # fall back to the value in alembic.ini
        pass

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
