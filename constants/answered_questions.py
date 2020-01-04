from constants.Book import Book

QUESTION = 'question'
ANSWER = 'answer'
VERSE = 'verse'

ANSWERED_QUESTION = [
    {
        QUESTION: 'when did God create the heavens and the earth?',
        ANSWER: 'in the beginning.',
        VERSE: '{} 1:1'.format(Book.genesis)
    },
    {
        QUESTION: 'what did God create in the beginning?',
        ANSWER: 'the heavens and the earth.',
        VERSE: '{} 1:1'.format(Book.genesis)
    },
    {
        QUESTION: 'who created everything in the beginning?',
        ANSWER: 'God',
        VERSE: '{} 1:1'.format(Book.genesis)
    },
    {
        QUESTION: 'what was the earth like in the beginning?',
        ANSWER: 'The earth was formless and empty.',
        VERSE: '{} 1:2'.format(Book.genesis)
    },
    {
        QUESTION: 'was the Holy Spirit present on earth in the beginning?',
        ANSWER: 'the spirit of God was hovering over the waters before the earth was ordered.',
        VERSE: '{} 1:2'.format(Book.genesis)
    },
    {
        QUESTION: 'how did God create light?',
        ANSWER: 'God spoke light into existence.',
        VERSE: '{} 1:3'.format(Book.genesis)
    },

    # Genesis 1:4 "And God saw that light was good, and he separated the light from the darkness.
    {
        QUESTION: 'how did God perceive light, after he created it?',
        ANSWER: 'God saw it that light was good after he spoke it into existence.',
        VERSE: '{} 1:4'.format(Book.genesis)
    },
    {
        QUESTION: 'where does it say that light is good?',
        ANSWER: 'In Genesis chapter 1, verse 4, it is written that God saw that the light was good after he created it.',
        VERSE: '{} 1:4'.format(Book.genesis)
    },
    {
        QUESTION: 'what did God do on the first day?',
        ANSWER: 'God created light, and separated it from darkness. After evening and morning, the first day was '
                'complete.',
        VERSE: '{} 1:5'.format(Book.genesis)
    },
    {
        QUESTION: 'when did God name light "day" and darkness "night"?',
        ANSWER: 'God named light "day" and darkness "night" on the first day, after he created light?',
        VERSE: '{} 1:5'.format(Book.genesis)
    },
    {
        QUESTION: 'when did God create light?',
        ANSWER: 'God created light on the first day of creation.',
        VERSE: '{} 1:5'.format(Book.genesis)
    },
    {
        QUESTION: 'how did God create the skies?',
        ANSWER: 'And God said, "Let there be vault between waters to separate waters from waters,'
                '", so God made a space that is now the atmosphere.',
        VERSE: '{} 1:6'.format(Book.genesis)
    },
    {
        QUESTION: 'did God separate waters that were on top of waters when creating the skies?',
        ANSWER: 'Yes, the bible says that to create the skies God separated the waters and put a vault between them.',
        VERSE: '{} 1:7'.format(Book.genesis)
    },
    {
        QUESTION: 'how do we know that the space God made between the waters was the sky?',
        ANSWER: 'after God created the vault (expanse, space) between the waters above and below he called it sky.',
        VERSE: '{} 1:7-{} 1:8'.format(Book.genesis, Book.genesis)
    },
    {
        QUESTION: 'what day did God create the sky on earth.',
        ANSWER: 'God created the skies on earth on the second day of creation.',
        VERSE: '{} 1:8'.format(Book.genesis)
    },
    {
        QUESTION: 'how did God create the land we walk on?',
        ANSWER: 'On the third day of creation God commanded the waters be gathered to one place, and dry ground '
                'appeared.',
        VERSE: '{} 1:9'.format(Book.genesis)
    },
    {
        QUESTION: 'did God name the land and sea?',
        ANSWER: 'After creating dry ground, God named it "land", and after gathering the waters he called them "seas".',
        VERSE: '{} 1:10'.format(Book.genesis)
    },
    {
        QUESTION: 'how did God create plants and trees?',
        ANSWER: 'God spoke, and commanded the dry land to produce vegetation.',
        VERSE: '{} 1:11'.format(Book.genesis)
    },
    {
        QUESTION: "how did the dry land respond to God's command to produce vegetation?",
        ANSWER: "When God commanded, the dry land responded by producing fruit bearing trees and vegetation that had "
                "seeds.  Creation always responds according to God's will and decrees.",
        VERSE: "{} 1:11-{} 1:12".format(Book.genesis, Book.genesis)
    },
    {
        QUESTION: 'In what day did God create the skies, seas and vegetation?',
        ANSWER: 'God created the skies along with the seas, dry land, and vegetation on the third day of creation.',
        VERSE: '{} 1:9-{} 1:13'.format(Book.genesis, Book.genesis)
    },
    {
        QUESTION: "what was God's command for creating the sun and the moon.",
        ANSWER: "In Genesis chapter 1 verse 14 we find God's command for creating the sun and the moon.",
        VERSE: "{} 1:14".format(Book.genesis)
    },
    {
        QUESTION: "what is the purpose for the sun and moon.",
        ANSWER: "God purpose for the sun and moon were and still are to bring light over the earth.",
        VERSE: "{} 1:15-{} 1:18".format(Book.genesis, Book.genesis)
    },
    {
        QUESTION: 'did God make the sun, moon and stars?',
        ANSWER: "God made the sun and moon to and stars, each with its purpose, to bring light to day time and night "
                "time. ",
        VERSE: '{} 1:16'.format(Book.genesis)
    },
    {
        QUESTION: 'does God want to separate the light from darkness?',
        ANSWER: "In God's perfect creation, his will is to separate light from darkness.",
        VERSE: '{} 1:18'.format(Book.genesis)
    },
    {
        QUESTION: 'when did God create the sun, moon and stars',
        ANSWER: "God created the sun, moon and stars on the fourth day",
        VERSE: '{} 1:14- {} 1:19'.format(Book.genesis, Book.genesis)
    },
    {
        QUESTION: 'What was God command to create fish and birds',
        ANSWER: "God's command to create fish and birds can be found in Genesis chapter 1 verse 20.",
        VERSE : '{} 1:20'.format(Book.genesis)
    },
    {
        QUESTION: "did God create the all the creatures in the sea, and all the creautres that fly?",
        ANSWER: 'on the fifth day of creation God created all animals that live in the sea and all the animals that '
                'fly in the sky.',
        VERSE: "{} 1:21".format(Book.genesis)
    },
    {
        QUESTION: "did God bless the fish and birds?",
        ANSWER: "After creating all the creatures in the sea and all the creatures that fly in the sky he blessed "
                "them.  God commanded them to increase in number to fill the earth and sea.",
        VERSE: "{} 1:23".format(Book.genesis)
    },
    {
        QUESTION: "when did God create all the sea creatures and birds of the sky?",
        ANSWER: "God created all the sea creatures and the birds on the fifth day of creation.",
        VERSE: "{} 1:23".format(Book.genesis)
    },
    {
        QUESTION: "what was God command to create the walk on the ground?",
        ANSWER: 'you can find God\'s command for the land to produce all the creatures that walk in the ground in the '
                'book of Genesis chapter 1 verse 25.',
        VERSE: "{} 1:24".format(Book.genesis)
    },
    {
        QUESTION: 'did God create the animals that walk on the land?',
        ANSWER: "God created all the animals of the land.",
        VERSE: '{} 1:25'.format(Book.genesis)
    },
    {
        QUESTION: 'did God create man according to his image?',
        ANSWER: 'God declared man would be according to his likeness, and image.',
        VERSE: '{} 1:26-{} 1:27'.format(Book.genesis, Book.genesis)
    },
    {
        QUESTION: 'did God give mankind authority over all the animals?',
        ANSWER: 'When creating mankind, God declared that they would rule over all fish, bird and animal that walked '
                'in the ground.',
        VERSE: '{} 1:26'.format(Book.genesis)
    },
    {
        QUESTION: 'how many genders did God create for mankind?',
        ANSWER: 'God created two genders for mankind, male and female.',
        VERSE: '{} 1:27'.format(Book.genesis)
    },
    {
        QUESTION: 'does God want mankind to populate the earth?',
        ANSWER: 'God commanded mankind to be fruitful, increase in number and populate the earth?',
        VERSE: '{} 1:28'.format(Book.genesis)
    },
    {
        QUESTION: 'did God intend mankind to rule over all the animals?',
        ANSWER: 'When blessing man kind, God stated mankind should rule over all the animals in the world.',
        VERSE: '{} 1:28'.format(Book.genesis)
    }
]
