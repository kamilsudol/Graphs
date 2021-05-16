# Check if the incidence matrix already contains an edge
# inc -> incidence matrix
# v_one -> row index of vertex one in checked edge
# v_two -> row index of vertex two in checked edge
# checked_edge -> column index of the checked edge
# Returns True if there is a duplicate, False otherwise
def is_duplicate_edge(inc, v_one, v_two, checked_edge):
    # Get row indexes of vertices in checked edge
    for edge in range(len(inc[v_one])):
        if edge != checked_edge:
            #  Get row indexes of vertices in current edge
            [vertex_one_temp, vertex_two_temp] = edrng.find_vertices(len(inc), inc, edge)

            # Check if the vertices in current edge are the same as those in checked edge
            if v_one == vertex_one_temp and v_two == vertex_two_temp:
                return True
    return False