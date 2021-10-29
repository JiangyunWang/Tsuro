```
Server              Client                          User
  |        ||         +<----------------             | Start client
  | Connect to socket |                              |
  |<==================|                              |
  |        ||         |                              |
  |        ||         |                              |
  |        ||         |                              |
  |        ||         |<---------------------------- | User Input
  |        ||         | Check if input is valid JSON |
  |        ||         | if not, jump to the end to   |
  |        ||         |      close connection        |
  |        ||         |     Req. to create           |
  |        ||         |                              |
  |        ||         | labyrinth with list of       |
  |        ||         | distinct edges               |
  |        ||         | lab_creation(list-of-edges)  |
  |<------------------|                              |
  | create labyrinth  |                              |
  |------------------>|                              | 
  |Send labyrinth obj |----------------------------->|
  |        ||         | store labyrinth obj and add  |
  |        ||         | edges with name of           |                   
  |        ||         | Nodes as from and to         |
  |        ||         |                              |
  |        ||         | Check if the given edge does |
  |        ||         | not exist in current edge    |
  |        ||         | edge realtions               |
  |<------------------| (distinct, unorderd edges)   |
  |add edge one by one|                              |
  | to labyrinth obj  |  addEdge(from, to)           |
  |------------------>|                              |
  |Send if successful |                              |
  |        ||         |----------------------------->|
  |        ||         |   Show response in JSON      |
  |        ||         |<-----------------------------|
  |        ||         |Req. to add Token with token's|
  |        ||         |color as color-string and name|
  |        ||         |of Node as name               |
  |        ||         |                              |
  |        ||         | Check if the Node is in the  |
  |        ||         | given labyrinth and the the  |
  |        ||         | color is one of              | 
  |        ||         | the color-string             |
  |        ||         |                              |
  |        ||         | token_check(list-of-tokens)  |
  |        ||         | addToken(color-string, name) |
  |<------------------|                              |
  |find node with func|                              |
  |getNode(name)      |                              |
  |Check if it exist  |                              |
  |and check if       |                              |
  |color-string is    |                              |
  |unique to create   |                              |
  |token and add to   |                              |
  |Node of that name  |                              |
  |------------------>|                              |
  |Send if successful |                              |
  |        ||         |----------------------------->|
  |        ||         |   Show response in JSON      |
  |        ||         |<-----------------------------|
  |        ||         |Req. to move Token with dest  |
  |        ||         |Node's name as name and token |
  |        ||         |color as color-string         |
  |        ||         |                              |
  |        ||         |Check if the Node of a        |
  |        ||         |moving token                  |
  |        ||         |was added to the labyrinth obj|
  |        ||         |and if the color is matched   |
  |        ||         |                              |
  |        ||         |                              |
  |        ||         |move(color-string, name)      |
  |<------------------|                              |
  |find node with func|                              |
  |getNode(name)      |                              |
  |getToken(color-str)|                              |
  |remove token from  |                              |
  |its current Node's |                              |
  |token list and add |                              |
  |it to the given    |                              |
  |Node's token list  |                              |
  |------------------>|                              |
  |Send if successful |                              |
  |        ||         |----------------------------->|
  |        ||         |   Show response in JSON      |
  |        ||         |<-----------------------------|
  |        ||         |   close connection           |
  |<==================|                              |
  | close connection  |                              |
  |                   |                              |
  |                   |                              |
  
                    .
```
