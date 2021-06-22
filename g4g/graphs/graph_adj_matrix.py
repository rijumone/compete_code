'''
Ref:
https://www.geeksforgeeks.org/graph-and-its-representations/
https://ide.geeksforgeeks.org/9je5j6jJ13

'''

from pprint import pprint


class Graph:
    def __init__(self, n_vertex) -> None:
        self.adj_matrix = [[-1] * n_vertex for _ in range(n_vertex)]
        self.n_vertices = n_vertex
        self.vertices = {}  # key to index mapping
        self.vertice_lst = [0] * n_vertex  # just a list to store vertex_keys

    def add_vertex(self, vertex_idx, vertex_key):
        '''
        Add a new vertex and add it to\
            self.vertices and self.vertice_lst 
        Args:
            vertex_idx (int): should be in range: 0, len(self.vertice_lst) - 1)
            vertex_key (str): Data to be stored in the vertex
        '''
        if vertex_idx < 0 or vertex_idx >= len(self.vertice_lst):
            raise ValueError(
                f'Invalid vertex_idx: {vertex_idx}.\n'
                + f'vertex_idx needs to be between: 0 and {len(self.vertice_lst) - 1}')

        self.vertices[vertex_key] = vertex_idx  # key to index mapping
        self.vertice_lst[vertex_idx] = vertex_key

    def set_edge(self, _from, to, weight=1, is_directed=False):
        '''
        Add an edge between two vertices.
        Args:
            _from (str): key of vertex to add edge from
            to (str): key of vertex to add edge to
            weight (int): weight associated with the edge
            is_directed (bool): Whether graph is directed,\
                will add additional edge as per this arg
        '''
        # get index of vertex using mapping
        from_vertex = self.vertices[_from]
        to_vertex = self.vertices[to]
        self.adj_matrix[from_vertex][to_vertex] = weight
        if not is_directed:
            self.adj_matrix[to_vertex][from_vertex] = weight

    def get_vertex(self, ):
        return self.vertice_lst

    def get_edges(self, ):
        '''
        Will return a list of edges with each edge represented\
            as a tuple (ordered set) with items:
            - from vertex index
            - to vertex index
            - weight
        '''
        edges = []
        for i in range(self.n_vertices):
            for j in range(self.n_vertices):
                if self.adj_matrix[i][j] == -1:
                    # untouched
                    continue
                edges.append(
                    (self.vertice_lst[i], self.vertice_lst[j], self.adj_matrix[i][j]))
        return edges

    def get_matrix(self,):
        '''
        Pretty print adjacency matrix
        '''
        for i in range(self.n_vertices):
            for j in range(self.n_vertices):
                print(self.adj_matrix[i][j], end=' ')
            print()


def main():
    g = Graph(6)
    g.add_vertex(0, 'a')
    g.add_vertex(1, 'b')
    g.add_vertex(2, 'c')
    g.add_vertex(3, 'd')
    g.add_vertex(4, 'e')
    g.add_vertex(5, 'f')
    # g.add_vertex(6, 'g')
    g.set_edge('a', 'e', 10)
    g.set_edge('a', 'c', 20)
    g.set_edge('c', 'b', 30)
    g.set_edge('b', 'e', 40)
    g.set_edge('e', 'd', 50)
    g.set_edge('f', 'e', 60)
    print("Vertices of Graph")
    print(g.get_vertex())
    print("Edges of Graph")
    pprint(g.get_edges())
    print("Adjacency Matrix of Graph")
    print(g.get_matrix())


if __name__ == '__main__':
    main()
