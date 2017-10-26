from wsgiref import simple_server

from catx import app

simple_server.make_server('0.0.0.0', 6543, app.app).serve_forever()
