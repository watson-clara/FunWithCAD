
import pyautocad

# Connect to AutoCAD
acad = pyautocad.Autocad()

# Define cone parameters
cone_radius = 10  # Radius of the cone base
cone_height = 20  # Height of the cone
scoop_radius = 8  # Radius of the ice cream scoop

# Draw cone
cone_center = (0, 0)  # Center of the cone base
cone_base = acad.model.AddCircle(cone_center, cone_radius)
cone_apex = (cone_center[0], cone_center[1] + cone_height)
cone_side = acad.model.AddLine(cone_center, cone_apex)

# Draw ice cream scoop
scoop_center = (cone_center[0], cone_center[1], cone_height)
scoop = acad.model.AddCircle(scoop_center, scoop_radius)

# Apply colors
cone_base.TrueColor = pyautocad.RGB(255, 215, 0)  # Gold color
cone_side.TrueColor = pyautocad.RGB(255, 215, 0)  # Gold color
scoop.TrueColor = pyautocad.RGB(255, 105, 180)   # Pink color

# Set layer properties
acad.model.AddLayer("IceCream", pyautocad.constants.acColorMagenta)
acad.model.ActiveLayer = "IceCream"
cone_base.Layer = "IceCream"
cone_side.Layer = "IceCream"
scoop.Layer = "IceCream"