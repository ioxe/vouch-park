class InputTransformerService:

    class Vertex:

        def __init__(self):
            self.line = ""
            self.start_index = 0
            self.end_index = 0

    def __init__(self):
        self.currentVertex = 0
        self.vertices = {}
        self.edges = {}

    def transform_array_to_graph(self, input_arr):
        self.currentVertex = 0
        self.vertices = {}
        self.edges = {}
        return self.create_graph(input_arr)

    def create_graph(self, input_arr):
        self.recurse_for_vertex(input_arr, 0, self.Vertex())
        self.get_edges_for_graph()
        output_vertices = {}
        for key, val in self.vertices.items():
            output_vertices[key] = val.line
        return output_vertices, self.edges

    def get_edges_for_graph(self):
        for key in self.vertices.keys():
            self.edges[key] = set()
        k = list(self.vertices.keys())[0]
        self.recurse_for_edge(k, self.vertices[k])

    def recurse_for_edge(self, current_vertex_id, current_vertex):
        vertices = self.find_vertices_with_start_index(current_vertex.end_index + 1)
        for vertex_id in vertices:
            self.edges[current_vertex_id].add(vertex_id)
            self.recurse_for_edge(vertex_id, self.vertices[vertex_id])

    def recurse_for_vertex(self, input_arr, current_index, vertex):

        # termination - end of the i/p array
        if len(input_arr) - 1 < current_index:
            vertex.end_index = current_index - 1
            if self.is_new_vertex(vertex):
                self.currentVertex += 1
                self.vertices[self.currentVertex] = vertex
            return

        for ele in input_arr[current_index]:
            if ele == ',':
                vertex.end_index = current_index - 1
                if self.is_new_vertex(vertex):
                    self.currentVertex += 1
                    self.vertices[self.currentVertex] = vertex

                new_vertex = self.Vertex()
                new_vertex.start_index = current_index
                self.recurse_for_vertex(input_arr, current_index + 1, new_vertex)
            else:

                temp_vertex = self.Vertex()
                temp_vertex.line = vertex.line + ele
                temp_vertex.start_index = vertex.start_index
                temp_vertex.end_index = vertex.end_index

                self.recurse_for_vertex(input_arr, current_index + 1, temp_vertex)

    def is_new_vertex(self, vertex_under_test):

        is_new_vertex = True

        for vertex in self.vertices.values():
            if vertex.line == vertex_under_test.line and vertex.start_index == vertex_under_test.start_index and vertex.end_index == vertex_under_test.end_index:
                is_new_vertex = False

        return is_new_vertex

    def find_vertices_with_start_index(self, start_index):
        result = []
        for key, value in self.vertices.items():
            if value.start_index == start_index:
                result.append(key)
        return result
