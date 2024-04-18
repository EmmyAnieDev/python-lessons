from cars_packages.car_module_one import CarColor


class CarMove:

    @classmethod
    def move(cls):
        return 'Car moved by driving'

class UseColor:

    @classmethod
    def color(cls):
        return f'All the cars color are {CarColor.all_color}'  # type: ignore
    
print(UseColor.color())