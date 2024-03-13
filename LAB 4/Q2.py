def get_cube_surface_area(length):
    try: 
        length = float(length)
    except ValueError:
        return (0, 'ERROR: The value is invalid!')
    except TypeError:
        return (0, 'ERROR: The type is incorrect!')
    else: 
        if length < 0:
            return (0, 'ERROR: length must be positive!')
        if length == 0:
            return (0, 'ERROR: Not a cube!')
        
        return (round(6*length**2), '')
    
print(get_cube_surface_area(10.5))   
print(get_cube_surface_area(-1))
print(get_cube_surface_area(0))
print(get_cube_surface_area('ten'))
print(get_cube_surface_area([1,2,3]))