import logging
from django.db import connections, OperationalError

logger = logging.getLogger(__name__)

class PrimaryReplicaRouter:
    def db_for_read(self, model, **hints):
        return self._get_db()

    def db_for_write(self, model, **hints):
        return self._get_db()

    def _get_db(self):
        try:
            # Try to use the default database with a simple query
            with connections['default'].cursor() as cursor:
                cursor.execute('SELECT 1;')
                print("Using default database.")
            logger.info("Using default database.")
            return 'default'
        except OperationalError as e:
            print(f"Default database connection failed: {e}. Switching to alternative.")
            logger.warning(f"Default database connection failed: {e}. Switching to alternative.")
            try:
                # Use the alternative database if the default one fails
                with connections['alternative'].cursor() as cursor:
                    cursor.execute('SELECT 1;')
                logger.info("Using alternative database.")
                return 'alternative'
            except OperationalError as e:
                logger.error(f"Both default and alternative database connections failed: {e}")
                # Handle both databases failing gracefully (e.g., return default)
                return 'default'  # Or raise a custom exception

    def allow_relation(self, obj1, obj2, **hints):
        db_list = {'default', 'alternative'}
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
    