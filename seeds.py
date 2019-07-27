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
    radiant = Category(name='Radiant')

    burn_the_witch = Song(
        title='Burn The Witch',
        album='A Moon Shaped Pool',
        music='../assets/resource/music/BurnTheWitch.mp3',
        image='../assets/resource/pictures/burnthewitch.jpg',
        lyric='This is a low flying panic attack',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic, smash]
    )
    daydreaming = Song(
        title='Daydreaming',
        album='A Moon Shaped Pool',
        music='../assets/resource/music/Daydreaming.mp3',
        image='../assets/resource/pictures/anima.jpg',
        lyric='Dreamers, they never learn',
        description='.',
        review_link='.',
        external='.',
        categories=[melancholy]
    )
    true_love_waits = Song(
        title='True Love Waits',
        album='A Moon Shaped Pool',
        music='../assets/resource/music/TrueLoveWaits.mp3',
        image='../assets/resource/pictures/thomslight.jpg',
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
        music='../assets/resource/music/DecksDark.mp3',
        image='../assets/resource/pictures/moonshapedpool.jpg',
        lyric='There’s a spaceship blocking out the sky',
        description='.',
        review_link='.',
        external='.',
        categories=[melancholy]
    )
    fifteen_step = Song(
        title='15 Step',
        album='In Rainbows',
        music='../assets/resource/music/15Step.mp3',
        image='../assets/resource/pictures/inrainbows.jpg',
        lyric='You reel me out when you cut the string',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic]
    )
    bodysnatchers = Song(
        title='Bodysnatchers',
        album='In Rainbows',
        music='../assets/resource/music/Bodysnatchers.mp3',
        image='../assets/resource/pictures/epiclights.jpg',
        lyric='And for anyone else to see, I’m alive',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic, smash]
    )
    nude = Song(
        title='Nude',
        album='In Rainbows',
        music='../assets/resource/music/Nude.mp3',
        image='../assets/resource/pictures/thomdrawing.jpg',
        lyric='You paint yourself white',
        description='.',
        review_link='.',
        external='.',
        categories=[radiant]
    )
    reckoner = Song(
        title='Reckoner',
        album='In Rainbows',
        music='../assets/resource/music/Reckoner.mp3',
        image='../assets/resource/pictures/radioheadart.jpg',
        lyric='Because we separate like ripples on a blank shore',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic, smash, radiant]
    )
    house_of_cards = Song(
        title='House of Cards',
        album='In Rainbows',
        music='../assets/resource/music/HouseOfCards.mp3',
        image='../assets/resource/pictures/inrainbowsart.jpg',
        lyric='Forget about your house of cards and I’ll do mine',
        description='.',
        review_link='.',
        external='.',
        categories=[radiant]
    )
    jigsaw_falling_into_place = Song(
        title='Jigsaw Falling Into Place',
        album='In Rainbows',
        music='../assets/resource/music/JigsawFallingIntoPlace.mp3',
        image='../assets/resource/pictures/fjord.jpg',
        lyric='Words are a sawed off shotgun',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic, smash, radiant]
    )
    bangers_and_mash = Song(
        title='Bangers and Mash',
        album='In Rainbows',
        music='../assets/resource/music/BangersandMash.mp3',
        image='../assets/resource/pictures/glastored.jpg',
        lyric='I got the poison, poison, and now I want more',
        description='.',
        review_link='.',
        external='.',
        categories=[smash]
    )
    airbag = Song(
        title='Airbag',
        album='OK Computer',
        music='../assets/resource/music/Airbag.mp3',
        image='../assets/resource/pictures/OKComputer.jpg',
        lyric='I am born again',
        description='.',
        review_link='.',
        external='.',
        categories=[smash, radiant]
    )
    paranoid_android = Song(
        title='Paranoid Android',
        album='OK Computer',
        music='../assets/resource/music/ParanoidAndroid.mp3',
        image='../assets/resource/pictures/band.jpg',
        lyric='Please could you stop the noise',
        description='.',
        review_link='.',
        external='.',
        categories=[melancholy, erratic]
    )
    karma_police = Song(
        title='Karma Police',
        album='OK Computer',
        music='../assets/resource/music/KarmaPolice.mp3',
        image='../assets/resource/pictures/yorkebow.jpg',
        lyric='Phew, for a minute there, I lost myself, I lost myself',
        description='.',
        review_link='.',
        external='.',
        categories=[radiant]
    )
    no_surprises = Song(
        title='No Surprises',
        album='OK Computer',
        music='../assets/resource/music/NoSurprises.mp3',
        image='../assets/resource/pictures/thomlight.jpg',
        lyric='I’ll take a quiet life',
        description='.',
        review_link='.',
        external='.',
        categories=[radiant]
    )
    man_of_war = Song(
        title='Man of War',
        album='OK Computer',
        music='../assets/resource/music/ManofWar.mp3',
        image='../assets/resource/pictures/manofwar.jpg',
        lyric='Dressed for the kill',
        description='.',
        review_link='.',
        external='.',
        categories=[radiant]
    )
    just = Song(
        title='Just',
        album='The Bends',
        music='../assets/resource/music/Just.mp3',
        image='../assets/resource/pictures/oldbandppic.jpg',
        lyric='You do it to yourself, just you',
        description='.',
        review_link='.',
        external='.',
        categories=[smash]
    )
    high_and_dry = Song(
        title='High And Dry',
        album='The Bends',
        music='../assets/resource/music/HighandDry.mp3',
        image='../assets/resource/pictures/oldtable.jpg',
        lyric='The best thing that you ever, ever had',
        description='.',
        review_link='.',
        external='.',
        categories=[radiant]
    )
    fake_plastic_trees = Song(
        title='Fake Plastic Trees',
        album='The Bends',
        music='../assets/resource/music/FakePlasticTrees.mp3',
        image='../assets/resource/pictures/thompink.jpg',
        lyric='A cracked polystyrene man',
        description='.',
        review_link='.',
        external='.',
        categories=[radiant]
    )
    talk_show_host = Song(
        title='Talk Show Host',
        album='The Bends',
        music='../assets/resource/music/TalkShowHost.mp3',
        image='../assets/resource/pictures/jackets.jpg',
        lyric='With a gun and a pack of sandwiches and nothing',
        description='.',
        review_link='.',
        external='.',
        categories=[melancholy]
    )
    everything_in_its_right_place = Song(
        title='Everything in its Right Place',
        album='Kid A',
        music='../assets/resource/music/EverythinginItsRightPlace.mp3',
        image='../assets/resource/pictures/rhred.jpg',
        lyric='Yesterday I woke up sucking on a lemon',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic]
    )
    kid_a = Song(
        title='Kid A',
        album='Kid A',
        music='../assets/resource/music/KidA.mp3',
        image='../assets/resource/pictures/kidamountains.jpg',
        lyric='Standing in the shadows at the end of my bed',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic, radiant]
    )
    national_anthem = Song(
        title='The National Anthem',
        album='Kid A',
        music='../assets/resource/music/TheNationalAnthem.mp3',
        image='../assets/resource/pictures/jonnyg.jpg',
        lyric='Everyone, everyone around here',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic]
    )
    idioteque = Song(
        title='Idioteque',
        album='Kid A',
        music='../assets/resource/music/Idioteque.mp3',
        image='../assets/resource/pictures/teal.jpg',
        lyric='Who\'s in a bunker?',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic, smash]
    )
    two_plus_two_equals_five = Song(
        title='2+2=5',
        album='Hail to The Thief',
        music='../assets/resource/music/2+2=5.mp3',
        image='../assets/resource/pictures/htttcow.jpg',
        lyric='I try to sing along and I get it all wrong',
        description='.',
        review_link='.',
        external='.',
        categories=[melancholy, smash]
    )
    there_there = Song(
        title='There There',
        album='Hail to The Thief',
        music='../assets/resource/music/ThereThere.mp3',
        image='../assets/resource/pictures/radioheadgpstage.jpg',
        lyric='Steer away from these rocks',
        description='.',
        review_link='.',
        external='.',
        categories=[radiant]
    )
    packt = Song(
        title='Packt Like Sardines in a Crushed Tin Box',
        album='Amnesiac',
        music='../assets/resource/music/PacktLikeSardinesinaCrushdTinBox.mp3',
        image='../assets/resource/pictures/radioheadbeargrass.jpg',
        lyric='Get off, get off, get off my case',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic]
    )
    i_might_be_wrong = Song(
        title='I Might Be Wrong',
        album='Amnesiac',
        music='../assets/resource/music/IMightBeWrong.mp3',
        image='../assets/resource/pictures/planet.jpg',
        lyric='If I did not have you?',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic]
    )
    knives_out = Song(
        title='Knives Out',
        album='Amnesiac',
        music='../assets/resource/music/KnivesOut.mp3',
        image='../assets/resource/pictures/amnesiac.jpg',
        lyric='I’m not coming back',
        description='.',
        review_link='.',
        external='.',
        categories=[melancholy, erratic]
    )
    lotus_flower = Song(
        title='Lotus Flower',
        album='The King of Limbs',
        music='../assets/resource/music/LotusFlower.mp3',
        image='../assets/resource/pictures/thomdance.jpg',
        lyric='Listen to your heart',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic]
    )
    little_by_little = Song(
        title='Little by Little',
        album='The King of Limbs',
        music='../assets/resource/music/LittleByLittle.mp3',
        image='../assets/resource/pictures/artgrey.jpg',
        lyric='The last one out of the box',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic]
    )
    the_daily_mail = Song(
        title='The Daily Mail',
        album='The King of Limbs',
        music='../assets/resource/music/TheDailyMail.mp3',
        image='../assets/resource/pictures/thomjonny.jpg',
        lyric='Where’s the truth',
        description='.',
        review_link='.',
        external='.',
        categories=[radiant]
    )
    the_butcher = Song(
        title='The Butcher',
        album='The King of Limbs',
        music='../assets/resource/music/TheButcher.mp3',
        image='../assets/resource/pictures/nightmare.jpg',
        lyric='My heart still pumping',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic, smash]
    )
    creep = Song(
        title='Creep',
        album='Pablo Honey',
        music='../assets/resource/music/Creep.mp3',
        image='../assets/resource/pictures/creep.jpg',
        lyric='You\'re so fucking special',
        description='.',
        review_link='.',
        external='.',
        categories=[radiant]
    )
    black_star = Song(
        title='Black Star',
        album='The Bends',
        music='../assets/resource/music/BlackStar.mp3',
        image='../assets/resource/pictures/90srh.jpg',
        lyric='Blame it on the satellite that beams me home',
        description='.',
        review_link='.',
        external='.',
        categories=[radiant]
    )
    optimistic = Song(
        title='Optimistic',
        album='Kid A',
        music='../assets/resource/music/Optimistic.mp3',
        image='../assets/resource/pictures/colorful.jpg',
        lyric='This one\'s optimistic',
        description='.',
        review_link='.',
        external='.',
        categories=[radiant, smash]
    )
    go_to_sleep = Song(
        title='Go to Sleep',
        album='Hail to the Thief',
        music='../assets/resource/music/GotoSleep.mp3',
        image='../assets/resource/pictures/greenwoodbros.jpg',
        lyric='May pretty horses come to you as you sleep',
        description='.',
        review_link='.',
        external='.',
        categories=[radiant]
    )
    ful_stop = Song(
        title='Ful Stop',
        album='A Moon Shaped Pool',
        music='../assets/resource/music/FulStop.mp3',
        image='../assets/resource/pictures/blucurtain.jpg',
        lyric='This is a foul tasting medicine',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic, smash]
    )
    you_and_whose_army = Song(
        title='You and Whose Army',
        album='Amnesiac',
        music='../assets/resource/music/YouandWhoseArmy.mp3',
        image='../assets/resource/pictures/bearminecraft.jpg',
        lyric='Holy Roman Empire',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic, radiant]
    )
    paperbag_writer = Song(
        title='Paperbag Writer',
        album='Hail to the Thief',
        music='../assets/resource/music/PaperbagWriter.mp3',
        image='../assets/resource/pictures/redbear.jpg',
        lyric='Blow into this paperbag',
        description='.',
        review_link='.',
        external='.',
        categories=[erratic]
    )
    pop_is_dead = Song(
        title='Pop is Dead',
        album='Pablo Honey',
        music='../assets/resource/music/PopIsDead.mp3',
        image='../assets/resource/pictures/tealthom.jpg',
        lyric='He left this message for us',
        description='.',
        review_link='.',
        external='.',
        categories=[radiant, smash]
    )



    db.session.add(dav)
    db.session.add(wes)
    db.session.add(melancholy)
    db.session.add(erratic)
    db.session.add(smash)
    db.session.add(radiant)
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
    db.session.add(black_star)
    db.session.add(optimistic)
    db.session.add(go_to_sleep)
    db.session.add(ful_stop)
    db.session.add(you_and_whose_army)
    db.session.add(paperbag_writer)
    db.session.add(pop_is_dead)

    db.session.commit()
