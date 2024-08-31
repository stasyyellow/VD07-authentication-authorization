# VD07-authentication-authorization
 authentication |  authorization


PS C:\_Python AI\github\VD07-authentication-authorization> python -m flask db init
Creating directory 'C:\\_Python AI\\github\\VD07-authentication-authorization\\migrations' ...  done
Creating directory 'C:\\_Python AI\\github\\VD07-authentication-authorization\\migrations\\versions' ...  done
Generating C:\_Python AI\github\VD07-authentication-authorization\migrations\alembic.ini ...  done
Generating C:\_Python AI\github\VD07-authentication-authorization\migrations\README ...  done
Generating C:\_Python AI\github\VD07-authentication-authorization\migrations\script.py.mako ...  done
Please edit configuration/connection/logging settings in 'C:\\_Python AI\\github\\VD07-authentication-authorization\\migrations\\alembic.ini' before proceeding.   
PS C:\_Python AI\github\VD07-authentication-authorization> python -m flask db migrate -m "nitial migration"
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'user'
Generating C:\_Python AI\github\VD07-authentication-authorization\migrations\versions\174e0cea1901_nitial_migration.py ...  done
PS C:\_Python AI\github\VD07-authentication-authorization> python -m flask db upgrade
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 174e0cea1901, nitial migration
PS C:\_Python AI\github\VD07-authentication-authorization> 
