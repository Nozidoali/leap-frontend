//----------------------------------------------------------------------------
// LegUp High-Level Synthesis Tool Version 5.0 (http://legup.org)
// Copyright (c) 2009-23 University of Toronto. All Rights Reserved.
// For research and academic purposes only. Commercial use is prohibited.
// Please report bugs at: http://legup.org/bugs
// Please email questions to: legup@eecg.toronto.edu
// Date: Sun Oct  6 18:22:34 2024
// ----------------------------------------------------------------------------
`timescale 1 ns / 1 ns
module gemver
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
	arg_A,
	arg_u1,
	arg_v1,
	arg_u2,
	arg_v2,
	arg_w,
	arg_x,
	arg_y,
	arg_z,
	main_0_u1_write_enable_a,
	main_0_u1_in_a,
	main_0_u1_byteena_a,
	main_0_u1_enable_a,
	main_0_u1_address_a,
	main_0_u1_out_a,
	main_0_u1_write_enable_b,
	main_0_u1_in_b,
	main_0_u1_byteena_b,
	main_0_u1_enable_b,
	main_0_u1_address_b,
	main_0_u1_out_b,
	main_0_v1_write_enable_a,
	main_0_v1_in_a,
	main_0_v1_byteena_a,
	main_0_v1_enable_a,
	main_0_v1_address_a,
	main_0_v1_out_a,
	main_0_v1_write_enable_b,
	main_0_v1_in_b,
	main_0_v1_byteena_b,
	main_0_v1_enable_b,
	main_0_v1_address_b,
	main_0_v1_out_b,
	main_0_u2_write_enable_a,
	main_0_u2_in_a,
	main_0_u2_byteena_a,
	main_0_u2_enable_a,
	main_0_u2_address_a,
	main_0_u2_out_a,
	main_0_u2_write_enable_b,
	main_0_u2_in_b,
	main_0_u2_byteena_b,
	main_0_u2_enable_b,
	main_0_u2_address_b,
	main_0_u2_out_b,
	main_0_v2_write_enable_a,
	main_0_v2_in_a,
	main_0_v2_byteena_a,
	main_0_v2_enable_a,
	main_0_v2_address_a,
	main_0_v2_out_a,
	main_0_v2_write_enable_b,
	main_0_v2_in_b,
	main_0_v2_byteena_b,
	main_0_v2_enable_b,
	main_0_v2_address_b,
	main_0_v2_out_b,
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
	main_0_x_write_enable_a,
	main_0_x_in_a,
	main_0_x_byteena_a,
	main_0_x_enable_a,
	main_0_x_address_a,
	main_0_x_out_a,
	main_0_x_write_enable_b,
	main_0_x_in_b,
	main_0_x_byteena_b,
	main_0_x_enable_b,
	main_0_x_address_b,
	main_0_x_out_b,
	main_0_y_write_enable_a,
	main_0_y_in_a,
	main_0_y_byteena_a,
	main_0_y_enable_a,
	main_0_y_address_a,
	main_0_y_out_a,
	main_0_y_write_enable_b,
	main_0_y_in_b,
	main_0_y_byteena_b,
	main_0_y_enable_b,
	main_0_y_address_b,
	main_0_y_out_b,
	main_0_z_write_enable_a,
	main_0_z_in_a,
	main_0_z_byteena_a,
	main_0_z_enable_a,
	main_0_z_address_a,
	main_0_z_out_a,
	main_0_z_write_enable_b,
	main_0_z_in_b,
	main_0_z_byteena_b,
	main_0_z_enable_b,
	main_0_z_address_b,
	main_0_z_out_b,
	main_0_w_write_enable_a,
	main_0_w_in_a,
	main_0_w_byteena_a,
	main_0_w_enable_a,
	main_0_w_address_a,
	main_0_w_out_a,
	main_0_w_write_enable_b,
	main_0_w_in_b,
	main_0_w_byteena_b,
	main_0_w_enable_b,
	main_0_w_address_b,
	main_0_w_out_b
);

parameter [5:0] LEGUP_0 = 6'd0;
parameter [5:0] LEGUP_F_gemver_BB__1_1 = 6'd1;
parameter [5:0] LEGUP_F_gemver_BB__3_2 = 6'd2;
parameter [5:0] LEGUP_F_gemver_BB__3_3 = 6'd3;
parameter [5:0] LEGUP_F_gemver_BB__3_4 = 6'd4;
parameter [5:0] LEGUP_F_gemver_BB__3_5 = 6'd5;
parameter [5:0] LEGUP_F_gemver_BB__3_6 = 6'd6;
parameter [5:0] LEGUP_F_gemver_BB__15_7 = 6'd7;
parameter [5:0] LEGUP_F_gemver_BB__15_8 = 6'd8;
parameter [5:0] LEGUP_F_gemver_BB_preheader2preheaderpreheader_9 = 6'd9;
parameter [5:0] LEGUP_F_gemver_BB_preheader2preheader_10 = 6'd10;
parameter [5:0] LEGUP_F_gemver_BB_preheader2preheader_11 = 6'd11;
parameter [5:0] LEGUP_F_gemver_BB__18_12 = 6'd12;
parameter [5:0] LEGUP_F_gemver_BB__18_13 = 6'd13;
parameter [5:0] LEGUP_F_gemver_BB__18_14 = 6'd14;
parameter [5:0] LEGUP_F_gemver_BB__18_15 = 6'd15;
parameter [5:0] LEGUP_F_gemver_BB__18_16 = 6'd16;
parameter [5:0] LEGUP_F_gemver_BB_preheader2_17 = 6'd17;
parameter [5:0] LEGUP_F_gemver_BB_preheader2_18 = 6'd18;
parameter [5:0] LEGUP_F_gemver_BB_preheader1preheader_19 = 6'd19;
parameter [5:0] LEGUP_F_gemver_BB_preheader1_20 = 6'd20;
parameter [5:0] LEGUP_F_gemver_BB_preheader1_21 = 6'd21;
parameter [5:0] LEGUP_F_gemver_BB_preheader1_22 = 6'd22;
parameter [5:0] LEGUP_F_gemver_BB_preheaderpreheaderpreheader_23 = 6'd23;
parameter [5:0] LEGUP_F_gemver_BB_preheaderpreheader_24 = 6'd24;
parameter [5:0] LEGUP_F_gemver_BB_preheaderpreheader_25 = 6'd25;
parameter [5:0] LEGUP_F_gemver_BB__34_26 = 6'd26;
parameter [5:0] LEGUP_F_gemver_BB__34_27 = 6'd27;
parameter [5:0] LEGUP_F_gemver_BB__34_28 = 6'd28;
parameter [5:0] LEGUP_F_gemver_BB__34_29 = 6'd29;
parameter [5:0] LEGUP_F_gemver_BB__34_30 = 6'd30;
parameter [5:0] LEGUP_F_gemver_BB_preheader_31 = 6'd31;
parameter [5:0] LEGUP_F_gemver_BB_preheader_32 = 6'd32;
parameter [5:0] LEGUP_F_gemver_BB__43_33 = 6'd33;

input  clk;
input  clk2x;
input  clk1x_follower;
input  reset;
input  memory_controller_waitrequest;
input  start;
output reg  finish;
input [31:0] arg_alpha;
input [31:0] arg_beta;
input [31:0] arg_A;
input [31:0] arg_u1;
input [31:0] arg_v1;
input [31:0] arg_u2;
input [31:0] arg_v2;
input [31:0] arg_w;
input [31:0] arg_x;
input [31:0] arg_y;
input [31:0] arg_z;
output  main_0_u1_write_enable_a;
output [31:0] main_0_u1_in_a;
output  main_0_u1_byteena_a;
output reg  main_0_u1_enable_a;
output reg [4:0] main_0_u1_address_a;
input [31:0] main_0_u1_out_a;
output  main_0_u1_write_enable_b;
output [31:0] main_0_u1_in_b;
output  main_0_u1_byteena_b;
output  main_0_u1_enable_b;
output [4:0] main_0_u1_address_b;
input [31:0] main_0_u1_out_b;
output  main_0_v1_write_enable_a;
output [31:0] main_0_v1_in_a;
output  main_0_v1_byteena_a;
output reg  main_0_v1_enable_a;
output reg [4:0] main_0_v1_address_a;
input [31:0] main_0_v1_out_a;
output  main_0_v1_write_enable_b;
output [31:0] main_0_v1_in_b;
output  main_0_v1_byteena_b;
output  main_0_v1_enable_b;
output [4:0] main_0_v1_address_b;
input [31:0] main_0_v1_out_b;
output  main_0_u2_write_enable_a;
output [31:0] main_0_u2_in_a;
output  main_0_u2_byteena_a;
output reg  main_0_u2_enable_a;
output reg [4:0] main_0_u2_address_a;
input [31:0] main_0_u2_out_a;
output  main_0_u2_write_enable_b;
output [31:0] main_0_u2_in_b;
output  main_0_u2_byteena_b;
output  main_0_u2_enable_b;
output [4:0] main_0_u2_address_b;
input [31:0] main_0_u2_out_b;
output  main_0_v2_write_enable_a;
output [31:0] main_0_v2_in_a;
output  main_0_v2_byteena_a;
output reg  main_0_v2_enable_a;
output reg [4:0] main_0_v2_address_a;
input [31:0] main_0_v2_out_a;
output  main_0_v2_write_enable_b;
output [31:0] main_0_v2_in_b;
output  main_0_v2_byteena_b;
output  main_0_v2_enable_b;
output [4:0] main_0_v2_address_b;
input [31:0] main_0_v2_out_b;
output reg  main_0_A_write_enable_a;
output reg [31:0] main_0_A_in_a;
output  main_0_A_byteena_a;
output reg  main_0_A_enable_a;
output reg [9:0] main_0_A_address_a;
input [31:0] main_0_A_out_a;
output  main_0_A_write_enable_b;
output [31:0] main_0_A_in_b;
output  main_0_A_byteena_b;
output  main_0_A_enable_b;
output [9:0] main_0_A_address_b;
input [31:0] main_0_A_out_b;
output reg  main_0_x_write_enable_a;
output reg [31:0] main_0_x_in_a;
output  main_0_x_byteena_a;
output reg  main_0_x_enable_a;
output reg [4:0] main_0_x_address_a;
input [31:0] main_0_x_out_a;
output  main_0_x_write_enable_b;
output [31:0] main_0_x_in_b;
output  main_0_x_byteena_b;
output  main_0_x_enable_b;
output [4:0] main_0_x_address_b;
input [31:0] main_0_x_out_b;
output  main_0_y_write_enable_a;
output [31:0] main_0_y_in_a;
output  main_0_y_byteena_a;
output reg  main_0_y_enable_a;
output reg [4:0] main_0_y_address_a;
input [31:0] main_0_y_out_a;
output  main_0_y_write_enable_b;
output [31:0] main_0_y_in_b;
output  main_0_y_byteena_b;
output  main_0_y_enable_b;
output [4:0] main_0_y_address_b;
input [31:0] main_0_y_out_b;
output  main_0_z_write_enable_a;
output [31:0] main_0_z_in_a;
output  main_0_z_byteena_a;
output reg  main_0_z_enable_a;
output reg [4:0] main_0_z_address_a;
input [31:0] main_0_z_out_a;
output  main_0_z_write_enable_b;
output [31:0] main_0_z_in_b;
output  main_0_z_byteena_b;
output  main_0_z_enable_b;
output [4:0] main_0_z_address_b;
input [31:0] main_0_z_out_b;
output reg  main_0_w_write_enable_a;
output reg [31:0] main_0_w_in_a;
output  main_0_w_byteena_a;
output reg  main_0_w_enable_a;
output reg [4:0] main_0_w_address_a;
input [31:0] main_0_w_out_a;
output  main_0_w_write_enable_b;
output [31:0] main_0_w_in_b;
output  main_0_w_byteena_b;
output  main_0_w_enable_b;
output [4:0] main_0_w_address_b;
input [31:0] main_0_w_out_b;
reg [5:0] cur_state;
reg [5:0] next_state;
reg [31:0] arg_alpha_reg;
reg [31:0] arg_beta_reg;
reg [31:0] arg_A_reg;
reg [31:0] arg_u1_reg;
reg [31:0] arg_v1_reg;
reg [31:0] arg_u2_reg;
reg [31:0] arg_v2_reg;
reg [31:0] arg_w_reg;
reg [31:0] arg_x_reg;
reg [31:0] arg_y_reg;
reg [31:0] arg_z_reg;
reg  fsm_stall;
reg [5:0] gemver_1_i011;
reg [5:0] gemver_1_i011_reg;
reg [11:0] gemver_1_2;
reg [11:0] gemver_1_2_reg;
reg [31:0] gemver_1_scevgep22;
reg [31:0] gemver_1_scevgep22_reg;
reg [31:0] gemver_1_scevgep21;
reg [31:0] gemver_1_scevgep21_reg;
reg [31:0] gemver_3_j010;
reg [31:0] gemver_3_j010_reg;
reg [31:0] gemver_3_4;
reg [31:0] gemver_3_4_reg;
reg [31:0] gemver_3_scevgep18;
reg [31:0] gemver_3_scevgep18_reg;
reg [31:0] gemver_3_scevgep17;
reg [31:0] gemver_3_scevgep16;
reg [31:0] gemver_3_5;
reg [31:0] gemver_3_6;
reg [31:0] gemver_3_7;
reg [31:0] gemver_3_8;
reg [31:0] gemver_3_9;
reg [31:0] gemver_3_9_reg;
reg [31:0] gemver_3_10;
reg [31:0] gemver_3_11;
reg [31:0] gemver_3_12;
reg [31:0] gemver_3_12_reg;
reg [31:0] gemver_3_13;
reg [31:0] gemver_3_14;
reg [31:0] gemver_3_14_reg;
reg  gemver_3_exitcond25;
reg  gemver_3_exitcond25_reg;
reg [6:0] gemver_15_16;
reg [6:0] gemver_15_16_reg;
reg  gemver_15_exitcond29;
reg [5:0] gemver_preheader2preheader_i19;
reg [5:0] gemver_preheader2preheader_i19_reg;
reg [31:0] gemver_preheader2preheader_scevgep14;
reg [31:0] gemver_preheader2preheader_scevgep14_reg;
reg [31:0] gemver_preheader2preheader_17;
reg [31:0] gemver_18_tmp08;
reg [31:0] gemver_18_tmp08_reg;
reg [31:0] gemver_18_j17;
reg [31:0] gemver_18_j17_reg;
reg [31:0] gemver_18_19;
reg [31:0] gemver_18_20;
reg [31:0] gemver_18_20_reg;
reg [31:0] gemver_18_scevgep11;
reg [31:0] gemver_18_scevgep10;
reg [31:0] gemver_18_21;
reg [31:0] gemver_18_22;
reg [31:0] gemver_18_23;
reg [31:0] gemver_18_23_reg;
reg [31:0] gemver_18_24;
reg [31:0] gemver_18_25;
reg [31:0] gemver_18_26;
reg [31:0] gemver_18_26_reg;
reg  gemver_18_exitcond16;
reg  gemver_18_exitcond16_reg;
reg [31:0] gemver_preheader2_lcssa1;
reg [31:0] gemver_preheader2_lcssa1_reg;
reg [6:0] gemver_preheader2_27;
reg [6:0] gemver_preheader2_27_reg;
reg  gemver_preheader2_exitcond21;
reg [5:0] gemver_preheader1_i26;
reg [5:0] gemver_preheader1_i26_reg;
reg [31:0] gemver_preheader1_scevgep8;
reg [31:0] gemver_preheader1_scevgep8_reg;
reg [31:0] gemver_preheader1_scevgep7;
reg [31:0] gemver_preheader1_28;
reg [31:0] gemver_preheader1_29;
reg [31:0] gemver_preheader1_30;
reg [6:0] gemver_preheader1_31;
reg [6:0] gemver_preheader1_31_reg;
reg  gemver_preheader1_exitcond;
reg  gemver_preheader1_exitcond_reg;
reg [5:0] gemver_preheaderpreheader_i35;
reg [5:0] gemver_preheaderpreheader_i35_reg;
reg [11:0] gemver_preheaderpreheader_32;
reg [11:0] gemver_preheaderpreheader_32_reg;
reg [31:0] gemver_preheaderpreheader_scevgep5;
reg [31:0] gemver_preheaderpreheader_scevgep5_reg;
reg [31:0] gemver_preheaderpreheader_33;
reg [31:0] gemver_34_tmp104;
reg [31:0] gemver_34_tmp104_reg;
reg [31:0] gemver_34_j23;
reg [31:0] gemver_34_j23_reg;
reg [31:0] gemver_34_35;
reg [31:0] gemver_34_35_reg;
reg [31:0] gemver_34_scevgep3;
reg [31:0] gemver_34_scevgep;
reg [31:0] gemver_34_36;
reg [31:0] gemver_34_37;
reg [31:0] gemver_34_38;
reg [31:0] gemver_34_38_reg;
reg [31:0] gemver_34_39;
reg [31:0] gemver_34_40;
reg [31:0] gemver_34_41;
reg [31:0] gemver_34_41_reg;
reg  gemver_34_exitcond3;
reg  gemver_34_exitcond3_reg;
reg [31:0] gemver_preheader_lcssa;
reg [31:0] gemver_preheader_lcssa_reg;
reg [6:0] gemver_preheader_42;
reg [6:0] gemver_preheader_42_reg;
reg  gemver_preheader_exitcond7;
reg  legup_mult_1_unsigned_32_32_1_0_clock;
reg  legup_mult_1_unsigned_32_32_1_0_aclr;
reg  legup_mult_1_unsigned_32_32_1_0_sum;
reg  legup_mult_1_unsigned_32_32_1_0_clken;
reg [31:0] legup_mult_1_unsigned_32_32_1_0_dataa;
reg [31:0] legup_mult_1_unsigned_32_32_1_0_datab;
wire [63:0] legup_mult_1_unsigned_32_32_1_0_result;
reg [63:0] legup_mult_gemver_3_8_out_actual;
reg [31:0] legup_mult_gemver_3_8_out;
reg  legup_mult_gemver_3_8_en;
reg  legup_mult_1_unsigned_32_32_1_1_clock;
reg  legup_mult_1_unsigned_32_32_1_1_aclr;
reg  legup_mult_1_unsigned_32_32_1_1_sum;
reg  legup_mult_1_unsigned_32_32_1_1_clken;
reg [31:0] legup_mult_1_unsigned_32_32_1_1_dataa;
reg [31:0] legup_mult_1_unsigned_32_32_1_1_datab;
wire [63:0] legup_mult_1_unsigned_32_32_1_1_result;
reg [63:0] legup_mult_gemver_3_12_out_actual;
reg [31:0] legup_mult_gemver_3_12_out;
reg  legup_mult_gemver_3_12_en;
reg  legup_mult_1_unsigned_32_32_1_2_clock;
reg  legup_mult_1_unsigned_32_32_1_2_aclr;
reg  legup_mult_1_unsigned_32_32_1_2_sum;
reg  legup_mult_1_unsigned_32_32_1_2_clken;
reg [31:0] legup_mult_1_unsigned_32_32_1_2_dataa;
reg [31:0] legup_mult_1_unsigned_32_32_1_2_datab;
wire [63:0] legup_mult_1_unsigned_32_32_1_2_result;
reg [63:0] legup_mult_gemver_18_22_out_actual;
reg [31:0] legup_mult_gemver_18_22_out;
reg  legup_mult_gemver_18_22_en;
reg  legup_mult_1_unsigned_32_32_1_3_clock;
reg  legup_mult_1_unsigned_32_32_1_3_aclr;
reg  legup_mult_1_unsigned_32_32_1_3_sum;
reg  legup_mult_1_unsigned_32_32_1_3_clken;
reg [31:0] legup_mult_1_unsigned_32_32_1_3_dataa;
reg [31:0] legup_mult_1_unsigned_32_32_1_3_datab;
wire [63:0] legup_mult_1_unsigned_32_32_1_3_result;
reg [63:0] legup_mult_gemver_18_24_out_actual;
reg [31:0] legup_mult_gemver_18_24_out;
reg  legup_mult_gemver_18_24_en;
reg  legup_mult_1_unsigned_32_32_1_4_clock;
reg  legup_mult_1_unsigned_32_32_1_4_aclr;
reg  legup_mult_1_unsigned_32_32_1_4_sum;
reg  legup_mult_1_unsigned_32_32_1_4_clken;
reg [31:0] legup_mult_1_unsigned_32_32_1_4_dataa;
reg [31:0] legup_mult_1_unsigned_32_32_1_4_datab;
wire [63:0] legup_mult_1_unsigned_32_32_1_4_result;
reg [63:0] legup_mult_gemver_34_37_out_actual;
reg [31:0] legup_mult_gemver_34_37_out;
reg  legup_mult_gemver_34_37_en;
reg  legup_mult_1_unsigned_32_32_1_5_clock;
reg  legup_mult_1_unsigned_32_32_1_5_aclr;
reg  legup_mult_1_unsigned_32_32_1_5_sum;
reg  legup_mult_1_unsigned_32_32_1_5_clken;
reg [31:0] legup_mult_1_unsigned_32_32_1_5_dataa;
reg [31:0] legup_mult_1_unsigned_32_32_1_5_datab;
wire [63:0] legup_mult_1_unsigned_32_32_1_5_result;
reg [63:0] legup_mult_gemver_34_39_out_actual;
reg [31:0] legup_mult_gemver_34_39_out;
reg  legup_mult_gemver_34_39_en;

/*   %8 = mul nsw i32 %6, %7, !MSB !6, !LSB !3, !extendFrom !6*/
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

/*   %12 = mul nsw i32 %10, %11, !MSB !6, !LSB !3, !extendFrom !6*/
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

/*   %22 = mul nsw i32 %21, %beta, !MSB !6, !LSB !3, !extendFrom !6*/
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

/*   %24 = mul nsw i32 %22, %23, !MSB !6, !LSB !3, !extendFrom !6*/
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

/*   %37 = mul nsw i32 %36, %alpha, !MSB !6, !LSB !3, !extendFrom !6*/
legup_mult_1 legup_mult_1_unsigned_32_32_1_4 (
	.clock (legup_mult_1_unsigned_32_32_1_4_clock),
	.aclr (legup_mult_1_unsigned_32_32_1_4_aclr),
	.sum (legup_mult_1_unsigned_32_32_1_4_sum),
	.clken (legup_mult_1_unsigned_32_32_1_4_clken),
	.dataa (legup_mult_1_unsigned_32_32_1_4_dataa),
	.datab (legup_mult_1_unsigned_32_32_1_4_datab),
	.result (legup_mult_1_unsigned_32_32_1_4_result)
);

/*
defparam
	legup_mult_1_unsigned_32_32_1_4.widtha = 32,
	legup_mult_1_unsigned_32_32_1_4.widthb = 32,
	legup_mult_1_unsigned_32_32_1_4.widthp = 64,
	legup_mult_1_unsigned_32_32_1_4.representation = "UNSIGNED";
*/

/*   %39 = mul nsw i32 %37, %38, !MSB !6, !LSB !3, !extendFrom !6*/
legup_mult_1 legup_mult_1_unsigned_32_32_1_5 (
	.clock (legup_mult_1_unsigned_32_32_1_5_clock),
	.aclr (legup_mult_1_unsigned_32_32_1_5_aclr),
	.sum (legup_mult_1_unsigned_32_32_1_5_sum),
	.clken (legup_mult_1_unsigned_32_32_1_5_clken),
	.dataa (legup_mult_1_unsigned_32_32_1_5_dataa),
	.datab (legup_mult_1_unsigned_32_32_1_5_datab),
	.result (legup_mult_1_unsigned_32_32_1_5_result)
);

/*
defparam
	legup_mult_1_unsigned_32_32_1_5.widtha = 32,
	legup_mult_1_unsigned_32_32_1_5.widthb = 32,
	legup_mult_1_unsigned_32_32_1_5.widthp = 64,
	legup_mult_1_unsigned_32_32_1_5.representation = "UNSIGNED";
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
		next_state = LEGUP_F_gemver_BB__1_1;
LEGUP_F_gemver_BB__15_7:
		next_state = LEGUP_F_gemver_BB__15_8;
LEGUP_F_gemver_BB__15_8:
	if ((fsm_stall == 1'd0) && (gemver_15_exitcond29 == 1'd1))
		next_state = LEGUP_F_gemver_BB_preheader2preheaderpreheader_9;
	else if ((fsm_stall == 1'd0) && (gemver_15_exitcond29 == 1'd0))
		next_state = LEGUP_F_gemver_BB__1_1;
LEGUP_F_gemver_BB__18_12:
		next_state = LEGUP_F_gemver_BB__18_13;
LEGUP_F_gemver_BB__18_13:
		next_state = LEGUP_F_gemver_BB__18_14;
LEGUP_F_gemver_BB__18_14:
		next_state = LEGUP_F_gemver_BB__18_15;
LEGUP_F_gemver_BB__18_15:
		next_state = LEGUP_F_gemver_BB__18_16;
LEGUP_F_gemver_BB__18_16:
	if ((fsm_stall == 1'd0) && (gemver_18_exitcond16_reg == 1'd1))
		next_state = LEGUP_F_gemver_BB_preheader2_17;
	else if ((fsm_stall == 1'd0) && (gemver_18_exitcond16_reg == 1'd0))
		next_state = LEGUP_F_gemver_BB__18_12;
LEGUP_F_gemver_BB__1_1:
		next_state = LEGUP_F_gemver_BB__3_2;
LEGUP_F_gemver_BB__34_26:
		next_state = LEGUP_F_gemver_BB__34_27;
LEGUP_F_gemver_BB__34_27:
		next_state = LEGUP_F_gemver_BB__34_28;
LEGUP_F_gemver_BB__34_28:
		next_state = LEGUP_F_gemver_BB__34_29;
LEGUP_F_gemver_BB__34_29:
		next_state = LEGUP_F_gemver_BB__34_30;
LEGUP_F_gemver_BB__34_30:
	if ((fsm_stall == 1'd0) && (gemver_34_exitcond3_reg == 1'd1))
		next_state = LEGUP_F_gemver_BB_preheader_31;
	else if ((fsm_stall == 1'd0) && (gemver_34_exitcond3_reg == 1'd0))
		next_state = LEGUP_F_gemver_BB__34_26;
LEGUP_F_gemver_BB__3_2:
		next_state = LEGUP_F_gemver_BB__3_3;
LEGUP_F_gemver_BB__3_3:
		next_state = LEGUP_F_gemver_BB__3_4;
LEGUP_F_gemver_BB__3_4:
		next_state = LEGUP_F_gemver_BB__3_5;
LEGUP_F_gemver_BB__3_5:
		next_state = LEGUP_F_gemver_BB__3_6;
LEGUP_F_gemver_BB__3_6:
	if ((fsm_stall == 1'd0) && (gemver_3_exitcond25_reg == 1'd1))
		next_state = LEGUP_F_gemver_BB__15_7;
	else if ((fsm_stall == 1'd0) && (gemver_3_exitcond25_reg == 1'd0))
		next_state = LEGUP_F_gemver_BB__3_2;
LEGUP_F_gemver_BB__43_33:
		next_state = LEGUP_0;
LEGUP_F_gemver_BB_preheader1_20:
		next_state = LEGUP_F_gemver_BB_preheader1_21;
LEGUP_F_gemver_BB_preheader1_21:
		next_state = LEGUP_F_gemver_BB_preheader1_22;
LEGUP_F_gemver_BB_preheader1_22:
	if ((fsm_stall == 1'd0) && (gemver_preheader1_exitcond_reg == 1'd1))
		next_state = LEGUP_F_gemver_BB_preheaderpreheaderpreheader_23;
	else if ((fsm_stall == 1'd0) && (gemver_preheader1_exitcond_reg == 1'd0))
		next_state = LEGUP_F_gemver_BB_preheader1_20;
LEGUP_F_gemver_BB_preheader1preheader_19:
		next_state = LEGUP_F_gemver_BB_preheader1_20;
LEGUP_F_gemver_BB_preheader2_17:
		next_state = LEGUP_F_gemver_BB_preheader2_18;
LEGUP_F_gemver_BB_preheader2_18:
	if ((fsm_stall == 1'd0) && (gemver_preheader2_exitcond21 == 1'd1))
		next_state = LEGUP_F_gemver_BB_preheader1preheader_19;
	else if ((fsm_stall == 1'd0) && (gemver_preheader2_exitcond21 == 1'd0))
		next_state = LEGUP_F_gemver_BB_preheader2preheader_10;
LEGUP_F_gemver_BB_preheader2preheader_10:
		next_state = LEGUP_F_gemver_BB_preheader2preheader_11;
LEGUP_F_gemver_BB_preheader2preheader_11:
		next_state = LEGUP_F_gemver_BB__18_12;
LEGUP_F_gemver_BB_preheader2preheaderpreheader_9:
		next_state = LEGUP_F_gemver_BB_preheader2preheader_10;
LEGUP_F_gemver_BB_preheader_31:
		next_state = LEGUP_F_gemver_BB_preheader_32;
LEGUP_F_gemver_BB_preheader_32:
	if ((fsm_stall == 1'd0) && (gemver_preheader_exitcond7 == 1'd1))
		next_state = LEGUP_F_gemver_BB__43_33;
	else if ((fsm_stall == 1'd0) && (gemver_preheader_exitcond7 == 1'd0))
		next_state = LEGUP_F_gemver_BB_preheaderpreheader_24;
LEGUP_F_gemver_BB_preheaderpreheader_24:
		next_state = LEGUP_F_gemver_BB_preheaderpreheader_25;
LEGUP_F_gemver_BB_preheaderpreheader_25:
		next_state = LEGUP_F_gemver_BB__34_26;
LEGUP_F_gemver_BB_preheaderpreheaderpreheader_23:
		next_state = LEGUP_F_gemver_BB_preheaderpreheader_24;
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
		arg_A_reg <= arg_A;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_u1_reg <= arg_u1;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_v1_reg <= arg_v1;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_u2_reg <= arg_u2;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_v2_reg <= arg_v2;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_w_reg <= arg_w;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_x_reg <= arg_x;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_y_reg <= arg_y;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_z_reg <= arg_z;
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
	/* gemver: %1*/
	/*   %i.011 = phi i32 [ 0, %0 ], [ %16, %15 ], !MSB !4, !LSB !3, !extendFrom !4*/
	if ((((cur_state == LEGUP_0) & (fsm_stall == 1'd0)) & (start == 1'd1))) begin
		gemver_1_i011 = 32'd0;
	end
	/* gemver: %1*/
	/*   %i.011 = phi i32 [ 0, %0 ], [ %16, %15 ], !MSB !4, !LSB !3, !extendFrom !4*/
	else /* if ((((cur_state == LEGUP_F_gemver_BB__15_8) & (fsm_stall == 1'd0)) & (gemver_15_exitcond29 == 1'd0))) */ begin
		gemver_1_i011 = gemver_15_16_reg;
	end
end
always @(posedge clk) begin
	/* gemver: %1*/
	/*   %i.011 = phi i32 [ 0, %0 ], [ %16, %15 ], !MSB !4, !LSB !3, !extendFrom !4*/
	if ((((cur_state == LEGUP_0) & (fsm_stall == 1'd0)) & (start == 1'd1))) begin
		gemver_1_i011_reg <= gemver_1_i011;
	end
	/* gemver: %1*/
	/*   %i.011 = phi i32 [ 0, %0 ], [ %16, %15 ], !MSB !4, !LSB !3, !extendFrom !4*/
	if ((((cur_state == LEGUP_F_gemver_BB__15_8) & (fsm_stall == 1'd0)) & (gemver_15_exitcond29 == 1'd0))) begin
		gemver_1_i011_reg <= gemver_1_i011;
	end
end
always @(*) begin
	/* gemver: %1*/
	/*   %2 = mul i32 %i.011, 32, !MSB !5, !LSB !4, !extendFrom !5*/
		gemver_1_2 = ({6'd0,gemver_1_i011_reg} * 32'd32);
end
always @(posedge clk) begin
	/* gemver: %1*/
	/*   %2 = mul i32 %i.011, 32, !MSB !5, !LSB !4, !extendFrom !5*/
	if ((cur_state == LEGUP_F_gemver_BB__1_1)) begin
		gemver_1_2_reg <= gemver_1_2;
	end
end
always @(*) begin
	/* gemver: %1*/
	/*   %scevgep22 = getelementptr i32* %u1, i32 %i.011, !MSB !2, !LSB !3, !extendFrom !2*/
		gemver_1_scevgep22 = (arg_u1_reg + (4 * {26'd0,gemver_1_i011_reg}));
end
always @(posedge clk) begin
	/* gemver: %1*/
	/*   %scevgep22 = getelementptr i32* %u1, i32 %i.011, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB__1_1)) begin
		gemver_1_scevgep22_reg <= gemver_1_scevgep22;
	end
end
always @(*) begin
	/* gemver: %1*/
	/*   %scevgep21 = getelementptr i32* %u2, i32 %i.011, !MSB !2, !LSB !3, !extendFrom !2*/
		gemver_1_scevgep21 = (arg_u2_reg + (4 * {26'd0,gemver_1_i011_reg}));
end
always @(posedge clk) begin
	/* gemver: %1*/
	/*   %scevgep21 = getelementptr i32* %u2, i32 %i.011, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB__1_1)) begin
		gemver_1_scevgep21_reg <= gemver_1_scevgep21;
	end
end
always @(*) begin
	/* gemver: %3*/
	/*   %j.010 = phi i32 [ 0, %1 ], [ %14, %3 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_gemver_BB__1_1) & (fsm_stall == 1'd0))) begin
		gemver_3_j010 = 32'd0;
	end
	/* gemver: %3*/
	/*   %j.010 = phi i32 [ 0, %1 ], [ %14, %3 ], !MSB !6, !LSB !3, !extendFrom !6*/
	else /* if ((((cur_state == LEGUP_F_gemver_BB__3_6) & (fsm_stall == 1'd0)) & (gemver_3_exitcond25_reg == 1'd0))) */ begin
		gemver_3_j010 = gemver_3_14_reg;
	end
end
always @(posedge clk) begin
	/* gemver: %3*/
	/*   %j.010 = phi i32 [ 0, %1 ], [ %14, %3 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_gemver_BB__1_1) & (fsm_stall == 1'd0))) begin
		gemver_3_j010_reg <= gemver_3_j010;
	end
	/* gemver: %3*/
	/*   %j.010 = phi i32 [ 0, %1 ], [ %14, %3 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_gemver_BB__3_6) & (fsm_stall == 1'd0)) & (gemver_3_exitcond25_reg == 1'd0))) begin
		gemver_3_j010_reg <= gemver_3_j010;
	end
end
always @(*) begin
	/* gemver: %3*/
	/*   %4 = add i32 %2, %j.010, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_3_4 = ({20'd0,gemver_1_2_reg} + gemver_3_j010_reg);
end
always @(posedge clk) begin
	/* gemver: %3*/
	/*   %4 = add i32 %2, %j.010, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__3_2)) begin
		gemver_3_4_reg <= gemver_3_4;
	end
end
always @(*) begin
	/* gemver: %3*/
	/*   %scevgep18 = getelementptr i32* %A, i32 %4, !MSB !2, !LSB !3, !extendFrom !2*/
		gemver_3_scevgep18 = (arg_A_reg + (4 * gemver_3_4_reg));
end
always @(posedge clk) begin
	/* gemver: %3*/
	/*   %scevgep18 = getelementptr i32* %A, i32 %4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB__3_3)) begin
		gemver_3_scevgep18_reg <= gemver_3_scevgep18;
	end
end
always @(*) begin
	/* gemver: %3*/
	/*   %scevgep17 = getelementptr i32* %v1, i32 %j.010, !MSB !2, !LSB !3, !extendFrom !2*/
		gemver_3_scevgep17 = (arg_v1_reg + (4 * gemver_3_j010_reg));
end
always @(*) begin
	/* gemver: %3*/
	/*   %scevgep16 = getelementptr i32* %v2, i32 %j.010, !MSB !2, !LSB !3, !extendFrom !2*/
		gemver_3_scevgep16 = (arg_v2_reg + (4 * gemver_3_j010_reg));
end
always @(*) begin
	/* gemver: %3*/
	/*   %5 = load i32* %scevgep18, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_3_5 = main_0_A_out_a;
end
always @(*) begin
	/* gemver: %3*/
	/*   %6 = load i32* %scevgep22, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_3_6 = main_0_u1_out_a;
end
always @(*) begin
	/* gemver: %3*/
	/*   %7 = load i32* %scevgep17, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_3_7 = main_0_v1_out_a;
end
always @(*) begin
	gemver_3_8 = legup_mult_gemver_3_8_out;
end
always @(*) begin
	/* gemver: %3*/
	/*   %9 = add nsw i32 %5, %8, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_3_9 = (gemver_3_5 + gemver_3_8);
end
always @(posedge clk) begin
	/* gemver: %3*/
	/*   %9 = add nsw i32 %5, %8, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__3_4)) begin
		gemver_3_9_reg <= gemver_3_9;
	end
end
always @(*) begin
	/* gemver: %3*/
	/*   %10 = load i32* %scevgep21, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_3_10 = main_0_u2_out_a;
end
always @(*) begin
	/* gemver: %3*/
	/*   %11 = load i32* %scevgep16, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_3_11 = main_0_v2_out_a;
end
always @(*) begin
	gemver_3_12 = legup_mult_gemver_3_12_out;
end
always @(posedge clk) begin
	/* gemver: %3*/
	/*   %12 = mul nsw i32 %10, %11, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__3_4)) begin
		gemver_3_12_reg <= gemver_3_12;
	end
	/* gemver: %3*/
	/*   %12 = mul nsw i32 %10, %11, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__3_4)) begin
		gemver_3_12_reg <= gemver_3_12;
	end
end
always @(*) begin
	/* gemver: %3*/
	/*   %13 = add nsw i32 %9, %12, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_3_13 = (gemver_3_9_reg + gemver_3_12_reg);
end
always @(*) begin
	/* gemver: %3*/
	/*   %14 = add nsw i32 %j.010, 1, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_3_14 = (gemver_3_j010_reg + 32'd1);
end
always @(posedge clk) begin
	/* gemver: %3*/
	/*   %14 = add nsw i32 %j.010, 1, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__3_2)) begin
		gemver_3_14_reg <= gemver_3_14;
	end
end
always @(*) begin
	/* gemver: %3*/
	/*   %exitcond25 = icmp eq i32 %14, 32, !MSB !3, !LSB !3, !extendFrom !3*/
		gemver_3_exitcond25 = (gemver_3_14_reg == 32'd32);
end
always @(posedge clk) begin
	/* gemver: %3*/
	/*   %exitcond25 = icmp eq i32 %14, 32, !MSB !3, !LSB !3, !extendFrom !3*/
	if ((cur_state == LEGUP_F_gemver_BB__3_3)) begin
		gemver_3_exitcond25_reg <= gemver_3_exitcond25;
	end
end
always @(*) begin
	/* gemver: %15*/
	/*   %16 = add nsw i32 %i.011, 1, !MSB !7, !LSB !3, !extendFrom !7*/
		gemver_15_16 = ({1'd0,gemver_1_i011_reg} + 32'd1);
end
always @(posedge clk) begin
	/* gemver: %15*/
	/*   %16 = add nsw i32 %i.011, 1, !MSB !7, !LSB !3, !extendFrom !7*/
	if ((cur_state == LEGUP_F_gemver_BB__15_7)) begin
		gemver_15_16_reg <= gemver_15_16;
	end
end
always @(*) begin
	/* gemver: %15*/
	/*   %exitcond29 = icmp eq i32 %16, 32, !MSB !3, !LSB !3, !extendFrom !3*/
		gemver_15_exitcond29 = (gemver_15_16_reg == 32'd32);
end
always @(*) begin
	/* gemver: %.preheader2.preheader*/
	/*   %i.19 = phi i32 [ %27, %.preheader2 ], [ 0, %.preheader2.preheader.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	if (((cur_state == LEGUP_F_gemver_BB_preheader2preheaderpreheader_9) & (fsm_stall == 1'd0))) begin
		gemver_preheader2preheader_i19 = 32'd0;
	end
	/* gemver: %.preheader2.preheader*/
	/*   %i.19 = phi i32 [ %27, %.preheader2 ], [ 0, %.preheader2.preheader.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	else /* if ((((cur_state == LEGUP_F_gemver_BB_preheader2_18) & (fsm_stall == 1'd0)) & (gemver_preheader2_exitcond21 == 1'd0))) */ begin
		gemver_preheader2preheader_i19 = gemver_preheader2_27_reg;
	end
end
always @(posedge clk) begin
	/* gemver: %.preheader2.preheader*/
	/*   %i.19 = phi i32 [ %27, %.preheader2 ], [ 0, %.preheader2.preheader.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	if (((cur_state == LEGUP_F_gemver_BB_preheader2preheaderpreheader_9) & (fsm_stall == 1'd0))) begin
		gemver_preheader2preheader_i19_reg <= gemver_preheader2preheader_i19;
	end
	/* gemver: %.preheader2.preheader*/
	/*   %i.19 = phi i32 [ %27, %.preheader2 ], [ 0, %.preheader2.preheader.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	if ((((cur_state == LEGUP_F_gemver_BB_preheader2_18) & (fsm_stall == 1'd0)) & (gemver_preheader2_exitcond21 == 1'd0))) begin
		gemver_preheader2preheader_i19_reg <= gemver_preheader2preheader_i19;
	end
end
always @(*) begin
	/* gemver: %.preheader2.preheader*/
	/*   %scevgep14 = getelementptr i32* %x, i32 %i.19, !MSB !2, !LSB !3, !extendFrom !2*/
		gemver_preheader2preheader_scevgep14 = (arg_x_reg + (4 * {26'd0,gemver_preheader2preheader_i19_reg}));
end
always @(posedge clk) begin
	/* gemver: %.preheader2.preheader*/
	/*   %scevgep14 = getelementptr i32* %x, i32 %i.19, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader2preheader_10)) begin
		gemver_preheader2preheader_scevgep14_reg <= gemver_preheader2preheader_scevgep14;
	end
end
always @(*) begin
	/* gemver: %.preheader2.preheader*/
	/*   %17 = load i32* %scevgep14, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_preheader2preheader_17 = main_0_x_out_a;
end
always @(*) begin
	/* gemver: %18*/
	/*   %tmp.08 = phi i32 [ %17, %.preheader2.preheader ], [ %25, %18 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_gemver_BB_preheader2preheader_11) & (fsm_stall == 1'd0))) begin
		gemver_18_tmp08 = gemver_preheader2preheader_17;
	end
	/* gemver: %18*/
	/*   %tmp.08 = phi i32 [ %17, %.preheader2.preheader ], [ %25, %18 ], !MSB !6, !LSB !3, !extendFrom !6*/
	else /* if ((((cur_state == LEGUP_F_gemver_BB__18_16) & (fsm_stall == 1'd0)) & (gemver_18_exitcond16_reg == 1'd0))) */ begin
		gemver_18_tmp08 = gemver_18_25;
	end
end
always @(posedge clk) begin
	/* gemver: %18*/
	/*   %tmp.08 = phi i32 [ %17, %.preheader2.preheader ], [ %25, %18 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_gemver_BB_preheader2preheader_11) & (fsm_stall == 1'd0))) begin
		gemver_18_tmp08_reg <= gemver_18_tmp08;
	end
	/* gemver: %18*/
	/*   %tmp.08 = phi i32 [ %17, %.preheader2.preheader ], [ %25, %18 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_gemver_BB__18_16) & (fsm_stall == 1'd0)) & (gemver_18_exitcond16_reg == 1'd0))) begin
		gemver_18_tmp08_reg <= gemver_18_tmp08;
	end
end
always @(*) begin
	/* gemver: %18*/
	/*   %j.17 = phi i32 [ 0, %.preheader2.preheader ], [ %26, %18 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_gemver_BB_preheader2preheader_11) & (fsm_stall == 1'd0))) begin
		gemver_18_j17 = 32'd0;
	end
	/* gemver: %18*/
	/*   %j.17 = phi i32 [ 0, %.preheader2.preheader ], [ %26, %18 ], !MSB !6, !LSB !3, !extendFrom !6*/
	else /* if ((((cur_state == LEGUP_F_gemver_BB__18_16) & (fsm_stall == 1'd0)) & (gemver_18_exitcond16_reg == 1'd0))) */ begin
		gemver_18_j17 = gemver_18_26_reg;
	end
end
always @(posedge clk) begin
	/* gemver: %18*/
	/*   %j.17 = phi i32 [ 0, %.preheader2.preheader ], [ %26, %18 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_gemver_BB_preheader2preheader_11) & (fsm_stall == 1'd0))) begin
		gemver_18_j17_reg <= gemver_18_j17;
	end
	/* gemver: %18*/
	/*   %j.17 = phi i32 [ 0, %.preheader2.preheader ], [ %26, %18 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_gemver_BB__18_16) & (fsm_stall == 1'd0)) & (gemver_18_exitcond16_reg == 1'd0))) begin
		gemver_18_j17_reg <= gemver_18_j17;
	end
end
always @(*) begin
	/* gemver: %18*/
	/*   %19 = mul i32 %j.17, 32, !MSB !6, !LSB !4, !extendFrom !6*/
		gemver_18_19 = (gemver_18_j17_reg * 32'd32);
end
always @(*) begin
	/* gemver: %18*/
	/*   %20 = add i32 %i.19, %19, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_18_20 = ({26'd0,gemver_preheader2preheader_i19_reg} + gemver_18_19);
end
always @(posedge clk) begin
	/* gemver: %18*/
	/*   %20 = add i32 %i.19, %19, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__18_12)) begin
		gemver_18_20_reg <= gemver_18_20;
	end
end
always @(*) begin
	/* gemver: %18*/
	/*   %scevgep11 = getelementptr i32* %A, i32 %20, !MSB !2, !LSB !3, !extendFrom !2*/
		gemver_18_scevgep11 = (arg_A_reg + (4 * gemver_18_20_reg));
end
always @(*) begin
	/* gemver: %18*/
	/*   %scevgep10 = getelementptr i32* %y, i32 %j.17, !MSB !2, !LSB !3, !extendFrom !2*/
		gemver_18_scevgep10 = (arg_y_reg + (4 * gemver_18_j17_reg));
end
always @(*) begin
	/* gemver: %18*/
	/*   %21 = load i32* %scevgep11, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_18_21 = main_0_A_out_a;
end
always @(*) begin
	gemver_18_22 = legup_mult_gemver_18_22_out;
end
always @(*) begin
	/* gemver: %18*/
	/*   %23 = load i32* %scevgep10, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_18_23 = main_0_y_out_a;
end
always @(posedge clk) begin
	/* gemver: %18*/
	/*   %23 = load i32* %scevgep10, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__18_13)) begin
		gemver_18_23_reg <= gemver_18_23;
	end
end
always @(*) begin
	gemver_18_24 = legup_mult_gemver_18_24_out;
end
always @(*) begin
	/* gemver: %18*/
	/*   %25 = add nsw i32 %tmp.08, %24, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_18_25 = (gemver_18_tmp08_reg + gemver_18_24);
end
always @(*) begin
	/* gemver: %18*/
	/*   %26 = add nsw i32 %j.17, 1, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_18_26 = (gemver_18_j17_reg + 32'd1);
end
always @(posedge clk) begin
	/* gemver: %18*/
	/*   %26 = add nsw i32 %j.17, 1, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__18_12)) begin
		gemver_18_26_reg <= gemver_18_26;
	end
end
always @(*) begin
	/* gemver: %18*/
	/*   %exitcond16 = icmp eq i32 %26, 32, !MSB !3, !LSB !3, !extendFrom !3*/
		gemver_18_exitcond16 = (gemver_18_26_reg == 32'd32);
end
always @(posedge clk) begin
	/* gemver: %18*/
	/*   %exitcond16 = icmp eq i32 %26, 32, !MSB !3, !LSB !3, !extendFrom !3*/
	if ((cur_state == LEGUP_F_gemver_BB__18_13)) begin
		gemver_18_exitcond16_reg <= gemver_18_exitcond16;
	end
end
always @(*) begin
	/* gemver: %.preheader2*/
	/*   %.lcssa1 = phi i32 [ %25, %18 ], !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_preheader2_lcssa1 = gemver_18_25;
end
always @(posedge clk) begin
	/* gemver: %.preheader2*/
	/*   %.lcssa1 = phi i32 [ %25, %18 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_gemver_BB__18_16) & (fsm_stall == 1'd0)) & (gemver_18_exitcond16_reg == 1'd1))) begin
		gemver_preheader2_lcssa1_reg <= gemver_preheader2_lcssa1;
	end
end
always @(*) begin
	/* gemver: %.preheader2*/
	/*   %27 = add nsw i32 %i.19, 1, !MSB !7, !LSB !3, !extendFrom !7*/
		gemver_preheader2_27 = ({1'd0,gemver_preheader2preheader_i19_reg} + 32'd1);
end
always @(posedge clk) begin
	/* gemver: %.preheader2*/
	/*   %27 = add nsw i32 %i.19, 1, !MSB !7, !LSB !3, !extendFrom !7*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader2_17)) begin
		gemver_preheader2_27_reg <= gemver_preheader2_27;
	end
end
always @(*) begin
	/* gemver: %.preheader2*/
	/*   %exitcond21 = icmp eq i32 %27, 32, !MSB !3, !LSB !3, !extendFrom !3*/
		gemver_preheader2_exitcond21 = (gemver_preheader2_27_reg == 32'd32);
end
always @(*) begin
	/* gemver: %.preheader1*/
	/*   %i.26 = phi i32 [ %31, %.preheader1 ], [ 0, %.preheader1.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	if (((cur_state == LEGUP_F_gemver_BB_preheader1preheader_19) & (fsm_stall == 1'd0))) begin
		gemver_preheader1_i26 = 32'd0;
	end
	/* gemver: %.preheader1*/
	/*   %i.26 = phi i32 [ %31, %.preheader1 ], [ 0, %.preheader1.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	else /* if ((((cur_state == LEGUP_F_gemver_BB_preheader1_22) & (fsm_stall == 1'd0)) & (gemver_preheader1_exitcond_reg == 1'd0))) */ begin
		gemver_preheader1_i26 = gemver_preheader1_31_reg;
	end
end
always @(posedge clk) begin
	/* gemver: %.preheader1*/
	/*   %i.26 = phi i32 [ %31, %.preheader1 ], [ 0, %.preheader1.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	if (((cur_state == LEGUP_F_gemver_BB_preheader1preheader_19) & (fsm_stall == 1'd0))) begin
		gemver_preheader1_i26_reg <= gemver_preheader1_i26;
	end
	/* gemver: %.preheader1*/
	/*   %i.26 = phi i32 [ %31, %.preheader1 ], [ 0, %.preheader1.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	if ((((cur_state == LEGUP_F_gemver_BB_preheader1_22) & (fsm_stall == 1'd0)) & (gemver_preheader1_exitcond_reg == 1'd0))) begin
		gemver_preheader1_i26_reg <= gemver_preheader1_i26;
	end
end
always @(*) begin
	/* gemver: %.preheader1*/
	/*   %scevgep8 = getelementptr i32* %x, i32 %i.26, !MSB !2, !LSB !3, !extendFrom !2*/
		gemver_preheader1_scevgep8 = (arg_x_reg + (4 * {26'd0,gemver_preheader1_i26_reg}));
end
always @(posedge clk) begin
	/* gemver: %.preheader1*/
	/*   %scevgep8 = getelementptr i32* %x, i32 %i.26, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader1_20)) begin
		gemver_preheader1_scevgep8_reg <= gemver_preheader1_scevgep8;
	end
end
always @(*) begin
	/* gemver: %.preheader1*/
	/*   %scevgep7 = getelementptr i32* %z, i32 %i.26, !MSB !2, !LSB !3, !extendFrom !2*/
		gemver_preheader1_scevgep7 = (arg_z_reg + (4 * {26'd0,gemver_preheader1_i26_reg}));
end
always @(*) begin
	/* gemver: %.preheader1*/
	/*   %28 = load i32* %scevgep8, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_preheader1_28 = main_0_x_out_a;
end
always @(*) begin
	/* gemver: %.preheader1*/
	/*   %29 = load i32* %scevgep7, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_preheader1_29 = main_0_z_out_a;
end
always @(*) begin
	/* gemver: %.preheader1*/
	/*   %30 = add nsw i32 %28, %29, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_preheader1_30 = (gemver_preheader1_28 + gemver_preheader1_29);
end
always @(*) begin
	/* gemver: %.preheader1*/
	/*   %31 = add nsw i32 %i.26, 1, !MSB !7, !LSB !3, !extendFrom !7*/
		gemver_preheader1_31 = ({1'd0,gemver_preheader1_i26_reg} + 32'd1);
end
always @(posedge clk) begin
	/* gemver: %.preheader1*/
	/*   %31 = add nsw i32 %i.26, 1, !MSB !7, !LSB !3, !extendFrom !7*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader1_20)) begin
		gemver_preheader1_31_reg <= gemver_preheader1_31;
	end
end
always @(*) begin
	/* gemver: %.preheader1*/
	/*   %exitcond = icmp eq i32 %31, 32, !MSB !3, !LSB !3, !extendFrom !3*/
		gemver_preheader1_exitcond = (gemver_preheader1_31_reg == 32'd32);
end
always @(posedge clk) begin
	/* gemver: %.preheader1*/
	/*   %exitcond = icmp eq i32 %31, 32, !MSB !3, !LSB !3, !extendFrom !3*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader1_21)) begin
		gemver_preheader1_exitcond_reg <= gemver_preheader1_exitcond;
	end
end
always @(*) begin
	/* gemver: %.preheader.preheader*/
	/*   %i.35 = phi i32 [ %42, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	if (((cur_state == LEGUP_F_gemver_BB_preheaderpreheaderpreheader_23) & (fsm_stall == 1'd0))) begin
		gemver_preheaderpreheader_i35 = 32'd0;
	end
	/* gemver: %.preheader.preheader*/
	/*   %i.35 = phi i32 [ %42, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	else /* if ((((cur_state == LEGUP_F_gemver_BB_preheader_32) & (fsm_stall == 1'd0)) & (gemver_preheader_exitcond7 == 1'd0))) */ begin
		gemver_preheaderpreheader_i35 = gemver_preheader_42_reg;
	end
end
always @(posedge clk) begin
	/* gemver: %.preheader.preheader*/
	/*   %i.35 = phi i32 [ %42, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	if (((cur_state == LEGUP_F_gemver_BB_preheaderpreheaderpreheader_23) & (fsm_stall == 1'd0))) begin
		gemver_preheaderpreheader_i35_reg <= gemver_preheaderpreheader_i35;
	end
	/* gemver: %.preheader.preheader*/
	/*   %i.35 = phi i32 [ %42, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	if ((((cur_state == LEGUP_F_gemver_BB_preheader_32) & (fsm_stall == 1'd0)) & (gemver_preheader_exitcond7 == 1'd0))) begin
		gemver_preheaderpreheader_i35_reg <= gemver_preheaderpreheader_i35;
	end
end
always @(*) begin
	/* gemver: %.preheader.preheader*/
	/*   %32 = mul i32 %i.35, 32, !MSB !5, !LSB !4, !extendFrom !5*/
		gemver_preheaderpreheader_32 = ({6'd0,gemver_preheaderpreheader_i35_reg} * 32'd32);
end
always @(posedge clk) begin
	/* gemver: %.preheader.preheader*/
	/*   %32 = mul i32 %i.35, 32, !MSB !5, !LSB !4, !extendFrom !5*/
	if ((cur_state == LEGUP_F_gemver_BB_preheaderpreheader_24)) begin
		gemver_preheaderpreheader_32_reg <= gemver_preheaderpreheader_32;
	end
end
always @(*) begin
	/* gemver: %.preheader.preheader*/
	/*   %scevgep5 = getelementptr i32* %w, i32 %i.35, !MSB !2, !LSB !3, !extendFrom !2*/
		gemver_preheaderpreheader_scevgep5 = (arg_w_reg + (4 * {26'd0,gemver_preheaderpreheader_i35_reg}));
end
always @(posedge clk) begin
	/* gemver: %.preheader.preheader*/
	/*   %scevgep5 = getelementptr i32* %w, i32 %i.35, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB_preheaderpreheader_24)) begin
		gemver_preheaderpreheader_scevgep5_reg <= gemver_preheaderpreheader_scevgep5;
	end
end
always @(*) begin
	/* gemver: %.preheader.preheader*/
	/*   %33 = load i32* %scevgep5, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_preheaderpreheader_33 = main_0_w_out_a;
end
always @(*) begin
	/* gemver: %34*/
	/*   %tmp1.04 = phi i32 [ %33, %.preheader.preheader ], [ %40, %34 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_gemver_BB_preheaderpreheader_25) & (fsm_stall == 1'd0))) begin
		gemver_34_tmp104 = gemver_preheaderpreheader_33;
	end
	/* gemver: %34*/
	/*   %tmp1.04 = phi i32 [ %33, %.preheader.preheader ], [ %40, %34 ], !MSB !6, !LSB !3, !extendFrom !6*/
	else /* if ((((cur_state == LEGUP_F_gemver_BB__34_30) & (fsm_stall == 1'd0)) & (gemver_34_exitcond3_reg == 1'd0))) */ begin
		gemver_34_tmp104 = gemver_34_40;
	end
end
always @(posedge clk) begin
	/* gemver: %34*/
	/*   %tmp1.04 = phi i32 [ %33, %.preheader.preheader ], [ %40, %34 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_gemver_BB_preheaderpreheader_25) & (fsm_stall == 1'd0))) begin
		gemver_34_tmp104_reg <= gemver_34_tmp104;
	end
	/* gemver: %34*/
	/*   %tmp1.04 = phi i32 [ %33, %.preheader.preheader ], [ %40, %34 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_gemver_BB__34_30) & (fsm_stall == 1'd0)) & (gemver_34_exitcond3_reg == 1'd0))) begin
		gemver_34_tmp104_reg <= gemver_34_tmp104;
	end
end
always @(*) begin
	/* gemver: %34*/
	/*   %j.23 = phi i32 [ 0, %.preheader.preheader ], [ %41, %34 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_gemver_BB_preheaderpreheader_25) & (fsm_stall == 1'd0))) begin
		gemver_34_j23 = 32'd0;
	end
	/* gemver: %34*/
	/*   %j.23 = phi i32 [ 0, %.preheader.preheader ], [ %41, %34 ], !MSB !6, !LSB !3, !extendFrom !6*/
	else /* if ((((cur_state == LEGUP_F_gemver_BB__34_30) & (fsm_stall == 1'd0)) & (gemver_34_exitcond3_reg == 1'd0))) */ begin
		gemver_34_j23 = gemver_34_41_reg;
	end
end
always @(posedge clk) begin
	/* gemver: %34*/
	/*   %j.23 = phi i32 [ 0, %.preheader.preheader ], [ %41, %34 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_gemver_BB_preheaderpreheader_25) & (fsm_stall == 1'd0))) begin
		gemver_34_j23_reg <= gemver_34_j23;
	end
	/* gemver: %34*/
	/*   %j.23 = phi i32 [ 0, %.preheader.preheader ], [ %41, %34 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_gemver_BB__34_30) & (fsm_stall == 1'd0)) & (gemver_34_exitcond3_reg == 1'd0))) begin
		gemver_34_j23_reg <= gemver_34_j23;
	end
end
always @(*) begin
	/* gemver: %34*/
	/*   %35 = add i32 %32, %j.23, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_34_35 = ({20'd0,gemver_preheaderpreheader_32_reg} + gemver_34_j23_reg);
end
always @(posedge clk) begin
	/* gemver: %34*/
	/*   %35 = add i32 %32, %j.23, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__34_26)) begin
		gemver_34_35_reg <= gemver_34_35;
	end
end
always @(*) begin
	/* gemver: %34*/
	/*   %scevgep3 = getelementptr i32* %A, i32 %35, !MSB !2, !LSB !3, !extendFrom !2*/
		gemver_34_scevgep3 = (arg_A_reg + (4 * gemver_34_35_reg));
end
always @(*) begin
	/* gemver: %34*/
	/*   %scevgep = getelementptr i32* %x, i32 %j.23, !MSB !2, !LSB !3, !extendFrom !2*/
		gemver_34_scevgep = (arg_x_reg + (4 * gemver_34_j23_reg));
end
always @(*) begin
	/* gemver: %34*/
	/*   %36 = load i32* %scevgep3, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_34_36 = main_0_A_out_a;
end
always @(*) begin
	gemver_34_37 = legup_mult_gemver_34_37_out;
end
always @(*) begin
	/* gemver: %34*/
	/*   %38 = load i32* %scevgep, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_34_38 = main_0_x_out_a;
end
always @(posedge clk) begin
	/* gemver: %34*/
	/*   %38 = load i32* %scevgep, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__34_27)) begin
		gemver_34_38_reg <= gemver_34_38;
	end
end
always @(*) begin
	gemver_34_39 = legup_mult_gemver_34_39_out;
end
always @(*) begin
	/* gemver: %34*/
	/*   %40 = add nsw i32 %tmp1.04, %39, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_34_40 = (gemver_34_tmp104_reg + gemver_34_39);
end
always @(*) begin
	/* gemver: %34*/
	/*   %41 = add nsw i32 %j.23, 1, !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_34_41 = (gemver_34_j23_reg + 32'd1);
end
always @(posedge clk) begin
	/* gemver: %34*/
	/*   %41 = add nsw i32 %j.23, 1, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__34_26)) begin
		gemver_34_41_reg <= gemver_34_41;
	end
end
always @(*) begin
	/* gemver: %34*/
	/*   %exitcond3 = icmp eq i32 %41, 32, !MSB !3, !LSB !3, !extendFrom !3*/
		gemver_34_exitcond3 = (gemver_34_41_reg == 32'd32);
end
always @(posedge clk) begin
	/* gemver: %34*/
	/*   %exitcond3 = icmp eq i32 %41, 32, !MSB !3, !LSB !3, !extendFrom !3*/
	if ((cur_state == LEGUP_F_gemver_BB__34_27)) begin
		gemver_34_exitcond3_reg <= gemver_34_exitcond3;
	end
end
always @(*) begin
	/* gemver: %.preheader*/
	/*   %.lcssa = phi i32 [ %40, %34 ], !MSB !6, !LSB !3, !extendFrom !6*/
		gemver_preheader_lcssa = gemver_34_40;
end
always @(posedge clk) begin
	/* gemver: %.preheader*/
	/*   %.lcssa = phi i32 [ %40, %34 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_gemver_BB__34_30) & (fsm_stall == 1'd0)) & (gemver_34_exitcond3_reg == 1'd1))) begin
		gemver_preheader_lcssa_reg <= gemver_preheader_lcssa;
	end
end
always @(*) begin
	/* gemver: %.preheader*/
	/*   %42 = add nsw i32 %i.35, 1, !MSB !7, !LSB !3, !extendFrom !7*/
		gemver_preheader_42 = ({1'd0,gemver_preheaderpreheader_i35_reg} + 32'd1);
end
always @(posedge clk) begin
	/* gemver: %.preheader*/
	/*   %42 = add nsw i32 %i.35, 1, !MSB !7, !LSB !3, !extendFrom !7*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader_31)) begin
		gemver_preheader_42_reg <= gemver_preheader_42;
	end
end
always @(*) begin
	/* gemver: %.preheader*/
	/*   %exitcond7 = icmp eq i32 %42, 32, !MSB !3, !LSB !3, !extendFrom !3*/
		gemver_preheader_exitcond7 = (gemver_preheader_42_reg == 32'd32);
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
	legup_mult_1_unsigned_32_32_1_0_clken = legup_mult_gemver_3_8_en;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_0_dataa = gemver_3_6;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_0_datab = gemver_3_7;
end
always @(*) begin
	legup_mult_gemver_3_8_out_actual = legup_mult_1_unsigned_32_32_1_0_result;
end
always @(*) begin
	legup_mult_gemver_3_8_out = legup_mult_gemver_3_8_out_actual[31:0];
end
always @(*) begin
	legup_mult_gemver_3_8_en = ~(fsm_stall);
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
	legup_mult_1_unsigned_32_32_1_1_clken = legup_mult_gemver_3_12_en;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_1_dataa = gemver_3_10;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_1_datab = gemver_3_11;
end
always @(*) begin
	legup_mult_gemver_3_12_out_actual = legup_mult_1_unsigned_32_32_1_1_result;
end
always @(*) begin
	legup_mult_gemver_3_12_out = legup_mult_gemver_3_12_out_actual[31:0];
end
always @(*) begin
	legup_mult_gemver_3_12_en = ~(fsm_stall);
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
	legup_mult_1_unsigned_32_32_1_2_clken = legup_mult_gemver_18_22_en;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_2_dataa = gemver_18_21;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_2_datab = arg_beta_reg;
end
always @(*) begin
	legup_mult_gemver_18_22_out_actual = legup_mult_1_unsigned_32_32_1_2_result;
end
always @(*) begin
	legup_mult_gemver_18_22_out = legup_mult_gemver_18_22_out_actual[31:0];
end
always @(*) begin
	legup_mult_gemver_18_22_en = ~(fsm_stall);
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
	legup_mult_1_unsigned_32_32_1_3_clken = legup_mult_gemver_18_24_en;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_3_dataa = gemver_18_22;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_3_datab = gemver_18_23_reg;
end
always @(*) begin
	legup_mult_gemver_18_24_out_actual = legup_mult_1_unsigned_32_32_1_3_result;
end
always @(*) begin
	legup_mult_gemver_18_24_out = legup_mult_gemver_18_24_out_actual[31:0];
end
always @(*) begin
	legup_mult_gemver_18_24_en = ~(fsm_stall);
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_4_clock = clk;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_4_aclr = reset;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_4_sum = 1'd0;
if (reset) begin legup_mult_1_unsigned_32_32_1_4_sum = 0; end
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_4_clken = legup_mult_gemver_34_37_en;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_4_dataa = gemver_34_36;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_4_datab = arg_alpha_reg;
end
always @(*) begin
	legup_mult_gemver_34_37_out_actual = legup_mult_1_unsigned_32_32_1_4_result;
end
always @(*) begin
	legup_mult_gemver_34_37_out = legup_mult_gemver_34_37_out_actual[31:0];
end
always @(*) begin
	legup_mult_gemver_34_37_en = ~(fsm_stall);
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_5_clock = clk;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_5_aclr = reset;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_5_sum = 1'd0;
if (reset) begin legup_mult_1_unsigned_32_32_1_5_sum = 0; end
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_5_clken = legup_mult_gemver_34_39_en;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_5_dataa = gemver_34_37;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_5_datab = gemver_34_38_reg;
end
always @(*) begin
	legup_mult_gemver_34_39_out_actual = legup_mult_1_unsigned_32_32_1_5_result;
end
always @(*) begin
	legup_mult_gemver_34_39_out = legup_mult_gemver_34_39_out_actual[31:0];
end
always @(*) begin
	legup_mult_gemver_34_39_en = ~(fsm_stall);
end
always @(posedge clk) begin
	if ((cur_state == LEGUP_0)) begin
		finish <= 1'd0;
	end
	/* gemver: %43*/
	/*   ret void, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB__43_33)) begin
		finish <= (fsm_stall == 1'd0);
	end
end
assign main_0_u1_write_enable_a = 1'd0;
assign main_0_u1_in_a = 0;
assign main_0_u1_byteena_a = 1'd1;
always @(*) begin
	main_0_u1_enable_a = 1'd0;
	/* gemver: %3*/
	/*   %6 = load i32* %scevgep22, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__3_2)) begin
		main_0_u1_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_u1_address_a = 5'd0;
	/* gemver: %3*/
	/*   %6 = load i32* %scevgep22, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__3_2)) begin
		main_0_u1_address_a = (gemver_1_scevgep22_reg >>> 3'd2);
	end
end
assign main_0_u1_write_enable_b = 1'd0;
assign main_0_u1_in_b = 0;
assign main_0_u1_byteena_b = 1'd1;
assign main_0_u1_enable_b = 1'd0;
assign main_0_u1_address_b = 5'd0;
assign main_0_v1_write_enable_a = 1'd0;
assign main_0_v1_in_a = 0;
assign main_0_v1_byteena_a = 1'd1;
always @(*) begin
	main_0_v1_enable_a = 1'd0;
	/* gemver: %3*/
	/*   %7 = load i32* %scevgep17, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__3_2)) begin
		main_0_v1_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_v1_address_a = 5'd0;
	/* gemver: %3*/
	/*   %7 = load i32* %scevgep17, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__3_2)) begin
		main_0_v1_address_a = (gemver_3_scevgep17 >>> 3'd2);
	end
end
assign main_0_v1_write_enable_b = 1'd0;
assign main_0_v1_in_b = 0;
assign main_0_v1_byteena_b = 1'd1;
assign main_0_v1_enable_b = 1'd0;
assign main_0_v1_address_b = 5'd0;
assign main_0_u2_write_enable_a = 1'd0;
assign main_0_u2_in_a = 0;
assign main_0_u2_byteena_a = 1'd1;
always @(*) begin
	main_0_u2_enable_a = 1'd0;
	/* gemver: %3*/
	/*   %10 = load i32* %scevgep21, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__3_2)) begin
		main_0_u2_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_u2_address_a = 5'd0;
	/* gemver: %3*/
	/*   %10 = load i32* %scevgep21, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__3_2)) begin
		main_0_u2_address_a = (gemver_1_scevgep21_reg >>> 3'd2);
	end
end
assign main_0_u2_write_enable_b = 1'd0;
assign main_0_u2_in_b = 0;
assign main_0_u2_byteena_b = 1'd1;
assign main_0_u2_enable_b = 1'd0;
assign main_0_u2_address_b = 5'd0;
assign main_0_v2_write_enable_a = 1'd0;
assign main_0_v2_in_a = 0;
assign main_0_v2_byteena_a = 1'd1;
always @(*) begin
	main_0_v2_enable_a = 1'd0;
	/* gemver: %3*/
	/*   %11 = load i32* %scevgep16, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__3_2)) begin
		main_0_v2_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_v2_address_a = 5'd0;
	/* gemver: %3*/
	/*   %11 = load i32* %scevgep16, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__3_2)) begin
		main_0_v2_address_a = (gemver_3_scevgep16 >>> 3'd2);
	end
end
assign main_0_v2_write_enable_b = 1'd0;
assign main_0_v2_in_b = 0;
assign main_0_v2_byteena_b = 1'd1;
assign main_0_v2_enable_b = 1'd0;
assign main_0_v2_address_b = 5'd0;
always @(*) begin
	main_0_A_write_enable_a = 1'd0;
	/* gemver: %3*/
	/*   store i32 %13, i32* %scevgep18, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB__3_5)) begin
		main_0_A_write_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_A_in_a = 0;
	/* gemver: %3*/
	/*   store i32 %13, i32* %scevgep18, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB__3_5)) begin
		main_0_A_in_a = gemver_3_13;
	end
end
assign main_0_A_byteena_a = 1'd1;
always @(*) begin
	main_0_A_enable_a = 1'd0;
	/* gemver: %3*/
	/*   %5 = load i32* %scevgep18, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__3_3)) begin
		main_0_A_enable_a = 1'd1;
	end
	/* gemver: %3*/
	/*   store i32 %13, i32* %scevgep18, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB__3_5)) begin
		main_0_A_enable_a = 1'd1;
	end
	/* gemver: %18*/
	/*   %21 = load i32* %scevgep11, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__18_13)) begin
		main_0_A_enable_a = 1'd1;
	end
	/* gemver: %34*/
	/*   %36 = load i32* %scevgep3, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__34_27)) begin
		main_0_A_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_A_address_a = 10'd0;
	/* gemver: %3*/
	/*   %5 = load i32* %scevgep18, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__3_3)) begin
		main_0_A_address_a = (gemver_3_scevgep18 >>> 3'd2);
	end
	/* gemver: %3*/
	/*   store i32 %13, i32* %scevgep18, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB__3_5)) begin
		main_0_A_address_a = (gemver_3_scevgep18_reg >>> 3'd2);
	end
	/* gemver: %18*/
	/*   %21 = load i32* %scevgep11, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__18_13)) begin
		main_0_A_address_a = (gemver_18_scevgep11 >>> 3'd2);
	end
	/* gemver: %34*/
	/*   %36 = load i32* %scevgep3, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__34_27)) begin
		main_0_A_address_a = (gemver_34_scevgep3 >>> 3'd2);
	end
end
assign main_0_A_write_enable_b = 1'd0;
assign main_0_A_in_b = 0;
assign main_0_A_byteena_b = 1'd1;
assign main_0_A_enable_b = 1'd0;
assign main_0_A_address_b = 10'd0;
always @(*) begin
	main_0_x_write_enable_a = 1'd0;
	/* gemver: %.preheader2*/
	/*   store i32 %.lcssa1, i32* %scevgep14, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader2_17)) begin
		main_0_x_write_enable_a = 1'd1;
	end
	/* gemver: %.preheader1*/
	/*   store i32 %30, i32* %scevgep8, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader1_21)) begin
		main_0_x_write_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_x_in_a = 0;
	/* gemver: %.preheader2*/
	/*   store i32 %.lcssa1, i32* %scevgep14, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader2_17)) begin
		main_0_x_in_a = gemver_preheader2_lcssa1_reg;
	end
	/* gemver: %.preheader1*/
	/*   store i32 %30, i32* %scevgep8, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader1_21)) begin
		main_0_x_in_a = gemver_preheader1_30;
	end
end
assign main_0_x_byteena_a = 1'd1;
always @(*) begin
	main_0_x_enable_a = 1'd0;
	/* gemver: %.preheader2.preheader*/
	/*   %17 = load i32* %scevgep14, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader2preheader_10)) begin
		main_0_x_enable_a = 1'd1;
	end
	/* gemver: %.preheader2*/
	/*   store i32 %.lcssa1, i32* %scevgep14, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader2_17)) begin
		main_0_x_enable_a = 1'd1;
	end
	/* gemver: %.preheader1*/
	/*   %28 = load i32* %scevgep8, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader1_20)) begin
		main_0_x_enable_a = 1'd1;
	end
	/* gemver: %.preheader1*/
	/*   store i32 %30, i32* %scevgep8, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader1_21)) begin
		main_0_x_enable_a = 1'd1;
	end
	/* gemver: %34*/
	/*   %38 = load i32* %scevgep, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__34_26)) begin
		main_0_x_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_x_address_a = 5'd0;
	/* gemver: %.preheader2.preheader*/
	/*   %17 = load i32* %scevgep14, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader2preheader_10)) begin
		main_0_x_address_a = (gemver_preheader2preheader_scevgep14 >>> 3'd2);
	end
	/* gemver: %.preheader2*/
	/*   store i32 %.lcssa1, i32* %scevgep14, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader2_17)) begin
		main_0_x_address_a = (gemver_preheader2preheader_scevgep14_reg >>> 3'd2);
	end
	/* gemver: %.preheader1*/
	/*   %28 = load i32* %scevgep8, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader1_20)) begin
		main_0_x_address_a = (gemver_preheader1_scevgep8 >>> 3'd2);
	end
	/* gemver: %.preheader1*/
	/*   store i32 %30, i32* %scevgep8, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader1_21)) begin
		main_0_x_address_a = (gemver_preheader1_scevgep8_reg >>> 3'd2);
	end
	/* gemver: %34*/
	/*   %38 = load i32* %scevgep, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__34_26)) begin
		main_0_x_address_a = (gemver_34_scevgep >>> 3'd2);
	end
end
assign main_0_x_write_enable_b = 1'd0;
assign main_0_x_in_b = 0;
assign main_0_x_byteena_b = 1'd1;
assign main_0_x_enable_b = 1'd0;
assign main_0_x_address_b = 5'd0;
assign main_0_y_write_enable_a = 1'd0;
assign main_0_y_in_a = 0;
assign main_0_y_byteena_a = 1'd1;
always @(*) begin
	main_0_y_enable_a = 1'd0;
	/* gemver: %18*/
	/*   %23 = load i32* %scevgep10, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__18_12)) begin
		main_0_y_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_y_address_a = 5'd0;
	/* gemver: %18*/
	/*   %23 = load i32* %scevgep10, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB__18_12)) begin
		main_0_y_address_a = (gemver_18_scevgep10 >>> 3'd2);
	end
end
assign main_0_y_write_enable_b = 1'd0;
assign main_0_y_in_b = 0;
assign main_0_y_byteena_b = 1'd1;
assign main_0_y_enable_b = 1'd0;
assign main_0_y_address_b = 5'd0;
assign main_0_z_write_enable_a = 1'd0;
assign main_0_z_in_a = 0;
assign main_0_z_byteena_a = 1'd1;
always @(*) begin
	main_0_z_enable_a = 1'd0;
	/* gemver: %.preheader1*/
	/*   %29 = load i32* %scevgep7, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader1_20)) begin
		main_0_z_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_z_address_a = 5'd0;
	/* gemver: %.preheader1*/
	/*   %29 = load i32* %scevgep7, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader1_20)) begin
		main_0_z_address_a = (gemver_preheader1_scevgep7 >>> 3'd2);
	end
end
assign main_0_z_write_enable_b = 1'd0;
assign main_0_z_in_b = 0;
assign main_0_z_byteena_b = 1'd1;
assign main_0_z_enable_b = 1'd0;
assign main_0_z_address_b = 5'd0;
always @(*) begin
	main_0_w_write_enable_a = 1'd0;
	/* gemver: %.preheader*/
	/*   store i32 %.lcssa, i32* %scevgep5, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader_31)) begin
		main_0_w_write_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_w_in_a = 0;
	/* gemver: %.preheader*/
	/*   store i32 %.lcssa, i32* %scevgep5, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader_31)) begin
		main_0_w_in_a = gemver_preheader_lcssa_reg;
	end
end
assign main_0_w_byteena_a = 1'd1;
always @(*) begin
	main_0_w_enable_a = 1'd0;
	/* gemver: %.preheader.preheader*/
	/*   %33 = load i32* %scevgep5, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB_preheaderpreheader_24)) begin
		main_0_w_enable_a = 1'd1;
	end
	/* gemver: %.preheader*/
	/*   store i32 %.lcssa, i32* %scevgep5, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader_31)) begin
		main_0_w_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_w_address_a = 5'd0;
	/* gemver: %.preheader.preheader*/
	/*   %33 = load i32* %scevgep5, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_gemver_BB_preheaderpreheader_24)) begin
		main_0_w_address_a = (gemver_preheaderpreheader_scevgep5 >>> 3'd2);
	end
	/* gemver: %.preheader*/
	/*   store i32 %.lcssa, i32* %scevgep5, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_gemver_BB_preheader_31)) begin
		main_0_w_address_a = (gemver_preheaderpreheader_scevgep5_reg >>> 3'd2);
	end
end
assign main_0_w_write_enable_b = 1'd0;
assign main_0_w_in_b = 0;
assign main_0_w_byteena_b = 1'd1;
assign main_0_w_enable_b = 1'd0;
assign main_0_w_address_b = 5'd0;

endmodule
