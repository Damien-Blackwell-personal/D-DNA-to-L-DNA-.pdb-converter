# dbb's invert_dna.py

# replace "import_your.pdb" whith the file path to the d-dna .pdb you want to translate. 
#replace "name_for_exported_file.pdb" with the name you want for the exported file 



#-----------------------------------------------------------------------------------------------------------------------
  just coppy the script below:


with open('import_your.pdb', 'r') as f_in, open('name_for_exported_file.pdb', 'w') as f_out:
    for line in f_in:
        #this Only targets rows that contain atomic coordinates
        if line.startswith("ATOM") or line.startswith("HETATM"):
            try:
                #this Isolates the exact 8 characters containing the X coordinate
                x_str = line[30:38]
                #this Converts to a decimal number and invert the sign
                x_val = -float(x_str)
                #this Stitches the line back together with the new inverted X value
                new_line = line[:30] + f"{x_val:8.3f}" + line[38:]
                f_out.write(new_line)
            except ValueError:
                # If there is a formatting error, pass the line unchanged
                f_out.write(line)
        else:
            #this Keeps all headers, footers, and connectivity data exactly the same
            f_out.write(line)

#------------------------------------------------------------------------------------------------------------------------
