import matplotlib.pyplot as plt

# Simple graph

plt.plot(solution.t, solution.y[0], label=r"$\tex$")
plt.plot(0, theta_0[0], "o", label=r"$\tex$")
plt.legend()
plt.title("Pendule simple")
plt.xlabel(r"Temps $[s]$")
plt.ylabel(r"$\theta \; [rad]$")
plt.savefig("pendule simple.png")

# Animation

frame_per_second = 30  # Determines quality

fig = plt.figure(figsize=(5, 5))
plt.axis("equal")


def animation(i):  # Will be called each time a frame is rendered
    i = (
        i / (frame_per_second * duration) * len(solution.t)
    )  # To translate in solution.t
    i = int(i)

    plt.cla()  # Clears the screeen
    x = [0, -1 * np.cos(np.pi / 2 + solution.y[0][i])]
    y = [0, -1 * np.sin(np.pi / 2 + solution.y[0][i])]
    plt.plot(x, y)
    plt.plot(x[1], y[1], "o")
    plt.xlim(-1.2, 1.2)
    plt.ylim(-1.2, 1.2)

    plt.title("Pendule simple")


anim = FuncAnimation(
    fig,
    animation,
    frames=frame_per_second * duration,
    interval=1000 / frame_per_second,
)  # Makes the animation

anim.save("Pendule simple.gif")
