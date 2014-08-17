# Include the Dropbox SDK libraries
from dropbox import client, session

app_key = 'nhlimxrosp0e8tq'
app_secret = 'sxnbh3a95c4deod'

sess = session.DropboxSession(app_key, app_secret)

client_key = 'lrqwgxm5b6jpsuct'
client_secret = 'iarmqk7zdlmi1ln'

sess.set_token(client_key, client_secret)

client = client.DropboxClient(sess)


def get_quotes():
    f, _ = client.get_file_and_metadata('/Public/quotes/quotes.txt')
    return f.read().split('\r\n\r\n')


def get_music():
    f, _ = client.get_file_and_metadata('/Public/quotes/music.txt')
    return f.read().split('\r\n\r\n')
