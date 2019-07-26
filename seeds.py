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
        image='http://theinspirationroom.com/daily/musicvideos/2016/5/radiohead_burn_the_witch_cider.jpg',
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
        image='https://i.ytimg.com/vi/idOcP_gNFDk/maxresdefault.jpg',
        lyric='Dreamers, they never learn',
        description='.',
        review_link='.',
        external='.',
        categories=[melancholy]
    )
    true_love_waits = Song(
        title='True Love Waits',
        album='A Moon Shaped Pool',
        music='../assets/resource/pictures/rhbluocean.jpg',
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

    decks_dark = Song(
        title='Decks Dark',
        album='A Moon Shaped Pool',
        music='.',
        image='.',
        lyric='There’s a spaceship blocking out the sky',
        description='.',
        review_link='.',
        external='.',
        categories=[melancholy]
    )
    fifteen_step = Song(
        title='15 Step',
        album='In Rainbows',
        music='.',
        image='.',
        lyric='You reel me out when you cut the string',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic]
    )
    bodysnatchers = Song(
        title='Bodysnatchers',
        album='In Rainbows',
        music='.',
        image='.',
        lyric='And for anyone else to see, I’m alive',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic, smash]
    )
    nude = Song(
        title='Nude',
        album='In Rainbows',
        music='.',
        image='.',
        lyric='You paint yourself white',
        description='.',
        review_link='.',
        external='.',
        categories=[benevolent]
    )
    reckoner = Song(
        title='Reckoner',
        album='In Rainbows',
        music='.',
        image='.',
        lyric='Because we separate like ripples on a blank shore',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic, smash, benevolent]
    )
    house_of_cards = Song(
        title='House of Cards',
        album='In Rainbows',
        music='.',
        image='.',
        lyric='Forget about your house of cards and I’ll do mine',
        description='.',
        review_link='.',
        external='.',
        categories=[benevolent]
    )
    jigsaw_falling_into_place = Song(
        title='Jigsaw Falling Into Place',
        album='In Rainbows',
        music='.',
        image='.',
        lyric='Words are a sawed off shotgun',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic, smash, benevolent]
    )
    bangers_and_mash = Song(
        title='Bangers and Mash',
        album='In Rainbows',
        music='.',
        image='.',
        lyric='I got the poison, poison, and now I want more',
        description='.',
        review_link='.',
        external='.',
        categories=[smash]
    )
    airbag = Song(
        title='Airbag',
        album='OK Computer',
        music='.',
        image='.',
        lyric='I am born again',
        description='.',
        review_link='.',
        external='.',
        categories=[smash, benevolent]
    )
    paranoid_android = Song(
        title='Paranoid Android',
        album='OK Computer',
        music='.',
        image='.',
        lyric='Please could you stop the noise',
        description='.',
        review_link='.',
        external='.',
        categories=[melancholy, erratic]
    )
    karma_police = Song(
        title='Karma Police',
        album='OK Computer',
        music='.',
        image='.',
        lyric='Phew, for a minute there, I lost myself, I lost myself',
        description='.',
        review_link='.',
        external='.',
        categories=[benevolent]
    )
    no_surprises = Song(
        title='No Surprises',
        album='OK Computer',
        music='.',
        image='.',
        lyric='I’ll take a quiet life',
        description='.',
        review_link='.',
        external='.',
        categories=[benevolent]
    )
    man_of_war = Song(
        title='Man of War',
        album='OK Computer',
        music='.',
        image='.',
        lyric='Dressed for the kill',
        description='.',
        review_link='.',
        external='.',
        categories=[benevolent]
    )
    just = Song(
        title='Just',
        album='The Bends',
        music='.',
        image='.',
        lyric='You do it to yourself, just you',
        description='.',
        review_link='.',
        external='.',
        categories=[smash]
    )
    high_and_dry = Song(
        title='High And Dry',
        album='The Bends',
        music='.',
        image='.',
        lyric='The best thing that you ever, ever had',
        description='.',
        review_link='.',
        external='.',
        categories=[benevolent]
    )
    fake_plastic_trees = Song(
        title='Fake Plastic Trees',
        album='The Bends',
        music='.',
        image='.',
        lyric='A cracked polystyrene man',
        description='.',
        review_link='.',
        external='.',
        categories=[benevolent]
    )
    talk_show_host = Song(
        title='Talk Show Host',
        album='The Bends',
        music='.',
        image='.',
        lyric='With a gun and a pack of sandwiches and nothing',
        description='.',
        review_link='.',
        external='.',
        categories=[melancholy]
    )
    everything_in_its_right_place = Song(
        title='Everything in its Right Place',
        album='Kid A',
        music='.',
        image='.',
        lyric='Yesterday I woke up sucking on a lemon',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic]
    )
    kid_a = Song(
        title='Kid A',
        album='Kid A',
        music='.',
        image='.',
        lyric='Standing in the shadows at the end of my bed',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic, benevolent]
    )
    national_anthem = Song(
        title='The National Anthem',
        album='Kid A',
        music='.',
        image='.',
        lyric='Everyone, everyone around here',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic]
    )
    idioteque = Song(
        title='Idioteque',
        album='Kid A',
        music='.',
        image='.',
        lyric='Who\'s in a bunker?',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic, smash]
    )
    two_plus_two_equals_five = Song(
        title='2+2=5',
        album='Hail to The Thief',
        music='.',
        image='.',
        lyric='I try to sing along and I get it all wrong',
        description='.',
        review_link='.',
        external='.',
        categories=[melancholy, smash]
    )
    there_there = Song(
        title='There There',
        album='Hail to The Thief',
        music='.',
        image='.',
        lyric='Steer away from these rocks',
        description='.',
        review_link='.',
        external='.',
        categories=[benevolent]
    )
    packt = Song(
        title='Packt Like Sardines in a Crushed Tin Box',
        album='Amnesiac',
        music='.',
        image='.',
        lyric='Get off, get off, get off my case',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic]
    )
    i_might_be_wrong = Song(
        title='I Might Be Wrong',
        album='Amnesiac',
        music='.',
        image='.',
        lyric='If I did not have you?',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic]
    )
    knives_out = Song(
        title='Knives Out',
        album='Amnesiac',
        music='.',
        image='.',
        lyric='I’m not coming back',
        description='.',
        review_link='.',
        external='.',
        categories=[melancholy, erratic]
    )
    lotus_flower = Song(
        title='Lotus Flower',
        album='The King of Limbs',
        music='.',
        image='.',
        lyric='Listen to your heart',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic]
    )
    little_by_little = Song(
        title='Little by Little',
        album='The King of Limbs',
        music='.',
        image='.',
        lyric='The last one out of the box',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic]
    )
    the_daily_mail = Song(
        title='The Daily Mail',
        album='The King of Limbs',
        music='.',
        image='.',
        lyric='Where’s the truth',
        description='.',
        review_link='.',
        external='.',
        categories=[benevolent]
    )
    the_butcher = Song(
        title='The Butcher',
        album='The King of Limbs',
        music='.',
        image='.',
        lyric='My heart still pumping',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic, smash]
    )
    creep = Song(
        title='Creep',
        album='Pablo Honey',
        music='.',
        image='.',
        lyric='You\'re so fucking special',
        description='.',
        review_link='.',
        external='.',
        categories=[benevolent]
    )



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

# bulk add

    db.session.add(decks_dark)
    db.session.add(fifteen_step)
    db.session.add(bodysnatchers)
    db.session.add(nude)
    db.session.add(reckoner)
    db.session.add(house_of_cards)
    db.session.add(jigsaw_falling_into_place)
    db.session.add(bangers_and_mash)
    db.session.add(airbag)
    db.session.add(paranoid_android)
    db.session.add(karma_police)
    db.session.add(no_surprises)
    db.session.add(man_of_war)
    db.session.add(just)
    db.session.add(high_and_dry)
    db.session.add(fake_plastic_trees)
    db.session.add(talk_show_host)
    db.session.add(everything_in_its_right_place)
    db.session.add(kid_a)
    db.session.add(national_anthem)
    db.session.add(idioteque)
    db.session.add(two_plus_two_equals_five)
    db.session.add(there_there)
    db.session.add(packt)
    db.session.add(i_might_be_wrong)
    db.session.add(knives_out)
    db.session.add(lotus_flower)
    db.session.add(little_by_little)
    db.session.add(the_daily_mail)
    db.session.add(the_butcher)
    db.session.add(creep)

    db.session.commit()
