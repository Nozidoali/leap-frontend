//----------------------------------------------------------------------------
// LegUp High-Level Synthesis Tool Version 5.0 (http://legup.org)
// Copyright (c) 2009-23 University of Toronto. All Rights Reserved.
// For research and academic purposes only. Commercial use is prohibited.
// Please report bugs at: http://legup.org/bugs
// Please email questions to: legup@eecg.toronto.edu
// Date: Sat Oct  5 16:03:37 2024
// ----------------------------------------------------------------------------
//`define MEMORY_CONTROLLER_ADDR_SIZE 32
//`define MEMORY_CONTROLLER_DATA_SIZE 64
// Number of RAM elements: 2
//`define MEMORY_CONTROLLER_TAG_SIZE 9
//`timescale 1 ns / 1 ns
module getTanh
(
	clk,
	clk2x,
	clk1x_follower,
	reset,
	memory_controller_waitrequest,
	start,
	finish,
	arg_A,
	arg_addr,
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
	main_0_a_out_b
);

parameter [3:0] LEGUP_0 = 4'd0;
parameter [3:0] LEGUP_F_getTanh_BB__1_1 = 4'd1;
parameter [3:0] LEGUP_F_getTanh_BB__1_2 = 4'd2;
parameter [3:0] LEGUP_F_getTanh_BB__1_3 = 4'd3;
parameter [3:0] LEGUP_F_getTanh_BB__6_4 = 4'd4;
parameter [3:0] LEGUP_F_getTanh_BB__6_5 = 4'd5;
parameter [3:0] LEGUP_F_getTanh_BB__6_6 = 4'd6;
parameter [3:0] LEGUP_F_getTanh_BB__6_7 = 4'd7;
parameter [3:0] LEGUP_F_getTanh_BB__6_8 = 4'd8;
parameter [3:0] LEGUP_F_getTanh_BB__13_9 = 4'd9;
parameter [3:0] LEGUP_F_getTanh_BB__13_10 = 4'd10;
parameter [3:0] LEGUP_F_getTanh_BB__15_11 = 4'd11;

