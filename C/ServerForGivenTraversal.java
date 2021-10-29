import java.util.List;

public class Node {
    public String name;
    public List<Node> neighbors;

    public Node(String name, List<Node> neighbors) {
        this.name = name;
        this.neighbors = neighbors;
    }

    protected boolean checkContain(Node node, List<Node> nodes) {
        for (Node n: nodes) {
            if(n.name == node.name) {
                return true;
            }
        }
        return false;
    }

    public void addNeighbors(Node neighbor) {
        if (!checkContain(neighbor, this.neighbors)) {
            this.neighbors.add(neighbor);
            if (!checkContain(this, neighbor.neighbors)) {
                neighbor.neighbors.add(this);
            }
        }
    }

}




