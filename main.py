import time
from elevator import *
from robot import *

client_id="555dbfe3-a660-4cdd-b984-782db54521da"
client_secret="H1fM0hP0kO3tT8uW4rB3cG3tX4wL6bV0wD5tN4uL6lG2yO2mC6"
building_id=9990000508

source_area="area:9990000508:1000"
dest_area="area:9990000508:5000"

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
call_object = call_elevator(building_id, source_area, dest_area)                 ####### TODO #######
beep("Follow Betty")

# Porter opens building entry.
beep("Open building entry") 

# Betty & Porter enter & walk to elevator
follow_until_stop()             ####### TODO #######

beep("Wait for elevator")
wait_for_elevator_at_start(call_object)
beep("Enter elevator")

# Betty & Porter enter & walk to elevator
follow_until_stop()

beep("Wait for Betty's floor")
wait_for_elevator_at_dest(call_object)
beep("Leave elevator")

# Betty & Porter leave elevator, walk to her door.
beep("Follow Betty")
follow_until_stop()

display("Unloading")
# Betty unloads and says "Bye, Porter"

display("Released")
beep("Return to Lobby")