input  clk;
input  clk2x;
input  clk1x_follower;
input  reset;
input  memory_controller_waitrequest;
input  start;
output reg  finish;
input [31:0] arg_A;
input [31:0] arg_addr;
output  main_0_b_write_enable_a;
output [31:0] main_0_b_in_a;
output  main_0_b_byteena_a;
output reg  main_0_b_enable_a;
output reg [9:0] main_0_b_address_a;
input [31:0] main_0_b_out_a;
output  main_0_b_write_enable_b;
output [31:0] main_0_b_in_b;
output  main_0_b_byteena_b;
output  main_0_b_enable_b;
output [9:0] main_0_b_address_b;
input [31:0] main_0_b_out_b;
output reg  main_0_a_write_enable_a;
output reg [31:0] main_0_a_in_a;
output  main_0_a_byteena_a;
output reg  main_0_a_enable_a;
output reg [9:0] main_0_a_address_a;
input [31:0] main_0_a_out_a;
output  main_0_a_write_enable_b;
output [31:0] main_0_a_in_b;
output  main_0_a_byteena_b;
output  main_0_a_enable_b;
output [9:0] main_0_a_address_b;
input [31:0] main_0_a_out_b;
reg [3:0] cur_state;
reg [3:0] next_state;
reg [31:0] arg_A_reg;
reg [31:0] arg_addr_reg;
reg  fsm_stall;
reg [9:0] getTanh_1_i01;
reg [9:0] getTanh_1_i01_reg;
reg [31:0] getTanh_1_scevgep;
reg [31:0] getTanh_1_2;
reg [31:0] getTanh_1_3;
reg [31:0] getTanh_1_3_reg;
reg [31:0] getTanh_1_4;
reg [31:0] getTanh_1_4_reg;
reg  getTanh_1_5;
reg [31:0] getTanh_6_7;
reg [31:0] getTanh_6_8;
reg [31:0] getTanh_6_9;
reg [31:0] getTanh_6_10;
reg [31:0] getTanh_6_11;
reg [31:0] getTanh_6_12;
reg [31:0] getTanh_13_result0;
reg [31:0] getTanh_13_result0_reg;
reg [10:0] getTanh_13_14;
reg [10:0] getTanh_13_14_reg;
reg  getTanh_13_exitcond;
reg [1:0] getTanh_1_5_op1_temp;
reg  legup_mult_1_unsigned_32_32_1_0_clock;
reg  legup_mult_1_unsigned_32_32_1_0_aclr;
reg  legup_mult_1_unsigned_32_32_1_0_sum;
reg  legup_mult_1_unsigned_32_32_1_0_clken;
reg [31:0] legup_mult_1_unsigned_32_32_1_0_dataa;
reg [31:0] legup_mult_1_unsigned_32_32_1_0_datab;
wire [63:0] legup_mult_1_unsigned_32_32_1_0_result;
reg [63:0] legup_mult_getTanh_6_7_out_actual;
reg [31:0] legup_mult_getTanh_6_7_out;
reg  legup_mult_getTanh_6_7_en;
reg  legup_mult_1_unsigned_32_32_1_1_clock;
reg  legup_mult_1_unsigned_32_32_1_1_aclr;
reg  legup_mult_1_unsigned_32_32_1_1_sum;
reg  legup_mult_1_unsigned_32_32_1_1_clken;
reg [31:0] legup_mult_1_unsigned_32_32_1_1_dataa;
reg [31:0] legup_mult_1_unsigned_32_32_1_1_datab;
wire [63:0] legup_mult_1_unsigned_32_32_1_1_result;
reg [63:0] legup_mult_getTanh_6_9_out_actual;
reg [31:0] legup_mult_getTanh_6_9_out;
reg  legup_mult_getTanh_6_9_en;
reg  legup_mult_1_unsigned_32_32_1_2_clock;
reg  legup_mult_1_unsigned_32_32_1_2_aclr;
reg  legup_mult_1_unsigned_32_32_1_2_sum;
reg  legup_mult_1_unsigned_32_32_1_2_clken;
reg [31:0] legup_mult_1_unsigned_32_32_1_2_dataa;
reg [31:0] legup_mult_1_unsigned_32_32_1_2_datab;
wire [63:0] legup_mult_1_unsigned_32_32_1_2_result;
reg [63:0] legup_mult_getTanh_6_10_out_actual;
reg [31:0] legup_mult_getTanh_6_10_out;
reg  legup_mult_getTanh_6_10_en;
reg  legup_mult_1_unsigned_32_32_1_3_clock;
reg  legup_mult_1_unsigned_32_32_1_3_aclr;
reg  legup_mult_1_unsigned_32_32_1_3_sum;
reg  legup_mult_1_unsigned_32_32_1_3_clken;
reg [31:0] legup_mult_1_unsigned_32_32_1_3_dataa;
reg [31:0] legup_mult_1_unsigned_32_32_1_3_datab;
wire [63:0] legup_mult_1_unsigned_32_32_1_3_result;
reg [63:0] legup_mult_getTanh_6_12_out_actual;
reg [31:0] legup_mult_getTanh_6_12_out;
reg  legup_mult_getTanh_6_12_en;

/*   %7 = mul nsw i32 %4, %4, !MSB !4, !LSB !2, !extendFrom !4*/
legup_mult_1 legup_mult_1_unsigned_32_32_1_0 (
	.clock (legup_mult_1_unsigned_32_32_1_0_clock),
	.aclr (legup_mult_1_unsigned_32_32_1_0_aclr),
	.sum (legup_mult_1_unsigned_32_32_1_0_sum),
	.clken (legup_mult_1_unsigned_32_32_1_0_clken),
	.dataa (legup_mult_1_unsigned_32_32_1_0_dataa),
	.datab (legup_mult_1_unsigned_32_32_1_0_datab),
	.result (legup_mult_1_unsigned_32_32_1_0_result)
);

