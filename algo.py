import pyvista as pv
import numpy as np


def create_parametric_surface(x_func, y_func, z_func, x0, y0, z0, t_min, t_max, num_points=10):
    t = np.linspace(t_min, t_max, num_points)
    k = np.linspace(-10, 12, num_points)

    k,t = np.meshgrid(k,t)
    x_curves = x_func(t)
    y_curves = y_func(t)
    z_curves = z_func(t)

    x_1 = x_curves + k * (x0 - x_curves)
    y_1 = y_curves + k * (y0 - y_curves)
    z_1 = z_curves + k * (z0 - z_curves)


    return pv.StructuredGrid(x_1,y_1,z_1)

def create_cylinder_surface(x_func, y_func, z_func, vx, vy, vz, t_min, t_max, num_points=10):
    t = np.linspace(t_min, t_max, num_points)
    k = np.linspace(0, 1, num_points)

    k,t = np.meshgrid(k,t)

    x_curves = x_func(t)
    y_curves = y_func(t)
    z_curves = z_func(t)

    x_1 = x_curves + k * vx
    y_1 = y_curves + k * vy
    z_1 = z_curves + k * vz

    return pv.StructuredGrid(x_1,y_1,z_1)

def parametric_plane(u, v, P0, A, B):
    return P0 + u * A + v * B

# Define a point on the plane (P0) and two non-parallel vectors (A, B)
P0 = np.array([1, 0, 0])
A = np.array([0, 1, 0])
B = np.array([0, 0, 1])

# Define the parameters u and v
u = np.linspace(-10, 10, 100)
v = np.linspace(-10, 10, 100)

# Create a grid of points for u and v
U, V = np.meshgrid(u, v)

# Compute the points on the plane
points = np.array([parametric_plane(u, v, P0, A, B) for u, v in zip(np.ravel(U), np.ravel(V))])

# Reshape the points array to match the shape of U and V
points = points.reshape(U.shape + (3,))

# Print some points on the plane
print(points)


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def toList(self):
        return [self.x, self.y, self.z]

def create_straight_line(A, B):
    return pv.Line(A.toList(), B.toList())

def create_curve_line(x_func, y_func, z_func, t_min, t_max, num_points=100):
    t = np.linspace(t_min, t_max, num_points)
    x = x_func(t)
    y = y_func(t)
    z = z_func(t)
    points = np.column_stack((x, y, z))
    return pv.Spline(points)

class StraightLine:
    def __init__(self, plot, A, B, color='red', width=1):
        plot.add_mesh(create_straight_line(A, B), color=color, line_width=4)

class CurveLine:
    def __init__(self, plot, x_func, y_func, z_fun, t_min, t_max, color='red', num_points=100):
        plot.add_mesh(create_curve_line(x_func, y_func, z_fun, t_min, t_max, num_points), color=color, line_width=4)

def find_direction_vectors(normal):
    if not np.all(normal == np.array([0, 0, 1])):
        V = np.array([1, 0, 0])
    else:
        V = np.array([0, 1, 0])

    D1 = np.cross(normal, V)
    D2 = np.cross(normal, D1)
    return D1, D2

def parametric_plane_equation(point, normal, t, s):
    D1, D2 = find_direction_vectors(normal)
    return point + t * D1 + s * D2

# Введите вектор нормали и точку на плоскости
normal = np.array([1, 2, 3])
point = np.array([1, 1, 1])

# Выберите значения для параметров t и s
t = 0.5
s = 0.3

# Вычислите точку на плоскости с использованием параметрического уравнения
result_point = parametric_plane_equation(point, normal, t, s)
print("Точка на плоскости с параметрами t и s:", result_point)


def parametric_curve(t):
    x = np.cos(t)*0
    y = np.sin(t)
    z = t
    return np.vstack((x, y, z)).T

def create_revolution_surface(curve_func, t_range, direction, num_points_t=100, num_points_theta=100):
    t = np.linspace(t_range[0], t_range[1], num_points_t)
    points_on_curve = curve_func(t)

    direction = direction / np.linalg.norm(direction)
    theta = np.linspace(0, 2 * np.pi, num_points_theta)

    surface_points = []

    for point in points_on_curve:
        plane_points = []
        for angle in theta:
            rotation_matrix = np.array([[np.cos(angle) + direction[0] ** 2 * (1 - np.cos(angle)),
                                          direction[0] * direction[1] * (1 - np.cos(angle)) - direction[2] * np.sin(angle),
                                          direction[0] * direction[2] * (1 - np.cos(angle)) + direction[1] * np.sin(angle)],
                                         [direction[1] * direction[0] * (1 - np.cos(angle)) + direction[2] * np.sin(angle),
                                          np.cos(angle) + direction[1] ** 2 * (1 - np.cos(angle)),
                                          direction[1] * direction[2] * (1 - np.cos(angle)) - direction[0] * np.sin(angle)],
                                         [direction[2] * direction[0] * (1 - np.cos(angle)) - direction[1] * np.sin(angle),
                                          direction[2] * direction[1] * (1 - np.cos(angle)) + direction[0] * np.sin(angle),
                                          np.cos(angle) + direction[2] ** 2 * (1 - np.cos(angle))]])
            rotated_point = point.dot(rotation_matrix)
            plane_points.append(rotated_point)
        surface_points.append(plane_points)

    surface_points = np.array(surface_points)
    X, Y, Z = surface_points[:, :, 0], surface_points[:, :, 1], surface_points[:, :, 2]

    return X, Y, Z

t_range = (0, 4 * np.pi)
direction = np.array([0, 0, 1])
X, Y, Z = create_revolution_surface(parametric_curve, t_range, direction)
grid = pv.StructuredGrid(X, Y, Z)