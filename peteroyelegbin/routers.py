import logging
from django.db import connections
from django.db.utils import OperationalError

logger = logging.getLogger(__name__)

class PrimaryReplicaRouter:
    def db_for_read(self, model, **hints):
        return self._get_db()

    def db_for_write(self, model, **hints):
        return self._get_db()

    def _get_db(self):
        try:
            # Try to use the default database
            connections['default'].cursor()
            return 'default'
        except OperationalError:
            logger.warning("Default database connection failed. Switching to alternative.")
            # Use the alternative database if the default one fails
            try:
                connections['alternative'].cursor()
                return 'alternative'
            except OperationalError:
                logger.error("Both default and alternative database connections failed.")
                raise

    def allow_relation(self, obj1, obj2, **hints):
        db_list = ('default', 'alternative')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
