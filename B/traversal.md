##### Develop a module, dubbed Labyrinth, which is a connectivity specification for nodes in a simple graph.
##### Language specification: use version 3.7.3 Python   

To create a graph, we need to have nodes which connect the graph. We will create a class called Node. It's supposed to have a name variable to store the name of the Node, and have a list variable to store the neighbor nodes. There's only one edge between each pair of nodes.

Implement method `create_graph(x, y)`. X is the width of the labyrinth and y is the height of the labyrinth. It uses nested for-loop to construct a rectangle graph with named nodes. Implement Python [module random](https://docs.python.org/3/library/random.html) and use it to choose a node randomly and develop the labyrinth from there.

Implement `ColorToken` class that contains a color varaible. This is the representation of user's current location in labyrinth. By importing [PIL library](https://pillow.readthedocs.io/en/4.2.x/reference/Image.html), we can import image module and use method `Image.new("RGB", (x-coordinate, y-coordinate))` to color the `ColorToken` object. As the ColorToken move, update the Node object, remove `ColorToken` from previous's node's list, and then add it to the current node's list. Keep a global variable `ColorList` in the code. Every time when a `ColorToken` is constructed, first check if the color is already contained in the `ColorList`, raise and exception, else add the new color into the list to make sure every `ColorToken` object has an unique color.

Implement method `isReachable(src, dest)` to check if some colored token can reach some named graph node. In this method, using Breath First Search on the node graph and return true if a path is found. The colored token's Node object should be the `src` parameter and this function should return a boolean indicating whether the destination Node is reachable or not.

Test functions with unit testing by importing [unittest module](https://docs.python.org/3/library/unittest.html#module-unittest) and be aware of the choice of naming of variables.
