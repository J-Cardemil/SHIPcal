"""
This file includes the base Element class, this inherits most of the
components of any simulation.
"""
from iapws import IAPWS97

class Element:
    """
    Base class inherits every other element in SHIPcal.
    """

    def __init__(self):
        self._state_1 = IAPWS97(P=0.1, T=303) #Init state 1bar / 30ºC
        self._state_2 = IAPWS97(P=0.1, T=303) #Init state 1bar / 30ºC
        # First sets everything to 0
        [
            self.pressure_1_in, self.m_dot_1_in, self.temp_1_in,
            self.h_1_in, self.s_1_in, self.pressure_1_out,
            self.m_dot_1_out, self.temp_1_out, self.h_1_out,
            self.s_1_out, self.pressure_s_in, self.m_dot_s_in,
            self.temp_s_in, self.h_s_in, self.s_s_in,
            self.pressure_s_out, self.m_dot_s_out,
            self.temp_s_out, self.h_s_out, self.s_s_out
        ] = [0]*20

    # Primary
    # Inlet
    @property
    def pressure_1_in(self):
        """ [ bar ] Pressure at the primary inlet of the element """
        return self._pressure_1_in
    @pressure_1_in.setter
    def pressure_1_in(self, val):
        self._pressure_1_in = val

    @property
    def m_dot_1_in(self):
        """ [ kg/s ] Massic fluid at the primary inlet of the element """
        return self._m_dot_1_in
    @m_dot_1_in.setter
    def m_dot_1_in(self, val):
        self._m_dot_1_in = val

    @property
    def temp_1_in(self):
        """ [ C ] Temperature at the primary inlet of the element """
        return self._state_1.T-273
    @temp_1_in.setter
    def temp_1_in(self, val):
        self._state_1 = IAPWS97(P=self.pressure_1_in/10, T=val+273)

    @property
    def h_1_in(self):
        """ [ kWh/kg ] Specific enthalpy at the primary inlet of the element """
        return self._state_1.h/3600
    @h_1_in.setter
    def h_1_in(self,val):
        self._state_1 = IAPWS97(P=self.pressure_1_in/10, h=val*3600)

    @property
    def s_1_in(self):
        """ [ kWh/kgK ] Specifi entropy at the primary inlet of the element """
        return self._state_1.s/3600
    @s_1_in.setter
    def s_1_in(self, val):
        self._state_1 = IAPWS97(P=self.pressure_1_in/10, s=val*3600)

    # Outlet
    @property
    def pressure_1_out(self):
        """ [ bar ] Pressure at the primary outlet of the element """
        return self._pressure_1_out
    @pressure_1_out.setter
    def pressure_1_out(self, val):
        self._pressure_1_out = val

    @property
    def m_dot_1_out(self):
        """ [ kg/s ] Massic fluid at the primary outlet of the element """
        return self._m_dot_1_out
    @m_dot_1_out.setter
    def m_dot_1_out(self, val):
        self._m_dot_1_out = val

    @property
    def temp_1_out(self):
        """ [ C ] Temperature at the primary outlet of the element """
        return self._temp_1_out
    @temp_1_out.setter
    def temp_1_out(self, val):
        self._temp_1_out = val

    @property
    def h_1_out(self):
        """ [ kWh ] Enthalpy at the primary outlet of the element """
        return self._h_1_out
    @h_1_out.setter
    def h_1_out(self, val):
        self._h_1_out = val

    @property
    def s_1_out(self):
        """ [ kWh ] Entropy at the primary outlet of the element """
        return self._s_1_out
    @s_1_out.setter
    def s_1_out(self, val):
        self._s_1_out = val


    # Secondary
    # Inlet
    @property
    def pressure_s_in(self):
        """ [ bar ] Pressure at the secondary inlet of the element """
        return self._pressure_s_in
    @pressure_s_in.setter
    def pressure_s_in(self, val):
        self._pressure_s_in=val

    @property
    def m_dot_s_in(self):
        """ [ kg/s ] Massic fluid at the secondary inlet of the element """
        return self._m_dot_s_in
    @m_dot_s_in.setter
    def m_dot_s_in(self, val):
        self._m_dot_s_in=val

    @property
    def temp_s_in(self):
        """ [ C ] Temperature at the secondary inlet of the element """
        return self._temp_s_in
    @temp_s_in.setter
    def temp_s_in(self, val):
        self._temp_s_in=val

    @property
    def h_s_in(self):
        """ [ kWh ] Enthalpy at the secondary inlet of the element """
        return self._h_s_in
    @h_s_in.setter
    def h_s_in(self, val):
        self._h_s_in=val

    @property
    def s_s_in(self):
        """ [ kWh ] Entropy at the secondary inlet of the element """
        return self._s_s_in
    @s_s_in.setter
    def s_s_in(self, val):
        self._s_s_in=val

    # Outlet
    @property
    def pressure_s_out(self):
        """ [ bar ] Pressure at the secondary outlet of the element """
        return self._pressure_s_out
    @pressure_s_out.setter
    def pressure_s_out(self, val):
        self._pressure_s_out = val

    @property
    def m_dot_s_out(self):
        """ [ kg/s ] Massic fluid at the secondary outlet of the element """
        return self._m_dot_s_out
    @m_dot_s_out.setter
    def m_dot_s_out(self, val):
        self._m_dot_s_out = val

    @property
    def temp_s_out(self):
        """ [ C ] Temperature at the secondary outlet of the element """
        return self._temp_s_out
    @temp_s_out.setter
    def temp_s_out(self, val):
        self._temp_s_out = val

    @property
    def h_s_out(self):
        """ [ kWh ] Enthalpy at the secondary outlet of the element """
        return self._h_s_out
    @h_s_out.setter
    def h_s_out(self, val):
        self._h_s_out = val

    @property
    def s_s_out(self):
        """ [ kWh ] Entropy at the secondary outlet of the element """
        return self._s_s_out
    @s_s_out.setter
    def s_s_out(self, val):
        self._s_s_out = val


    # Thermal innertia
    
test1 = Element()
test1.pressure_1_in=6
test1.temp_1_in=60
print(test1.h_1_in)
test1.h_1_in = 0.06
print(test1.h_1_in)
