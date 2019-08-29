import pytest


#@pytest.fixture
#def client(_app):
    # db_fd, db_path = tempfile.mkstemp()
    #_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/test_flash01'
    # app.config['DATABASE'] = db_path
#    _app.config['TESTING'] = True
#    client = _app.test_client()

    # with app.app_context():

 #   yield client

    # os.close(db_fd)

@pytest.mark.options(debug=False)
def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    print(rv)
    assert rv.status_code == 200
