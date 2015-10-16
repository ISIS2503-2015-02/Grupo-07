class defaultBackupRouter(object):

    def allow_syncdb(self, db, model):
        """
        All non-auth models end up in this pool.
        """
        return True
