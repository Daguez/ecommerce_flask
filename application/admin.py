from flask import Blueprint
from sqlalchemy.exc import SQLAlchemyError
from . import db
from application.model import Item

# admin Blueprint
adminbp = Blueprint('admin', __name__, url_prefix='/admin/')


# Data for loading in the database

@adminbp.route('/dbseed/')
@adminbp.route('test')
def dbseed():
    item1 = Item(id=1, name='Darth Vader', image='darthvader.jpg', \
                 description='<p>Kids and fans alike can imagine the biggest battles and missions in the Star Wars saga with figures from The Black Series!</p> <p>With exquisite features and decoration, this series embodies the quality and realism that Star Wars devotees love. Once a heroic Jedi Knight, Darth Vader was seduced by the dark side of the Force, became a Sith Lord, and led the Empire’s eradication of the Jedi Order. He remained in service of the Emperor for decades, enforcing his Master’s will and seeking to crush the fledgling Rebel Alliance.</p> <p> This 6-inch-scale Darth Vader figure is carefully detailed to look like the Sith Lord from Star Wars: A New Hope. This figure features premium detail and multiple points of articulation, and includes a character-specific accessory.</p> <p>Star Wars products are produced by Hasbro under license from Lucasfilm Ltd. Hasbro and all related terms are trademarks of Hasbro.</p>', \
                 itemShort='Kids and fans alike can imagine the biggest battles and missions in the Star Wars saga.',
                 price=30.00, category=2)
    item11 = Item(id=11, name='Gamorean gard', image='gam7.jpg', \
                  description='''<p>This Gamorrean Guard was released individually carded in November 2010 as part of The Vintage Collection. Gamorrean Guard's can be seen in The Return Of The Jedi inside of Jabba's Palace.</p>
<p>The figure has a total of 14 joints, including ball-joints in the neck, shoulders, elbows, knees and ankles. The wrists, the waist and both legs are swivel-jointed. The figure has absolutely no balancing problems, even with both arms raised and weapons in both hands. All three weapons (2 different axes, vibrostaff) fit very well into either of the Gamorrean Guard's hands. The helmet sits a little loose, but it has the perfect size to cover the entire back, and looks overall
    nice. The soft-goods skirt can be lifted, but it's glued in place and can't be removed. The hard to see harness/belt can be taken off if you'd like to display the figure without it.</p>
<p>The paint application on the Gamorrean Guard is perfectly executed, especially the paint application in the facial area is fantastic. The entire sculpt is one of the best Hasbro has ever released of an action figure. The scale is right, the
    likeness is spot-on, and the joints are well hidden. Add to that, that it's a super articulated sculpt! This figure turned out so well that it's well worth picking up several of them to fill your Jabba's Palace diorama. </p>
<p>Another bonus is that Hasbro included three different weapons, so if you choose to pick up more than just one Gamorrean Guard, you can make them look a little different by having them carry different weapons. </p>
<p>To sum it all up, this Gamorrean Guard is a
    perfect 10 out of 10 and one of the best Star Wars figures Hasbro has released as of 2010.</p>
''',
                  itemShort='This Gamorrean Guard was released individually carded in November 2010 as part of The Vintage Collection''', \
                  price=29.99, category=2)
    item3 = Item(id=3, name='Mandalorian', image='manda.jpg', \
                 description='''<p>The Mandalorian is battle-worn and tight-lipped, a formidable bounty hunter in an increasingly dangerous galaxy!</p>

<p>Kids and collectors alike can imagine the biggest battles and missions in the Star Wars saga with figures from Star Wars The Black Series! With exquisite features and decoration, this series embodies the quality and realism that Star Wars devotees love. Star Wars The Black Series includes figures, vehicles, and roleplay items from the 40-plus-year legacy of the Star Wars Galaxy, including comics, movies, and animated series. (Additional products each sold separately. Subject to availability.)</p>

<p>The 6-inch scale Black Series figure is carefully detailed to look like the character from The Mandalorian live-action TV series, featuring premium detail and multiple points of articulation.</p>

<p>May the Force be with you!</p>''',
                 itemShort='The Mandalorian is battle-worn and tight-lipped, a formidable bounty hunter in an increasingly ...', \
                 price=25.99, category=2)
    item4 = Item(id=4, name='Snowspeeder', image='snow.jpg', \
                 description='''<p>Kids and collectors alike can imagine the biggest battles and missions in the Star Wars saga with toys from Star Wars The Black Series! With exquisite features and decoration, this series embodies the quality and realism that Star Wars devotees love. Star Wars The Black Series includes figures, vehicles, and roleplay items from the 40-plus-year legacy of the Star Wars Galaxy, including comics, movies, and animated series. (Additional products each sold separately. Subject to availability.)</p>
<p>The 6-inch-scale Black Series snowspeeder vehicle with Dak Ralter action figure are detailed to look like the vehicle and character from Star Wars: The Empire Strikes Back, featuring premium detail and multiple points of articulation.</p>
<p>Star Wars products are produced by Hasbro under license from Lucasfilm Ltd.</p>
<p>Hasbro and all related terms are trademarks of Hasbro.</p>

<p>SNOWSPEEDER: On Hoth, the Rebels modified T-47 airspeeders to become snowspeeders, fast flying conveyances for patrol and defense of their hidden base</p>
<p>STAR WARS: THE EMPIRE STRIKES BACK: Fans and collectors can imagine scenes from the Star Wars</p>
''', itemShort='On Hoth, the Rebels modified T-47 airspeeders to become snowspeeders, fast flying conveyances ...', \
                 price=235.45, category=1)
    item5 = Item(id=5, name='Boba Fett’s Slave I', image='slave.jpg', \
                 description='''<p>It was on the Slave I that Boba Fett transported a carbonite-frozen Han Solo to the vile gangster Jabba the Hutt on Tatooine, collecting on a long-standing reward for the former smuggler.</p>
<p>Celebrate the legacy of Star Wars, the action-and-adventure-packed space saga from a galaxy far, far away, with premium 3.75-inch scale vehicles from Star Wars The Vintage Collection. Vehicles feature premium detail and design across product and packaging inspired by the original line, as well as the movie-inspired collector grade deco that fans have come to know and love. (Additional products each sold separately. Subject to availability.)</p>
<p>Featuring premium detail inspired by Star Wars: The Empire Strikes Back, this collectible Star Wars The Vintage Collection 3.75-inch-scale vehicle makes a great gift for Star Wars fans and collectors.</p>
<p>Star Wars products are produced by Hasbro under license from Lucasfilm Ltd.
Hasbro and all related terms are trademarks of Hasbro.</p>

<p>SLAVE I: The deadly Slave I was infamous for its association with two bounty hunters who wore Mandalorian armor: first Jango Fett, then it was inherited by Boba Fett</p>
''',
                 itemShort='The deadly Slave I was infamous for its association with two bounty hunters who wore Mandalorian armor.', \
                 price=205.00, category=1)
    item6 = Item(id=6, name='Poe Dameron’s X-Wing Fighter.', image='xwing.jpg', \
                 description='''<p>Faster than the Alliance-era T-65s, Resistance X-Wings are maneuverable enough to engage TIE Fighters in dogfights, yet still hold considerable firepower.</p>

<p>Celebrate the legacy of Star Wars, the action-and-adventure-packed space saga from a galaxy far, far away, with premium 3.75-inch scale vehicles from Star Wars The Vintage Collection. Vehicles feature premium detail and design across product and packaging inspired by the original line, as well as the movie-real collector grade deco that fans have come to know and love. (Additional products each sold separately. Subject to availability.)</p>

<p>Featuring premium detail inspired by Star Wars: The Rise of Skywalker, this collectible Star Wars The Vintage Collection 3.75-inch-scale vehicle makes a great gift for Star Wars fans and collectors.</p>

<p>Star Wars products are produced by Hasbro under license from Lucasfilm Ltd.
Hasbro and all related terms are trademarks of Hasbro.</p>''',
                 itemShort='Resistance X-Wings are maneuverable enough to engage TIE Fighters in dogfights', \
                 price=199.00, category=1)
    item7 = Item(id=7, name='Mandalorian Imperial Troop Transport', image='imper.jpg', \
                 description='''<p>Imperial Troop Transports weren’t war machines like AT-AT or AT-DP walkers, but these deadly-looking craft still proved effective at ferrying troops to the battlefield, controlling crowds, and dealing with small-scale threats.</p>
<p>Celebrate the legacy of Star Wars, the action-and-adventure-packed space saga from a galaxy far, far away, with premium 3.75-inch scale vehicles from Star Wars The Vintage Collection. Vehicles feature premium detail and design across product and packaging inspired by the original line, as well as the movie-real collector grade deco that fans have come to know and love. (Additional products each sold separately. Subject to availability.)</p>
<p>Featuring premium detail inspired by The Mandalorian live-action TV series, this collectible Star Wars The Vintage Collection 3.75-inch-scale vehicle makes a great gift for Star Wars fans and collectors.</p>
<p>Star Wars products are produced by Hasbro under license from Lucasfilm Ltd.</p>
<p>Hasbro and all related terms are trademarks of Hasbro.</p>

<p>IMPERIAL TROOP TRANSPORT: The Imperial Troop Transport was used to move the Empire’s soldiers</p>
''',
                 itemShort='The Imperial Troop Transport was used to move the Empire’s soldiers. These deadly-looking craft...', \
                 price=215.00, category=1)
    item8 = Item(id=8, name='Sith Trooper', image='sithtrooper.jpg', \
                 description='''<p>Specialized Stormtroopers of the First Order, Sith Jet Troopers soar into battle equipped with agile rocket packs!<p>

<p>Celebrate the legacy of Star Wars, the action-and-adventure-packed space saga from a galaxy far, far away, with premium 3.75-inch scale figures and vehicles from Star Wars The Vintage Collection. Figures feature premium detail and design across product and packaging inspired by the original line, as well as the movie- inspired collector grade deco that fans have come to know and love. (Additional products each sold separately. Subject to availability.)</p>

<p>Featuring premium detail and design inspired by Star Wars: The Rise of Skywalker, this collectible Star Wars The Vintage Collection 3.75-inch-scale Sith Jet Trooper action figure makes a great gift for Star Wars fans and collectors.</p>

<p>Star Wars products are produced by Hasbro under license from Lucasfilm Ltd</p>''', \
                 itemShort='Specialized Stormtroopers of the First Order, Sith Jet Troopers soar into battle equipped with agile rocket packs!', \
                 price=26.45, category=2)
    item9 = Item(id=9, name='Jawa', image='jawa.jpg', \
                 description='''<p>Jawas that arrive on new planets continue their old habits in their new surroundings, but their obsessive need for technology still drives them.</p>

<p>Kids and collectors alike can imagine the biggest battles and missions in the Star Wars saga with figures from Star Wars The Black Series! With exquisite features and decoration, this series embodies the quality and realism that Star Wars devotees love. Star Wars The Black Series includes figures, vehicles, and roleplay items from the 40-plus-year legacy of the Star Wars Galaxy, including comics, movies, and animated series. (Additional products each sold separately. Subject to availability.)</p>

<p>The 6-inch scale Black Series Offworld Jawa figure is carefully detailed to look like the character from The Mandalorian live-action TV series, featuring premium detail and multiple points of articulation.</p>

<p><em>May the Force be with you!</em></p>
<p>Star Wars products are produced by Hasbro under license from Lucasfilm Ltd.</p>''',
                 itemShort='Jawas that arrive on new planets continue their old habits in their new surroundings, but their obsessive need for...', \
                 price=29.90, category=2)
    item10 = Item(id=10, name='Boba Feet', image='boba.jpg', \
                  description=''' <p>The notorious bounty hunter Boba Fett prepares to deliver the carbonite-frozen Han Solo to Jabba the Hutt.</p>

<p>The most epic figures from Star Wars The Black Series are back with the Black Series Archive collection. These archive figures have the same premium design and detailing as the original issue, so new and old collectors alike can add to their Star Wars collection. </p>

<p>Kids and fans alike can imagine the biggest battles and missions in the Star Wars saga with figures from Star Wars The Black Series! With exquisite features and decoration, this series embodies the quality and realism that Star Wars devotees love.</p>

<p>Star Wars products are produced by Hasbro under license from Lucasfilm Ltd. Hasbro and all related terms are trademarks of Hasbro.</p>
''',
                  itemShort='The notorious bounty hunter Boba Fett prepares to deliver the carbonite-frozen Han Solo to Jabba the Hutt.', \
                  price=33.00, category=2)

    item2 = Item(id=2, name='Flame Trooper', image='flame.jpg', \
                 description='''<p>Re-create the biggest battles and missions of the Star Wars saga with these figures from The Black Series! With exquisite features and articulated movement, the figures in this series embody the quality and realism that Star Wars devotees love. Specialized Stormtroopers of the First Order, Flametroopers carry incendiary weapons that can transform any battlefield into an inferno. This 6-inch-scale First Order Flametrooper figure is carefully detailed to look just like the First Order soldier from Star Wars: The Force Awakens. This figure is crafted to display true-to-story detail and comes with 2 accurately decorated accessories. Act out favorite battles or create brand new ones! No collection -- or adventure -- is complete without this First Order Flametrooper figure. Build up an epic collection with all the figures and vehicles from The Black Series. Each sold separately.</p>

<p>Includes figure and 2 accessories.</p>
<ul>
<li>Detailed 6-inch figure looks like a First Order Flametrooper from Star Wars: The Force Awakens. </li>
<li>Play with the 2 included accessories </li>
<li>Expand and enhance Star Wars collections </li>
</ul>
<p>WARNING: CHOKING HAZARD – Small parts may be generated. Not for children under 3 years.</p>
<p>Ages 4 and up.</p>''',
                 itemShort='Specialized Stormtroopers of the First Order, Flametroopers carry incendiary weapons.', \
                 price=35.00, category=2)

    item12 = Item(id=12, name='Han Solo', image='han.jpg', \
                  description='''<p>Re-create the biggest battles and missions of the Star Wars saga with these figures from The Black Series! With exquisite features and articulated movement, the figures in this series embody the quality and realism that Star Wars devotees love. This 6-inch-scale Han Solo figure is carefully detailed to look just like the heroic character from Star Wars: The Force Awakens. Han Solo was many things over the course of his long and legendary career. Hunted as a criminal and fugitive, and lauded as one of the greatest heroes of the Rebellion, he was perhaps most renowned for his skills as a pilot. This figure is crafted to display true-to-story detail and comes with an accurately decorated accessory. Act out favorite battles or create brand new ones! No collection -- or adventure -- is complete without this Han Solo figure. Build up an epic collection with all the figures and vehicles from The Black Series.</p>

<p>Star Wars products are produced by Hasbro under license from Lucasfilm Ltd. Hasbro and all related terms are trademarks of Hasbro.</p>

<p>Includes figure and accessory.</p>''',
                  itemShort='This 6-inch-scale Han Solo figure is carefully detailed to look just like the heroic character from Star Wars.', \
                  price=33.00, category=2)

    item13 = Item(id=13, name='Tie fighter', image='tie.jpg', \
                  description='''<p>The return of the Vintage Collection! Celebrate the legacy of Star Wars, the action-and-adventure-packed space saga from a galaxy far, far away, with premium, highly-detailed 3.75-inch scale figures and vehicles from Star Wars The Vintage Collection! </p>
<p>The TIE fighter was the unforgettable symbol of the Imperial fleet. Carried aboard Star Destroyers and battle stations, TIE fighters were single-pilot vehicles designed for fast-paced dogfights with Rebel X-wings and other starfighters.</p>
<p>Imagine recreating iconic moments from Star Wars: The Empire Strikes Back with this Star Wars The Vintage Collection 3.75-inch-scale Imperial TIE Fighter vehicle, featuring premium deco and movie-inspired design, and including an Imperial TIE Fighter Pilot figure.</p>
<h6>Product Features</h6>
<ul>
<li>3.75 inch (9.53cm) scaled</li> 
<li>Made of plastic</li>
<li>Vintage-inspired packaging with original Kenner branding </li>
<li>Eject figure from seat and blast off TIE Fighter wings </li>
<li>Open hatch to fit included 3.75-inch-scale TIE Fighter Pilot figure in cockpit</li>
</ul>
''', itemShort='The TIE fighter was the unforgettable symbol of the Imperial fleet. Carried aboard Star Destroyers.', \
                  price=39.99, category=1)
    item14 = Item(id=14, name='AT-ST Walker', image='atw.jpg', \
                  description='''<p>Kids and fans alike can imagine the biggest battles and missions in the Star Wars saga with figures from Star Wars: The Black Series! With exquisite features and decoration, this series embodies the quality and realism that Star Wars devotees love.</p>
<p>The two-man AT-ST is a lightly armored walker featuring chin-mounted laser cannons and side-mounted weapon pods. The two-legged transport, dubbed the Scout Walker by many, serves as a recon and patrol vehicle.</p>
<p>This 3.75-inch-scale Imperial AT-ST Driver figure and AT-ST Walker vehicle from Star Wars The Black Series are carefully detailed to look like the Imperial driver and vehicle from the Star Wars films. These Star Wars Black Series AT-ST figures feature premium detail and multiple points of articulation, and vehicle features detailed, movie-accurate design.</p>
<h6>Product Features</h6>
<ul>
<li>3.75 inch (9.53cm) Driver figure</li>
<li>Approximately 13.5 inches (34.29cm) AT-ST Walker</li>
<li>Made of plastic</li>
<li>Collector grade quality figure and vehicle with authentic, movie-accurate detail</li>
<li>Premium packaging and design</li>
<li>Recreate adventures from the Star Wars Universe</li>

</ul>
''',
                  itemShort='The AT-ST is a lightly armored walker featuring chin-mounted laser cannons and side-mounted weapon pods.', \
                  price=80.00, category=1)
    item15 = Item(id=15, name='Bossk', image='bossk.jpg', \
                  description='''<p>Bossk is one of the bounty hunters hired by Darth Vader to search for the Millennium Falcon and its rebel crew.</p>

<p>The most epic figures from Star Wars The Black Series are back with the Black Series Archive collection. These archive figures have the same premium design and detailing as the original issue, so new and old collectors alike can add to their Star Wars collection. </p>


<p>Kids and fans alike can imagine the biggest battles and missions in the Star Wars saga with figures from Star Wars The Black Series! With exquisite features and decoration, this series embodies the quality and realism that Star Wars devotees love.</p>

<p>Star Wars products are produced by Hasbro under license from Lucasfilm Ltd. Hasbro and all related terms are trademarks of Hasbro.</p>
''',
                  itemShort='Bossk is one of the bounty hunters hired by Darth Vader to search for the Millennium Falcon and its rebel crew.', \
                  price=27.00, category=2)
    # item16 = Item(id=16, name='Landspeeder', image='', \
    #               description='', itemShort='', \
    #               price=205.00, category=1)
    # item17 = Item(id=17, name='Landspeeder', image='', \
    #               description='', itemShort='', \
    #               price=205.00, category=1)
    # item18 = Item(id=18, name='Landspeeder', image='', \
    #               description='', itemShort='', \
    #               price=205.00, category=1)

    try:
        db.session.add(item1)
        db.session.add(item2)
        db.session.add(item3)
        db.session.add(item4)
        db.session.add(item5)
        db.session.add(item6)
        db.session.add(item7)
        db.session.add(item8)
        db.session.add(item9)
        db.session.add(item10)
        db.session.add(item11)
        db.session.add(item12)
        db.session.add(item13)
        db.session.add(item14)
        db.session.add(item15)
        db.session.commit()
    except SQLAlchemyError as e:
        print(e)
        return "<h1>There was an issue adding an item in dbseed function</h1>"
    else:
        return "All Good"
