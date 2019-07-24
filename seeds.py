from app import app, db
from models.song import Song, Comment
from models.user import UserSchema
from models.category import Category
from models.forumtopic import Forumtopic, Forumcomment

user_schema = UserSchema()

with app.app_context():
    db.drop_all()
    db.create_all()

    dav, errors = user_schema.load({
        'username': 'Dav',
        'email': 'dav@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    if errors:
        raise Exception(errors)

    wes, errors = user_schema.load({
        'username': 'WesleyDale',
        'email': 'wes@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    melancholy = Category(name='Melancholy')
    erratic = Category(name='Erratic')
    smash = Category(name='Smash')
    benevolent = Category(name='Benevolent')

    burn_the_witch = Song(
        title='Burn The Witch',
        album='A Moon Shaped Pool',
        music='.',
        image='.',
        lyric='This is a low flying panic attack',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic, smash]
    )
    daydreaming = Song(
        title='Daydreaming',
        album='A Moon Shaped Pool',
        music='.',
        image='.',
        lyric='Dreamers, they never learn',
        description='.',
        review_link='.',
        external='.',
        categories=[melancholy]
    )
    true_love_waits = Song(
        title='True Love Waits',
        album='A Moon Shaped Pool',
        music='.',
        image='.',
        lyric='I’m not living, I’m just killing time',
        description='.',
        review_link='.',
        external='.',
        categories=[melancholy]
    )


    comment_one = Comment(
        content='Beautiful song',
        song=daydreaming,
        creator=wes
    )

    comment_two = Comment(
        content='What a smasher',
        song=burn_the_witch,
        creator=dav
    )

    comment_three = Comment(
        content='Radiohead is back',
        song=burn_the_witch,
        creator=wes
    )

    new_album = Forumtopic(
        title='Does anyone know if they are working on a new album?',
        description='Anyone know??',
        creator=wes
    )
    OK_song = Forumtopic(
        title='Favourite song on OK Computer',
        description='Hey guys, mine is Airbag. I think it has such an incredible uplifting vibe. How about you and why?',
        creator=dav
    )

    new_albumcomment = Forumcomment(
        content='I have not heard much about that but you know they are most probably making something all the time.',
        forumtopic=new_album,
        creator=dav
    )
    OK_songcomment = Forumcomment(
        content='It has to be Karma Police, that song sends me chills',
        forumtopic=OK_song,
        creator=wes
    )

# Seed Bulk

    # decks_dark = Song(
    #     title='Decks Dark',
    #     album='A Moon Shaped Pool',
    #     music='.',
    #     image='.',
    #     lyric='There’s a spaceship blocking out the sky',
    #     description='.',
    #     review_link='.',
    #     external='.',
    #     categories=[melancholy]
    # )
    # fifteen_step = Song(
    #     title='15 Step',
    #     album='In Rainbows',
    #     music='.',
    #     image='.',
    #     lyric='You reel me out when you cut the string',
    #     description='.',
    #     review_link='.',
    #     external='.',
    #     categories=[erratic]
    # )



    db.session.add(dav)
    db.session.add(wes)
    db.session.add(melancholy)
    db.session.add(erratic)
    db.session.add(smash)
    db.session.add(benevolent)
    db.session.add(burn_the_witch)
    db.session.add(daydreaming)
    db.session.add(true_love_waits)
    db.session.add(comment_one)
    db.session.add(comment_two)
    db.session.add(comment_three)
    db.session.add(new_album)
    db.session.add(OK_song)
    db.session.add(new_albumcomment)
    db.session.add(OK_songcomment)

    db.session.commit()
