"""plot_bsd_nf.py

Exercise 4 on Sheet 2
"""

# just checks we're live
# print(2 + 5)

# let's first do the exercise over Q

import matplotlib.pyplot as plt


def plot_points(E, B):
    """[summary]

    Args:
        E ([type]): [description]
        B ([type]): [description]
    """

    running_product = 1
    data_points = []
    K = E.base_field()

    it = K.primes_of_bounded_norm_iter(ZZ(B))

    do_i_continue = True
    norm_tracker = 1

    while do_i_continue:
        try:
            fp = next(it)
            fp_norm = fp.norm()
            if fp_norm != norm_tracker:
                data_points.append((fp_norm, running_product))
                norm_tracker = fp_norm
            try:
                Ered = E.reduction(fp)
                new_term = Ered.cardinality() / fp_norm
                running_product *= new_term
            except ValueError:
                # hopefully means E has bad reduction at fp
                # we do nothing in this case, just continue
                pass

        except StopIteration:
            # this means we've hit all prime ideals up to norm B
            do_i_continue = False
            pass

    # do the log stuff
    logged_data_points = [(log(log(x)), log(y)) for (x, y) in data_points]

    plt.scatter(*zip(*logged_data_points))


def plot_bsd(ecs_list, B=1000):
    """some info

    Args:
        ecs_list ([type]): [description]
        B (int, optional): [description]. Defaults to 1000.
    """

    plt.title("ny title")
    plt.xlabel("fddgf")

    for E in ecs_list:
        plot_points(E, B)

    plt.legend()
    plt.show()
    return


K0 = QuadraticField(5, "a")
a0 = K.gen()
E0 = EllipticCurve([1, a0])


ecs_list = [
    E,
]

plot_bsd(ecs_list, B=5000)
