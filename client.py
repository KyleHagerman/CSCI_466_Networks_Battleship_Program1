import socket, requests, re, sys

opponent_board = r".\opponent_board.txt"

def main():
    IP_address = str(sys.argv[1])       #the first argument is an IP address
    port_number = str(sys.argv[2])      #the second argument is the port number
    x_coord = str(sys.argv[3])          #the third argument is the x coordinate
    y_coord = str(sys.argv[4])          #the fourth argument is the y coordinate

    http_message = "http://" + IP_address + ":" + port_number + "/?x=" + x_coord + "&y=" + y_coord
    print(http_message)

    fire(http_message, int(x_coord), int(y_coord))

def fire(message, x_coord, y_coord):
    response = requests.post(message) #sends a URL formatted like 'http://0.0.0.0:0000/?x=#&y=#'

    http_code = int(response.status_code)

    if http_code == 200:
        response_body = str(response.content)                #get the reponse message from the body and make it a string from bytes
        hit_result_list = re.findall(r'\d', response_body)       #get whether the hit was successful or not
        hit_result = int(hit_result_list[0])
        matches = re.findall(r'=\w', response_body)  #intermediary step to find ship sunk
        if len(matches) == 2:
            matches = matches[0] + matches[1]
        else:
            matches = matches[0]
        ship_sunk = re.findall(r'\w', matches)       #get char of ship sunk

        board = open(opponent_board, "r")            #open the board to read the lines in
        board_rows = board.readlines()               #reads the current lines of the board
        board.close()                                #closes the file
        if hit_result == 1:                          #we hit a ship
            board_rows[y_coord] = board_rows[y_coord][0:x_coord] + "X" + board_rows[y_coord][x_coord + 1:]
        elif hit_result == 0:                        #we missed the ships
            board_rows[y_coord] = board_rows[y_coord][0:x_coord] + "O" + board_rows[y_coord][x_coord + 1:]
        else:
            print("Do I need to put an else statement?")

        board = open(opponent_board, "w")            #open the board again but to write this time
        for i in board_rows:                              #write the new lines into the board
            board.write(i)
        board.close()                                #close the file
    elif http_code == 404:                           #the shot was outside the limits of the board
        print("HTTP/1.1 404 Not Found")
        print("Fire again, sailor!")
    elif http_code == 410:                           #the player has already used those coordinates this game
        print("HTTP/1.1 410 Gone")
        print("You've already fired on that location, sailor!")
    elif http_code == 400:                           #the command line arguments were formatted incorrectly
        print("HTTP/1.1 400 Bad Request")
        print("Your fire message could not be read properly. Fire again, sailor!")
    elif http_code == 403:                           #it's not the player's turn
        print("HTTP/1.1 403 Forbidden")
        print("Sailor! This is a gentlemen's game, you must wait your turn!")




if __name__ == "__main__": main()
