#!/usr/bin/env python

from __future__ import division

import random

import pyglet

class MW10(pyglet.window.Window):
    def __init__(self):
        super(MW10, self).__init__(caption='MW10', width=800, height=600)
        self.batch = pyglet.graphics.Batch()
        self.player = Player(batch=self.batch)
        self.stars = []
        for count in xrange(10):
            self.stars.append(Star(self.player, batch=self.batch))
        pyglet.clock.schedule_interval(self.update, 1/60)
        self.fps_display = pyglet.clock.ClockDisplay()
        pyglet.app.run()
    def on_draw(self):
        self.clear()
        self.fps_display.draw()
        self.batch.draw()
    def update(self, dt):
        self.player.update(dt)
        for star in self.stars:
            star.update(dt)
    def on_key_press(self, symbol, modifiers):
        self.player.handle_key(symbol, modifiers)

class Player(pyglet.sprite.Sprite):
    def __init__(self, batch):
        solid_color = pyglet.image.SolidColorImagePattern((255, 255, 255, 255))
        super(Player, self).__init__(solid_color.create_image(20, 20), x=400, y=300, batch=batch)
        self.vel = 0.
        self.rot_vel = 0.
        self.heading = 0.
    def handle_key(self, symbol, modifiers):
        if symbol == pyglet.window.key.D:
            self.rot_vel -= 1
        elif symbol == pyglet.window.key.A:
            self.rot_vel += 1
        elif symbol == pyglet.window.key.S:
            self.vel += 1
        elif symbol == pyglet.window.key.W:
            self.vel -= 1
    def update(self, dt):
        self.heading += dt * self.rot_vel

class Star(pyglet.sprite.Sprite):
    def __init__(self, player, batch):
        self.player = player
        solid_color = pyglet.image.SolidColorImagePattern((128, 128, 128, 255))
        super(Star, self).__init__(solid_color.create_image(2, 2), x=random.uniform(100, 700), y=random.uniform(100, 500), batch=batch)
    def update(self, dt):
        self.x += dt * self.player.vx
        self.y += dt * self.player.vy
        

if __name__ == '__main__':
    MW10()
