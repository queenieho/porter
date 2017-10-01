import time
from elevator import *
from robot import *

def display(s):
    print('"%s"' % s)
    time.sleep(1)
def beep(s):
    print('** ' + s)
    time.sleep(1)

# Porter detects someone in the active zone and approaches:
display("Who's there?")
move_to_person()                ####### TODO #######

# Porter recognizes Betty due by her SmartKey / phone, and greets her:
display("Welcome Betty! Need a hand?")
# Betty says "Yes, Porter".
display("Loading")
# Betty loads Porter.
# Betty says "let's go"

# Porter requests destination. "Welcome, Betty. Heading home?"
display("Heading home?")
# Betty says "yes"
#display("Escort Betty home")
beep("Call elevator")        # POST /building/{id}/call { lobby, Betty's floor}
call_elevator()                 ####### TODO #######
beep("Follow Betty")

# Porter opens building entry.
beep("Open building entry") 

# Betty & Porter enter & walk to elevator
follow_until_stop()             ####### TODO #######

beep("Wait for elevator")
wait_for_elevator_at_start()
beep("Enter elevator")

# Betty & Porter enter & walk to elevator
follow_until_stop()

beep("Wait for Betty's floor")
wait_for_elevator_at_dest()
beep("Leave elevator")

# Betty & Porter leave elevator, walk to her door.
beep("Follow Betty")
follow_until_stop()

display("Unloading")
# Betty unloads and says "Bye, Porter"

display("Released")
beep("Return to Lobby")
