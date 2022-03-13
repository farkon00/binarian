from sys import exit, argv

def throw_exception(text : str, state, display_line=True):
    exc_text = "\nWhile executing code, exception was thrown :\n\n"

    if display_line:
        for j, i in enumerate(state.call_stack):
            exc_text += f"line {i[1] + 1 - state.std_lines} "
            if j > 0:
                exc_text += f"in {state.call_stack[j-1][0]} "
            exc_text += ":\n"

            clear_text = " ".join(state.lines[i[1]].split()) 
            exc_text += "  " + clear_text + "\n"

        exc_text += f"line {state.current_line + 1 - state.std_lines} "
        if state.call_stack:
            exc_text += f"in {state.call_stack[-1][0]} "
        exc_text += ":\n"

        clear_text = " ".join(state.lines[state.current_line].split()) 
        exc_text += "  " + clear_text + "\n"

    exc_text += "\n" + text

    print(exc_text)

    if "-d" in argv:
        del state.vars["0"]
        del state.vars["1"]

        print("\n" + str({i : str(j) for i, j in state.vars.items()}))

    exit(1)

def binarian_assert(condition : bool, text : str, state, display_line=True):
    if condition:
        throw_exception(text, state, display_line=display_line)