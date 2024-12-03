import os

def combine_pdb_frames(input_folder, output_pdb):
    """
    Combine multiple PDB files into a single multi-frame PDB file for VMD.
    
    Args:
        input_folder (str): Folder containing individual PDB files (e.g., frame_000.pdb, frame_001.pdb, ...).
        output_pdb (str): Path to save the combined PDB file.
    """
    pdb_files = sorted([f for f in os.listdir(input_folder) if f.endswith(".pdb")])
    
    with open(output_pdb, 'w') as outfile:
        for pdb_file in pdb_files:
            with open(os.path.join(input_folder, pdb_file), 'r') as infile:
                for line in infile:
                    if not line.startswith("END"):  # Skip END lines
                        outfile.write(line)
                outfile.write("END\n")  # Add END line after each frame
    
    print(f"Combined {len(pdb_files)} frames into: {output_pdb}")

# Combine frames
input_folder = 'animate'  # Folder where intermediate frames are stored
output_pdb = 'equilibrium_trajectory.pdb'  # Path to save the combined PDB
combine_pdb_frames(input_folder, output_pdb)
