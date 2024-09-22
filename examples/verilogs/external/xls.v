module user_module(
  input wire clk,
  input wire [7:0] a,
  input wire [7:0] b,
  input wire [7:0] c,
  output wire [7:0] out
);
  // lint_off MULTIPLY
  function automatic [7:0] umul8b_8b_x_8b (input reg [7:0] lhs, input reg [7:0] rhs);
    begin
      umul8b_8b_x_8b = lhs * rhs;
    end
  endfunction
  // lint_on MULTIPLY

  // ===== Pipe stage 0:

  // Registers for pipe stage 0:
  reg [7:0] p0_a;
  reg [7:0] p0_b;
  reg [7:0] p0_c;
  always_ff @ (posedge clk) begin
    p0_a <= a;
    p0_b <= b;
    p0_c <= c;
  end

  // ===== Pipe stage 1:
  wire [7:0] p1_umul_15_comb;
  assign p1_umul_15_comb = umul8b_8b_x_8b(p0_a, p0_b);

  // Registers for pipe stage 1:
  reg [7:0] p1_c;
  reg [7:0] p1_umul_15;
  always_ff @ (posedge clk) begin
    p1_c <= p0_c;
    p1_umul_15 <= p1_umul_15_comb;
  end

  // ===== Pipe stage 2:
  wire [7:0] p2_add_20_comb;
  assign p2_add_20_comb = p1_umul_15 + p1_c;

  // Registers for pipe stage 2:
  reg [7:0] p2_add_20;
  always_ff @ (posedge clk) begin
    p2_add_20 <= p2_add_20_comb;
  end
  assign out = p2_add_20;
endmodule