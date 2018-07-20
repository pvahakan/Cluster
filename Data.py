import csv
import numpy as np

class Data:

    def __init__(self, path, write=False, limit=0.005):
        """
        Initialize.

        :param path: A string, a path to the coordinate file.
        :param write: A boolean, selection of writing VMD-style
                      xyz file.
        """
        self.limit = limit
        self.path = path
        self.write = write
        self.atoms = []
        self.x = []
        self.y = []
        self.z = []
        self.t = []
        Data.read_data(self)

    def read_data(self):
        """
        Reads data from given path.

        If write parameter has been given True, function 
        will also write VMD-style xyz file.
        """

        # Read file
        try:
            with open(self.path, newline='') as datafile:
                reader = csv.reader(datafile, delimiter=',')
                for row in reader:
                    if len(row) == 5:
                        if float(row[4]) < 2 and float(row[4]) >= self.limit:
                            self.atoms.append(row[0])
                            self.x.append(float(row[1]))
                            self.y.append(float(row[2]))
                            self.z.append(float(row[3]))
                            self.t.append(float(row[4]))
                    elif len(row) == 4:
                        self.atoms.append(row[0])
                        self.x.append(float(row[1]))
                        self.y.append(float(row[2]))
                        self.z.append(float(row[3]))
                    else:
                        print("Unknown amount of columns in xyz file (", len(row), ")")
        except FileNotFoundError:
            print("Coordinate file not found. Check the file path.")

        # Convert to numpy arrays
        self.x = np.array(self.x)
        self.y = np.array(self.y)
        self.z = np.array(self.z)
        self.t = np.array(self.t)

        # Write xyz file
        if self.write == True:
            Data.write_to_file(self)
            print("VMD-compatible xyz file written.")
            
    def write_to_file(self):
        """
        Writes VMD-compatible .xyz file.
        """
        
        # Clean old stuff
        f = open("nv_coords_rmsd_" + str(self.limit) + ".xyz", "w")
        f.close()

        # Write coordinates
        f = open("nv_coords_rmsd_" + str(self.limit) + ".xyz", "a")
        f.write(str(len(self.atoms)) + "\n\n")
        for i in range(len(self.atoms)):
            f.write(
                str(self.atoms[i]) + "\t" +
                str(self.x[i]) + "\t" +
                str(self.y[i]) + "\t" +
                str(self.z[i]) + "\n"
            )
        f.close()

