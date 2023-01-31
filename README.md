# streaming-03-bonus-SamanthaCress
1. By Samantha Cress Date: 1/31/2023
2. Link to original dataset: https://datadryad.org/stash/dataset/doi:10.5061/dryad.f6t39kj 
3. Steps I took:
    # I begin creating my producer by going back to my process streaming .py file and getting some lines of code from there. 
    # Next I adapted lines of code from this week's v2_emit_message py file to work with the code from the previous file. 
    # I did get stuck at this point, at first I had all of my CSV contents being sent at once not line by line. I eventually did some google searches and different code combinations and was able to get it to work. 
    # To create my consumer, I referenced this week's v2_listen_for_message file and adapted it to work with my file and queue. I also used the RabbitMq tutorial. 
    # I will admit that even though I was able to create my output text file each time I would run the consumer code the text file would end up blank. I ended up having to copy and paste my recieved messages into the text file. I also tried writing to csv file but it too was blank. I hope to find what is wrong in my code. 

