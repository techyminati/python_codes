import math


# Define all surface area and volume formulas
def surface_area_cube(side):
    return 6 * side * side

def volume_cube(side):
    return side * side * side

def surface_area_sphere(radius):
    return 4 * math.pi * radius * radius

def volume_sphere(radius):
    return (4.0 / 3.0) * math.pi * radius * radius * radius

def surface_area_cylinder(radius, height):
    return (2 * math.pi * radius * height) + (2 * math.pi * radius * radius)

def volume_cylinder(radius, height):
    return math.pi * radius * radius * height

def surface_area_cuboid(length, width, height):
    return 2 * (length * width + width * height + height * length)

def volume_cuboid(length, width, height):
    return length * width * height

def surface_area_cone(radius, height):
    return math.pi * radius * (radius + math.sqrt(height * height + radius * radius))

def volume_cone(radius, height):
    return (1.0 / 3.0) * math.pi * radius * radius * height

def surface_area_hemisphere(radius):
    return 3 * math.pi * radius * radius

def volume_hemisphere(radius):
    return (2.0 / 3.0) * math.pi * radius * radius * radius

def surface_area_frustum(radius1, radius2, height):
    return math.pi * (radius1 + radius2) * math.sqrt(height * height + (radius2 - radius1) * (radius2 - radius1))

def volume_frustum(radius1, radius2, height):
    return (1.0 / 3.0) * math.pi * height * (radius1 * radius1 + radius2 * radius2 + radius1 * radius2)

def surface_area_cone_hemisphere(radius, height):
    return surface_area_cone(radius, height) + surface_area_hemisphere(radius)

def volume_cone_hemisphere(radius, height):
    return volume_cone(radius, height) + volume_hemisphere(radius)

def surface_area_cylinder_cone(radius, height1, height2):
    return surface_area_cylinder(radius, height1) + surface_area_cone(radius, height2)

def volume_cylinder_cone(radius, height1, height2):
    return volume_cylinder(radius, height1) + volume_cone(radius, height2)

def surface_area_cylinder_hemisphere(radius, height):
    return surface_area_cylinder(radius, height) + 2 * surface_area_hemisphere(radius)

def volume_cylinder_hemisphere(radius, height):
    return volume_cylinder(radius, height) + 2 * (2.0 / 3.0) * volume_hemisphere(radius)

def surface_area_cylinder_2_cones(radius, height1, height2):
    return surface_area_cylinder(radius, height1) + 2 * surface_area_cone(radius, height2)

def volume_cylinder_2_cones(radius, height1, height2):
    return volume_cylinder(radius, height1) + 2 * volume_cone(radius, height2)
    
def main():
    print("Do you want normal surface area and volume of 3d shape or combination of multiple 3d shapes?")
    print("1. Singular shape")
    print("2. Combination of shapes")
    normorcomb = int(input())
    if normorcomb == 1:
        print("Enter the shape you want to calculate the surface area or volume for:")
        print("1. Cube")
        print("2. Sphere")
        print("3. Cylinder")
        print("4. Cuboid")
        print("5. Cone")
        print("6. Hemisphere")
        print("7. Frustrum of a cone")

        shape = int(input())

        print("Enter your choice:")
        print("1. Surface Area")
        print("2. Volume")

        option = int(input())

        if shape == 1:
            side = float(input("Enter the side length of the cube: "))
            if option == 1:
                print("Surface area of cube:", surface_area_cube(side))
            elif option == 2:
                print("Volume of cube:", volume_cube(side))
            else:
                print("Invalid choice. Try again.")
        elif shape == 2:
            radius = float(input("Enter the radius of the sphere: "))
            if option == 1:
                print("Surface area of sphere:", surface_area_sphere(radius))
            elif option == 2:
                print("Volume of sphere:", volume_sphere(radius))
            else:
                print("Invalid choice. Try again.")
        elif shape == 3:
            radius = float(input("Enter the radius of the cylinder: "))
            height = float(input("Enter the height of the cylinder: "))
            if option == 1:
                print("Surface area of cylinder:", surface_area_cylinder(radius, height))
            elif option == 2:
                print("Volume of cylinder:", volume_cylinder(radius, height))
            else:
                print("Invalid choice. Try again.")
        elif shape == 4:
            length = float(input("Enter the length of the cuboid: "))
            width = float(input("Enter the width of the cuboid: "))
            height = float(input("Enter the height of the cuboid: "))
            if option == 1:
                print("Surface area of cuboid:", surface_area_cuboid(length, width, height))
            elif option == 2:
                print("Volume of cuboid:", volume_cuboid(length, width, height))
            else:
                print("Invalid choice. Try again.")
        elif shape == 5:
            radius = float(input("Enter the radius of the cone: "))
            height = float(input("Enter the height of the cone: "))
            if option == 1:
                print("Surface area of cone:", surface_area_cone(radius, height))
            elif option == 2:
                print("Volume of cone:", volume_cone(radius, height))
            else:
                print("Invalid choice. Try again.")
        elif shape == 6:
            radius = float(input("Enter the radius of the hemisphere: "))
            if option == 1:
                print("Surface area of hemisphere:", surface_area_hemisphere(radius))
            elif option == 2:
                print("Volume of hemisphere:", volume_hemisphere(radius))
            else:
                print("Invalid choice. Try again.")
        elif shape == 7:
            radius1 = float(input("Enter the radius of the first base of the frustum: "))
            radius2 = float(input("Enter the radius of the second base of the frustrum: "))
            height = float(input("Enter the height of the frustum: "))
            if option == 1:
                print("Surface area of frustum:", surface_area_frustum(radius1, radius2, height))
            elif option == 2:
                print("Volume of frustum:", volume_frustum(radius1, radius2, height))
            else:
                print("Invalid choice. Try again.")
        else:
            print("Invalid shape. Try again.")
    else:
        print("Enter the Combination of shape you want to calculate the surface area and volume for:")
        print("1. Cone and hemisphere")
        print("2. Cylinder and Cone")
        print("3. Cylinder and hemisphere")
        print("4. cylinder with 2 cones")

        optioncomb = int(input())

        if optioncomb == 1:
            radius = float(input("Enter the radius of the cone: "))
            height = float(input("Enter the height of the cone: "))
            print("Surface area of the cone and hemisphere:", surface_area_cone_hemisphere(radius, height))
            print("Volume of the cone and hemisphere:", volume_cone_hemisphere(radius, height))
        elif optioncomb == 2:
            radius = float(input("Enter the radius of the cylinder: "))
            height = float(input("Enter the height of the cylinder: "))
            slant_height = float(input("Enter the height of the cone: "))
            print("Surface area of the cylinder and cone:", surface_area_cylinder_cone(radius, height, slant_height))
            print("Volume of the cylinder and cone:", volume_cylinder_cone(radius, height, slant_height))
        elif optioncomb == 3:
            radius = float(input("Enter the radius : "))
            height = float(input("Enter the height of the cylinder: "))
            print("Surface area of the Cylinder and hemisphere:", surface_area_cylinder_hemisphere(radius, height))
            print("Volume of the cylinder and hemisphere:", volume_cylinder_hemisphere(radius, height))
        elif optioncomb == 4:
            radius = float(input("Enter the radius: "))
            height1 = float(input("Enter the height of the cone 1: "))
            height2 = float(input("Enter the height of the cone 2: "))
            print("Surface area of the cylinder and 2 cones:", surface_area_cylinder_2_cones(radius, height1, height2))
            print("Volume of the cylinder and cone:", volume_cylinder_2_cones(radius, height1, height2))
        else:
            print("Invalid combination option. Try again.")

if __name__ == "__main__":
    main()

