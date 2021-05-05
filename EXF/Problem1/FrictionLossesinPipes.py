import math

class PipeFriction():
    def __init__(self):
        # Given by User
        self.units = 0
        self.fluid_dynamic_viscosity = None
        self.fluid_density = None
        self.diameter = None
        self.length = None
        self.volumetric_flow_rate = None

        # Calculated in Program
        self.roughness = None
        self.Re = None  # Reynolds Number
        self.friction_factor = None
        self.flow = None
        self.velocity = None
        self.head_loss = None

    def calc_velocity(self):
        self.velocity = self.volumetric_flow_rate / math.pi * (self.diameter / 2) ** 2

    def calc_reynolds_number(self):
        self.calc_velocity()
        self.Re = (self.fluid_density*self.velocity*self.diameter) / self.fluid_dynamic_viscosity

    def calc_roughness(self):
        self.roughness = 0.0000015 if self.units == 0 else .000005  # m or ft

    def calc_friction_factor(self):
        self.calc_reynolds_number()
        self.calc_roughness()
        if self.Re < 2000:
            self.friction_factor = 64 / self.Re
            self.flow = 'Laminar'
        elif self.Re > 4000:
            self.friction_factor = 1.325 / (
                math.log(self.roughness / (3.7 * self.diameter) + 5.74 / self.Re ** 0.9)) ** 2
            self.flow = 'Turbulent'
        else:
            self.friction_factor = 0.316 * self.Re ** (-0.25)
            self.flow = 'Transition'

    def calc_head_loss(self, gravity):
        self.calc_friction_factor()
        self.head_loss = self.friction_factor*(self.length/self.diameter)*((self.velocity**2)/2*gravity)

    def run(self):

        print('Friction Loss in a Pipe\t - Please input the the following values:.')
        self.units = int(input('Input 0 for Metric Units, or 1 for English Units: '))
        if self.units == 0:  # Metric
            self.fluid_dynamic_viscosity = float(input('Fluid Viscosity (Default = 0.00089) (Pa*s): '))
            self.fluid_density = float(input('Fluid Density (Default = 1000) (kg/m^3): '))
            self.diameter = float(input('Pipe Diameter(m): '))
            self.length = float(input('Pipe Length(m): '))
            self.volumetric_flow_rate = float(input('Volumetric Flow Rate(L/m): '))
            self.calc_head_loss(9.81)
            print('\n'*2)
            print(f'Reynolds Number: {self.Re:.2f}\nFlow Regime: {self.flow}\nHead Loss: {self.head_loss:.2f} N/m^2')

        elif self.units == 1:  # English
            self.fluid_dynamic_viscosity = float(input('Fluid Viscosity (Default = .00003732) (lb*s/ft^2): '))
            self.fluid_density = float(input('Fluid Density (Default = 62.4) (lb/ft^3): '))
            self.diameter = float(input('Pipe Diameter(ft): '))
            self.length = float(input('Pipe Length(ft): '))
            self.volumetric_flow_rate = float(input('Volumetric Flow Rate(Gpm): '))
            self.calc_head_loss(32.2)
            print('\n' * 2)
            print(f'Reynolds Number: {self.Re:.2f}\nFlow Regime: {self.flow}\nHead Loss: {self.head_loss:.2f} lb/ft^2')


if __name__ == '__main__':
    program = PipeFriction()
    program.run()