// Commented out since it does not matter to CDFG extraction
/*
defparam
	legup_mult_1_unsigned_32_32_1_0.widtha = 32,
	legup_mult_1_unsigned_32_32_1_0.widthb = 32,
	legup_mult_1_unsigned_32_32_1_0.widthp = 64,
	legup_mult_1_unsigned_32_32_1_0.representation = "UNSIGNED";
*/

/*   %9 = mul nsw i32 %8, %4, !MSB !4, !LSB !2, !extendFrom !4*/
legup_mult_1 legup_mult_1_unsigned_32_32_1_1 (
	.clock (legup_mult_1_unsigned_32_32_1_1_clock),
	.aclr (legup_mult_1_unsigned_32_32_1_1_aclr),
	.sum (legup_mult_1_unsigned_32_32_1_1_sum),
	.clken (legup_mult_1_unsigned_32_32_1_1_clken),
	.dataa (legup_mult_1_unsigned_32_32_1_1_dataa),
	.datab (legup_mult_1_unsigned_32_32_1_1_datab),
	.result (legup_mult_1_unsigned_32_32_1_1_result)
);

// Commented out since it does not matter to CDFG extraction
/*
defparam
	legup_mult_1_unsigned_32_32_1_1.widtha = 32,
	legup_mult_1_unsigned_32_32_1_1.widthb = 32,
	legup_mult_1_unsigned_32_32_1_1.widthp = 64,
	legup_mult_1_unsigned_32_32_1_1.representation = "UNSIGNED";
*/

/*   %10 = mul nsw i32 %9, %4, !MSB !4, !LSB !2, !extendFrom !4*/
legup_mult_1 legup_mult_1_unsigned_32_32_1_2 (
	.clock (legup_mult_1_unsigned_32_32_1_2_clock),
	.aclr (legup_mult_1_unsigned_32_32_1_2_aclr),
	.sum (legup_mult_1_unsigned_32_32_1_2_sum),
	.clken (legup_mult_1_unsigned_32_32_1_2_clken),
	.dataa (legup_mult_1_unsigned_32_32_1_2_dataa),
	.datab (legup_mult_1_unsigned_32_32_1_2_datab),
	.result (legup_mult_1_unsigned_32_32_1_2_result)
);
// Commented out since it does not matter to CDFG extraction
/*
defparam
	legup_mult_1_unsigned_32_32_1_2.widtha = 32,
	legup_mult_1_unsigned_32_32_1_2.widthb = 32,
	legup_mult_1_unsigned_32_32_1_2.widthp = 64,
	legup_mult_1_unsigned_32_32_1_2.representation = "UNSIGNED";
*/
/*   %12 = mul nsw i32 %11, %4, !MSB !4, !LSB !2, !extendFrom !4*/
legup_mult_1 legup_mult_1_unsigned_32_32_1_3 (
	.clock (legup_mult_1_unsigned_32_32_1_3_clock),
	.aclr (legup_mult_1_unsigned_32_32_1_3_aclr),
	.sum (legup_mult_1_unsigned_32_32_1_3_sum),
	.clken (legup_mult_1_unsigned_32_32_1_3_clken),
	.dataa (legup_mult_1_unsigned_32_32_1_3_dataa),
	.datab (legup_mult_1_unsigned_32_32_1_3_datab),
	.result (legup_mult_1_unsigned_32_32_1_3_result)
);
// Commented out since it does not matter to CDFG extraction
/*
defparam
	legup_mult_1_unsigned_32_32_1_3.widtha = 32,
	legup_mult_1_unsigned_32_32_1_3.widthb = 32,
	legup_mult_1_unsigned_32_32_1_3.widthp = 64,
	legup_mult_1_unsigned_32_32_1_3.representation = "UNSIGNED";
*/
// Local Rams

// End Local Rams

