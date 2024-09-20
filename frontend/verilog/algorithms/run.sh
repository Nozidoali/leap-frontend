input_file=$1
output_file=$2
top_module=$3

# yosys -p "read_verilog $input_file; 
#     hierarchy -check -top $top_module; 
#     proc;
#     opt -nodffe -nosdff;
#     memory -nomap;
#     flatten;
#     clean;
#     write_blif $output_file" > /dev/null

yosys -p "read_verilog $input_file; 
    hierarchy -check -top $top_module; 
    synth;
    write_verilog $output_file" > /dev/null