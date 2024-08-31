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

вроде работает
"C:\Users\US laptop\AppData\Local\Microsoft\WindowsApps\python3.12.exe" "C:\_Python AI\github\VD07-authentication-authorization\run.py" 
 * Serving Flask app 'app'
 * Debug mode: on
INFO:werkzeug:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
INFO:werkzeug:Press CTRL+C to quit
INFO:werkzeug: * Restarting with stat
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 116-850-822
INFO:werkzeug:127.0.0.1 - - [31/Aug/2024 16:23:23] "GET / HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [31/Aug/2024 16:23:23] "GET / HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [31/Aug/2024 16:23:27] "GET /home HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [31/Aug/2024 16:23:30] "GET /register HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [31/Aug/2024 16:23:42] "GET / HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [31/Aug/2024 16:24:11] "POST /register HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [31/Aug/2024 16:24:29] "GET /logout HTTP/1.1" 302 -
INFO:werkzeug:127.0.0.1 - - [31/Aug/2024 16:24:29] "GET /home HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [31/Aug/2024 16:24:32] "GET /login HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [31/Aug/2024 16:24:44] "POST /login HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [31/Aug/2024 16:24:53] "GET /edit_profile HTTP/1.1" 302 -
INFO:werkzeug:127.0.0.1 - - [31/Aug/2024 16:24:53] "GET /login?next=/edit_profile HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [31/Aug/2024 16:24:57] "GET /edit_profile HTTP/1.1" 302 -
INFO:werkzeug:127.0.0.1 - - [31/Aug/2024 16:24:57] "GET /login?next=/edit_profile HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [31/Aug/2024 16:25:19] "POST /login HTTP/1.1" 200 -
