//----------------------------------------------------------------------------
// LegUp High-Level Synthesis Tool Version 5.0 (http://legup.org)
// Copyright (c) 2009-23 University of Toronto. All Rights Reserved.
// For research and academic purposes only. Commercial use is prohibited.
// Please report bugs at: http://legup.org/bugs
// Please email questions to: legup@eecg.toronto.edu
// Date: Sun Oct  6 20:40:31 2024
// ----------------------------------------------------------------------------
`timescale 1 ns / 1 ns
module kernel_2mm
(
	clk,
	clk2x,
	clk1x_follower,
	reset,
	memory_controller_waitrequest,
	start,
	finish,
	arg_alpha,
	arg_beta,
	arg_tmp,
	arg_A,
	arg_B,
	arg_C,
	arg_D,
	main_0_tmp_write_enable_a,
	main_0_tmp_in_a,
	main_0_tmp_byteena_a,
	main_0_tmp_enable_a,
	main_0_tmp_address_a,
	main_0_tmp_out_a,
	main_0_tmp_write_enable_b,
	main_0_tmp_in_b,
	main_0_tmp_byteena_b,
	main_0_tmp_enable_b,
	main_0_tmp_address_b,
	main_0_tmp_out_b,
	main_0_A_write_enable_a,
	main_0_A_in_a,
	main_0_A_byteena_a,
	main_0_A_enable_a,
	main_0_A_address_a,
	main_0_A_out_a,
	main_0_A_write_enable_b,
	main_0_A_in_b,
	main_0_A_byteena_b,
	main_0_A_enable_b,
	main_0_A_address_b,
	main_0_A_out_b,
	main_0_B_write_enable_a,
	main_0_B_in_a,
	main_0_B_byteena_a,
	main_0_B_enable_a,
	main_0_B_address_a,
	main_0_B_out_a,
	main_0_B_write_enable_b,
	main_0_B_in_b,
	main_0_B_byteena_b,
	main_0_B_enable_b,
	main_0_B_address_b,
	main_0_B_out_b,
	main_0_D_write_enable_a,
	main_0_D_in_a,
	main_0_D_byteena_a,
	main_0_D_enable_a,
	main_0_D_address_a,
	main_0_D_out_a,
	main_0_D_write_enable_b,
	main_0_D_in_b,
	main_0_D_byteena_b,
	main_0_D_enable_b,
	main_0_D_address_b,
	main_0_D_out_b,
	main_0_C_write_enable_a,
	main_0_C_in_a,
	main_0_C_byteena_a,
	main_0_C_enable_a,
	main_0_C_address_a,
	main_0_C_out_a,
	main_0_C_write_enable_b,
	main_0_C_in_b,
	main_0_C_byteena_b,
	main_0_C_enable_b,
	main_0_C_address_b,
	main_0_C_out_b
);

parameter [4:0] LEGUP_0 = 5'd0;
parameter [4:0] LEGUP_F_kernel_2mm_BB__1_1 = 5'd1;
parameter [4:0] LEGUP_F_kernel_2mm_BB__3_2 = 5'd2;
parameter [4:0] LEGUP_F_kernel_2mm_BB__3_3 = 5'd3;
parameter [4:0] LEGUP_F_kernel_2mm_BB__3_4 = 5'd4;
parameter [4:0] LEGUP_F_kernel_2mm_BB__6_5 = 5'd5;
parameter [4:0] LEGUP_F_kernel_2mm_BB__6_6 = 5'd6;
parameter [4:0] LEGUP_F_kernel_2mm_BB__6_7 = 5'd7;
parameter [4:0] LEGUP_F_kernel_2mm_BB__6_8 = 5'd8;
parameter [4:0] LEGUP_F_kernel_2mm_BB__6_9 = 5'd9;
parameter [4:0] LEGUP_F_kernel_2mm_BB__16_10 = 5'd10;
parameter [4:0] LEGUP_F_kernel_2mm_BB__16_11 = 5'd11;
parameter [4:0] LEGUP_F_kernel_2mm_BB__18_12 = 5'd12;
parameter [4:0] LEGUP_F_kernel_2mm_BB__18_13 = 5'd13;
parameter [4:0] LEGUP_F_kernel_2mm_BB_preheaderpreheaderpreheader_14 = 5'd14;
parameter [4:0] LEGUP_F_kernel_2mm_BB_preheaderpreheader_15 = 5'd15;
parameter [4:0] LEGUP_F_kernel_2mm_BB__21_16 = 5'd16;
parameter [4:0] LEGUP_F_kernel_2mm_BB__21_17 = 5'd17;
parameter [4:0] LEGUP_F_kernel_2mm_BB__21_18 = 5'd18;
parameter [4:0] LEGUP_F_kernel_2mm_BB__21_19 = 5'd19;
parameter [4:0] LEGUP_F_kernel_2mm_BB__25_20 = 5'd20;
parameter [4:0] LEGUP_F_kernel_2mm_BB__25_21 = 5'd21;
parameter [4:0] LEGUP_F_kernel_2mm_BB__25_22 = 5'd22;
parameter [4:0] LEGUP_F_kernel_2mm_BB__25_23 = 5'd23;
parameter [4:0] LEGUP_F_kernel_2mm_BB__34_24 = 5'd24;
parameter [4:0] LEGUP_F_kernel_2mm_BB__34_25 = 5'd25;
parameter [4:0] LEGUP_F_kernel_2mm_BB_preheader_26 = 5'd26;
parameter [4:0] LEGUP_F_kernel_2mm_BB_preheader_27 = 5'd27;
parameter [4:0] LEGUP_F_kernel_2mm_BB__37_28 = 5'd28;

input  clk;
input  clk2x;
input  clk1x_follower;
input  reset;
input  memory_controller_waitrequest;
input  start;
output reg  finish;
input [31:0] arg_alpha;
input [31:0] arg_beta;
input [31:0] arg_tmp;
input [31:0] arg_A;
input [31:0] arg_B;
input [31:0] arg_C;
input [31:0] arg_D;
output reg  main_0_tmp_write_enable_a;
output reg [31:0] main_0_tmp_in_a;
output  main_0_tmp_byteena_a;
output reg  main_0_tmp_enable_a;
output reg [5:0] main_0_tmp_address_a;
input [31:0] main_0_tmp_out_a;
output  main_0_tmp_write_enable_b;
output [31:0] main_0_tmp_in_b;
output  main_0_tmp_byteena_b;
output  main_0_tmp_enable_b;
output [5:0] main_0_tmp_address_b;
input [31:0] main_0_tmp_out_b;
output  main_0_A_write_enable_a;
output [31:0] main_0_A_in_a;
output  main_0_A_byteena_a;
output reg  main_0_A_enable_a;
output reg [5:0] main_0_A_address_a;
input [31:0] main_0_A_out_a;
output  main_0_A_write_enable_b;
output [31:0] main_0_A_in_b;
output  main_0_A_byteena_b;
output  main_0_A_enable_b;
output [5:0] main_0_A_address_b;
input [31:0] main_0_A_out_b;
output  main_0_B_write_enable_a;
output [31:0] main_0_B_in_a;
output  main_0_B_byteena_a;
output reg  main_0_B_enable_a;
output reg [5:0] main_0_B_address_a;
input [31:0] main_0_B_out_a;
output  main_0_B_write_enable_b;
output [31:0] main_0_B_in_b;
output  main_0_B_byteena_b;
output  main_0_B_enable_b;
output [5:0] main_0_B_address_b;
input [31:0] main_0_B_out_b;
output reg  main_0_D_write_enable_a;
output reg [31:0] main_0_D_in_a;
output  main_0_D_byteena_a;
output reg  main_0_D_enable_a;
output reg [5:0] main_0_D_address_a;
input [31:0] main_0_D_out_a;
output  main_0_D_write_enable_b;
output [31:0] main_0_D_in_b;
output  main_0_D_byteena_b;
output  main_0_D_enable_b;
output [5:0] main_0_D_address_b;
input [31:0] main_0_D_out_b;
output  main_0_C_write_enable_a;
output [31:0] main_0_C_in_a;
output  main_0_C_byteena_a;
output reg  main_0_C_enable_a;
output reg [5:0] main_0_C_address_a;
input [31:0] main_0_C_out_a;
output  main_0_C_write_enable_b;
output [31:0] main_0_C_in_b;
output  main_0_C_byteena_b;
output  main_0_C_enable_b;
output [5:0] main_0_C_address_b;
input [31:0] main_0_C_out_b;
reg [4:0] cur_state;
reg [4:0] next_state;
reg [31:0] arg_alpha_reg;
reg [31:0] arg_beta_reg;
reg [31:0] arg_tmp_reg;
reg [31:0] arg_A_reg;
reg [31:0] arg_B_reg;
reg [31:0] arg_C_reg;
reg [31:0] arg_D_reg;
reg  fsm_stall;
reg [3:0] kernel_2mm_1_i08;
reg [3:0] kernel_2mm_1_i08_reg;
reg [7:0] kernel_2mm_1_2;
reg [7:0] kernel_2mm_1_2_reg;
reg [31:0] kernel_2mm_3_j07;
reg [31:0] kernel_2mm_3_j07_reg;
reg [31:0] kernel_2mm_3_4;
reg [31:0] kernel_2mm_3_4_reg;
reg [31:0] kernel_2mm_3_scevgep14;
reg [31:0] kernel_2mm_3_scevgep14_reg;
reg [31:0] kernel_2mm_3_5;
reg [31:0] kernel_2mm_6_x06;
reg [31:0] kernel_2mm_6_x06_reg;
reg [31:0] kernel_2mm_6_k05;
reg [31:0] kernel_2mm_6_k05_reg;
reg [31:0] kernel_2mm_6_7;
reg [31:0] kernel_2mm_6_7_reg;
reg [31:0] kernel_2mm_6_scevgep11;
reg [31:0] kernel_2mm_6_8;
reg [31:0] kernel_2mm_6_9;
reg [31:0] kernel_2mm_6_9_reg;
reg [31:0] kernel_2mm_6_scevgep10;
reg [31:0] kernel_2mm_6_10;
reg [31:0] kernel_2mm_6_11;
reg [31:0] kernel_2mm_6_12;
reg [31:0] kernel_2mm_6_12_reg;
reg [31:0] kernel_2mm_6_13;
reg [31:0] kernel_2mm_6_14;
reg [31:0] kernel_2mm_6_15;
reg [31:0] kernel_2mm_6_15_reg;
reg  kernel_2mm_6_exitcond14;
reg  kernel_2mm_6_exitcond14_reg;
reg [31:0] kernel_2mm_16_lcssa1;
reg [31:0] kernel_2mm_16_lcssa1_reg;
reg [31:0] kernel_2mm_16_17;
reg [31:0] kernel_2mm_16_17_reg;
reg  kernel_2mm_16_exitcond17;
reg [4:0] kernel_2mm_18_19;
reg [4:0] kernel_2mm_18_19_reg;
reg  kernel_2mm_18_exitcond20;
reg [3:0] kernel_2mm_preheaderpreheader_i14;
reg [3:0] kernel_2mm_preheaderpreheader_i14_reg;
reg [7:0] kernel_2mm_preheaderpreheader_20;
reg [7:0] kernel_2mm_preheaderpreheader_20_reg;
reg [31:0] kernel_2mm_21_j13;
reg [31:0] kernel_2mm_21_j13_reg;
reg [31:0] kernel_2mm_21_22;
reg [31:0] kernel_2mm_21_22_reg;
reg [31:0] kernel_2mm_21_scevgep5;
reg [31:0] kernel_2mm_21_scevgep5_reg;
reg [31:0] kernel_2mm_21_23;
reg [31:0] kernel_2mm_21_24;
reg [31:0] kernel_2mm_25_x102;
reg [31:0] kernel_2mm_25_x102_reg;
reg [31:0] kernel_2mm_25_k11;
reg [31:0] kernel_2mm_25_k11_reg;
reg [31:0] kernel_2mm_25_26;
reg [31:0] kernel_2mm_25_26_reg;
reg [31:0] kernel_2mm_25_scevgep3;
reg [31:0] kernel_2mm_25_27;
reg [31:0] kernel_2mm_25_28;
reg [31:0] kernel_2mm_25_28_reg;
reg [31:0] kernel_2mm_25_scevgep;
reg [31:0] kernel_2mm_25_29;
reg [31:0] kernel_2mm_25_30;
reg [31:0] kernel_2mm_25_31;
reg [31:0] kernel_2mm_25_32;
reg [31:0] kernel_2mm_25_33;
reg [31:0] kernel_2mm_25_33_reg;
reg  kernel_2mm_25_exitcond3;
reg  kernel_2mm_25_exitcond3_reg;
reg [31:0] kernel_2mm_34_lcssa;
reg [31:0] kernel_2mm_34_lcssa_reg;
reg [31:0] kernel_2mm_34_35;
reg [31:0] kernel_2mm_34_35_reg;
reg  kernel_2mm_34_exitcond7;
reg [4:0] kernel_2mm_preheader_36;
reg [4:0] kernel_2mm_preheader_36_reg;
reg  kernel_2mm_preheader_exitcond;
reg  legup_mult_1_unsigned_32_32_1_0_clock;
reg  legup_mult_1_unsigned_32_32_1_0_aclr;
reg  legup_mult_1_unsigned_32_32_1_0_sum;
reg  legup_mult_1_unsigned_32_32_1_0_clken;
reg [31:0] legup_mult_1_unsigned_32_32_1_0_dataa;
reg [31:0] legup_mult_1_unsigned_32_32_1_0_datab;
wire [63:0] legup_mult_1_unsigned_32_32_1_0_result;
reg [63:0] legup_mult_kernel_2mm_6_11_out_actual;
reg [31:0] legup_mult_kernel_2mm_6_11_out;
reg  legup_mult_kernel_2mm_6_11_en;
reg  legup_mult_1_unsigned_32_32_1_1_clock;
reg  legup_mult_1_unsigned_32_32_1_1_aclr;
reg  legup_mult_1_unsigned_32_32_1_1_sum;
reg  legup_mult_1_unsigned_32_32_1_1_clken;
reg [31:0] legup_mult_1_unsigned_32_32_1_1_dataa;
reg [31:0] legup_mult_1_unsigned_32_32_1_1_datab;
wire [63:0] legup_mult_1_unsigned_32_32_1_1_result;
reg [63:0] legup_mult_kernel_2mm_6_13_out_actual;
reg [31:0] legup_mult_kernel_2mm_6_13_out;
reg  legup_mult_kernel_2mm_6_13_en;
reg  legup_mult_1_unsigned_32_32_1_2_clock;
reg  legup_mult_1_unsigned_32_32_1_2_aclr;
reg  legup_mult_1_unsigned_32_32_1_2_sum;
reg  legup_mult_1_unsigned_32_32_1_2_clken;
reg [31:0] legup_mult_1_unsigned_32_32_1_2_dataa;
reg [31:0] legup_mult_1_unsigned_32_32_1_2_datab;
wire [63:0] legup_mult_1_unsigned_32_32_1_2_result;
reg [63:0] legup_mult_kernel_2mm_21_24_out_actual;
reg [31:0] legup_mult_kernel_2mm_21_24_out;
reg  legup_mult_kernel_2mm_21_24_en;
reg  legup_mult_1_unsigned_32_32_1_3_clock;
reg  legup_mult_1_unsigned_32_32_1_3_aclr;
reg  legup_mult_1_unsigned_32_32_1_3_sum;
reg  legup_mult_1_unsigned_32_32_1_3_clken;
reg [31:0] legup_mult_1_unsigned_32_32_1_3_dataa;
reg [31:0] legup_mult_1_unsigned_32_32_1_3_datab;
wire [63:0] legup_mult_1_unsigned_32_32_1_3_result;
reg [63:0] legup_mult_kernel_2mm_25_31_out_actual;
reg [31:0] legup_mult_kernel_2mm_25_31_out;
reg  legup_mult_kernel_2mm_25_31_en;

/*   %11 = mul nsw i32 %10, %alpha, !MSB !6, !LSB !3, !extendFrom !6*/
legup_mult_1 legup_mult_1_unsigned_32_32_1_0 (
	.clock (legup_mult_1_unsigned_32_32_1_0_clock),
	.aclr (legup_mult_1_unsigned_32_32_1_0_aclr),
	.sum (legup_mult_1_unsigned_32_32_1_0_sum),
	.clken (legup_mult_1_unsigned_32_32_1_0_clken),
	.dataa (legup_mult_1_unsigned_32_32_1_0_dataa),
	.datab (legup_mult_1_unsigned_32_32_1_0_datab),
	.result (legup_mult_1_unsigned_32_32_1_0_result)
);

/*
defparam
	legup_mult_1_unsigned_32_32_1_0.widtha = 32,
	legup_mult_1_unsigned_32_32_1_0.widthb = 32,
	legup_mult_1_unsigned_32_32_1_0.widthp = 64,
	legup_mult_1_unsigned_32_32_1_0.representation = "UNSIGNED";
*/
/*   %13 = mul nsw i32 %11, %12, !MSB !6, !LSB !3, !extendFrom !6*/
legup_mult_1 legup_mult_1_unsigned_32_32_1_1 (
	.clock (legup_mult_1_unsigned_32_32_1_1_clock),
	.aclr (legup_mult_1_unsigned_32_32_1_1_aclr),
	.sum (legup_mult_1_unsigned_32_32_1_1_sum),
	.clken (legup_mult_1_unsigned_32_32_1_1_clken),
	.dataa (legup_mult_1_unsigned_32_32_1_1_dataa),
	.datab (legup_mult_1_unsigned_32_32_1_1_datab),
	.result (legup_mult_1_unsigned_32_32_1_1_result)
);

/*
defparam
	legup_mult_1_unsigned_32_32_1_1.widtha = 32,
	legup_mult_1_unsigned_32_32_1_1.widthb = 32,
	legup_mult_1_unsigned_32_32_1_1.widthp = 64,
	legup_mult_1_unsigned_32_32_1_1.representation = "UNSIGNED";
*/
/*   %24 = mul nsw i32 %23, %beta, !MSB !6, !LSB !3, !extendFrom !6*/
legup_mult_1 legup_mult_1_unsigned_32_32_1_2 (
	.clock (legup_mult_1_unsigned_32_32_1_2_clock),
	.aclr (legup_mult_1_unsigned_32_32_1_2_aclr),
	.sum (legup_mult_1_unsigned_32_32_1_2_sum),
	.clken (legup_mult_1_unsigned_32_32_1_2_clken),
	.dataa (legup_mult_1_unsigned_32_32_1_2_dataa),
	.datab (legup_mult_1_unsigned_32_32_1_2_datab),
	.result (legup_mult_1_unsigned_32_32_1_2_result)
);

/*
defparam
	legup_mult_1_unsigned_32_32_1_2.widtha = 32,
	legup_mult_1_unsigned_32_32_1_2.widthb = 32,
	legup_mult_1_unsigned_32_32_1_2.widthp = 64,
	legup_mult_1_unsigned_32_32_1_2.representation = "UNSIGNED";
*/
/*   %31 = mul nsw i32 %29, %30, !MSB !6, !LSB !3, !extendFrom !6*/
legup_mult_1 legup_mult_1_unsigned_32_32_1_3 (
	.clock (legup_mult_1_unsigned_32_32_1_3_clock),
	.aclr (legup_mult_1_unsigned_32_32_1_3_aclr),
	.sum (legup_mult_1_unsigned_32_32_1_3_sum),
	.clken (legup_mult_1_unsigned_32_32_1_3_clken),
	.dataa (legup_mult_1_unsigned_32_32_1_3_dataa),
	.datab (legup_mult_1_unsigned_32_32_1_3_datab),
	.result (legup_mult_1_unsigned_32_32_1_3_result)
);

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
		next_state = LEGUP_F_kernel_2mm_BB__1_1;
LEGUP_F_kernel_2mm_BB__16_10:
		next_state = LEGUP_F_kernel_2mm_BB__16_11;
LEGUP_F_kernel_2mm_BB__16_11:
	if ((fsm_stall == 1'd0) && (kernel_2mm_16_exitcond17 == 1'd1))
		next_state = LEGUP_F_kernel_2mm_BB__18_12;
	else if ((fsm_stall == 1'd0) && (kernel_2mm_16_exitcond17 == 1'd0))
		next_state = LEGUP_F_kernel_2mm_BB__3_2;
LEGUP_F_kernel_2mm_BB__18_12:
		next_state = LEGUP_F_kernel_2mm_BB__18_13;
LEGUP_F_kernel_2mm_BB__18_13:
	if ((fsm_stall == 1'd0) && (kernel_2mm_18_exitcond20 == 1'd1))
		next_state = LEGUP_F_kernel_2mm_BB_preheaderpreheaderpreheader_14;
	else if ((fsm_stall == 1'd0) && (kernel_2mm_18_exitcond20 == 1'd0))
		next_state = LEGUP_F_kernel_2mm_BB__1_1;
LEGUP_F_kernel_2mm_BB__1_1:
		next_state = LEGUP_F_kernel_2mm_BB__3_2;
LEGUP_F_kernel_2mm_BB__21_16:
		next_state = LEGUP_F_kernel_2mm_BB__21_17;
LEGUP_F_kernel_2mm_BB__21_17:
		next_state = LEGUP_F_kernel_2mm_BB__21_18;
LEGUP_F_kernel_2mm_BB__21_18:
		next_state = LEGUP_F_kernel_2mm_BB__21_19;
LEGUP_F_kernel_2mm_BB__21_19:
		next_state = LEGUP_F_kernel_2mm_BB__25_20;
LEGUP_F_kernel_2mm_BB__25_20:
		next_state = LEGUP_F_kernel_2mm_BB__25_21;
LEGUP_F_kernel_2mm_BB__25_21:
		next_state = LEGUP_F_kernel_2mm_BB__25_22;
LEGUP_F_kernel_2mm_BB__25_22:
		next_state = LEGUP_F_kernel_2mm_BB__25_23;
LEGUP_F_kernel_2mm_BB__25_23:
	if ((fsm_stall == 1'd0) && (kernel_2mm_25_exitcond3_reg == 1'd1))
		next_state = LEGUP_F_kernel_2mm_BB__34_24;
	else if ((fsm_stall == 1'd0) && (kernel_2mm_25_exitcond3_reg == 1'd0))
		next_state = LEGUP_F_kernel_2mm_BB__25_20;
LEGUP_F_kernel_2mm_BB__34_24:
		next_state = LEGUP_F_kernel_2mm_BB__34_25;
LEGUP_F_kernel_2mm_BB__34_25:
	if ((fsm_stall == 1'd0) && (kernel_2mm_34_exitcond7 == 1'd1))
		next_state = LEGUP_F_kernel_2mm_BB_preheader_26;
	else if ((fsm_stall == 1'd0) && (kernel_2mm_34_exitcond7 == 1'd0))
		next_state = LEGUP_F_kernel_2mm_BB__21_16;
LEGUP_F_kernel_2mm_BB__37_28:
		next_state = LEGUP_0;
LEGUP_F_kernel_2mm_BB__3_2:
		next_state = LEGUP_F_kernel_2mm_BB__3_3;
LEGUP_F_kernel_2mm_BB__3_3:
		next_state = LEGUP_F_kernel_2mm_BB__3_4;
LEGUP_F_kernel_2mm_BB__3_4:
		next_state = LEGUP_F_kernel_2mm_BB__6_5;
LEGUP_F_kernel_2mm_BB__6_5:
		next_state = LEGUP_F_kernel_2mm_BB__6_6;
LEGUP_F_kernel_2mm_BB__6_6:
		next_state = LEGUP_F_kernel_2mm_BB__6_7;
LEGUP_F_kernel_2mm_BB__6_7:
		next_state = LEGUP_F_kernel_2mm_BB__6_8;
LEGUP_F_kernel_2mm_BB__6_8:
		next_state = LEGUP_F_kernel_2mm_BB__6_9;
LEGUP_F_kernel_2mm_BB__6_9:
	if ((fsm_stall == 1'd0) && (kernel_2mm_6_exitcond14_reg == 1'd1))
		next_state = LEGUP_F_kernel_2mm_BB__16_10;
	else if ((fsm_stall == 1'd0) && (kernel_2mm_6_exitcond14_reg == 1'd0))
		next_state = LEGUP_F_kernel_2mm_BB__6_5;
LEGUP_F_kernel_2mm_BB_preheader_26:
		next_state = LEGUP_F_kernel_2mm_BB_preheader_27;
LEGUP_F_kernel_2mm_BB_preheader_27:
	if ((fsm_stall == 1'd0) && (kernel_2mm_preheader_exitcond == 1'd1))
		next_state = LEGUP_F_kernel_2mm_BB__37_28;
	else if ((fsm_stall == 1'd0) && (kernel_2mm_preheader_exitcond == 1'd0))
		next_state = LEGUP_F_kernel_2mm_BB_preheaderpreheader_15;
LEGUP_F_kernel_2mm_BB_preheaderpreheader_15:
		next_state = LEGUP_F_kernel_2mm_BB__21_16;
LEGUP_F_kernel_2mm_BB_preheaderpreheaderpreheader_14:
		next_state = LEGUP_F_kernel_2mm_BB_preheaderpreheader_15;
default:
	next_state = cur_state;
endcase

end
always @(posedge clk) begin
	if (start) begin
		arg_alpha_reg <= arg_alpha;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_beta_reg <= arg_beta;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_tmp_reg <= arg_tmp;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_A_reg <= arg_A;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_B_reg <= arg_B;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_C_reg <= arg_C;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_D_reg <= arg_D;
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
	/* kernel_2mm: %1*/
	/*   %i.08 = phi i32 [ 0, %0 ], [ %19, %18 ], !MSB !4, !LSB !3, !extendFrom !4*/
	if ((((cur_state == LEGUP_0) & (fsm_stall == 1'd0)) & (start == 1'd1))) begin
		kernel_2mm_1_i08 = 32'd0;
	end
	/* kernel_2mm: %1*/
	/*   %i.08 = phi i32 [ 0, %0 ], [ %19, %18 ], !MSB !4, !LSB !3, !extendFrom !4*/
	else /* if ((((cur_state == LEGUP_F_kernel_2mm_BB__18_13) & (fsm_stall == 1'd0)) & (kernel_2mm_18_exitcond20 == 1'd0))) */ begin
		kernel_2mm_1_i08 = kernel_2mm_18_19_reg;
	end
end
always @(posedge clk) begin
	/* kernel_2mm: %1*/
	/*   %i.08 = phi i32 [ 0, %0 ], [ %19, %18 ], !MSB !4, !LSB !3, !extendFrom !4*/
	if ((((cur_state == LEGUP_0) & (fsm_stall == 1'd0)) & (start == 1'd1))) begin
		kernel_2mm_1_i08_reg <= kernel_2mm_1_i08;
	end
	/* kernel_2mm: %1*/
	/*   %i.08 = phi i32 [ 0, %0 ], [ %19, %18 ], !MSB !4, !LSB !3, !extendFrom !4*/
	if ((((cur_state == LEGUP_F_kernel_2mm_BB__18_13) & (fsm_stall == 1'd0)) & (kernel_2mm_18_exitcond20 == 1'd0))) begin
		kernel_2mm_1_i08_reg <= kernel_2mm_1_i08;
	end
end
always @(*) begin
	/* kernel_2mm: %1*/
	/*   %2 = mul i32 %i.08, 8, !MSB !5, !LSB !4, !extendFrom !5*/
		kernel_2mm_1_2 = ({4'd0,kernel_2mm_1_i08_reg} * 32'd8);
end
always @(posedge clk) begin
	/* kernel_2mm: %1*/
	/*   %2 = mul i32 %i.08, 8, !MSB !5, !LSB !4, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__1_1)) begin
		kernel_2mm_1_2_reg <= kernel_2mm_1_2;
	end
end
always @(*) begin
	/* kernel_2mm: %3*/
	/*   %j.07 = phi i32 [ 0, %1 ], [ %17, %16 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_kernel_2mm_BB__1_1) & (fsm_stall == 1'd0))) begin
		kernel_2mm_3_j07 = 32'd0;
	end
	/* kernel_2mm: %3*/
	/*   %j.07 = phi i32 [ 0, %1 ], [ %17, %16 ], !MSB !6, !LSB !3, !extendFrom !6*/
	else /* if ((((cur_state == LEGUP_F_kernel_2mm_BB__16_11) & (fsm_stall == 1'd0)) & (kernel_2mm_16_exitcond17 == 1'd0))) */ begin
		kernel_2mm_3_j07 = kernel_2mm_16_17_reg;
	end
end
always @(posedge clk) begin
	/* kernel_2mm: %3*/
	/*   %j.07 = phi i32 [ 0, %1 ], [ %17, %16 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_kernel_2mm_BB__1_1) & (fsm_stall == 1'd0))) begin
		kernel_2mm_3_j07_reg <= kernel_2mm_3_j07;
	end
	/* kernel_2mm: %3*/
	/*   %j.07 = phi i32 [ 0, %1 ], [ %17, %16 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_kernel_2mm_BB__16_11) & (fsm_stall == 1'd0)) & (kernel_2mm_16_exitcond17 == 1'd0))) begin
		kernel_2mm_3_j07_reg <= kernel_2mm_3_j07;
	end
end
always @(*) begin
	/* kernel_2mm: %3*/
	/*   %4 = add i32 %2, %j.07, !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_3_4 = ({24'd0,kernel_2mm_1_2_reg} + kernel_2mm_3_j07_reg);
end
always @(posedge clk) begin
	/* kernel_2mm: %3*/
	/*   %4 = add i32 %2, %j.07, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__3_2)) begin
		kernel_2mm_3_4_reg <= kernel_2mm_3_4;
	end
end
always @(*) begin
	/* kernel_2mm: %3*/
	/*   %scevgep14 = getelementptr i32* %tmp, i32 %4, !MSB !2, !LSB !3, !extendFrom !2*/
		kernel_2mm_3_scevgep14 = (arg_tmp_reg + (4 * kernel_2mm_3_4_reg));
end
always @(posedge clk) begin
	/* kernel_2mm: %3*/
	/*   %scevgep14 = getelementptr i32* %tmp, i32 %4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__3_3)) begin
		kernel_2mm_3_scevgep14_reg <= kernel_2mm_3_scevgep14;
	end
end
always @(*) begin
	/* kernel_2mm: %3*/
	/*   %5 = load i32* %scevgep14, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_3_5 = main_0_tmp_out_a;
end
always @(*) begin
	/* kernel_2mm: %6*/
	/*   %x.06 = phi i32 [ %5, %3 ], [ %14, %6 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_kernel_2mm_BB__3_4) & (fsm_stall == 1'd0))) begin
		kernel_2mm_6_x06 = kernel_2mm_3_5;
	end
	/* kernel_2mm: %6*/
	/*   %x.06 = phi i32 [ %5, %3 ], [ %14, %6 ], !MSB !6, !LSB !3, !extendFrom !6*/
	else /* if ((((cur_state == LEGUP_F_kernel_2mm_BB__6_9) & (fsm_stall == 1'd0)) & (kernel_2mm_6_exitcond14_reg == 1'd0))) */ begin
		kernel_2mm_6_x06 = kernel_2mm_6_14;
	end
end
always @(posedge clk) begin
	/* kernel_2mm: %6*/
	/*   %x.06 = phi i32 [ %5, %3 ], [ %14, %6 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_kernel_2mm_BB__3_4) & (fsm_stall == 1'd0))) begin
		kernel_2mm_6_x06_reg <= kernel_2mm_6_x06;
	end
	/* kernel_2mm: %6*/
	/*   %x.06 = phi i32 [ %5, %3 ], [ %14, %6 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_kernel_2mm_BB__6_9) & (fsm_stall == 1'd0)) & (kernel_2mm_6_exitcond14_reg == 1'd0))) begin
		kernel_2mm_6_x06_reg <= kernel_2mm_6_x06;
	end
end
always @(*) begin
	/* kernel_2mm: %6*/
	/*   %k.05 = phi i32 [ 0, %3 ], [ %15, %6 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_kernel_2mm_BB__3_4) & (fsm_stall == 1'd0))) begin
		kernel_2mm_6_k05 = 32'd0;
	end
	/* kernel_2mm: %6*/
	/*   %k.05 = phi i32 [ 0, %3 ], [ %15, %6 ], !MSB !6, !LSB !3, !extendFrom !6*/
	else /* if ((((cur_state == LEGUP_F_kernel_2mm_BB__6_9) & (fsm_stall == 1'd0)) & (kernel_2mm_6_exitcond14_reg == 1'd0))) */ begin
		kernel_2mm_6_k05 = kernel_2mm_6_15_reg;
	end
end
always @(posedge clk) begin
	/* kernel_2mm: %6*/
	/*   %k.05 = phi i32 [ 0, %3 ], [ %15, %6 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_kernel_2mm_BB__3_4) & (fsm_stall == 1'd0))) begin
		kernel_2mm_6_k05_reg <= kernel_2mm_6_k05;
	end
	/* kernel_2mm: %6*/
	/*   %k.05 = phi i32 [ 0, %3 ], [ %15, %6 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_kernel_2mm_BB__6_9) & (fsm_stall == 1'd0)) & (kernel_2mm_6_exitcond14_reg == 1'd0))) begin
		kernel_2mm_6_k05_reg <= kernel_2mm_6_k05;
	end
end
always @(*) begin
	/* kernel_2mm: %6*/
	/*   %7 = add i32 %2, %k.05, !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_6_7 = ({24'd0,kernel_2mm_1_2_reg} + kernel_2mm_6_k05_reg);
end
always @(posedge clk) begin
	/* kernel_2mm: %6*/
	/*   %7 = add i32 %2, %k.05, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__6_5)) begin
		kernel_2mm_6_7_reg <= kernel_2mm_6_7;
	end
end
always @(*) begin
	/* kernel_2mm: %6*/
	/*   %scevgep11 = getelementptr i32* %A, i32 %7, !MSB !2, !LSB !3, !extendFrom !2*/
		kernel_2mm_6_scevgep11 = (arg_A_reg + (4 * kernel_2mm_6_7_reg));
end
always @(*) begin
	/* kernel_2mm: %6*/
	/*   %8 = mul i32 %k.05, 8, !MSB !6, !LSB !4, !extendFrom !6*/
		kernel_2mm_6_8 = (kernel_2mm_6_k05_reg * 32'd8);
end
always @(*) begin
	/* kernel_2mm: %6*/
	/*   %9 = add i32 %j.07, %8, !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_6_9 = (kernel_2mm_3_j07_reg + kernel_2mm_6_8);
end
always @(posedge clk) begin
	/* kernel_2mm: %6*/
	/*   %9 = add i32 %j.07, %8, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__6_5)) begin
		kernel_2mm_6_9_reg <= kernel_2mm_6_9;
	end
end
always @(*) begin
	/* kernel_2mm: %6*/
	/*   %scevgep10 = getelementptr i32* %B, i32 %9, !MSB !2, !LSB !3, !extendFrom !2*/
		kernel_2mm_6_scevgep10 = (arg_B_reg + (4 * kernel_2mm_6_9_reg));
end
always @(*) begin
	/* kernel_2mm: %6*/
	/*   %10 = load i32* %scevgep11, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_6_10 = main_0_A_out_a;
end
always @(*) begin
	kernel_2mm_6_11 = legup_mult_kernel_2mm_6_11_out;
end
always @(*) begin
	/* kernel_2mm: %6*/
	/*   %12 = load i32* %scevgep10, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_6_12 = main_0_B_out_a;
end
always @(posedge clk) begin
	/* kernel_2mm: %6*/
	/*   %12 = load i32* %scevgep10, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__6_7)) begin
		kernel_2mm_6_12_reg <= kernel_2mm_6_12;
	end
end
always @(*) begin
	kernel_2mm_6_13 = legup_mult_kernel_2mm_6_13_out;
end
always @(*) begin
	/* kernel_2mm: %6*/
	/*   %14 = add nsw i32 %x.06, %13, !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_6_14 = (kernel_2mm_6_x06_reg + kernel_2mm_6_13);
end
always @(*) begin
	/* kernel_2mm: %6*/
	/*   %15 = add nsw i32 %k.05, 1, !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_6_15 = (kernel_2mm_6_k05_reg + 32'd1);
end
always @(posedge clk) begin
	/* kernel_2mm: %6*/
	/*   %15 = add nsw i32 %k.05, 1, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__6_5)) begin
		kernel_2mm_6_15_reg <= kernel_2mm_6_15;
	end
end
always @(*) begin
	/* kernel_2mm: %6*/
	/*   %exitcond14 = icmp eq i32 %15, 8, !MSB !3, !LSB !3, !extendFrom !3*/
		kernel_2mm_6_exitcond14 = (kernel_2mm_6_15_reg == 32'd8);
end
always @(posedge clk) begin
	/* kernel_2mm: %6*/
	/*   %exitcond14 = icmp eq i32 %15, 8, !MSB !3, !LSB !3, !extendFrom !3*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__6_6)) begin
		kernel_2mm_6_exitcond14_reg <= kernel_2mm_6_exitcond14;
	end
end
always @(*) begin
	/* kernel_2mm: %16*/
	/*   %.lcssa1 = phi i32 [ %14, %6 ], !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_16_lcssa1 = kernel_2mm_6_14;
end
always @(posedge clk) begin
	/* kernel_2mm: %16*/
	/*   %.lcssa1 = phi i32 [ %14, %6 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_kernel_2mm_BB__6_9) & (fsm_stall == 1'd0)) & (kernel_2mm_6_exitcond14_reg == 1'd1))) begin
		kernel_2mm_16_lcssa1_reg <= kernel_2mm_16_lcssa1;
	end
end
always @(*) begin
	/* kernel_2mm: %16*/
	/*   %17 = add nsw i32 %j.07, 1, !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_16_17 = (kernel_2mm_3_j07_reg + 32'd1);
end
always @(posedge clk) begin
	/* kernel_2mm: %16*/
	/*   %17 = add nsw i32 %j.07, 1, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__16_10)) begin
		kernel_2mm_16_17_reg <= kernel_2mm_16_17;
	end
end
always @(*) begin
	/* kernel_2mm: %16*/
	/*   %exitcond17 = icmp eq i32 %17, 8, !MSB !3, !LSB !3, !extendFrom !3*/
		kernel_2mm_16_exitcond17 = (kernel_2mm_16_17_reg == 32'd8);
end
always @(*) begin
	/* kernel_2mm: %18*/
	/*   %19 = add nsw i32 %i.08, 1, !MSB !7, !LSB !3, !extendFrom !7*/
		kernel_2mm_18_19 = ({1'd0,kernel_2mm_1_i08_reg} + 32'd1);
end
always @(posedge clk) begin
	/* kernel_2mm: %18*/
	/*   %19 = add nsw i32 %i.08, 1, !MSB !7, !LSB !3, !extendFrom !7*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__18_12)) begin
		kernel_2mm_18_19_reg <= kernel_2mm_18_19;
	end
end
always @(*) begin
	/* kernel_2mm: %18*/
	/*   %exitcond20 = icmp eq i32 %19, 8, !MSB !3, !LSB !3, !extendFrom !3*/
		kernel_2mm_18_exitcond20 = (kernel_2mm_18_19_reg == 32'd8);
end
always @(*) begin
	/* kernel_2mm: %.preheader.preheader*/
	/*   %i.14 = phi i32 [ %36, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	if (((cur_state == LEGUP_F_kernel_2mm_BB_preheaderpreheaderpreheader_14) & (fsm_stall == 1'd0))) begin
		kernel_2mm_preheaderpreheader_i14 = 32'd0;
	end
	/* kernel_2mm: %.preheader.preheader*/
	/*   %i.14 = phi i32 [ %36, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	else /* if ((((cur_state == LEGUP_F_kernel_2mm_BB_preheader_27) & (fsm_stall == 1'd0)) & (kernel_2mm_preheader_exitcond == 1'd0))) */ begin
		kernel_2mm_preheaderpreheader_i14 = kernel_2mm_preheader_36_reg;
	end
end
always @(posedge clk) begin
	/* kernel_2mm: %.preheader.preheader*/
	/*   %i.14 = phi i32 [ %36, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	if (((cur_state == LEGUP_F_kernel_2mm_BB_preheaderpreheaderpreheader_14) & (fsm_stall == 1'd0))) begin
		kernel_2mm_preheaderpreheader_i14_reg <= kernel_2mm_preheaderpreheader_i14;
	end
	/* kernel_2mm: %.preheader.preheader*/
	/*   %i.14 = phi i32 [ %36, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	if ((((cur_state == LEGUP_F_kernel_2mm_BB_preheader_27) & (fsm_stall == 1'd0)) & (kernel_2mm_preheader_exitcond == 1'd0))) begin
		kernel_2mm_preheaderpreheader_i14_reg <= kernel_2mm_preheaderpreheader_i14;
	end
end
always @(*) begin
	/* kernel_2mm: %.preheader.preheader*/
	/*   %20 = mul i32 %i.14, 8, !MSB !5, !LSB !4, !extendFrom !5*/
		kernel_2mm_preheaderpreheader_20 = ({4'd0,kernel_2mm_preheaderpreheader_i14_reg} * 32'd8);
end
always @(posedge clk) begin
	/* kernel_2mm: %.preheader.preheader*/
	/*   %20 = mul i32 %i.14, 8, !MSB !5, !LSB !4, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB_preheaderpreheader_15)) begin
		kernel_2mm_preheaderpreheader_20_reg <= kernel_2mm_preheaderpreheader_20;
	end
end
always @(*) begin
	/* kernel_2mm: %21*/
	/*   %j.13 = phi i32 [ 0, %.preheader.preheader ], [ %35, %34 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_kernel_2mm_BB_preheaderpreheader_15) & (fsm_stall == 1'd0))) begin
		kernel_2mm_21_j13 = 32'd0;
	end
	/* kernel_2mm: %21*/
	/*   %j.13 = phi i32 [ 0, %.preheader.preheader ], [ %35, %34 ], !MSB !6, !LSB !3, !extendFrom !6*/
	else /* if ((((cur_state == LEGUP_F_kernel_2mm_BB__34_25) & (fsm_stall == 1'd0)) & (kernel_2mm_34_exitcond7 == 1'd0))) */ begin
		kernel_2mm_21_j13 = kernel_2mm_34_35_reg;
	end
end
always @(posedge clk) begin
	/* kernel_2mm: %21*/
	/*   %j.13 = phi i32 [ 0, %.preheader.preheader ], [ %35, %34 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_kernel_2mm_BB_preheaderpreheader_15) & (fsm_stall == 1'd0))) begin
		kernel_2mm_21_j13_reg <= kernel_2mm_21_j13;
	end
	/* kernel_2mm: %21*/
	/*   %j.13 = phi i32 [ 0, %.preheader.preheader ], [ %35, %34 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_kernel_2mm_BB__34_25) & (fsm_stall == 1'd0)) & (kernel_2mm_34_exitcond7 == 1'd0))) begin
		kernel_2mm_21_j13_reg <= kernel_2mm_21_j13;
	end
end
always @(*) begin
	/* kernel_2mm: %21*/
	/*   %22 = add i32 %20, %j.13, !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_21_22 = ({24'd0,kernel_2mm_preheaderpreheader_20_reg} + kernel_2mm_21_j13_reg);
end
always @(posedge clk) begin
	/* kernel_2mm: %21*/
	/*   %22 = add i32 %20, %j.13, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__21_16)) begin
		kernel_2mm_21_22_reg <= kernel_2mm_21_22;
	end
end
always @(*) begin
	/* kernel_2mm: %21*/
	/*   %scevgep5 = getelementptr i32* %D, i32 %22, !MSB !2, !LSB !3, !extendFrom !2*/
		kernel_2mm_21_scevgep5 = (arg_D_reg + (4 * kernel_2mm_21_22_reg));
end
always @(posedge clk) begin
	/* kernel_2mm: %21*/
	/*   %scevgep5 = getelementptr i32* %D, i32 %22, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__21_17)) begin
		kernel_2mm_21_scevgep5_reg <= kernel_2mm_21_scevgep5;
	end
end
always @(*) begin
	/* kernel_2mm: %21*/
	/*   %23 = load i32* %scevgep5, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_21_23 = main_0_D_out_a;
end
always @(*) begin
	kernel_2mm_21_24 = legup_mult_kernel_2mm_21_24_out;
end
always @(*) begin
	/* kernel_2mm: %25*/
	/*   %x1.02 = phi i32 [ %24, %21 ], [ %32, %25 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_kernel_2mm_BB__21_19) & (fsm_stall == 1'd0))) begin
		kernel_2mm_25_x102 = kernel_2mm_21_24;
	end
	/* kernel_2mm: %25*/
	/*   %x1.02 = phi i32 [ %24, %21 ], [ %32, %25 ], !MSB !6, !LSB !3, !extendFrom !6*/
	else /* if ((((cur_state == LEGUP_F_kernel_2mm_BB__25_23) & (fsm_stall == 1'd0)) & (kernel_2mm_25_exitcond3_reg == 1'd0))) */ begin
		kernel_2mm_25_x102 = kernel_2mm_25_32;
	end
end
always @(posedge clk) begin
	/* kernel_2mm: %25*/
	/*   %x1.02 = phi i32 [ %24, %21 ], [ %32, %25 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_kernel_2mm_BB__21_19) & (fsm_stall == 1'd0))) begin
		kernel_2mm_25_x102_reg <= kernel_2mm_25_x102;
	end
	/* kernel_2mm: %25*/
	/*   %x1.02 = phi i32 [ %24, %21 ], [ %32, %25 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_kernel_2mm_BB__25_23) & (fsm_stall == 1'd0)) & (kernel_2mm_25_exitcond3_reg == 1'd0))) begin
		kernel_2mm_25_x102_reg <= kernel_2mm_25_x102;
	end
end
always @(*) begin
	/* kernel_2mm: %25*/
	/*   %k.11 = phi i32 [ 0, %21 ], [ %33, %25 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_kernel_2mm_BB__21_19) & (fsm_stall == 1'd0))) begin
		kernel_2mm_25_k11 = 32'd0;
	end
	/* kernel_2mm: %25*/
	/*   %k.11 = phi i32 [ 0, %21 ], [ %33, %25 ], !MSB !6, !LSB !3, !extendFrom !6*/
	else /* if ((((cur_state == LEGUP_F_kernel_2mm_BB__25_23) & (fsm_stall == 1'd0)) & (kernel_2mm_25_exitcond3_reg == 1'd0))) */ begin
		kernel_2mm_25_k11 = kernel_2mm_25_33_reg;
	end
end
always @(posedge clk) begin
	/* kernel_2mm: %25*/
	/*   %k.11 = phi i32 [ 0, %21 ], [ %33, %25 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_kernel_2mm_BB__21_19) & (fsm_stall == 1'd0))) begin
		kernel_2mm_25_k11_reg <= kernel_2mm_25_k11;
	end
	/* kernel_2mm: %25*/
	/*   %k.11 = phi i32 [ 0, %21 ], [ %33, %25 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_kernel_2mm_BB__25_23) & (fsm_stall == 1'd0)) & (kernel_2mm_25_exitcond3_reg == 1'd0))) begin
		kernel_2mm_25_k11_reg <= kernel_2mm_25_k11;
	end
end
always @(*) begin
	/* kernel_2mm: %25*/
	/*   %26 = add i32 %20, %k.11, !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_25_26 = ({24'd0,kernel_2mm_preheaderpreheader_20_reg} + kernel_2mm_25_k11_reg);
end
always @(posedge clk) begin
	/* kernel_2mm: %25*/
	/*   %26 = add i32 %20, %k.11, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__25_20)) begin
		kernel_2mm_25_26_reg <= kernel_2mm_25_26;
	end
end
always @(*) begin
	/* kernel_2mm: %25*/
	/*   %scevgep3 = getelementptr i32* %tmp, i32 %26, !MSB !2, !LSB !3, !extendFrom !2*/
		kernel_2mm_25_scevgep3 = (arg_tmp_reg + (4 * kernel_2mm_25_26_reg));
end
always @(*) begin
	/* kernel_2mm: %25*/
	/*   %27 = mul i32 %k.11, 8, !MSB !6, !LSB !4, !extendFrom !6*/
		kernel_2mm_25_27 = (kernel_2mm_25_k11_reg * 32'd8);
end
always @(*) begin
	/* kernel_2mm: %25*/
	/*   %28 = add i32 %j.13, %27, !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_25_28 = (kernel_2mm_21_j13_reg + kernel_2mm_25_27);
end
always @(posedge clk) begin
	/* kernel_2mm: %25*/
	/*   %28 = add i32 %j.13, %27, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__25_20)) begin
		kernel_2mm_25_28_reg <= kernel_2mm_25_28;
	end
end
always @(*) begin
	/* kernel_2mm: %25*/
	/*   %scevgep = getelementptr i32* %C, i32 %28, !MSB !2, !LSB !3, !extendFrom !2*/
		kernel_2mm_25_scevgep = (arg_C_reg + (4 * kernel_2mm_25_28_reg));
end
always @(*) begin
	/* kernel_2mm: %25*/
	/*   %29 = load i32* %scevgep3, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_25_29 = main_0_tmp_out_a;
end
always @(*) begin
	/* kernel_2mm: %25*/
	/*   %30 = load i32* %scevgep, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_25_30 = main_0_C_out_a;
end
always @(*) begin
	kernel_2mm_25_31 = legup_mult_kernel_2mm_25_31_out;
end
always @(*) begin
	/* kernel_2mm: %25*/
	/*   %32 = add nsw i32 %x1.02, %31, !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_25_32 = (kernel_2mm_25_x102_reg + kernel_2mm_25_31);
end
always @(*) begin
	/* kernel_2mm: %25*/
	/*   %33 = add nsw i32 %k.11, 1, !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_25_33 = (kernel_2mm_25_k11_reg + 32'd1);
end
always @(posedge clk) begin
	/* kernel_2mm: %25*/
	/*   %33 = add nsw i32 %k.11, 1, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__25_20)) begin
		kernel_2mm_25_33_reg <= kernel_2mm_25_33;
	end
end
always @(*) begin
	/* kernel_2mm: %25*/
	/*   %exitcond3 = icmp eq i32 %33, 8, !MSB !3, !LSB !3, !extendFrom !3*/
		kernel_2mm_25_exitcond3 = (kernel_2mm_25_33_reg == 32'd8);
end
always @(posedge clk) begin
	/* kernel_2mm: %25*/
	/*   %exitcond3 = icmp eq i32 %33, 8, !MSB !3, !LSB !3, !extendFrom !3*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__25_21)) begin
		kernel_2mm_25_exitcond3_reg <= kernel_2mm_25_exitcond3;
	end
end
always @(*) begin
	/* kernel_2mm: %34*/
	/*   %.lcssa = phi i32 [ %32, %25 ], !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_34_lcssa = kernel_2mm_25_32;
end
always @(posedge clk) begin
	/* kernel_2mm: %34*/
	/*   %.lcssa = phi i32 [ %32, %25 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_kernel_2mm_BB__25_23) & (fsm_stall == 1'd0)) & (kernel_2mm_25_exitcond3_reg == 1'd1))) begin
		kernel_2mm_34_lcssa_reg <= kernel_2mm_34_lcssa;
	end
end
always @(*) begin
	/* kernel_2mm: %34*/
	/*   %35 = add nsw i32 %j.13, 1, !MSB !6, !LSB !3, !extendFrom !6*/
		kernel_2mm_34_35 = (kernel_2mm_21_j13_reg + 32'd1);
end
always @(posedge clk) begin
	/* kernel_2mm: %34*/
	/*   %35 = add nsw i32 %j.13, 1, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__34_24)) begin
		kernel_2mm_34_35_reg <= kernel_2mm_34_35;
	end
end
always @(*) begin
	/* kernel_2mm: %34*/
	/*   %exitcond7 = icmp eq i32 %35, 8, !MSB !3, !LSB !3, !extendFrom !3*/
		kernel_2mm_34_exitcond7 = (kernel_2mm_34_35_reg == 32'd8);
end
always @(*) begin
	/* kernel_2mm: %.preheader*/
	/*   %36 = add nsw i32 %i.14, 1, !MSB !7, !LSB !3, !extendFrom !7*/
		kernel_2mm_preheader_36 = ({1'd0,kernel_2mm_preheaderpreheader_i14_reg} + 32'd1);
end
always @(posedge clk) begin
	/* kernel_2mm: %.preheader*/
	/*   %36 = add nsw i32 %i.14, 1, !MSB !7, !LSB !3, !extendFrom !7*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB_preheader_26)) begin
		kernel_2mm_preheader_36_reg <= kernel_2mm_preheader_36;
	end
end
always @(*) begin
	/* kernel_2mm: %.preheader*/
	/*   %exitcond = icmp eq i32 %36, 8, !MSB !3, !LSB !3, !extendFrom !3*/
		kernel_2mm_preheader_exitcond = (kernel_2mm_preheader_36_reg == 32'd8);
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
	legup_mult_1_unsigned_32_32_1_0_clken = legup_mult_kernel_2mm_6_11_en;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_0_dataa = kernel_2mm_6_10;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_0_datab = arg_alpha_reg;
end
always @(*) begin
	legup_mult_kernel_2mm_6_11_out_actual = legup_mult_1_unsigned_32_32_1_0_result;
end
always @(*) begin
	legup_mult_kernel_2mm_6_11_out = legup_mult_kernel_2mm_6_11_out_actual[31:0];
end
always @(*) begin
	legup_mult_kernel_2mm_6_11_en = ~(fsm_stall);
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
	legup_mult_1_unsigned_32_32_1_1_clken = legup_mult_kernel_2mm_6_13_en;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_1_dataa = kernel_2mm_6_11;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_1_datab = kernel_2mm_6_12_reg;
end
always @(*) begin
	legup_mult_kernel_2mm_6_13_out_actual = legup_mult_1_unsigned_32_32_1_1_result;
end
always @(*) begin
	legup_mult_kernel_2mm_6_13_out = legup_mult_kernel_2mm_6_13_out_actual[31:0];
end
always @(*) begin
	legup_mult_kernel_2mm_6_13_en = ~(fsm_stall);
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
	legup_mult_1_unsigned_32_32_1_2_clken = legup_mult_kernel_2mm_21_24_en;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_2_dataa = kernel_2mm_21_23;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_2_datab = arg_beta_reg;
end
always @(*) begin
	legup_mult_kernel_2mm_21_24_out_actual = legup_mult_1_unsigned_32_32_1_2_result;
end
always @(*) begin
	legup_mult_kernel_2mm_21_24_out = legup_mult_kernel_2mm_21_24_out_actual[31:0];
end
always @(*) begin
	legup_mult_kernel_2mm_21_24_en = ~(fsm_stall);
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
	legup_mult_1_unsigned_32_32_1_3_clken = legup_mult_kernel_2mm_25_31_en;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_3_dataa = kernel_2mm_25_29;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_3_datab = kernel_2mm_25_30;
end
always @(*) begin
	legup_mult_kernel_2mm_25_31_out_actual = legup_mult_1_unsigned_32_32_1_3_result;
end
always @(*) begin
	legup_mult_kernel_2mm_25_31_out = legup_mult_kernel_2mm_25_31_out_actual[31:0];
end
always @(*) begin
	legup_mult_kernel_2mm_25_31_en = ~(fsm_stall);
end
always @(posedge clk) begin
	if ((cur_state == LEGUP_0)) begin
		finish <= 1'd0;
	end
	/* kernel_2mm: %37*/
	/*   ret void, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__37_28)) begin
		finish <= (fsm_stall == 1'd0);
	end
end
always @(*) begin
	main_0_tmp_write_enable_a = 1'd0;
	/* kernel_2mm: %16*/
	/*   store i32 %.lcssa1, i32* %scevgep14, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__16_10)) begin
		main_0_tmp_write_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_tmp_in_a = 0;
	/* kernel_2mm: %16*/
	/*   store i32 %.lcssa1, i32* %scevgep14, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__16_10)) begin
		main_0_tmp_in_a = kernel_2mm_16_lcssa1_reg;
	end
end
assign main_0_tmp_byteena_a = 1'd1;
always @(*) begin
	main_0_tmp_enable_a = 1'd0;
	/* kernel_2mm: %3*/
	/*   %5 = load i32* %scevgep14, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__3_3)) begin
		main_0_tmp_enable_a = 1'd1;
	end
	/* kernel_2mm: %16*/
	/*   store i32 %.lcssa1, i32* %scevgep14, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__16_10)) begin
		main_0_tmp_enable_a = 1'd1;
	end
	/* kernel_2mm: %25*/
	/*   %29 = load i32* %scevgep3, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__25_21)) begin
		main_0_tmp_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_tmp_address_a = 6'd0;
	/* kernel_2mm: %3*/
	/*   %5 = load i32* %scevgep14, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__3_3)) begin
		main_0_tmp_address_a = (kernel_2mm_3_scevgep14 >>> 3'd2);
	end
	/* kernel_2mm: %16*/
	/*   store i32 %.lcssa1, i32* %scevgep14, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__16_10)) begin
		main_0_tmp_address_a = (kernel_2mm_3_scevgep14_reg >>> 3'd2);
	end
	/* kernel_2mm: %25*/
	/*   %29 = load i32* %scevgep3, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__25_21)) begin
		main_0_tmp_address_a = (kernel_2mm_25_scevgep3 >>> 3'd2);
	end
end
assign main_0_tmp_write_enable_b = 1'd0;
assign main_0_tmp_in_b = 0;
assign main_0_tmp_byteena_b = 1'd1;
assign main_0_tmp_enable_b = 1'd0;
assign main_0_tmp_address_b = 6'd0;
assign main_0_A_write_enable_a = 1'd0;
assign main_0_A_in_a = 0;
assign main_0_A_byteena_a = 1'd1;
always @(*) begin
	main_0_A_enable_a = 1'd0;
	/* kernel_2mm: %6*/
	/*   %10 = load i32* %scevgep11, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__6_6)) begin
		main_0_A_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_A_address_a = 6'd0;
	/* kernel_2mm: %6*/
	/*   %10 = load i32* %scevgep11, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__6_6)) begin
		main_0_A_address_a = (kernel_2mm_6_scevgep11 >>> 3'd2);
	end
end
assign main_0_A_write_enable_b = 1'd0;
assign main_0_A_in_b = 0;
assign main_0_A_byteena_b = 1'd1;
assign main_0_A_enable_b = 1'd0;
assign main_0_A_address_b = 6'd0;
assign main_0_B_write_enable_a = 1'd0;
assign main_0_B_in_a = 0;
assign main_0_B_byteena_a = 1'd1;
always @(*) begin
	main_0_B_enable_a = 1'd0;
	/* kernel_2mm: %6*/
	/*   %12 = load i32* %scevgep10, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__6_6)) begin
		main_0_B_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_B_address_a = 6'd0;
	/* kernel_2mm: %6*/
	/*   %12 = load i32* %scevgep10, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__6_6)) begin
		main_0_B_address_a = (kernel_2mm_6_scevgep10 >>> 3'd2);
	end
end
assign main_0_B_write_enable_b = 1'd0;
assign main_0_B_in_b = 0;
assign main_0_B_byteena_b = 1'd1;
assign main_0_B_enable_b = 1'd0;
assign main_0_B_address_b = 6'd0;
always @(*) begin
	main_0_D_write_enable_a = 1'd0;
	/* kernel_2mm: %34*/
	/*   store i32 %.lcssa, i32* %scevgep5, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__34_24)) begin
		main_0_D_write_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_D_in_a = 0;
	/* kernel_2mm: %34*/
	/*   store i32 %.lcssa, i32* %scevgep5, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__34_24)) begin
		main_0_D_in_a = kernel_2mm_34_lcssa_reg;
	end
end
assign main_0_D_byteena_a = 1'd1;
always @(*) begin
	main_0_D_enable_a = 1'd0;
	/* kernel_2mm: %21*/
	/*   %23 = load i32* %scevgep5, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__21_17)) begin
		main_0_D_enable_a = 1'd1;
	end
	/* kernel_2mm: %34*/
	/*   store i32 %.lcssa, i32* %scevgep5, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__34_24)) begin
		main_0_D_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_D_address_a = 6'd0;
	/* kernel_2mm: %21*/
	/*   %23 = load i32* %scevgep5, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__21_17)) begin
		main_0_D_address_a = (kernel_2mm_21_scevgep5 >>> 3'd2);
	end
	/* kernel_2mm: %34*/
	/*   store i32 %.lcssa, i32* %scevgep5, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__34_24)) begin
		main_0_D_address_a = (kernel_2mm_21_scevgep5_reg >>> 3'd2);
	end
end
assign main_0_D_write_enable_b = 1'd0;
assign main_0_D_in_b = 0;
assign main_0_D_byteena_b = 1'd1;
assign main_0_D_enable_b = 1'd0;
assign main_0_D_address_b = 6'd0;
assign main_0_C_write_enable_a = 1'd0;
assign main_0_C_in_a = 0;
assign main_0_C_byteena_a = 1'd1;
always @(*) begin
	main_0_C_enable_a = 1'd0;
	/* kernel_2mm: %25*/
	/*   %30 = load i32* %scevgep, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__25_21)) begin
		main_0_C_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_C_address_a = 6'd0;
	/* kernel_2mm: %25*/
	/*   %30 = load i32* %scevgep, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kernel_2mm_BB__25_21)) begin
		main_0_C_address_a = (kernel_2mm_25_scevgep >>> 3'd2);
	end
end
assign main_0_C_write_enable_b = 1'd0;
assign main_0_C_in_b = 0;
assign main_0_C_byteena_b = 1'd1;
assign main_0_C_enable_b = 1'd0;
assign main_0_C_address_b = 6'd0;

endmodule
