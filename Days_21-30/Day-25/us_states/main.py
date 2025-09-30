import turtle
import pandas as pd
import os

# Constants
SCORE_TITLE = "U.S. States Game"
STATES_CSV = "50_states.csv"
MAP_IMAGE = "blank_states_img.gif"
OUTPUT_CSV = "states_to_learn.csv"
TOTAL_STATES = 50

def setup_screen():
    """Initialize the game screen and load the map."""
    screen = turtle.Screen()
    screen.title(SCORE_TITLE)
    try:
        screen.bgpic(MAP_IMAGE)
    except turtle.TurtleGraphicsError:
        print(f"Error: Could not load map image '{MAP_IMAGE}'.")
        screen.bye()
        exit(1)
    return screen

def load_states_data():
    """Load states data from CSV file."""
    try:
        if not os.path.exists(STATES_CSV):
            raise FileNotFoundError(f"Could not find {STATES_CSV}")
        
        states_data = pd.read_csv(STATES_CSV)
        return states_data, states_data.state.tolist()
    except Exception as e:
        print(f"Error loading states data: {e}")
        return None, []

def create_turtle():
    """Create and configure a turtle for writing text."""
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    return t

def write_state_on_map(turtle_obj, state_data, state_name):
    """Write the state name on the map at its coordinates."""
    try:
        state = state_data[state_data.state == state_name]
        turtle_obj.goto(state.x.item(), state.y.item())
        turtle_obj.write(state_name, align="center", font=("Arial", 8, "normal"))
        return True
    except (IndexError, KeyError):
        return False

def save_missed_states(missed_states):
    #Save missed states to a CSV file.
    if not missed_states:
        print("No missed states to save.")
        return
    
    try:
        df = pd.DataFrame(missed_states, columns=["Missed States"])
        df.to_csv(OUTPUT_CSV, index=False)
        print(f"Missed states saved to: {os.path.abspath(OUTPUT_CSV)}")
    except Exception as e:
        print(f"Error saving missed states: {e}")

def display_final_message(score):
    """Display the final game message."""
    t = create_turtle()
    t.color("red")
    if score == TOTAL_STATES:
        message = " Congratulations! You've named all 50 states! "
    else:
        message = f"Game Over! You guessed {score}/{TOTAL_STATES} states."
    
    t.goto(0, 0)
    t.write(message, align="center", font=("Arial", 16, "bold"))

def main():
    # Initialize game
    screen = setup_screen()
    states_data, all_states = load_states_data()
    
    if not all_states:
        print("Failed to load states data. Exiting...")
        return
    
    guessed_states = []
    writer = create_turtle()
    
    # Game loop
    while len(guessed_states) < TOTAL_STATES:
        score = len(guessed_states)
        answer = screen.textinput(
            title=f"{score}/{TOTAL_STATES} States Correct",
            prompt="What's another state's name?\n(Type 'Exit' to quit)"
        )
        
        # Handle exit conditions
        if not answer or answer.lower() == 'exit':
            break
            
        answer = answer.title()
        
        # Check if answer is valid
        if answer not in all_states:
            print("Invalid state name. Please try again.")
            continue
            
        if answer in guessed_states:
            print("You already guessed that state.")
            continue
            
        # Process correct answer
        guessed_states.append(answer)
        write_state_on_map(writer, states_data, answer)
    
    # Game over - handle missed states
    missed_states = [state for state in all_states if state not in guessed_states]
    save_missed_states(missed_states) # this saves the missed states to a CSV file as defined by function above
    display_final_message(len(guessed_states))
    


if __name__ == "__main__":
    main()