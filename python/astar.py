from PriorityQueue import PriorityQueueWithFunction


class Agent:
    """Agent based on the A* algorithm."""

    def __init__(
        self, defaultMove, isGoal, stateToKey, generateSuccessors, costFunction
    ):
        """
        defaultMove : move to perform when nothing to do anymore
        isGoal : checks state to see if it's a goal
        stateToKey : function that takes a state as arg and returns
            an hashable key tuple to uniquely identify an env state.
        generateSuccessors : function that takes as input a state and
            returns a list of tuples (successorState, actionToGetThere)
        costFunction: a function that returns the estimated cost to get
            to the goal
            Arguments (all in a tuple):
                initialState
                pastState
                currentState
                pathToCurrentState
            Returns :
                The estimated cost
        """

        self.moves = None
        self.defaultMove = defaultMove
        self.isGoal = isGoal
        self.stateToKey = stateToKey
        self.generateSuccessors = generateSuccessors
        self.costFunction = costFunction

    def get_action(self, state):
        """Given an env state, returns a move.

        Arguments:
            state: an env state.

        Returns:
            A move
        """

        if self.moves is None:
            self.moves = self.astar(state)

        if self.moves:
            return self.moves.pop(0)
        else:
            return self.defaultMove

    def astar(self, state):
        """Given an env state, returns a list of moves.

        Arguments:
            state: an env state.

        Returns:
            A list of moves.
        """

        path = []
        fringe = PriorityQueueWithFunction(self.costFunction)
        fringe.push((state, path, 0))
        closed = set()

        while True:
            if fringe.isEmpty():
                return []

            priority, (current, path, cost) = fringe.pop()

            if self.isGoal(current):
                return path

            current_key = self.stateToKey(current)

            if current_key in closed:
                continue
            else:
                closed.add(current_key)

            for successor, action in self.generateSuccessors(current):
                fringe.push(
                    (
                        state,
                        current,
                        successor,
                        path + [action],
                    )
                )

        return path
