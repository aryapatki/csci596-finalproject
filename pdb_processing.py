# Define the Python script to process the PDB file as described

def process_pdb_and_color(input_pdb, output_pdb):
    """
    Reads a PDB file, categorizes the 5th column (B-factor or KE) values into 5 ranges, 
    assigns colors (RGB format) to each range, and writes the new PDB with colors.

    Args:
    - input_pdb (str): Path to the input PDB file.
    - output_pdb (str): Path to the output PDB file with assigned colors.
    """
    import numpy as np

    # RGB color gradient: blue (low) to red (high)
    colors = [
        (0, 0, 255),   # Blue
        (0, 255, 255), # Cyan
        (0, 255, 0),   # Green
        (255, 255, 0), # Yellow
        (255, 0, 0)    # Red
    ]

    rows = []
    b_factors = []

    # Step 1: Read the input PDB file and extract the 5th column (B-factor values)
    with open(input_pdb, 'r') as infile:
        for line in infile:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                rows.append(line)
                b_factors.append(float(line[60:66].strip()))

    # Step 2: Determine value ranges for the B-factor
    b_factors = np.array(b_factors)
    min_b = b_factors.min()
    max_b = b_factors.max()
    ranges = np.linspace(min_b, max_b, num=6)  # 5 ranges, 6 boundaries

    # Step 3: Assign colors based on the range the B-factor falls into
    output_lines = []
    for line in rows:
        b_factor = float(line[60:66].strip())
        # Determine which range the B-factor belongs to
        for i in range(5):
            if ranges[i] <= b_factor < ranges[i+1]:
                color = colors[i]
                break
        else:
            color = colors[-1]  # Assign red to the highest value
        
        # Add the RGB color as a comment to the line
        color_comment = f"REMARK RGB {color[0]} {color[1]} {color[2]}"
        output_lines.append(line.strip() + f" {color_comment}\n")

    # Step 4: Write the new PDB file with colors
    with open(output_pdb, 'w') as outfile:
        outfile.writelines(output_lines)

# Process the uploaded file
input_pdb_path = 'output_with_ke.pdb'
output_pdb_path = 'output_with_rgb.pdb'
process_pdb_and_color(input_pdb_path, output_pdb_path)

# Confirm the output file has been created
output_pdb_path
