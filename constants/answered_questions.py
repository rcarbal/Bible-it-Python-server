from constants.Book import Book

QUESTION = 'question'
ANSWER = 'answer'
VERSE = 'verse'

ANSWERED_QUESTION = [
    {
        QUESTION: 'when did God create the heavens and the earth?',
        ANSWER: 'in the beginning was everything created by God.',
        VERSE: '{} 1:1'.format(Book.genesis)
    },
    {
        QUESTION: 'what did God create in the beginning?',
        ANSWER: 'God created all the the heavens and the earth in the beginning.',
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
        QUESTION: 'what did God do on the first day of creation?',
        ANSWER: 'God created light, and separated it from darkness. After evening and morning, the first day was '
                'complete.',
        VERSE: '{} 1:5'.format(Book.genesis)
    },
    {
        QUESTION: 'when did God name light "day" and darkness "night"?',
        ANSWER: 'God named light "day" and darkness "night" on the first day creation, after he created light.',
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
        ANSWER: 'When blessing mankind, God stated mankind should rule over all the animals in the world.',
        VERSE: '{} 1:28'.format(Book.genesis)
    },
    {
        QUESTION: 'what did God intend mankind to eat?',
        ANSWER: 'God gave all the plants with seeds, and trees with fruit that have seeds as food for mankind.',
        VERSE: '{} 1:29'.format(Book.genesis)
    },
    {
        QUESTION: 'what did God intend all the animals in the earth to eat?',
        ANSWER: 'God gave all green plant as food for all the animals on earth.',
        VERSE: '{} 1:30'.format(Book.genesis)
    },
    {
        QUESTION: 'when did God create mankind?',
        ANSWER: 'God created mankind on the sixth day of creation.',
        VERSE: '{} 1:26-{} 1:31'.format(Book.genesis, Book.genesis)
    },
    {
        QUESTION: 'when did God create all the animals that walk on land?',
        ANSWER: 'God created all the animals that walk on the ground on the sixth day of creation, along with mankind.',
        VERSE: '{} 1:24-{} 1:25, {} 1:31'.format(Book.genesis, Book.genesis, Book.genesis)
    },

    # Genesis 2
    {
        QUESTION: 'was creation ever completed?',
        ANSWER: 'After the sixth day of creation, it the bible declares that everything was finished.',
        VERSE: '{} 2:1'.format(Book.genesis)
    },
    {
        QUESTION: 'what was completed when God finished creation?',
        ANSWER: 'All the heavens and the earth and all the hosts of them were completed',
        VERSE: '{} 2:1'.format(Book.genesis)
    },
    {
        QUESTION: 'when did God rest after finishing all of creation?',
        ANSWER: 'On the seventh day, good ended his work and rested.',
        VERSE: '{} 2:2'.format(Book.genesis)
    },
    {
        QUESTION: 'how long did it take God to finish everything?',
        ANSWER: 'It took God six days to finish the work of creation.',
        VERSE: '{} 2:2'.format(Book.genesis)
    },
    {
        QUESTION: 'why is the seventh day considered holy?',
        ANSWER: 'The seventh day is holy because God rested from all his work, and he blessed it and made it holy.',
        VERSE: '{} 2:3'.format(Book.genesis)
    },
    {
        QUESTION: 'how was the ground watered before man was created?',
        ANSWER: 'Before God sent rain, the ground was watered by streams that rose from the ground.',
        VERSE: '{} 2:5-{} 2:6'.format(Book.genesis, Book.genesis)
    },
    {
        QUESTION: 'what did God use to form man?',
        ANSWER: 'God used the dust from the ground to form man.',
        VERSE: '{} 2:7'.format(Book.genesis)
    },
    {
        QUESTION: 'how did God form man?',
        ANSWER: 'God took dust from the ground and breathed into his nostrils the breath of life.',
        VERSE: '{} 2:7'.format(Book.genesis)
    },
    {
        QUESTION: 'did God plant a garden in Eden?',
        ANSWER: 'the Lord planted a garden in the east, in Eden.',
        VERSE: '{} 2:8'.format(Book.genesis)
    },
    {
        QUESTION: 'in what direction was the garden of Eden placed?',
        ANSWER: 'the Lord planted the garden of Eden to the east.',
        VERSE: '{} 2:8'.format(Book.genesis)
    },
    {
        QUESTION: 'did God place man in the garden of Eden?',
        ANSWER: 'God placed man in the garden of Eden?',
        VERSE: '{} 2:8'.format(Book.genesis)
    },
    {
        QUESTION: 'what kind of trees did God put in the garden of Eden?',
        ANSWER: 'God made all kinds of beautiful trees in the garden of Eden that were good for food.',
        VERSE: '{} 2:9'.format(Book.genesis)
    },
    {
        QUESTION: 'what was in the middle of the garden of Eden?',
        ANSWER: 'in the middle of the garden God placed the tree of life, and the tree of the knowledge of good and '
                'evil',
        VERSE: '{} 2:9'.format(Book.genesis)
    },
    {
        QUESTION: 'what is the tree of life?',
        ANSWER: 'the tree of life is on of the two trees God placed in the middle of the garden of Eden.',
        VERSE: '{} 2:9'.format(Book.genesis)
    },
    {
        QUESTION: 'what is the tree of knowledge of good and evil?',
        ANSWER: 'the tree of life is on of the two trees God placed in the middle of the garden of Eden.',
        VERSE: '{} 2:9'.format(Book.genesis)
    },
    {
        QUESTION: 'how was the garden of Eden watered?',
        ANSWER: 'a river flowed from the garden of Eden and watered it.',
        VERSE: '{} 2:10'.format(Book.genesis)
    },
    {
        QUESTION: 'did the river that watered the garden of Eden separate into other rivers?',
        ANSWER: 'the river that watered the garden of Eden separated into four other rivers; they are Pishon, Gihon, '
                'Tigris and Euphrates.',
        VERSE: '{} 2:10-{} 2:14'.format(Book.genesis, Book.genesis)
    },
    {
        QUESTION: 'what is the Pishon river?',
        ANSWER: 'When the river that waters the garden of Eden separates into four main rivers, the first is the '
                'Pishon river.',
        VERSE: '{} 2:11'.format(Book.genesis)
    },
    {
        QUESTION: 'where does the Pishon river travel trough?',
        ANSWER: 'The Pishon river travels through the entire land of Havilah.',
        VERSE: '{} 2:11'.format(Book.genesis)
    },
    {
        QUESTION: 'is there gold iin Havilah?',
        ANSWER: 'The gold in the land of Havilah is good, along with resin and onyx.',
        VERSE: '{} 2:11-{} 2:12'.format(Book.genesis, Book.genesis)
    },
    {
        QUESTION: 'What kind of natural resources are found in Havilah?',
        ANSWER: 'Havilah has gold, resin and onyx of good quality.',
        VERSE: '{} 2:11-{} 2:12'.format(Book.genesis, Book.genesis)
    },
    {
        QUESTION: 'what is the Gihon river?',
        ANSWER: 'When the river that waters the garden of Eden separates into four main rivers, the second is the '
                'Gihon river.',
        VERSE: '{} 2:13'.format(Book.genesis)
    },
    {
        QUESTION: 'where does the Gihon river travel through?',
        ANSWER: 'The Gihon river travels through the entire land of Cush.',
        VERSE: '{} 2:13'.format(Book.genesis)
    },
    {
        QUESTION: 'what is the Tigris river?',
        ANSWER: 'When the river that waters the garden of Eden separates into four main rivers, the third is the '
                'Tigris river.',
        VERSE: '{} 2:14'.format(Book.genesis)
    },
    {
        QUESTION: 'where does the Tigris river travel through?',
        ANSWER: 'The Tigris river travels through the east side of Ashur.',
        VERSE: '{} 2:14'.format(Book.genesis)
    },
    {
        QUESTION: 'What is the Euphrates river?',
        ANSWER: 'When the river that waters the garden of Eden separates into four main rivers, the fourth is the '
                'Euphrates river.',
        VERSE: '{} 2:14'.format(Book.genesis)
    },
    {
        QUESTION: 'Why did God put man in the garden of Eden?',
        ANSWER: 'The Lord put man in the garden of Eden to work it and care for it.',
        VERSE: '{} 2:15'.format(Book.genesis)
    },
    {
        QUESTION: 'what did man eat in the garden of Eden?',
        ANSWER: 'man was free to eat from any tree in the garden, except from the tree of the knowledge of good and '
                'evil. ',
        VERSE: '{} 2:15'.format(Book.genesis)
    },
    {
        QUESTION: 'what was man not allowed to eat in the garden of Eden?',
        ANSWER: 'Man was not allowed to eat from the tree of knowledge of good and evil.',
        VERSE: '{} 2:17'.format(Book.genesis)
    },
    {
        QUESTION: 'was man allowed to eat from the tree of knowledge of good and evil?',
        ANSWER: 'Man was not allowed to eat from the tree of knowledge of good and evil.',
        VERSE: '{} 2:17'.format(Book.genesis)
    },
    {
        QUESTION: 'what would happen to man if he ate from the fruit of the tree of knowledge of good and evil?',
        ANSWER: 'God declared that if man ate from the fruit of the tree of knowledge of good and evil, he would '
                'certainly die. ',
        VERSE: '{} 2:17'.format(Book.genesis)
    },
    {
        QUESTION: 'does God want man to be alone?',
        ANSWER: 'The Lord God said, "It is not good for man to be alone."',
        VERSE: '{} 2:18'.format(Book.genesis)
    },
    {
        QUESTION: 'what did God first do to aid mans\' loneliness?',
        ANSWER: 'God brought all the animals of the land and birds of the sky to Adam, so he could name them.',
        VERSE: '{} 2:19'.format(Book.genesis)
    },
    {
        QUESTION: 'did Adam give names to all the animals?',
        ANSWER: 'God gave Adam the task of naming all the animals.',
        VERSE: '{} 2:19'.format(Book.genesis)
    },
    {
        QUESTION: 'was any suitable helper found within the animals for Adam?',
        ANSWER: 'There was no suitable helper found in any animal.',
        VERSE: '{} 2:20'.format(Book.genesis)
    },
    {
        QUESTION: 'how did God remove a rib from Adam?',
        ANSWER: 'God made Adam fall into a deep sleep, and took a rib from him.',
        VERSE: '{} 2:21'.format(Book.genesis)
    },
    {
        QUESTION: 'what did God remove from Adam when he put him to sleep?',
        ANSWER: 'God removed a rib from Adam after putting him in a deep sleep.',
        VERSE: '{} 2:21'.format(Book.genesis)
    },
    {
        QUESTION: 'why did God remove a rib from Adam?',
        ANSWER: 'God removed a rib from Adam to create a woman.',
        VERSE: '{} 2:22'.format(Book.genesis)
    },
    {
        QUESTION: 'what did God create with Adam\'s rib?',
        ANSWER: 'God used Adams\'s rib to create a women.',
        VERSE: '{} 2:22'.format(Book.genesis)
    },
    {
        QUESTION: 'what did adam say when he saw Eve?',
        ANSWER: 'When Adam saw eve he said, "This is now bone of my bone and flesh of my flesh." and named her women',
        VERSE: '{} 2:23'.format(Book.genesis)
    },
    {
        QUESTION: 'Why does man leave his father and mother?',
        ANSWER: 'Man will leave his father and mother to become one with his wife.',
        VERSE: '{} 2:24'
    },
    {
        QUESTION: 'what happens when a man and a women unite?',
        ANSWER: 'When a man and a women unite, they become one flesh.',
        VERSE: '{} 2:24'.format(Book.genesis)
    },
    {
        QUESTION: 'were Adam and Eve naked in the garden of Eden?',
        ANSWER: 'Adam and Eve were naked in garden of Eden, but they were not ashamed.',
        VERSE: '{} 2:25'.format(Book.genesis)
    },
    {
        QUESTION: 'was Adam and Eve ashamed of being naked in the garden of Eden?',
        VERSE: 'Even thou Adam and Eve were naked in the garden of Eden, they were not ashamed.',
        ANSWER: '{} 2:25'.format(Book.genesis)
    },

    # Genesis 3
    {
        QUESTION: 'who was the craftiest animal the Lord had made?',
        ANSWER: 'Of all the animals, the serpent was the craftiest animal the Lord had made.',
        VERSE: '{} 3:1'.format(Book.genesis)
    },
    {
        QUESTION: 'did Eve know she was not suppose to eat the fruit of the three of knowledge of good and evil?',
        ANSWER: 'Eve knew that they were not allowed to touch or eat of the tree that is in the middle of the garden.',
        VERSE: '{} 3:2-{} 3:3'.format(Book.genesis, Book.genesis)
    },
    {
        QUESTION: 'how did the snake trick Eve into eating the fruit.',
        ANSWER: 'The serpent told Eve that if they ate of the fruit of knowledge they would not die.',
        VERSE: '{} 3:4'.format(Book.genesis)
    },
    {
        QUESTION: 'who did the snake trick into eating the fruit?',
        ANSWER: 'The serpent tricked Eve into eating the fruit of knowledge of good and evil.',
        VERSE: '{} 3:4'.format(Book.genesis)
    },
    {
        QUESTION: 'what would happen to Eve if she ate of the fruit of knowledge according to the snake?',
        ANSWER: 'The snake said that she would not die, and she would be like God.',
        VERSE: '{} 3:4-{} 3:5'.format(Book.genesis, Book.genesis)
    },
    {
        QUESTION: 'what did Eve see when she looked at the fruit of knowledge?',
        ANSWER: 'Eve saw that fruit was pleasing to look at and desirable for gaining knowledge.',
        VERSE: '{} 3:6'.format(Book.genesis)
    },
    {
        QUESTION: 'did Eve give to her husband Adam some of the fruit to eat?',
        ANSWER: 'After eating of the fruit of knowledge, she gave some to her husband Adam.',
        VERSE: '{} 3:6'.format(Book.genesis)
    },
    {
        QUESTION: 'did Adam eat of the fruit of knowledge of good and evil?',
        ANSWER: 'After Eve was tricked into eating of the fruit, she gave some to her husband Adam and he ate the '
                'fruit. ',
        VERSE: '{} 3:6'.format(Book.genesis)
    }

]
