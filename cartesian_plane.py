import matplotlib.pyplot as plt

class CartesianPlane:
    FALLBACK_AXES_LIMIT = 5

    def __init__(self, axes_limits = [(-5, 5)] ):
        if not self._check_limits_valid(axes_limits):
           axes_limits = [(CartesianPlane.FALLBACK_AXES_LIMIT * -1,CartesianPlane.FALLBACK_AXES_LIMIT)]
        self._set_axes_limits(axes_limits)
  
    def _set_axes_limits(self, limits):
        self._x_min = limits[0][0]
        self._x_max = limits[0][1]
        has_y = len(limits) > 1 and limits[1][1] 
        self._y_min = limits[1][0] if has_y else self._x_min
        self._y_max = limits[1][1] if has_y else self._x_max
         
    def _check_limits_valid(self, limits) -> bool:
        if not isinstance(limits, list):
            return False
        for limit in limits:
            if not isinstance(limit, tuple) or len(limit) != 2 or not all(isinstance(value, float) for value in limit):
                return False
        return True

    
