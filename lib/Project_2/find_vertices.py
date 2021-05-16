# Finds vertices in an edge
# num_vertices -> number of vertices (number of rows)
# inc_matrix -> graph as incidence matrix
# edge_index -> column index of an edge
# Returns indices of vertices in an edge as an array [v1, v2] 
def find_vertices(num_vertices, inc_matrix, edge_index):
    vertices = [-1, -1]
    for row in range(num_vertices):
        # If cell in column is a vertex
        if inc_matrix[row][edge_index] == 1:
            # and haven't found vertex one
            if vertices[0] == -1:
                # Save vertex one
                vertices[0] = row
            else:
                # Save vertex two
                vertices[1] = row
    return vertices