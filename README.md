# csci596-finalproject

1. run inpur_script.lmp 
2. step 1 generated dump file and log.lammps file
3. run convert_to_xyz.py this generates a xyz file
4. run xyzTopdb.py this generates the output_with_ke.pdb file. (this pdb file has only KE values)
5. run pdb_processing.py (this script gives RGB values to every atom according to its KE), this generates output_with_rgb.pdb
6. generate output_without_column.pdd where the rightmost column having one is removed.
7. run generate_animation to get a folder of 300 pdb files showing static frames of atoms at different times
8. run combinepdbs.py to cobine all the pdbs into single file 
9. upload the file to vmd as a new molecule.

