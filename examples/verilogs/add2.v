module add
(
    a,
    b,
    out
);

input [31:0] a;
input [31:0] b;

reg [31:0] c;

output [31:0] out;

assign out = c + a;
always @(*)
begin
    c = a + b;
end

endmodule