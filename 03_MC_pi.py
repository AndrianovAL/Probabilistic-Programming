# Estimate PI by running a Monte Carlo Simulation ("rain drops in a 1x1 square")

from __future__ import division
import matplotlib.pyplot as plt
from math import pi
from random import random


def random_point():
    """
    Simulate a onr random point draw in a 1x1 square
    """
    return (0.5 - random(), 0.5 - random())


def is_point_in_circle(point):
    """
    Return True if point is in the inscribed circle
    """
    return point[0]**2 + point[1]**2 <= 0.25


def plot_random_points(points_in_circle, points_out_of_circle, format='pdf'):
    """
    Drawing the points
    """
    num_of_points_in_circle = len(points_in_circle)
    num_of_points_out_of_circle = len(points_out_of_circle)
    num_of_points = num_of_points_in_circle + num_of_points_out_of_circle
    plt.figure()
    plt.xlim(-0.5, 0.5)
    plt.ylim(-0.5, 0.5)
    plt.scatter([e[0] for e in points_in_circle], [e[1] for e in points_in_circle], color='blue', label="Points in circle")
    plt.scatter([e[0] for e in points_out_of_circle], [e[1] for e in points_out_of_circle], color='black', label="Points out of circle")
    plt.legend(loc="center")
    plt.title("From {} points: {} are in the circle, $\pi$ estimate is {:4f}.".format(num_of_points, num_of_points_in_circle, 4 * num_of_points_in_circle / num_of_points))#FIXME
    plt.savefig("%s_points.%s" % (num_of_points, format))


def simulation(num_of_points=10000, plot=True, format='pdf'):
    """
    Simulation of random points draws.
    """
    num_of_points_in_circle = 0
    points_in_circle = []
    points_out_of_circle = []
    pi_estimate = []
    for k in range(num_of_points):
        d = random_point()
        if is_point_in_circle(d):
            points_in_circle.append(d)
            num_of_points_in_circle += 1
        else:
            points_out_of_circle.append(d)
        pi_estimate.append(4 * num_of_points_in_circle / (k + 1))  # update our list w/new estimate for pi
    # Plot the pi estimates
    plt.figure()
    plt.scatter(range(1, num_of_points + 1), pi_estimate)
    max_x = plt.xlim()[1]
    plt.hlines(pi, 0, max_x, color='black')
    plt.xlim(0, max_x)
    plt.title("$\pi$ estimate against num of rain drops")
    plt.xlabel("number of random pointss")
    plt.ylabel("$\pi$")
    plt.savefig("Pi_estimate_for_%s_drops_thrown.pdf" % num_of_points)

    if plot:  # ploting the final set of drops
        plot_random_points(points_in_circle, points_out_of_circle, format)

    return (num_of_points_in_circle, num_of_points)


if __name__ == "__main__":
    # Run the script from cli
    from sys import argv
    num_of_points = 50000
    if len(argv) > 1:  # if an arg is passed chg the simulated drops number
        num_of_drops = eval(argv[1])
    r = simulation(num_of_points, plot=True, format='png')
    print(f'{num_of_points} drops')
    print(f'pi is estimated as:\t{4 * r[0] / r[1]}')
