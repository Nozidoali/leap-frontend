`define MEMORY_CONTROLLER_ADDR_SIZE 32
`define MEMORY_CONTROLLER_DATA_SIZE 64
// Number of RAM elements: 3
`define MEMORY_CONTROLLER_TAG_SIZE 9
`timescale 1 ns / 1 ns

module leap_mem
(
	clk,
	reset,
	/* input address */
	addr_ld,
	addr_st,
	data_in,

	/* dual port - a */
	mem_en_a,
	mem_we_a,
	mem_addr_a,
	mem_in_a,
	mem_byteena_a,
	mem_out_a,
	/* dual port - b */
	mem_en_b,
	mem_we_b,
	mem_addr_b,
	mem_in_b,
	mem_byteena_b,
	mem_out_b,
	/* FSM */
	fsm_ld,
	fsm_st
);
input  clk;
input  reset;

output reg mem_we_a;
output reg [31:0] mem_in_a;
output mem_byteena_a;
output reg mem_en_a;
output reg [9:0] mem_addr_a;
input [31:0] mem_out_a;

output mem_we_b;
output [31:0] mem_in_b;
output mem_byteena_b;
output mem_en_b;
output [9:0] mem_addr_b;
input [31:0] mem_out_b;

input [31:0] addr_ld;
input [31:0] addr_st;
input [31:0] data_in;

input fsm_ld;
input fsm_st;

assign mem_byteena_a = 1'd1;

always @(*) begin
	mem_en_a = 1'd0;
	if ((fsm_ld)) begin
		mem_en_a = 1'd1;
	end
end

always @(*) begin
	mem_we_a = 1'd0;
	if ((fsm_st)) begin
		mem_we_a = 1'd1;
	end
end

always @(*) begin
	mem_in_a = 0;
	if ((fsm_st)) begin
		mem_in_a = data_in;
	end
end

