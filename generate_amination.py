import numpy as np

def generate_intermediate_frames(input_pdb, output_folder, num_frames=100):
    """
    Generate intermediate frames where atoms gradually equilibrate by interpolating positions and properties.
    
    Args:
        input_pdb (str): Path to the input PDB file.
        output_folder (str): Path to save the generated PDB files.
        num_frames (int): Number of intermediate frames to generate.
    """
    import os

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the input PDB file
    with open(input_pdb, 'r') as file:
        pdb_lines = file.readlines()

    # Parse the atom data
    atoms = []
    for line in pdb_lines:
        if line.startswith("ATOM"):
            # Parse atom properties: ID, x, y, z, scalar property (e.g., occupancy)
            atom_id = int(line[6:11].strip())
            x = float(line[30:38].strip())
            y = float(line[38:46].strip())
            z = float(line[46:54].strip())
            scalar = float(line[54:60].strip())  # Scalar property (e.g., temperature)
            atoms.append([atom_id, x, y, z, scalar])
    
    # Convert to a numpy array for easy processing
    atoms = np.array(atoms)

    # Define final equilibrium state (average positions and scalar properties)
    final_positions = atoms[:, 1:4] + np.random.uniform(-0.1, 0.1, size=atoms[:, 1:4].shape)  # Slightly shift positions
    final_scalar = np.mean(atoms[:, 4]) * np.ones_like(atoms[:, 4])  # Set scalar to equilibrium value

    # Generate intermediate frames
    for frame in range(num_frames):
        # Interpolate positions and scalar values
        interpolated_positions = atoms[:, 1:4] + frame / (num_frames - 1) * (final_positions - atoms[:, 1:4])
        interpolated_scalar = atoms[:, 4] + frame / (num_frames - 1) * (final_scalar - atoms[:, 4])

        # Write to a new PDB file
        with open(os.path.join(output_folder, f"frame_{frame:03d}.pdb"), 'w') as output_file:
            for i, atom in enumerate(atoms):
                output_file.write(
                    f"ATOM  {int(atom[0]):5d}  1   MOL     1    {interpolated_positions[i, 0]:8.3f}{interpolated_positions[i, 1]:8.3f}{interpolated_positions[i, 2]:8.3f}  {interpolated_scalar[i]:6.2f}  REMARK\n"
                )
            output_file.write("END\n")

    print(f"Generated {num_frames} intermediate frames in folder: {output_folder}")

# Run the script
input_pdb = 'output_without_column.pdb'  # Path to your input PDB
output_folder = 'animate'  # Folder to save intermediate frames
generate_intermediate_frames(input_pdb, output_folder, num_frames=100)