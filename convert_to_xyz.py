def convert_lammps_to_xyz(dump_file, output_file):
    import os

    try:
        # Check if input file exists
        if not os.path.exists(dump_file):
            print(f"Input file {dump_file} does not exist!")
            return

        print(f"Input file path: {os.path.abspath(dump_file)}")
        print(f"Output file path: {os.path.abspath(output_file)}")

        with open(dump_file, 'r') as f, open(output_file, 'w') as out:
            print("Files opened successfully.")
            lines = f.readlines()

            if not lines:
                print("Input file is empty.")
                return

            timestep = None
            num_atoms = None
            atom_data = []
            box_bounds = []

            print("Reading dump file...")
            for i, line in enumerate(lines):
                if "ITEM: TIMESTEP" in line:
                    timestep = int(lines[i + 1].strip())
                    print(f"Processing timestep: {timestep}")
                elif "ITEM: NUMBER OF ATOMS" in line:
                    num_atoms = int(lines[i + 1].strip())
                    print(f"Number of atoms: {num_atoms}")
                elif "ITEM: BOX BOUNDS" in line:
                    box_bounds = lines[i + 1:i + 4]
                    print(f"Box bounds: {box_bounds}")
                elif "ITEM: ATOMS" in line:
                    atom_data = lines[i + 1:i + 1 + num_atoms]
                    print(f"Found atom data for {num_atoms} atoms.")
                    print(f"Sample atom data: {atom_data[:5]}")  # Print a few atoms for debugging

                    # Write XYZ format
                    out.write(f"{num_atoms}\n")
                    out.write(f"Timestep: {timestep}\n")
                    for atom in atom_data:
                        atom_info = atom.split()
                        atom_type = atom_info[1]  # Assuming second column is atom type
                        x, y, z = atom_info[2:5]  # Assuming 3rd, 4th, 5th columns are x, y, z
                        out.write(f"{atom_type} {x} {y} {z}\n")
                    print(f"Data for timestep {timestep} written successfully.")

            print("Conversion complete. Output written to:", os.path.abspath(output_file))
    except Exception as e:
        print("An error occurred:", e)
