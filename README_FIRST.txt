Wahab Note: make clean slate on start

MINIMUM ALIEN INVASION STARTER
==============================

PURPOSE
-------
This is a small, runnable Alien Invasion starter. You are not expected to build
a complete game from nothing. The supplied code gives your group a working
foundation to read, test, explain, modify and extend.

The starter uses simple coloured rectangles, so no images folder is required.

FILES
-----
alien_invasion.py  Coordinates events, bullets, aliens, collisions and drawing.
settings.py        Stores screen, ship, bullet and alien settings.
ship.py            Defines the ship and left/right movement.
bullet.py          Defines bullets and upward movement.
alien.py           Defines aliens, fleet movement and edge detection.

WHAT ALREADY WORKS
------------------
* Pygame window opens.
* Ship appears at the bottom centre.
* LEFT and RIGHT move the ship.
* SPACEBAR fires bullets.
* Only three bullets may be active at once.
* A small alien fleet is displayed and moves sideways and down.
* Bullet-alien collisions remove both objects.
* A new fleet appears when all aliens are removed.
* The fleet resets if aliens reach the bottom.
* Q or the window close button exits.

WHAT IS NOT INCLUDED
--------------------
* score or scoreboard
* lives
* Play button
* game-over and restart behaviour
* levels or increasing difficulty
* sound or image assets
* high scores
* a complete polished game

Do not assume that your group must add all of these. Follow the assessment brief
and agree a realistic scope with your tutor.

BEFORE CHANGING THE CODE
------------------------
1. Install Pygame.
2. Run the starter without making changes.
3. Confirm that every group member can run it.
4. Identify which file controls settings, ship movement, bullets, aliens,
   events, collisions and fleet creation.
5. Trace what happens when RIGHT is pressed, SPACEBAR is pressed, a bullet hits
   an alien, an alien reaches an edge, and the fleet is removed.
6. Record problems before attempting corrections.

INSTALLING PYGAME
-----------------
From a terminal or Anaconda Prompt:

    python -m pip install pygame

In Jupyter Notebook, when Pygame is installed in another environment:

    import sys
    !{sys.executable} -m pip install pygame

Restart the kernel or editor after installation if necessary.


RUNNING THE STARTER
-------------------
Keep all five Python files in the same folder. Open a terminal in that folder:

    python alien_invasion.py

Controls:
    LEFT ARROW   move left
    RIGHT ARROW  move right
    SPACEBAR     fire
    Q            quit


GROUP PROJECT EXPECTATION
-------------------------
Use this starter as a foundation. Do not replace it with an unrelated complete
game.

Your group must:

-- make at least one meaningful modification to supplied behaviour;

-- implement at least one tutor-approved new feature;

-- clearly distinguish supplied code from code your group added or changed;

-- test the student-added or modified work;

-- record at least two tests showing interactions between supplied and
added/modified features;

-- keep debugging evidence showing a problem, diagnosis, correction and retest;

-- explain the final result accurately;

-- identify limitations honestly; and

-- provide evidence of individual contributions.

Your work should demonstrate understanding of the supplied structure, a
top-level plan, clear task allocation, appropriate Python design, testing,
debugging, technical explanation and evaluation.


POSSIBLE REALISTIC EXTENSIONS
-----------------------------
Subject to tutor approval, your group might add scoring, limited lives, a start
or restart state, changed fleet behaviour, a new alien type, difficulty options,
visual feedback, structured testing, or another small feature.

A small extension that works, is tested and is clearly explained is better than
many incomplete features.


ACADEMIC INTEGRITY
------------------
Follow the course rules on collaboration and generative AI. Every group member
must be able to explain the submitted code. Record what was supplied, what was
changed, who contributed to each change, how it was tested, and what remains
incomplete.
