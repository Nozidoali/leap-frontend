module test1 (
    input wire a,
    input wire b,
    output wire y
);

assign y = ~a & b;
endmodule