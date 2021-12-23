from vpython import *
e_graph = gcurve(color=color.blue)
#########################
# get gforce


def get_gforce(p1, p2):
    G = 1  # gravity
    distance = p1.pos - p2.pos
    distance_vector_magnitude = mag(distance)
    distance_hat = distance/distance_vector_magnitude
    G_Force = G * p1.mass * p2.mass / \
        distance_vector_magnitude**2  # G*p1.mass*p2.mass/r_mag**2
    force_vec = -G_Force*distance_hat
    return force_vec
#########################


#########################
# INIT OBJECTS
star = sphere(pos=vector(0, 0, 0), radius=0.2, color=color.yellow,
              mass=1000, momentum=vector(0, 0, 0), make_trail=True)
planet = sphere(pos=vector(1, 0, 0), radius=0.05, color=color.blue,
                mass=1, momentum=vector(0, 30, 0), make_trail=True)
planet1 = sphere(pos=vector(1.5, 0, 0), radius=0.08, color=color.green,
                 mass=0.9, momentum=vector(0, 20, 0), make_trail=True)

planet2 = sphere(pos=vector(0, -4, 0), radius=0.1, color=color.red,
                 mass=10, momentum=vector(160, 0, 0), make_trail=True)
comet = sphere(pos=vector(-6, 6, 0), radius=0.05, color=color.white,
               mass=0.55, momentum=vector(-1, -1, 0), make_trail=True)
#########################

#########################
# some vars
dt = 0.0001
t = 0
asteroids = []
rmin = 6
rmax = 9
mmin = 0.01
mmax = 0.10

#########################

#########################
# INIT ASTEROIDS
for i in range(0, 100):
    r = rmin+random()*(rmax-rmin)  # random velocity
    theta = random()*2*pi
    mass = mmin + random()*(mmax-mmin)  # random mass
    momentum = mass * sqrt(star.mass/r)  # random momentum
    asteroids.append(sphere(pos=r*vector(cos(theta), sin(theta), 0), momentum=momentum *
                     vector(-sin(theta), cos(theta), 0), mass=mass, color=color.white, radius=0.05))
#########################

#########################
# Game Loop
while (True):
    rate(1000)
    # forces
    star.force = get_gforce(star, planet) + get_gforce(star,
                                                       planet1) + get_gforce(star, planet2)
    planet.force = get_gforce(
        planet, star) + get_gforce(planet, planet1) + get_gforce(planet, planet2)
    planet1.force = get_gforce(
        planet1, star) + get_gforce(planet1, planet) + get_gforce(planet1, planet2)
    planet2.force = get_gforce(
        planet2, star) + get_gforce(planet2, planet) + get_gforce(planet2, planet1)
    comet.force = get_gforce(
        comet, star)

    for a in asteroids:
        a.force = get_gforce(
            a, star) + get_gforce(a, planet) + get_gforce(a, planet2)
    # momentums
    star.momentum += star.force*dt
    planet.momentum += planet.force*dt
    planet1.momentum += planet1.force*dt
    planet2.momentum += planet2.force*dt
    comet.momentum += comet.force*dt
    for a in asteroids:
        a.momentum += a.force*dt
    # update position
    star.pos += star.momentum/star.mass*dt
    planet.pos += planet.momentum/planet.mass*dt
    planet1.pos += planet1.momentum/planet1.mass*dt
    planet2.pos += planet2.momentum/planet2.mass*dt
    comet.pos += comet.momentum/comet.mass*dt
    for a in asteroids:
        a.pos = a.pos + a.momentum/a.mass*dt

    t += dt
#########################


# END
