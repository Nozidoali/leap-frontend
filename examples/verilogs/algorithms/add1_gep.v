// This module is a simple example of c = a[i+1]
module top(
    input a,
    output c
);
    wire [10:0] a;
    wire [2:0] i;

    wire [10:0] c;
    assign c = (a << 2) + (i + 1);
endmodule