# add imports at the beginning of the file
import pika
import sys
import csv
import time

# read from a file to get some fake data - declaring variable input_file
input_file = open("Lizards.csv", "r")

# Create a csv reader for a comma delimited file
reader = csv.reader(input_file, delimiter=",")

#Declare the name of the queue & host
queue_name = 'Lizard_queue'
host= 'localhost'

# define a main function to run the program
def main():

    try:
        for row in reader:
            # read a row from the file
            Species, Aquatic, Herbivorous, Nocturnal, Scansorial, Fossorial, Large, Terrestrial, Archetype  = row

            # use an fstring to create a message from our data
            # notice the f before the opening quote for our string?
            fstring_message = f"[{Species}, {Aquatic}, {Herbivorous}, {Nocturnal}, {Scansorial}, {Fossorial}, {Large}, {Terrestrial}, {Archetype}]"

            # prepare a binary (1s and 0s) message to stream
            MESSAGE = fstring_message.encode()

            # sleep for a few seconds
            time.sleep(2)
    
            try:
                # create a blocking connection to the RabbitMQ server
                connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
                # use the connection to create a communication channel
                channel = connection.channel()
                # use the channel to declare a queue
                channel.queue_declare(queue=queue_name)
                # use the channel to publish a message to the queue
                channel.basic_publish(exchange="", routing_key=queue_name, body=MESSAGE)
                # print a message to the console for the user
                print(f" [x] Sent {MESSAGE}")
            except pika.exceptions.AMQPConnectionError as e:
                print(f"Error: Connection to RabbitMQ server failed: {e}")
                sys.exit(1)
            finally:
                # close the connection to the server
                connection.close()
    except KeyboardInterrupt:
        # close the file objects to release the resources
        input_file.close()

# Standard Python idiom to indicate main program entry point
# This allows us to import this module and use its functions
# without executing the code below.
# If this is the program being run, then execute the code below
if __name__ == "__main__":
    main()