### Overview
The purpose of this document is to provide specifications for the interface of
Labyrinth module by providing data definition, interface features requirement, technical specification, and usability.

### 1. Data Definition
**Labyrinth** 
A labyrinth is a simple graph made up of Nodes and Edges. Each Node must have a unique name and at most one Edge
between a pair of Nodes. For our purpose, a simple graph follows the conventional definition of which it is
an unweighted and undirected graph composed of a set of Nodes and a set of Edges.

**Token**
A Token is a characteristic that describe a Node. For this interface, the design of a Token must allows
for creation of specific types of Token. Each concrete implementation of a Token is expected to be able to identity equality against another Token. This is used to detect when multiple instances of a Token are duplicates of each other.
In this design, we require color Token to be a concrete type of a Token. A color Token uses its color attributes to define its uniqueness (Example: there should not be two instances of a Color Token with the attribute of RGB(0,0,0)).

**Node**
A Node is a vertex that has a text name and a set of Tokens.

**Edge**
An Edge must have one from Node and one to Node.

### 2. Interface feature requirements
We should be able to use the labrynth module to:
1. Create a plain labirynth (a labyrinth with no Token) given a set of unique Node names
2. Create Tokens and add them to a Node within the labrynth. One required type of Token is a ColorToken
3. Check to see if there is a color Token in the labrynth can reach a Node within the Labrynth

We list the recommended methods to achieve these interface requirements below.

**void addToken(String name, Token Token)** adds the given Token to a Node with the given Node name. The Token will not be added If the Node doesn't exist or if there exist another Token in the labrynth that is a duplicate (as defined above in the data definition of a Token).

**boolean isReachableFrom(String name, Token Token)** checks whether the given Token existing in the Labrynth can reach the
Node with the given name.

**void addNode(String name)** adds a Node with the given text name. If the name already exists in the labrynth, nothing will happen.

**void addEdge(String Node1, String Node2)** identify the Edge relationship between given Node1 and Node2.

**void removeNode(String name)** removes the Node with the given string name.

**void removeEdge(String Node1, String Node2)** removes the Edge relationship between given Node1 and Node2.

### 3. Technical Specification
**Language specification**: 
We choose to use Java 8 to implement this interface. Labyrinth must be contained in its own package that includes Nodes and Edges and their necessary functionalities.

### 4. Open question: Stakeholder and Usability

Currently, stakeholders and usability of this program is undefined. Scope of request loads are also unknown.
However, potential usability of this module includes accessible by a client from CLI or as an API or via import. Usability is sufficent as long as the module supports the requirements above.
