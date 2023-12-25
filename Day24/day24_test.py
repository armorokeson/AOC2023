def do_vectors_intersect(p1, v1, p2, v2):
    # p1, p2 are initial positions
    # v1, v2 are velocities
    
    # Check if vectors are parallel
    cross_product = v1[0] * v2[1] - v1[1] * v2[0]
    if cross_product == 0:
        # Vectors are parallel, they either never intersect or overlap
        return "Parallel vectors, check for overlap"
    
    # Solve for time of intersection
    t = ((p2[0] - p1[0]) * v2[1] - (p2[1] - p1[1]) * v2[0]) / cross_product
    
    # Check if time is valid
    if t >= 0:
        # Vectors intersect at t
        intersection_point = (p1[0] + t * v1[0], p1[1] + t * v1[1])
        return f"Vectors intersect at time {t} at point {intersection_point}"
    else:
        # Vectors do not intersect
        return "Vectors do not intersect"

# Example usage:
p1 = (19, 13)
v1 = (-2, 1)
p2 = (18, 19)
v2 = (-1, -1)

result = do_vectors_intersect(p1, v1, p2, v2)
print(result)
