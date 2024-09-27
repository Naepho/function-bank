def odefunction(t, y, const):
    g = const[0]
    l = const[1]

    dy = np.zeros_like(y)
    dy[0] = theta[1]
    dy[1] = -1 * (g/l) * np.sin(theta[0]) - am * theta[1]

    return dy

def solve(function, duration, y0, max_step, atol = None, rtol = None):
    if (atol = None && rtol != None):
        solution = solve_ivp(lambda t, y: odefunction(t, y, c), [0, duration], y0, max_step = max_step, rtol = rtol)
    elif (atol != None && rtol = None):
        solution = solve_ivp(lambda t, y: odefunction(t, y, c), [0, duration], y0, max_step = max_step, atol = atol)
    elif (atol = None && rtol = None):
        solution = solve_ivp(lambda t, y: odefunction(t, y, c), [0, duration], y0, max_step = max_step)
    elif (atol != None && rtol != None):
        solution = solve_ivp(lambda t, y: odefunction(t, y, c), [0, duration], y0, max_step = max_step, atol = atol, rtol = rtol)

    return solution