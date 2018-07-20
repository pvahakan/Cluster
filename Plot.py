from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

class Plot:

    def __init__(self, data=None, cluster1=None, cluster2=None):
        """
        Initialize. At the moment three different atom data 
        files can be plotted same time.

        :param data: An object, of atomic data.
        :param cluster1: An object, optional another atomic data.
        :param cluster2: An object, optional another atomic data.
        """
        self.data = data
        self.cluster1 = cluster1
        self.cluster2 = cluster2

    def scatter_3d(self):
        """
        Makes 3d plot from atom coordinates.

        The first data object from __init__ will be plotted with 
        color map. The second and the third will be plotted red 
        and blue respectively.
        """
        
        lp = 21.4               # Lattice parameter to x, y and z limits
                                # 21.379738176 Å (6x6x6)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")

        cm = plt.get_cmap('gnuplot')  # color map

        # The first data with color map
        if self.data != None:
            p1 = ax.scatter(
                self.data.x, self.data.y, self.data.z,
                s=80, c=self.data.t, marker="o", cmap=cm
            )
            fig.colorbar(p1)

        # The second data, color red
        if self.cluster1 != None:
            p2 = ax.scatter(
                self.cluster1.x, self.cluster1.y, self.cluster1.z,
                c="red", marker="o"
            )

        # The third data, color blue
        if self.cluster2 != None:
            p3 = ax.scatter(
                self.cluster2.x, self.cluster2.y, self.cluster2.z,
                c="blue", marker="o"
            )

        # Figures outlook
        ax.grid(False)
        
        ax.set_xlim(0, lp)
        ax.set_ylim(0, lp)
        ax.set_zlim(0, lp)
                
        ax.set_xlabel("x_axis")
        ax.set_ylabel("y_axis")
        ax.set_zlabel("z_axis")
        
        
        
        plt.show()
