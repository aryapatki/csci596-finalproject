def xyz_to_pdb(xyz_file, pdb_file):
    """
    Convert an XYZ file to PDB format, including KE as the B-factor.
    
    Args:
    - xyz_file (str): Path to the input .xyz file.
    - pdb_file (str): Path to the output .pdb file.
    """
    with open(xyz_file, 'r') as xyz, open(pdb_file, 'w') as pdb:
        lines = xyz.readlines()
        num_atoms = int(lines[0].strip())  # First line contains the number of atoms
        timestep = lines[1].strip()       # Second line contains the timestep (optional description)
        
        pdb.write(f"REMARK   Timestep: {timestep}\n")  # Add a remark with the timestep
        pdb.write("MODEL 1\n")  # Start the first model
        
        # Iterate through atom data
        for i, line in enumerate(lines[2:2 + num_atoms]):
            parts = line.split()
            atom_type = parts[0]  # Atom type (e.g., 1)
            x, y, z = map(float, parts[1:4])  # Atom coordinates
            ke = float(parts[4])  # Kinetic energy
            
            # Write in PDB format
            pdb.write(
                f"ATOM  {i+1:5d}  {atom_type:2s}  MOL     1    "
                f"{x:8.3f}{y:8.3f}{z:8.3f}  1.00{ke:8.3f}\n"
            )
        
        pdb.write("ENDMDL\n")  # End the model

# Convert the .xyz file to .pdb format
xyz_to_pdb('output_with_ke.xyz', 'output_with_ke.pdb')
