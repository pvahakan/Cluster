from Data import Data
from Plot import Plot

### Usage ###
#
# Create data objects from xyz-files you want to plot.
# xyz files must be comma separated at the moment.
# It is possible to have one additional column in the
# xyz file to be plotted as color map. If you want to
# write VMD compatible .xyz file, give argument True to
# class Data creator. To plot the 3d atomic figures
# create Plot object and give data objects as an argument
# (max 3). Then plot_object.scatter_3d() will show the
# graph.
#
# If you want plot only clusters (without color map),
# set first argument None in Plot constructor.
#
# 1) Create Data object(s)
# 2) Create Plot object
# 3) Plot what you want. (scatter_3d available atm.)

# --------------
# ---- main ----

rmsd_limit = 0.001 # default 0.005

data = Data("nv_coordinates_with_rmsd.xyz", limit=rmsd_limit)
C44 = Data("nv_6x6x6_C44_bl_1.1.xyz")
C165 = Data("nv_6x6x6_C165_bl_1.1.xyz")
C286 = Data("defekti_huonossa_paikassa_nv_6x6x6_C286_bl_1.1.xyz")


print("--------------------")
print(" RMSD limit: ", data.limit)
print("--------------------")

plot = Plot(data)
# plot = Plot(data, C286, C165)
# plot = Plot(None, C286, C165)
plot.scatter_3d()
