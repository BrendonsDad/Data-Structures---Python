''' 
In this solution I wanted to focus on the bare bones of FIFO and our challenge assignment.
For this purpose I have decided not to create classes so that the student only sees what is 
necessary for queues. 
'''



keep_on = True
#While loop initialized to start questions

while keep_on:

    # Coppied queue
    appartment_queue = [{'name':'Jessie', 'type':'one'},{'name':'Herbert', 'type':'both'},{'name':'Sam', 'type':'one'},{'name':'John', 'type':'two'},{'name':'Peter', 'type':'two'},{'name':'Michael', 'type':'both'},{'name':'Noah', 'type':'both'},{'name':'Ron', 'type':'one'},]

    # Ask from user
    available_apartment = input("Please enter the apartment type, type '0' to finish: ")

    # This checks to see if they want to quit.
    if available_apartment == '0':
        keep_on = False
        # break will end the loop
        break

    # Initialize currently_helped
    currently_helped = None
    # This index will count for us each time to help us iterate through the loop
    index = 0
    for pair in appartment_queue:
        # Looping through normally should allow us to use the queue since we start at the front
        if pair['type'] == available_apartment or pair['type'] == 'both':
            currently_helped = pair['name']
            # pop removes our current tennate
            appartment_queue.pop(index)
            # Message delivered and formated
            print()
            print(f'{currently_helped} has been removed from the list')
            print()
            # break so we do not do every one who has a working type
            break
        index += 1

