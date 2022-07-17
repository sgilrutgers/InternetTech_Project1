Project 1: DNS 

Partners (RUID)(NETID): 
Aditya Dhami (ad1409)
Sebastian Gil-Avendano (sg1397)

1. Are there known issues or functions that aren't working currently in your attached code? If so, explain.

After testing our code with 500+ different domain names including invalid and non-reachable domain names, it is outputting accurate results. Tested in different and same ilab machine and did not encounter any error that would crash or abruptly stop out code. 

2. Collaboration: Who did you collaborate with on this project? What resources and references did you consult? Please also specify on what aspect of the project you collaborated or consulted.

Regarding resources used in effort to effectively make this project were all resources given to us by the professor and the curriculum. Our general understanding of DNS was derived from both lecture and resources given to us. More specifically lecture three and the routley.io article were much help. The other resources such as defining a struct, sockets were important to understand the complexities of the code and determine the structure

We would like to formally cite that a section of our code is from the routley.io, which is the format to hex function (formatHex). Citation is needed as this code was a resource given to us by the staff and we have used it to be an supportive part of our code.

3. What problems did you face developing code for this project? Around how long did you spend on this project (This helps me decide what I need to explain more clearly for the next projects)

Initially, the first problem we faced was to convert our domain name request into a UDP request, and later was to parse the response from google DNS server to just find 'A' records and ignore CNAMES. On average we spend 1 hour and half each day on the projects, so in total we spent around 10 hours on this project.

4. What interesting thing does you program do to accomplish the task

The program interestly is essentially a bunch of methods within eachother to make the code work. For ease on server and client connection, it only calls on one method for the data. The data is streamed into splicing, then hexed, and then sent to a DNS server encoded. Once our request is sent back to us, we recieve a hex sequence. My partner and I realized that there is a sequence in successful retrievals and unsuccessful ones. So, we have coded a parameter that checks if that result is unsuccessful it returns ("DXDOMAIN") and will continue down the line. Another thing we did is because we have tested it with 500 different domain names, we realized that the code did not work with domains with numbers in them, a bug that would have not been found if we stuck to the regular testcases, so we modified it to be able to work with ALL domains. We as a group believe it is interesting as it shows going above and beyond what is required
