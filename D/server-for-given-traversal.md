Task 2 Memo: Labyrinth Specification and Implementation

The first paragraph specified that a Node class contains a name and a list of neighbors. However, there
is some ambiguity when the specification mentioned that there is only one edge between each pair of nodes
because it is not specific on how the edges are created. We also added an Edge class because they did not
specify how the nodes were connected.

The second paragraph said to implement method create_graph(x, y) where x is the width and y is the height. 
The labyrinth is only made of connected Nodes and there is no specification of the direction and length 
of the edges connecting the nodes. In their specification, they wanted an edge between each pair of nodes, 
however this would make traversal on isReachable() unneccessary. Our solution to this issue is to construct
a rectangular graph of nodes and use a Minimal Spanning Tree to connect the Nodes. We decided to use a Minimal 
Spanning Tree because there is at most one edge between all nodes.

The third paragraph wanted the color token to be created with an RGB value and position using Python's
Image library. We believed that this part was over-specified since we don't need to display images, so 
we decided to treat the color of the tokens as a string within a dictionary of valid colors.

Finally, the specification asked us to implement a function isReachable(src, dest) to check if a node can
reach a node using Breadth First Search. "src" will be the starting Node while "dest" will be the Node trying
to be reached. One big issue that we have with the implementation of the function is that because the labyrinth
was created using a Minimal Spanning Tree, every Node is reachable no matter where the starting Node is at.
We could just return true, however the specification wanted Breadth First Search to be performed, so we decided
to implement Breadth First Search into the function. We also added a wrapper method is_color_reachable(color, node),
where "color" is a string representing the token color and node is the name of the node, to find the location of the
source node.

After creating the labyrinth, the specification wants us to unit test our implementation using Python's "unittest"
library. Because we are testing objects that are created using random number generators, we decided to use a seed
to generate the same "random" numbers, therefore being able to replicate a labyrinth for testing.

Additional Changes that we made according to Task 3:
The create_graph is to the original specifications because we tried to follow it as close as we can.
It contradicts the Task 3 specification because Task 3 takes in a list of edges to create the graph,
but the original said that it randomly creates the edges starting from a random node. We used a minimal spanning tree
to generate the labyrinth randomly, and so additional data structures were implemented to help with this.
AddToken was not in the original received specification, but we added it to match with with Task 3 with that
specification. We felt that based on some implications in the specification, this functionality was desired, even though
it was not specified.
The requested isReachable function took in two Nodes which we implemented. However, we anticipated that a more user
friendly method would be needed and wrapped that class in another version of the function that takes in a color string
and a Node. That function then searches for a Node with that color and calls the requested isReachable method with the
two Nodes.

Other Additions:
We added an Edge class to represent the connections between two Nodes. This helps with the random generation of the
labyrinth and the breadth-first search.
Added a Tree class and a MinimalSpanningTree class to help construct the minimal spanning tree.
Added another version of create_graph that also takes in a random seed. This was to help with testing but could
also be useful in a proper implementation.
Added several get methods to the various classes to access their values.
Added a method to get a particular Node by Name because it was useful in the implementation of the isReachable method.
