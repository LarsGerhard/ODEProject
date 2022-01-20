import matplotlib.pyplot as plt
from numpy import zeros_like, sin, cos, pi, linspace, e
from scipy.integrate import odeint

y0in = 1
omega = 4 * pi
tin = linspace(0, 10) * 0.1
A = -y0in / e ** (cos(0) / omega)


def W(t, y):
    dydt = y * (1 - sin(omega * t))
    return dydt


def analytic(t):
    y = - A * e ** (cos(omega * t) / omega) * e ** t
    return y


def euler(f, y0, t):
    y = zeros_like(t)
    y[0] = y0
    for i in range(len(y) - 1):
        dt = t[i + 1] - t[i]
        y[i + 1] = y[i] + f(t[i], y[i]) * dt
    return y


plt.plot(tin, euler(W, y0in, tin), label="Euler")

plt.plot(tin, odeint(W, y0in, tin, tfirst=True), label="ODEint")

plt.plot(tin, analytic(tin), label="analytic")

plt.legend()

plt.show()
