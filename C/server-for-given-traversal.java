import java.util.ArrayList;
import java.util.Stack;

// Labyrinth Class
public class Labyrinth {
  private ArrayList<Token> tokens;
  private ArrayList<Node> nodes;
  private ArrayList<Edge> edges;
  private String name;

  Labyrinth(name) {
    this.name = name;
    this.tokens = new ArrayList<>();
    this.nodes = new ArrayList<>();
    this.edges = new ArrayList<>();
  }

  // adds the given Token to a Node with the given Node name.
  public boolean addToken(String name, String color) {
    Token token = this.getToken(color);
    if(token != null && !this.tokens.contains(token)) {
      Node n = this.getNode(name);
      if(n != null) {
        n.addToken(token);
        return true;
      }
    }
    
    return false;
  }

  // adds a Node with the given text name.
  // If the name already exists in the labrynth, nothing will happen.
  public boolean addNode(String name) {
    Node nNode = new Node(name);
    if(!this.nodes.contains(nNode)) {
      this.nodes.add(nNode);
      return true;
    }

    return false;
  }

  // identify the Edge relationship between given Node1 and Node2
  public boolean addEdge(String node1, String node2) {
    Edge edge = this.getEdge(node1, node2);

    if(edge!= null && !this.edges.contains(edge)) {
      this.edges.add(edge);
      edge.getFrom().addToReachable(edge.getTo());
      return true;
    }

    return false;
  }

  // remove the Node with the given string name
  public boolean removeNode(String name){
    Node n = this.getNode(name);
    if(n != null) {
      this.nodes.remove(n);
      for(Edge edge: this.edges) {
        if(edge.getFrom().equals(n)) {
          this.edges.remove(edge);
        }
        if(edge.getTo().equals(n)) {
          this.edges.remove(edge);
          edge.getTo().removeFromReachable(n);
        }
      }
      return true;
    }
    
    return false;
  }

  // remove the Edge relationship between given Node objects with name Node1 and Node2
  public boolean removeEdge(String node1, String node2) {
    Edge edge = this.getEdge(node1, node2);
    if(edge!= null && !this.edges.contains(edge)) {
      this.edges.remove(edge);
      edge.getFrom().removeFromReachable(edge.getTo());
      return true;
    }

    return false;
  }

  // check whether the given Token existing in the Labyrinth
  // can reach the Node with the given name with DFS
  public boolean isReachableFrom(String name, Token token) {
    Node dest = this.getNode(name);
    if(name == null) return false;
    ArrayList<Node> visited = new ArrayList<>();
    Stack<Node> fringe = new Stack<>();
    fringe.add(token.getNode());
    visited.add(token.getNode());
    while(!fringe.isEmpty()) {
      Node node = fringe.pop();
      if(visited.contains(node)) {
        continue;
      }
      if(node.equals(dest)) {
        return true;
      }
      visited.add(node);
      for(Node n: node.getReachable()) {
        if(!visited.contains(n)) {
          fringe.push(n);
        }
      }
    }

    return false;
  }

  // move the Token with given string color to the Node with give name
  public boolean move(String color, String name) {
    Node node = this.getNode(name);
    Token token = this.getToken(color);
    if(node != null && token != null && this.isReachableFrom(name, token)) {
      Node oldNode = token.getNode();
      node.addToken(token);
      oldNode.removeToken(token);
      return true;
    }

    return false;
  }

  // helper method to get Edge with given name from the Edge list
  private Edge getEdge(String node1, String node2) {
    Node n1 = this.getNode(node1);
    Node n2 = this.getNode(node2);
    if(n1 == null || n2 == null) {
      return null;
    }
    return new Edge(n1, n2);
  }

  // helper method to get Token with given color string in the Token lists
  private Token getToken(String color) {
    for(Token token: this.tokens) {
      if(token.getColor().equals(color)) {
        return token;
      }
    }

    return null;
  }

  // helper method to get Node with given name from the Node list
  private Node getNode(String name) {
    for(Node n: this.nodes) {
      if(n.getName().equals(name)) {
        return n;
      }
    }
    return null;
  }
}

// Token Class
public class Token {
  private String color;
  private Node node;
  Token(String color) {
    this.color = color;
    this.node = null;
  }

  public String getColor() {
    return this.color;
  }

  public Node getNode() {
    return this.node;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (!(o instanceof Token)) return false;

    Token token = (Token) o;

    return getColor().equals(token.getColor());
  }
}

// Node Class
public class Node {
    private String name;
    private ArrayList<Token> tokens;
    private ArrayList<Node> reachable;

    Node(String name) {
      this.name = name;
      this.tokens = new ArrayList<>();
      this.reachable = new ArrayList<>();
    }

    public String getName() {
    return this.name;
  }

    public ArrayList<Node> getReachable() {
      return this.reachable;
    }

    public void addToReachable(Node node) {
      this.reachable.add(node);
    }

    public void removeFromReachable(Node node) {
      this.reachable.remove(node);
    }

    public void addToken(Token token) {
      if(!this.tokens.contains(token)) {
        this.tokens.add(token);
      }
    }

    public void removeToken(Token token) {
      if(this.tokens.contains(token)) {
        this.tokens.remove(token);
      }
    }

    @Override
    public boolean equals(Object obj) {
      if(obj == this) return true;
      if(!(obj instanceof Node)) return false;

      Node that = (Node) obj;

      return getName().equals(that.getName());
    }
}

// Edge class
public class Edge {
  private Node from;
  private Node to;

  Edge(Node from, Node to) {
    this.from = from;
    this.to = to;
  }

  public Node getFrom() {
    return this.from;
  }

  public Node getTo() {
    return this.to;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (!(o instanceof Edge)) return false;

    Edge edge = (Edge) o;

    return (getTo().equals(((Edge) o).getTo()) && getFrom().equals(((Edge) o).getFrom()))
    || (getTo().equals(((Edge) o).getFrom()) && getFrom().equals(((Edge) o).getTo()));
  }
}


