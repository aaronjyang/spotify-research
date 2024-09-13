import database as db

leftovers2018 = db.load("2018leftovers")
leftovers2019 = db.load("2019leftovers")
leftovers2020 = db.load("2020leftovers")
leftovers2021 = db.load("2021leftovers")
leftovers2022 = db.load("2022leftovers")
leftovers2023 = db.load("2023leftovers")




leftoverCodes = {
    ('Home', 'Machine Gun Kelly, X Ambassadors & Bebe Rexha'): "0OI7AFifLSoGzpb8bdBLLV",
    ('F**k Love', 'XXXTENTACION Featuring Trippie Redd'): "7AQim7LbvFVZJE3O8TYgf2",
    ('La Modelo', 'Ozuna x Cardi B'): "2SbzdGpOKlH3HIAGTWTbwU",
    ('Sorry Not Sorry', 'Demi Lovato'): "0yvPEnB032fojLfVluFjUv",
    ('Criminal', 'Natti Natasha x Ozuna'): "6Za3190Sbw39BBC77WSS1C",
    ('Look Alive', 'BlocBoy JB Featuring Drake'): "7165YDcOpr9yEypbdpU6fa",
    ('Found / Tonight', 'Lin-Manuel Miranda & Ben Platt'): "0ileL1L3Vtpf5VZ5RQZ94m",
    ('Guatemala', 'Swae Lee Featuring Slim Jxmmi'): "0TCnOEVeLQMXOUrpPlM7uY", 
    ('Dame Tu Cosita', 'Pitbull x El Chombo x Karol G Featuring Cutty Ranks'): "09SNuR471zu5nVvC4IVG8j",
    ('Kream', 'Iggy Azalea Feauring Tyga'): "5mu1uv8RmzDkF8foePK5qa",
    ('Ganja Burns', 'Nicki Minaj'): "3LHYmz86DxGInsRp3wiiW5",
    ('Thunderclouds', 'Labrinth, Sia & Diplo Present... LSD'): "7nLK5rjEy6LPZNPG1BXxu7",
    ('Rap Devil', 'Machine Gun Kelly'): "63TyoT9Ee03rQxv8xmdJ2l",
    ('Vaina Loca', 'Ozuna x Manuel Turizo'): "48zFZh27QU5qsrBjn4C2FA",
    ('Electricity', 'Silk City x Dua Lipa'): "5N4erncE7kuUccm7zEmwzk",
    ('Dope N****z', 'Lil Wayne Featuring Snoop Dogg'): "2AwyHlbA6f641SEkizD5JG",
    ("(There's No Place Like) Home For The Holidays (1959)", 'Perry Como With Mitchell Ayers And His Orchestra'): "2GapxG7BxK55ihQRAlR39e",
    ('95.south', 'J. Cole'): "5R691ipUYRDYW6ehapjoj6",
    ('My Universe', 'Coldplay x BTS'): "3FeVmId7tL5YN8B7R3imoM",
    ('Switch A N*gga Out', 'Summer Walker'): "5Mv7yjian35AddlklJgg1v",
    ('Classy 101', 'Feid x Young Miko'): "6XSqqQIy7Lm7SnwxS4NrGx", 
    ('Baguettes In The Face', 'Mustard featuring NAV, Playboi Carti & A Boogie Wit da Hoodie'): "2zjGJ0dChMR0KxBZS15aqo",
    ("punchin'.the.clock", 'J. Cole'): "57ZUX6TNyKLBydAdVVd02x",
    ('Brown Skin Girl', 'Beyonce, SAINt JHN & Wizkid Featuring Blue Ivy Carter'): "0B3FovCVaGKS5w1FTidEUP",
    ('Bloody Valentine', 'Machine Gun Kelly'): "6mADjHs6FXdroPzEGW6KVJ",
    ('Call Me Everyday', 'Chris Brown Featuring WizKid'): "7vVs4XCsQyGn1Au3drvo9Z",
    ("I'll Be Home For Christmas", 'Bing Crosby With John Scott Trotter And His Orchestra'): "4lftz0V8DZhWSVtL4GrzMH",
    ('AMG', 'Gabito Ballesteros, Peso Pluma & Natanael Cano'): "1lRtH4FszTrwwlK5gTSbXO", 
    ('Papercuts', 'Machine Gun Kelly'): "3nkW3TPQjBip1lER4h78NX", 
    ('Rich Men North Of Richmond', 'Oliver Anthony Music'): "78Du4CMFgnhdlG33gblkiP", 
    ('Fucking Fans', 'Drake'): "3RkNXZvOSMMElmmXztDc94", 
    ('Ran$om', 'Lil Tecca'): "1lOe9qE0vR9zwWQAOk6CoO", 
    ('El Azul', 'Junior H x Peso Pluma'): "1haJsMtoBhHfvuM7XWuT3W", 
    ('After Last Night', 'Silk Sonic (Bruno Mars & Anderson .Paak) With Thundercat & Bootsy Collins'): "6jGAh1bFnXt1Muj9zeHveZ", 
    ('Forget Me Too', 'Machine Gun Kelly & Halsey'): "1VSuFS7PahCN3SWbOcQ98m", 
    ('the.climb.back', 'J. Cole'): "5lLNBIyjp72btcnrjBG751", 
    ('Quema', 'Ryan Castro x Pe$o Pluma'): "2hn2zOA2XFlv6DSmesylrL", 
    ('Fragil', 'Yahritza y Su Esencia x Grupo Frontera'): "4JdSXF2p71cr8uCY3UiJM0", 
    ('Skate', 'Silk Sonic (Bruno Mars & Anderson .Paak)'): "3WTWh2WDk4j8GUCGj4xfOd", 
    ('Smokin Out The Window', 'Silk Sonic (Bruno Mars & Anderson .Paak)'): "1oERlssLrpssCAY6Yqqs6c", 
    ('One Too Many', 'Keith Urban Duet With P!nk'): "5NUXE8W12lWcUXgJRCjeEw", 
    ('Hellcats & Trackhawks', 'Lil Durk'): "53tv6ZbyeAwfAUwFaxYbfO", 
    ('Bipolar', 'Peso Pluma x Jasiel Nunez x Junior H'): "3wlIAXSDtlD9iU8ysld06Z", 
    ('F**k The Industry Pt. 2', 'YoungBoy Never Broke Again'): "5leAk8qQS6HGWwEvpyWSqd", 
    ('Plebada', 'El Alfa x Peso Pluma'): "7uSLF2yhpjLlYBLtyPX3Lb", 
    ('At The End Of A Bar', 'Chris Young With Mitchell Tenpenny'): "2NYOqKy4VX6dqVtzrv1Cx9", 
    ('Constant Bulls**t', 'Summer Walker'): "1luvsaicSpNDRLgOtRZxWO", 
    ('Past Life', 'Trevor Daniel x Selena Gomez'): "7MN8RYSofZsFROBlEOAzXq", 
    ('ZaZa', '6ix9ine'): "5cMoYjSCddCVVRUiVRv88q", 
    ('Know Your Worth', 'Khalid x Disclosure'): "0TrPqhAMoaKUFLR7iYDokf", 
    ('Put On A Smile', 'Silk Sonic (Bruno Mars & Anderson .Paak)'): "5lka5RUbLVQGO94mKAPMRO", 
    ('You', 'Regard x Troye Sivan x Tate McRae'): "2cc8Sw1OnCuA5bV8nqWqpE", 
    ('Fly As Me', 'Silk Sonic (Bruno Mars & Anderson .Paak)'): "7suB6D6uKX5DfPukdGaz0W", 
    ('TQG', 'Karol G x Shakira'): "0DWdj2oZMBFSzRsi2Cvfzf", 
    ('pride.is.the.devil', 'J. Cole & Lil Baby'): "5W8jRrZ6tWrTrqnKRtIQBf", 
    ('Emo Girl', 'Machine Gun Kelly & WILLOW'): "3tBZ60j1jQ7NJm8IjelyQe", 
    ('Ay!', 'Machine Gun Kelly & Lil Wayne'): "1T4tQ4SSagbhAKpvcWg035", 
    ('Be Like That', 'Kane Brown With Swae Lee & Khalid'): "5f1joOtoMeyppIcJGZQvqJ", 
    ('Stop Snitching', 'YG'): "5IjRKZlpKVBBRn0COL7pik", 
    ('After Hours', 'The Weeknd'): "2p8IUWQDrpjuFltbdgLOag", 
    ('applying.pressure', 'J. Cole'): "1d7q712nXjG98HiwHk7HFS", 
    ("I'm Dat N***a", 'Future'): "0AAVJIN4plafvmNKqRCltG", 
    ('hunger.on.hillside', 'J. Cole & Bas'): "5BwQjRasNcdRPuVWKcHto2", 
    ('Mr. Solo Dolo III', 'Kid Cudi'): "27oVCAziETRbNuo5A8LNpg", 
    ('Drunk Face', 'Machine Gun Kelly'): "3k0YJnqMKRZb8swo86vCkq", 
    ('Look What God Gave Her', 'Thomas Rhett'): "2KqJC0koTBUyDlsMt5ok1V", 
    ("100.mil'", 'J. Cole & Bas'): "4n6NDfYake476trCjJRNl0", 
    ('Maybe', 'Machine Gun Kelly & Bring Me The Horizon'): "25wdC7CJmCJPgnKw9rYquJ", 
    ('Crazy Story 2.0', 'King Von Featuring Lil Durk'): "6V20oVETqPBJ4suIEoEkIY", 
    ('Sigues Con El', 'Arcangel x Sech'): "7sQKy5vlPQllr0k9IjYJv3", 
    ('Real Shit', 'Juice WRLD x benny blanco'): "3uVPLtkmDu8pDkYEAVqbgS", 
    ('La Jeepeta', 'Nio Garcia x Anuel AA x Myke Towers x Brray x Juanka'): "1mohfLaTJtB2RplHLQVM70", 
    ('Lose Control', 'Teddy Swims'): "6usohdchdzW9oML7VC4Uhk", 
    ('The Other Girl', 'Kelsea Ballerini x Halsey'): "3CS5zwqrjggxlRD0QGJAva", 
    ('transparentsoul', 'Willow Featuring Travis Barker'): "1QL7nSDZCwZMnbisV4KOXt", 
    ('Daywalker!', 'Machine Gun Kelly & CORPSE'): "2NnJpRXIlx35Vij3bPZO0h", 
    ('How About Now', 'Drake'): "4n4BflhWjCHIxrI4v7Xt9s", 
    ("My Ex's Best Friend", 'Machine Gun Kelly X blackbear'): "7kDUspsoYfLkWnZR7qwHZl", 
    ('Make Up Sex', 'Machine Gun Kelly X blackbear'): "50eJOxJiGmJ7PBZaTKpje1", 
    ('Thank God', 'Kane Brown With Katelyn Brown'): "1brnLTvarI9D1hLP6z2Ar8", 
    ("Don't Pretend", 'Khalid x SAFE'): "1E6DEDWDKHoOW0fcFuDghV", 
    ('Come & Go', 'Juice WRLD x Marshmello'): "2Y0wPrPQBrGhoLn14xRYCG", 
    ('Lose', 'KSI x Lil Wayne'): "46vNe30zHBP2HUaYjqjL5g", 
    ('Blue Note$ II', 'Meek Mill Featuring Lil Uzi Vert'): "2kdhiombBoiHjvSKG3EI0m", 
    ('Blast Off', 'Silk Sonic (Bruno Mars & Anderson .Paak)'): "2NqyjfDXy0XfXCSPXMsKzi", 
    ('Just The Way', 'Parmalee x Blanco Brown'): "4h5OVQQbeqw3lNaFIbmlzG", 
    ('Caramelo', 'Ozuna x Karol G x Myke Towers'): "2uu2aGqA2UblCg581Q7l1g", 
    ('Gatubela', 'Karol G x Maldy'): "1ga4PztXOIw1yBbdUt2X8v", 
    ('Stuck In A Dream', 'Lil Mosey x Gunna'): '7iHHxY2NLlJRAmlAmC4ahQ', 
    ('No Love', 'Summer Walker & SZA'): '08SB2OtZkaliju77WYEKxk', 
    ('Volvi', 'Aventura x Bad Bunny'): "2vmfvSoZBFAt9hhRoEByLi", 
    ('Leave The Door Open', 'Silk Sonic (Bruno Mars & Anderson .Paak)'): "4pryE6cN2gFL1FVF5fYINl", 
    ('On Wat U On', 'Moneybagg Yo x GloRilla'): "2Q2mcoXVkioh4OBcL8mm4p", 
    ('Baila Baila Baila', 'Ozuna x Daddy Yankee x J Balvin x Farruko x Anuel AA'): "7mWFF4gPADjTQjC97CgFVt", 
    ('No Dribble', 'DaBaby x Stunna 4 Vegas'): "1gIlID64VBhXDDnzGDdn09", 
    ('Blinding Lights', 'The Weeknd'): "0VjIjW4GlUZAMYd2vXMi3b", 
    ('B*tch From da Souf', 'Mulatto'): "6tLWt7gkvvTSjS6OfJjiyJ", 
    ('Que Onda', 'Calle 24 x Chino Pacas x Fuerza Regida'): "6uIIdjYTxxpWOyWuVXrKQO", 
    ('Savage Love (Laxed - Siren Beat)', 'Jawsh 685 x Jason Derulo'): "1xQ6trAsedVPCdbtDAmk0c", 
    ('All These N**gas', 'King Von Featuring Lil Durk'): "4g27tVPyGHi38dczFoJZZy", 
    ('let.go.my.hand', 'J. Cole, Bas & 6LACK'): "0GAyuCo975IHGxxiLKDufB", 
    ('Leave Em Alone', 'Layton Greene, Lil Baby, City Girls & PnB Rock'): "1bIEvOOqf2V3QBrFiClE3Y"
}
songs = []
for x in leftovers2019 + leftovers2020 + leftovers2021 + leftovers2022 + leftovers2023:
    for y in x[1]:
        songs.append(y)
for x in set(songs):
    if (leftoverCodes.get(x) != None):
        print(x)


'''
print(leftoverCodes.get("dsfdfdsf"))
for x in leftovers2018:
    for y in x[1]:
        print(leftoverCodes.get(y))
'''