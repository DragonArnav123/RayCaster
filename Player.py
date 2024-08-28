# File handles all player related code
import pygame as pg
import math

class Player:
    def __init__(self, win_size: int, init_pos: pg.Vector2, init_dir: pg.Vector2, speed_pps: float, angular_speed_rps: float, fov_rad: float, color: tuple, player_radius: int) -> None:
        self.win_size = win_size
        self.pos = init_pos
        self.dir = init_dir
        self.speed = speed_pps # Pixels per second
        self.ang_speed_rps = angular_speed_rps # Radians per second
        self.fov = fov_rad # Radians
        self.color = color
        self.radius = player_radius

    def update(self, delta_time_sec):
        # Ensure direction is a unit vector
        self.dir = pg.Vector2(self.dir)
        self.dir.scale_to_length(1)

        # Update as per buttons pressed
        # Introduce concept of delta time
        # Forward / Backward
        if pg.key.get_pressed()[pg.K_w]:
            self.pos += delta_time_sec * self.speed * self.dir
        elif pg.key.get_pressed()[pg.K_s]:
            self.pos -= delta_time_sec * self.speed * self.dir

        # Strafing
        rotate_vec = lambda vec, angle_rad: pg.Vector2(vec.x * math.cos(angle_rad) - vec.y * math.sin(angle_rad), vec.x * math.sin(angle_rad) + vec.y * math.cos(angle_rad)) 
        if pg.key.get_pressed()[pg.K_a]:
            # Get perpendicular vector on left side of the direction
            strafe_dir = rotate_vec(self.dir, math.radians(-90))
            self.pos += delta_time_sec * self.speed * strafe_dir
        elif pg.key.get_pressed()[pg.K_d]:
            # Get perpendicular vector on right side of the direction
            strafe_dir = rotate_vec(self.dir, math.radians(90))
            self.pos += delta_time_sec * self.speed * strafe_dir

        # Turning
        if pg.key.get_pressed()[pg.K_LEFT]:
            self.dir = rotate_vec(self.dir, -delta_time_sec * self.ang_speed_rps) # Change 1 to delta time
        elif pg.key.get_pressed()[pg.K_RIGHT]:
            self.dir = rotate_vec(self.dir, delta_time_sec * self.ang_speed_rps)

    def draw(self, win: pg.Surface):
        # Draw the player
        pg.draw.circle(win, self.color, self.pos, self.radius)

        # Draw the direction the player is looking in
        pg.draw.line(win, self.color, self.pos, self.pos + 50 * self.dir)
        # Fix the issue of when rotating, two direnction vectors are drawn