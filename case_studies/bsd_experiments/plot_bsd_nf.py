"""plot_bsd_nf.py

this is a demo for today
"""

print(2 + 6)

import matplotlib.pyplot as plt


def plot_points(E, B):
    """stuff

    Args:
        E ([type]): [description]
        B ([type]): [description]
    """

    running_product = 1
    data_points = []

    K = E.base_field()
    it = K.primes_of_bounded_norm_iter(B)
    norm_tracker = 1

    for fp in it:
        fp_norm = fp.norm()
        if fp_norm != norm_tracker:
            # we plot only in this case
            data_points.append((fp_norm, running_product))
            norm_tracker = fp_norm
        try:
            Ered = E.reduction(fp)
            new_term = Ered.cardinality() / fp_norm
            running_product *= new_term
        except ValueError:
            # hopefully this means the curve has bad reduction
            pass

    logged_data_points = [(log(log(x)), log(y)) for (x, y) in data_points]

    plt.scatter(*zip(*logged_data_points))


def plot_bsd(ecs_list, B=1000):
    """some info

    Args:
        ecs_list ([type]): [description]
        B (int, optional): [description]. Defaults to 1000.
    """

    plt.title("blah")
    plt.xlabel("dsfdfd")

    for E in ecs_list:
        plot_points(E, B)

    plt.legend()
    plt.show()


K = QuadraticField(5, "a")
E = EllipticCurve([1, a])
ecs_list = [E]
plot_bsd(ecs_list, B=300)