always @(posedge clk) begin
if (reset == 1'b1)
	cur_state <= LEGUP_0;
else if (!fsm_stall)
	cur_state <= next_state;
end

always @(*)
begin
next_state = cur_state;
case(cur_state)  // synthesis parallel_case  
LEGUP_0:
	if ((fsm_stall == 1'd0) && (start == 1'd1))
		next_state = LEGUP_F_getTanh_BB__1_1;
LEGUP_F_getTanh_BB__13_10:
	if ((fsm_stall == 1'd0) && (getTanh_13_exitcond == 1'd1))
		next_state = LEGUP_F_getTanh_BB__15_11;
	else if ((fsm_stall == 1'd0) && (getTanh_13_exitcond == 1'd0))
		next_state = LEGUP_F_getTanh_BB__1_1;
LEGUP_F_getTanh_BB__13_9:
		next_state = LEGUP_F_getTanh_BB__13_10;
LEGUP_F_getTanh_BB__15_11:
		next_state = LEGUP_0;
LEGUP_F_getTanh_BB__1_1:
		next_state = LEGUP_F_getTanh_BB__1_2;
LEGUP_F_getTanh_BB__1_2:
		next_state = LEGUP_F_getTanh_BB__1_3;
LEGUP_F_getTanh_BB__1_3:
	if ((fsm_stall == 1'd0) && (getTanh_1_5 == 1'd1))
		next_state = LEGUP_F_getTanh_BB__13_9;
	else if ((fsm_stall == 1'd0) && (getTanh_1_5 == 1'd0))
		next_state = LEGUP_F_getTanh_BB__6_4;
LEGUP_F_getTanh_BB__6_4:
		next_state = LEGUP_F_getTanh_BB__6_5;
LEGUP_F_getTanh_BB__6_5:
		next_state = LEGUP_F_getTanh_BB__6_6;
LEGUP_F_getTanh_BB__6_6:
		next_state = LEGUP_F_getTanh_BB__6_7;
LEGUP_F_getTanh_BB__6_7:
		next_state = LEGUP_F_getTanh_BB__6_8;
LEGUP_F_getTanh_BB__6_8:
		next_state = LEGUP_F_getTanh_BB__13_9;
default:
	next_state = cur_state;
endcase

end
always @(posedge clk) begin
	if (start) begin
		arg_A_reg <= arg_A;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_addr_reg <= arg_addr;
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
	/* getTanh: %1*/
	/*   %i.01 = phi i32 [ 0, %0 ], [ %14, %13 ], !MSB !3, !LSB !2, !extendFrom !3*/
	if ((((cur_state == LEGUP_0) & (fsm_stall == 1'd0)) & (start == 1'd1))) begin
		getTanh_1_i01 = 32'd0;
	end
	/* getTanh: %1*/
	/*   %i.01 = phi i32 [ 0, %0 ], [ %14, %13 ], !MSB !3, !LSB !2, !extendFrom !3*/
	else /* if ((((cur_state == LEGUP_F_getTanh_BB__13_10) & (fsm_stall == 1'd0)) & (getTanh_13_exitcond == 1'd0))) */ begin
		getTanh_1_i01 = getTanh_13_14_reg;
	end
end
always @(posedge clk) begin
	/* getTanh: %1*/
	/*   %i.01 = phi i32 [ 0, %0 ], [ %14, %13 ], !MSB !3, !LSB !2, !extendFrom !3*/
	if ((((cur_state == LEGUP_0) & (fsm_stall == 1'd0)) & (start == 1'd1))) begin
		getTanh_1_i01_reg <= getTanh_1_i01;
	end
	/* getTanh: %1*/
	/*   %i.01 = phi i32 [ 0, %0 ], [ %14, %13 ], !MSB !3, !LSB !2, !extendFrom !3*/
	if ((((cur_state == LEGUP_F_getTanh_BB__13_10) & (fsm_stall == 1'd0)) & (getTanh_13_exitcond == 1'd0))) begin
		getTanh_1_i01_reg <= getTanh_1_i01;
	end
end
always @(*) begin
	/* getTanh: %1*/
	/*   %scevgep = getelementptr i32* %addr, i32 %i.01, !MSB !1, !LSB !2, !extendFrom !1*/
		getTanh_1_scevgep = (arg_addr_reg + (4 * {22'd0,getTanh_1_i01_reg}));
end
always @(*) begin
	/* getTanh: %1*/
	/*   %2 = load i32* %scevgep, align 4, !MSB !4, !LSB !2, !extendFrom !4*/
		getTanh_1_2 = main_0_b_out_a;
end
always @(*) begin
	/* getTanh: %1*/
	/*   %3 = getelementptr inbounds i32* %A, i32 %2, !MSB !1, !LSB !2, !extendFrom !1*/
		getTanh_1_3 = (arg_A_reg + (4 * getTanh_1_2));
end
always @(posedge clk) begin
	/* getTanh: %1*/
	/*   %3 = getelementptr inbounds i32* %A, i32 %2, !MSB !1, !LSB !2, !extendFrom !1*/
	if ((cur_state == LEGUP_F_getTanh_BB__1_2)) begin
		getTanh_1_3_reg <= getTanh_1_3;
	end
end
always @(*) begin
	/* getTanh: %1*/
	/*   %4 = load i32* %3, align 4, !MSB !4, !LSB !2, !extendFrom !4*/
		getTanh_1_4 = main_0_a_out_a;
end
always @(posedge clk) begin
	/* getTanh: %1*/
	/*   %4 = load i32* %3, align 4, !MSB !4, !LSB !2, !extendFrom !4*/
	if ((cur_state == LEGUP_F_getTanh_BB__1_3)) begin
		getTanh_1_4_reg <= getTanh_1_4;
	end
end
always @(*) begin
	/* getTanh: %1*/
	/*   %5 = icmp sgt i32 %4, 0, !MSB !2, !LSB !2, !extendFrom !2*/
		getTanh_1_5 = ((getTanh_1_4) > ({30'd0,getTanh_1_5_op1_temp}));
end
always @(*) begin
	getTanh_6_7 = legup_mult_getTanh_6_7_out;
end
always @(*) begin
	/* getTanh: %6*/
	/*   %8 = add nuw nsw i32 %7, 19, !MSB !4, !LSB !2, !extendFrom !4*/
		getTanh_6_8 = (getTanh_6_7 + 32'd19);
end
always @(*) begin
	getTanh_6_9 = legup_mult_getTanh_6_9_out;
end
always @(*) begin
	getTanh_6_10 = legup_mult_getTanh_6_10_out;
end
always @(*) begin
	/* getTanh: %6*/
	/*   %11 = add nsw i32 %10, 3, !MSB !4, !LSB !2, !extendFrom !4*/
		getTanh_6_11 = (getTanh_6_10 + 32'd3);
end
always @(*) begin
	getTanh_6_12 = legup_mult_getTanh_6_12_out;
end
always @(*) begin
	/* getTanh: %13*/
	/*   %result.0 = phi i32 [ %12, %6 ], [ 1, %1 ], !MSB !4, !LSB !2, !extendFrom !4*/
	if ((((cur_state == LEGUP_F_getTanh_BB__1_3) & (fsm_stall == 1'd0)) & (getTanh_1_5 == 1'd1))) begin
		getTanh_13_result0 = 32'd1;
	end
	/* getTanh: %13*/
	/*   %result.0 = phi i32 [ %12, %6 ], [ 1, %1 ], !MSB !4, !LSB !2, !extendFrom !4*/
	else /* if (((cur_state == LEGUP_F_getTanh_BB__6_8) & (fsm_stall == 1'd0))) */ begin
		getTanh_13_result0 = getTanh_6_12;
	end
end
always @(posedge clk) begin
	/* getTanh: %13*/
	/*   %result.0 = phi i32 [ %12, %6 ], [ 1, %1 ], !MSB !4, !LSB !2, !extendFrom !4*/
	if ((((cur_state == LEGUP_F_getTanh_BB__1_3) & (fsm_stall == 1'd0)) & (getTanh_1_5 == 1'd1))) begin
		getTanh_13_result0_reg <= getTanh_13_result0;
	end
	/* getTanh: %13*/
	/*   %result.0 = phi i32 [ %12, %6 ], [ 1, %1 ], !MSB !4, !LSB !2, !extendFrom !4*/
	if (((cur_state == LEGUP_F_getTanh_BB__6_8) & (fsm_stall == 1'd0))) begin
		getTanh_13_result0_reg <= getTanh_13_result0;
	end
end
always @(*) begin
	/* getTanh: %13*/
	/*   %14 = add nsw i32 %i.01, 1, !MSB !5, !LSB !2, !extendFrom !5*/
		getTanh_13_14 = ({1'd0,getTanh_1_i01_reg} + 32'd1);
end
always @(posedge clk) begin
	/* getTanh: %13*/
	/*   %14 = add nsw i32 %i.01, 1, !MSB !5, !LSB !2, !extendFrom !5*/
	if ((cur_state == LEGUP_F_getTanh_BB__13_9)) begin
		getTanh_13_14_reg <= getTanh_13_14;
	end
end
always @(*) begin
	/* getTanh: %13*/
	/*   %exitcond = icmp eq i32 %14, 1000, !MSB !2, !LSB !2, !extendFrom !2*/
		getTanh_13_exitcond = (getTanh_13_14_reg == 32'd1000);
end
always @(*) begin
	getTanh_1_5_op1_temp = 32'd0;
if (reset) begin getTanh_1_5_op1_temp = 0; end
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_0_clock = clk;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_0_aclr = reset;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_0_sum = 1'd0;
if (reset) begin legup_mult_1_unsigned_32_32_1_0_sum = 0; end
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_0_clken = legup_mult_getTanh_6_7_en;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_0_dataa = getTanh_1_4_reg;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_0_datab = getTanh_1_4_reg;
end
always @(*) begin
	legup_mult_getTanh_6_7_out_actual = legup_mult_1_unsigned_32_32_1_0_result;
end
always @(*) begin
	legup_mult_getTanh_6_7_out = legup_mult_getTanh_6_7_out_actual[31:0];
end
always @(*) begin
	legup_mult_getTanh_6_7_en = ~(fsm_stall);
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_1_clock = clk;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_1_aclr = reset;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_1_sum = 1'd0;
if (reset) begin legup_mult_1_unsigned_32_32_1_1_sum = 0; end
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_1_clken = legup_mult_getTanh_6_9_en;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_1_dataa = getTanh_6_8;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_1_datab = getTanh_1_4_reg;
end
always @(*) begin
	legup_mult_getTanh_6_9_out_actual = legup_mult_1_unsigned_32_32_1_1_result;
end
always @(*) begin
	legup_mult_getTanh_6_9_out = legup_mult_getTanh_6_9_out_actual[31:0];
end
always @(*) begin
	legup_mult_getTanh_6_9_en = ~(fsm_stall);
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_2_clock = clk;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_2_aclr = reset;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_2_sum = 1'd0;
if (reset) begin legup_mult_1_unsigned_32_32_1_2_sum = 0; end
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_2_clken = legup_mult_getTanh_6_10_en;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_2_dataa = getTanh_6_9;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_2_datab = getTanh_1_4_reg;
end
always @(*) begin
	legup_mult_getTanh_6_10_out_actual = legup_mult_1_unsigned_32_32_1_2_result;
end
always @(*) begin
	legup_mult_getTanh_6_10_out = legup_mult_getTanh_6_10_out_actual[31:0];
end
always @(*) begin
	legup_mult_getTanh_6_10_en = ~(fsm_stall);
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_3_clock = clk;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_3_aclr = reset;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_3_sum = 1'd0;
if (reset) begin legup_mult_1_unsigned_32_32_1_3_sum = 0; end
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_3_clken = legup_mult_getTanh_6_12_en;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_3_dataa = getTanh_6_11;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_3_datab = getTanh_1_4_reg;
end
always @(*) begin
	legup_mult_getTanh_6_12_out_actual = legup_mult_1_unsigned_32_32_1_3_result;
end
always @(*) begin
	legup_mult_getTanh_6_12_out = legup_mult_getTanh_6_12_out_actual[31:0];
end
always @(*) begin
	legup_mult_getTanh_6_12_en = ~(fsm_stall);
end
always @(posedge clk) begin
	if ((cur_state == LEGUP_0)) begin
		finish <= 1'd0;
	end
	/* getTanh: %15*/
	/*   ret void, !MSB !1, !LSB !2, !extendFrom !1*/
	if ((cur_state == LEGUP_F_getTanh_BB__15_11)) begin
		finish <= (fsm_stall == 1'd0);
	end
end
assign main_0_b_write_enable_a = 1'd0;
assign main_0_b_in_a = 0;
assign main_0_b_byteena_a = 1'd1;
always @(*) begin
	main_0_b_enable_a = 1'd0;
	/* getTanh: %1*/
	/*   %2 = load i32* %scevgep, align 4, !MSB !4, !LSB !2, !extendFrom !4*/
	if ((cur_state == LEGUP_F_getTanh_BB__1_1)) begin
		main_0_b_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_b_address_a = 10'd0;
	/* getTanh: %1*/
	/*   %2 = load i32* %scevgep, align 4, !MSB !4, !LSB !2, !extendFrom !4*/
	if ((cur_state == LEGUP_F_getTanh_BB__1_1)) begin
		main_0_b_address_a = (getTanh_1_scevgep >>> 3'd2);
	end
end
assign main_0_b_write_enable_b = 1'd0;
assign main_0_b_in_b = 0;
assign main_0_b_byteena_b = 1'd1;
assign main_0_b_enable_b = 1'd0;
assign main_0_b_address_b = 10'd0;
always @(*) begin
	main_0_a_write_enable_a = 1'd0;
	/* getTanh: %13*/
	/*   store i32 %result.0, i32* %3, align 4, !MSB !1, !LSB !2, !extendFrom !1*/
	if ((cur_state == LEGUP_F_getTanh_BB__13_9)) begin
		main_0_a_write_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_a_in_a = 0;
	/* getTanh: %13*/
	/*   store i32 %result.0, i32* %3, align 4, !MSB !1, !LSB !2, !extendFrom !1*/
	if ((cur_state == LEGUP_F_getTanh_BB__13_9)) begin
		main_0_a_in_a = getTanh_13_result0_reg;
	end
end
assign main_0_a_byteena_a = 1'd1;
always @(*) begin
	main_0_a_enable_a = 1'd0;
	/* getTanh: %1*/
	/*   %4 = load i32* %3, align 4, !MSB !4, !LSB !2, !extendFrom !4*/
	if ((cur_state == LEGUP_F_getTanh_BB__1_2)) begin
		main_0_a_enable_a = 1'd1;
	end
	/* getTanh: %13*/
	/*   store i32 %result.0, i32* %3, align 4, !MSB !1, !LSB !2, !extendFrom !1*/
	if ((cur_state == LEGUP_F_getTanh_BB__13_9)) begin
		main_0_a_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_a_address_a = 10'd0;
	/* getTanh: %1*/
	/*   %4 = load i32* %3, align 4, !MSB !4, !LSB !2, !extendFrom !4*/
	if ((cur_state == LEGUP_F_getTanh_BB__1_2)) begin
		main_0_a_address_a = (getTanh_1_3 >>> 3'd2);
	end
	/* getTanh: %13*/
	/*   store i32 %result.0, i32* %3, align 4, !MSB !1, !LSB !2, !extendFrom !1*/
	if ((cur_state == LEGUP_F_getTanh_BB__13_9)) begin
		main_0_a_address_a = (getTanh_1_3_reg >>> 3'd2);
	end
end
assign main_0_a_write_enable_b = 1'd0;
assign main_0_a_in_b = 0;
assign main_0_a_byteena_b = 1'd1;
assign main_0_a_enable_b = 1'd0;
assign main_0_a_address_b = 10'd0;

endmodule