always @(*) begin
	mem_addr_a = 10'd0;
	/* toy: %1*/
	/*   %4 = load i32* %scevgep4, align 4, !MSB !5, !LSB !2, !extendFrom !5*/
	if ((fsm_ld)) begin
		mem_addr_a = (addr_ld >>> 3'd2);
	end
	if ((fsm_st)) begin
		mem_addr_a = (addr_st >>> 3'd2);
	end
end

/* dual port - b is not used */
assign mem_en_b = 1'd0;
assign mem_we_b = 1'd0;
assign mem_in_b = 0;
assign mem_byteena_b = 1'd1;
assign mem_addr_b = 10'd0;

endmodule

module toy_fsm
(
	clk,
	reset,
	start,
	finish,
    fsm_stall,
    exitcond,
	is0,
	is_S1,
	is_S2,
	is_S3,
	is_S4
);

parameter [2:0] S0 = 3'd0;
parameter [2:0] S1 = 3'd1;
parameter [2:0] S2 = 3'd2;
parameter [2:0] S3 = 3'd3;
parameter [2:0] S4 = 3'd4;

input  clk;
input  reset;
input  start;
input  fsm_stall;
input  exitcond;
output reg  finish;
reg [2:0] cur_state;
reg [2:0] next_state;

output reg is0;
output reg is_S1;
output reg is_S2;
output reg is_S3;
output reg is_S4;


always @(posedge clk) begin
if (reset == 1'b1)
	cur_state <= S0;
else if (!fsm_stall)
	cur_state <= next_state;
end

always @(*)
begin
next_state = cur_state;
case(cur_state)  // synthesis parallel_case  
S0:
	if ((fsm_stall == 1'd0) && (start == 1'd1))
		next_state = S1;
S1:
		next_state = S2;
S2:
		next_state = S3;
S3:
	if ((fsm_stall == 1'd0) && (exitcond == 1'd1))
		next_state = S4;
	else if ((fsm_stall == 1'd0) && (exitcond == 1'd0))
		next_state = S1;
S4:
		next_state = S0;
default:
	next_state = cur_state;
endcase

end

always @(*)
begin
	is0 = (cur_state == S0);
	is_S1 = (cur_state == S1);
	is_S2 = (cur_state == S2);
	is_S3 = (cur_state == S3);
	is_S4 = (cur_state == S4);
end

always @(posedge clk) begin
	if ((is0)) begin
		finish <= 1'd0;
	end
	/* toy: %9*/
	/*   ret void, !MSB !1, !LSB !2, !extendFrom !1*/
	if ((is_S4)) begin
		finish <= (fsm_stall == 1'd0);
	end
end

endmodule

module leap_add
(
	clk,
	reset,

	/* inputs */
	in_a,
	in_b,

	/* outputs */
	out,

	/* control signals */
	fsm_add
);

input  clk;
input  reset;
input [31:0] in_a;
input [31:0] in_b;
output reg [31:0] out;
input  fsm_add;

always @(*) begin
	out = 0;
	if (fsm_add) begin
		out = (in_a + in_b);
	end
end

endmodule

module toy
(
	clk,
	clk2x,
	clk1x_follower,
	reset,
	memory_controller_waitrequest,
	start,
	finish,
	arg_a,
	arg_b,
	arg_c,
	main_0_a_write_enable_a,
	main_0_a_in_a,
	main_0_a_byteena_a,
	main_0_a_enable_a,
	main_0_a_address_a,
	main_0_a_out_a,
	main_0_a_write_enable_b,
	main_0_a_in_b,
	main_0_a_byteena_b,
	main_0_a_enable_b,
	main_0_a_address_b,
	main_0_a_out_b,
	main_0_b_write_enable_a,
	main_0_b_in_a,
	main_0_b_byteena_a,
	main_0_b_enable_a,
	main_0_b_address_a,
	main_0_b_out_a,
	main_0_b_write_enable_b,
	main_0_b_in_b,
	main_0_b_byteena_b,
	main_0_b_enable_b,
	main_0_b_address_b,
	main_0_b_out_b,
	main_0_c_write_enable_a,
	main_0_c_in_a,
	main_0_c_byteena_a,
	main_0_c_enable_a,
	main_0_c_address_a,
	main_0_c_out_a,
	main_0_c_write_enable_b,
	main_0_c_in_b,
	main_0_c_byteena_b,
	main_0_c_enable_b,
	main_0_c_address_b,
	main_0_c_out_b
);

input  clk;
input  clk2x;
input  clk1x_follower;
input  reset;
input  memory_controller_waitrequest;
input  start;
output finish;
input [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] arg_a;
input [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] arg_b;
input [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] arg_c;
output  main_0_a_write_enable_a;
output [31:0] main_0_a_in_a;
output  main_0_a_byteena_a;
output  main_0_a_enable_a;
output [9:0] main_0_a_address_a;
input [31:0] main_0_a_out_a;
output  main_0_a_write_enable_b;
output [31:0] main_0_a_in_b;
output  main_0_a_byteena_b;
output  main_0_a_enable_b;
output [9:0] main_0_a_address_b;
input [31:0] main_0_a_out_b;
output  main_0_b_write_enable_a;
output [31:0] main_0_b_in_a;
output  main_0_b_byteena_a;
output  main_0_b_enable_a;
output [9:0] main_0_b_address_a;
input [31:0] main_0_b_out_a;
output  main_0_b_write_enable_b;
output [31:0] main_0_b_in_b;
output  main_0_b_byteena_b;
output  main_0_b_enable_b;
output [9:0] main_0_b_address_b;
input [31:0] main_0_b_out_b;
output  main_0_c_write_enable_a;
output [31:0] main_0_c_in_a;
output  main_0_c_byteena_a;
output  main_0_c_enable_a;
output [9:0] main_0_c_address_a;
input [31:0] main_0_c_out_a;
output  main_0_c_write_enable_b;
output [31:0] main_0_c_in_b;
output  main_0_c_byteena_b;
output  main_0_c_enable_b;
output [9:0] main_0_c_address_b;
input [31:0] main_0_c_out_b;



reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] arg_a_reg;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] arg_b_reg;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] arg_c_reg;
reg  fsm_stall;
reg [9:0] toy_1_indvar;
reg [9:0] toy_1_indvar_reg;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] toy_1_scevgep2;
reg [10:0] i;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] toy_1_scevgep4;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] toy_1_scevgep3;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] toy_1_scevgep;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] toy_1_scevgep_reg;
reg [10:0] j;
reg [10:0] j_reg;
reg [31:0] toy_1_4;
reg [31:0] toy_1_5;
reg [31:0] toy_1_6;
reg [31:0] toy_1_7;
reg [31:0] toy_1_8;
reg  exitcond;
reg  exitcond_reg;

// Local Rams

