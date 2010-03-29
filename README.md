Space-Crawl.  Will space be the place to continue human civilization or the last great graveyard of mankind?  Only our pilots will determine the outcome of the human race.  As commander for your colony, you must make a place for your people to survive in the difficulty of space.

Playing
=======
Note that the following descriptions are the ideal, finished version of the game and not what is currently implemented.

Start
-----
Start the game by invoking the play.py executable script.  At the first screen, you will be prompted to select a faction.

Quit
----
Press _ESC_ at any time to leave the game with a description of the current score.

Ideas
=====
* no micro managing
* universe - show all galaxies
    * flashing if in conflict
    * faction color if discovered and producing
    * currently selected galaxy with stats (discovered resources, units)
* galaxy - can pan around, select planets to see stats, if has been explored
* missions
    * explore
    * attack
    * conquer
    * hold/defend
* factions
    * turtling - cheaper defensive structures
    * explorer - drones
    * aggressive - attackers
    * economy - production

    Universe screen
    ------------------------------------------------------------------------------
    |        .                               .                |stats for current |
    |      .             .                                    |selection         |
    |                                                         |                  |
    |                                .       .                |                  |
    |                                                         |                  |
    |            .          .                                 |                  |
    |                                                 .       |                  |
    |                  1                .                     |                  |
    |    .                                                    |                  |
    |                                                 .       |                  |
    |                                         >               |                  |
    |                    .            .                       |                  |
    |                                                         |                  |
    |             .                                           |                  |
    |                                            O       .    |                  |
    |                                 .                       |                  |
    |    .               #                                    |                  |
    |                                             .           |                  |
    |                           .                             |                  |
    |        O                             .                  |                  |
    |                                                         |                  |
    ------------------------------------------------------------------------------
    O = dicovered base
    1 = numbered fleet, flashing with object
    > = fleet in transit, flashig with number
    # = cursor

    Galaxy screen
    ------------------------------------------------------------------------------
    |                                                                            |
    |                                          o                                 |
    |                                                                            |
    |   f                                                                        |
    |                                                o                           |
    |                                                                            |
    |        i        o                                                          |
    |                             o                      o                       |
    |    C                                                                       |
    |                                     *         o                            |
    |                o                                                           |
    |          i                                           o                     |
    |                                  o                                         |
    |             i      o                      o                                |
    |                                                                            |
    |                                                                            |
    |                   o                                                        |
    |                                                                            |
    | #                                                                          |
    |                       o                                                    |
    |                             o                                              |
    ------------------------------------------------------------------------------
    o = planet
    * = star
    # = cursor
    f, C, i = ship type

    Fleet screen
    ------------------------------------------------------------------------------
    |  Fleet # (1-9)                                                             |
    |  Officer Name                                                              |
    |                                                                            |
    |  units                   stats                                             |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |  Mission                                                                   |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |  Cargo                                                                     |
    |  _ * / $ x ! %                                                             |
    |                                                                            |
    ------------------------------------------------------------------------------

    Production screen
    ------------------------------------------------------------------------------
    | Production                                                                 |
    |                                                                            |
    | unit                    materials/cost                                     |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    |                                                                            |
    ------------------------------------------------------------------------------

    Blank screen
    ------------------------------------------------------------------------------
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    |                                                         |                  |
    ------------------------------------------------------------------------------
