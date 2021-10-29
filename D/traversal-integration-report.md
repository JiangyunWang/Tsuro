### 1.	How well did the other team implement your specification? Did they follow it truthfully? If they deviated from it, was it well justified?

They implemented most of functions very well, expect for that it’s unnecessary to add Minimal Spanning Tree to connect nodes together. They seemed to misunderstand the words “There's only one edge between each pair of nodes” in our specification. It doesn’t mean that there has to be one edge between each pair of nodes. In a labyrinth, users need to figure out which way could take them out of labyrinth by themselves. We should not only give them one path. 

Since they misunderstood edges in our specification, they seemed to misunderstand **isReachable(src, dest)** function, as they thought “An edge between each pair of nodes would make traversal on **isReachable(src, dest)** unneccessary”. It is not necessary that one node could reach another node by only one edge, it could be through some intermediate nodes, and that’s the functionality of **isReachable(src, dest)**.

In addition, we didn’t specify weight in our specification, while they implemented weight. 

For **create_graph(x,y)**, when we was doing Assignment C task3, we noticed that this function was not expected as what we wrote in our specification. They did good job to implement this function in their way. 


### 2.	 Were you or would you be able to integrate the received implementation with your client module from Task 3 of Assignment C? What was the actual or what is estimated effort required?

Since when doing Assignment C, task 3, we figured out that in our specification, function like **create_graph(x, y)**, and use of **PIL** library is not expected to be implemented in that way.  Thus, it’s our responsibility that they did not have corresponding function like **lab_creation()** which takes in a list of edges (From: node_name, to: node_name) in server. 

The server does support function of adding token to named node. 

Because they misunderstood edges in our specification, they didn’t implement **isReachable(src, dest)** function as expected. 
For integrating received implementation with our client module from Task3, we need to reimplement function **lab_creation()** which takes a list of edges(from: node, to: node), and **isReachable(src, dest)** to check if some colored token can reach some named graph node.

### 3.	Based on the artifact you received and the above two questions, how could you improve your specification to make it more amenable for implementation as you intended?

We would add more specific description regarding how we want to deal with edges. 