toy_fsm toy_fsm_inst
(
	.clk(clk),
	.reset(reset),
	.start(start),
	.finish(finish),
    .fsm_stall(fsm_stall),
    .exitcond(exitcond_reg),
	.is0(is0),
	.is_S1(is_S1),
	.is_S2(is_S2),
	.is_S3(is_S3),
	.is_S4(is_S4)
);

leap_mem leap_mem_a_inst
(
	.clk(clk),
	.reset(reset),
	.addr_ld(toy_1_scevgep4),
	.addr_st(32'b0),
	.data_in(32'b0),
	.mem_en_a(main_0_a_enable_a),
	.mem_we_a(main_0_a_write_enable_a),
	.mem_addr_a(main_0_a_address_a),
	.mem_in_a(main_0_a_in_a),
	.mem_byteena_a(main_0_a_byteena_a),
	.mem_out_a(main_0_a_out_a),
	.mem_en_b(main_0_a_enable_b),
	.mem_we_b(main_0_a_write_enable_b),
	.mem_addr_b(main_0_a_address_b),
	.mem_in_b(main_0_a_in_b),
	.mem_byteena_b(main_0_a_byteena_b),
	.mem_out_b(main_0_a_out_b),
	.fsm_ld(is_S1),
	.fsm_st(1'b0)
);

leap_mem leap_mem_b_inst
(
	.clk(clk),
	.reset(reset),
	.addr_ld(toy_1_scevgep3),
	.addr_st(32'b0),
	.data_in(32'b0),
	.mem_en_a(main_0_b_enable_a),
	.mem_we_a(main_0_b_write_enable_a),
	.mem_addr_a(main_0_b_address_a),
	.mem_in_a(main_0_b_in_a),
	.mem_byteena_a(main_0_b_byteena_a),
	.mem_out_a(main_0_b_out_a),
	.mem_en_b(main_0_b_enable_b),
	.mem_we_b(main_0_b_write_enable_b),
	.mem_addr_b(main_0_b_address_b),
	.mem_in_b(main_0_b_in_b),
	.mem_byteena_b(main_0_b_byteena_b),
	.mem_out_b(main_0_b_out_b),
	.fsm_ld(is_S1),
	.fsm_st(1'b0)
);

leap_mem leap_mem_c_inst
(
	.clk(clk),
	.reset(reset),
	.addr_ld(toy_1_scevgep2),
	.addr_st(toy_1_scevgep_reg),
	.data_in(toy_1_8),
	.mem_en_a(main_0_c_enable_a),
	.mem_we_a(main_0_c_write_enable_a),
	.mem_addr_a(main_0_c_address_a),
	.mem_in_a(main_0_c_in_a),
	.mem_byteena_a(main_0_c_byteena_a),
	.mem_out_a(main_0_c_out_a),
	.mem_en_b(main_0_c_enable_b),
	.mem_we_b(main_0_c_write_enable_b),
	.mem_addr_b(main_0_c_address_b),
	.mem_in_b(main_0_c_in_b),
	.mem_byteena_b(main_0_c_byteena_b),
	.mem_out_b(main_0_c_out_b),
	.fsm_ld(is_S1),
	.fsm_st(is_S2)
);

// End Local Rams

always @(posedge clk) begin
	if (start) begin
		arg_a_reg <= arg_a;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_b_reg <= arg_b;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_c_reg <= arg_c;
	end
end
always @(*) begin
	fsm_stall = 1'd0;
	if (reset) begin
		fsm_stall = 1'd0;
	end
	if (memory_controller_waitrequest) begin
		fsm_stall = 1'd1;
	end
end
always @(*) begin
	/* toy: %1*/
	/*   %indvar = phi i32 [ %3, %1 ], [ 0, %0 ], !MSB !3, !LSB !2, !extendFrom !3*/
	if ((((is0) & (fsm_stall == 1'd0)) & (start == 1'd1))) begin
		toy_1_indvar = 32'd0;
	end
	/* toy: %1*/
	/*   %indvar = phi i32 [ %3, %1 ], [ 0, %0 ], !MSB !3, !LSB !2, !extendFrom !3*/
	else /* if ((((is_S3) & (fsm_stall == 1'd0)) & (exitcond_reg == 1'd0))) */ begin
		toy_1_indvar = j_reg;
	end
end
always @(posedge clk) begin
	/* toy: %1*/
	/*   %indvar = phi i32 [ %3, %1 ], [ 0, %0 ], !MSB !3, !LSB !2, !extendFrom !3*/
	if ((((is0) & (fsm_stall == 1'd0)) & (start == 1'd1))) begin
		toy_1_indvar_reg <= toy_1_indvar;
	end
	/* toy: %1*/
	/*   %indvar = phi i32 [ %3, %1 ], [ 0, %0 ], !MSB !3, !LSB !2, !extendFrom !3*/
	if ((((is_S3) & (fsm_stall == 1'd0)) & (exitcond_reg == 1'd0))) begin
		toy_1_indvar_reg <= toy_1_indvar;
	end
end
always @(*) begin
	/* toy: %1*/
	/*   %scevgep2 = getelementptr i32* %c, i32 %indvar, !MSB !1, !LSB !2, !extendFrom !1*/
		toy_1_scevgep2 = (arg_c_reg + (4 * {22'd0,toy_1_indvar_reg}));
end
always @(*) begin
	/* toy: %1*/
	/*   %2 = add i32 %indvar, 1, !MSB !4, !LSB !2, !extendFrom !4*/
		i = ({1'd0,toy_1_indvar_reg} + 32'd1);
end
always @(*) begin
	/* toy: %1*/
	/*   %scevgep4 = getelementptr i32* %a, i32 %2, !MSB !1, !LSB !2, !extendFrom !1*/
		toy_1_scevgep4 = (arg_a_reg + (4 * {21'd0,i}));
end
always @(*) begin
	/* toy: %1*/
	/*   %scevgep3 = getelementptr i32* %b, i32 %2, !MSB !1, !LSB !2, !extendFrom !1*/
		toy_1_scevgep3 = (arg_b_reg + (4 * {21'd0,i}));
end
always @(*) begin
	/* toy: %1*/
	/*   %scevgep = getelementptr i32* %c, i32 %2, !MSB !1, !LSB !2, !extendFrom !1*/
		toy_1_scevgep = (arg_c_reg + (4 * {21'd0,i}));
end
always @(posedge clk) begin
	/* toy: %1*/
	/*   %scevgep = getelementptr i32* %c, i32 %2, !MSB !1, !LSB !2, !extendFrom !1*/
	if ((is_S1)) begin
		toy_1_scevgep_reg <= toy_1_scevgep;
end
always @(*) begin
	/* toy: %1*/
	/*   %3 = add i32 %indvar, 1, !MSB !4, !LSB !2, !extendFrom !4*/
		j = ({1'd0,toy_1_indvar_reg} + 32'd1);
end
always @(posedge clk) begin
	/* toy: %1*/
	/*   %3 = add i32 %indvar, 1, !MSB !4, !LSB !2, !extendFrom !4*/
	if ((is_S1)) begin
		j_reg <= j;
	end
end
always @(*) begin
	/* toy: %1*/
	/*   %4 = load i32* %scevgep4, align 4, !MSB !5, !LSB !2, !extendFrom !5*/
		toy_1_4 = main_0_a_out_a;
end
always @(*) begin
	/* toy: %1*/
	/*   %5 = load i32* %scevgep3, align 4, !MSB !5, !LSB !2, !extendFrom !5*/
		toy_1_5 = main_0_b_out_a;
end
always @(*) begin
	/* toy: %1*/
	/*   %6 = add nsw i32 %4, %5, !MSB !5, !LSB !2, !extendFrom !5*/
		toy_1_6 = (toy_1_4 + toy_1_5);
end
always @(*) begin
	/* toy: %1*/
	/*   %7 = load i32* %scevgep2, align 4, !MSB !5, !LSB !2, !extendFrom !5*/
		toy_1_7 = main_0_c_out_a;
end
always @(*) begin
	/* toy: %1*/
	/*   %8 = add nsw i32 %6, %7, !MSB !5, !LSB !2, !extendFrom !5*/
		toy_1_8 = (toy_1_6 + toy_1_7);
end
always @(*) begin
	/* toy: %1*/
	/*   %exitcond = icmp eq i32 %3, 999, !MSB !2, !LSB !2, !extendFrom !2*/
		exitcond = (j == 32'd999);
end
always @(posedge clk) begin
	/* toy: %1*/
	/*   %exitcond = icmp eq i32 %3, 999, !MSB !2, !LSB !2, !extendFrom !2*/
	if ((is_S1)) begin
		exitcond_reg <= exitcond;
	end
end

endmodule
