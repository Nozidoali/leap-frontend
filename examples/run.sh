
input_file=toy.v
output_file=toy.blif
top_module=toy

yosys -p "read_verilog $input_file; 
    hierarchy -check -top $top_module; 
    proc;
    opt -nodffe -nosdff;
    memory -nomap;
    techmap;
    flatten;
    clean;
    write_blif $output_file" > /dev/null
