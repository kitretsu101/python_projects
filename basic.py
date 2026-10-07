from math import inf


def terminal(state):
    """
    Return True if the game is over.
    Example:
    return state["winner"] is not None or len(get_moves(state)) == 0
    """
    return False


def evaluate(state):
    """
    Return the score of the current state.

    Positive score: good for MAX
    Negative score: good for MIN
    Zero: draw or neutral
    """
    return 0


def get_moves(state):
    """
    Return a list of all possible moves.
    """
    return []


def make_move(state, move):
    """
    Apply a move to the state.
    """
    pass


def undo_move(state, move):
    """
    Undo the move from the state.
    """
    pass


def minimax(state, depth, maximizing):
    # Stop if the game is over or search depth is reached
    if terminal(state) or depth == 0:
        return evaluate(state)

    # MAX player's turn
    if maximizing:
        best_value = -inf

        for move in get_moves(state):
            make_move(state, move)

            value = minimax(state, depth - 1, False)

            undo_move(state, move)
            best_value = max(best_value, value)

        return best_value

    # MIN player's turn
    else:
        best_value = inf

        for move in get_moves(state):
            make_move(state, move)

            value = minimax(state, depth - 1, True)

            undo_move(state, move)
            best_value = min(best_value, value)

        return best_value


def best_move(state, depth):
    best_value = -inf
    selected_move = None

    for move in get_moves(state):
        make_move(state, move)

        value = minimax(state, depth - 1, False)

        undo_move(state, move)

        if value > best_value:
            best_value = value
            selected_move = move

    return selected_move


# Example state
state = {}

# Search three levels deep
answer = best_move(state, 3)

print("Best move:", answer)