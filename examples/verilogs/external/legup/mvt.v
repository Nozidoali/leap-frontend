//----------------------------------------------------------------------------
// LegUp High-Level Synthesis Tool Version 5.0 (http://legup.org)
// Copyright (c) 2009-23 University of Toronto. All Rights Reserved.
// For research and academic purposes only. Commercial use is prohibited.
// Please report bugs at: http://legup.org/bugs
// Please email questions to: legup@eecg.toronto.edu
// Date: Sun Oct  6 18:32:42 2024
// ----------------------------------------------------------------------------
`timescale 1 ns / 1 ns
module mvt
(
	clk,
	clk2x,
	clk1x_follower,
	reset,
	memory_controller_waitrequest,
	start,
	finish,
	arg_A,
	arg_x1,
	arg_x2,
	arg_y1,
	arg_y2,
	main_0_x1_write_enable_a,
	main_0_x1_in_a,
	main_0_x1_byteena_a,
	main_0_x1_enable_a,
	main_0_x1_address_a,
	main_0_x1_out_a,
	main_0_x1_write_enable_b,
	main_0_x1_in_b,
	main_0_x1_byteena_b,
	main_0_x1_enable_b,
	main_0_x1_address_b,
	main_0_x1_out_b,
	main_0_y1_write_enable_a,
	main_0_y1_in_a,
	main_0_y1_byteena_a,
	main_0_y1_enable_a,
	main_0_y1_address_a,
	main_0_y1_out_a,
	main_0_y1_write_enable_b,
	main_0_y1_in_b,
	main_0_y1_byteena_b,
	main_0_y1_enable_b,
	main_0_y1_address_b,
	main_0_y1_out_b,
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
	main_0_x2_write_enable_a,
	main_0_x2_in_a,
	main_0_x2_byteena_a,
	main_0_x2_enable_a,
	main_0_x2_address_a,
	main_0_x2_out_a,
	main_0_x2_write_enable_b,
	main_0_x2_in_b,
	main_0_x2_byteena_b,
	main_0_x2_enable_b,
	main_0_x2_address_b,
	main_0_x2_out_b,
	main_0_y2_write_enable_a,
	main_0_y2_in_a,
	main_0_y2_byteena_a,
	main_0_y2_enable_a,
	main_0_y2_address_a,
	main_0_y2_out_a,
	main_0_y2_write_enable_b,
	main_0_y2_in_b,
	main_0_y2_byteena_b,
	main_0_y2_enable_b,
	main_0_y2_address_b,
	main_0_y2_out_b
);

parameter [4:0] LEGUP_0 = 5'd0;
parameter [4:0] LEGUP_F_mvt_BB__1_1 = 5'd1;
parameter [4:0] LEGUP_F_mvt_BB__1_2 = 5'd2;
parameter [4:0] LEGUP_F_mvt_BB__4_3 = 5'd3;
parameter [4:0] LEGUP_F_mvt_BB__4_4 = 5'd4;
parameter [4:0] LEGUP_F_mvt_BB__4_5 = 5'd5;
parameter [4:0] LEGUP_F_mvt_BB__4_6 = 5'd6;
parameter [4:0] LEGUP_F_mvt_BB__11_7 = 5'd7;
parameter [4:0] LEGUP_F_mvt_BB__11_8 = 5'd8;
parameter [4:0] LEGUP_F_mvt_BB_preheaderpreheaderpreheader_9 = 5'd9;
parameter [4:0] LEGUP_F_mvt_BB_preheaderpreheader_10 = 5'd10;
parameter [4:0] LEGUP_F_mvt_BB_preheaderpreheader_11 = 5'd11;
parameter [4:0] LEGUP_F_mvt_BB__14_12 = 5'd12;
parameter [4:0] LEGUP_F_mvt_BB__14_13 = 5'd13;
parameter [4:0] LEGUP_F_mvt_BB__14_14 = 5'd14;
parameter [4:0] LEGUP_F_mvt_BB__14_15 = 5'd15;
parameter [4:0] LEGUP_F_mvt_BB_preheader_16 = 5'd16;
parameter [4:0] LEGUP_F_mvt_BB_preheader_17 = 5'd17;
parameter [4:0] LEGUP_F_mvt_BB__23_18 = 5'd18;

input  clk;
input  clk2x;
input  clk1x_follower;
input  reset;
input  memory_controller_waitrequest;
input  start;
output reg  finish;
input [31:0] arg_A;
input [31:0] arg_x1;
input [31:0] arg_x2;
input [31:0] arg_y1;
input [31:0] arg_y2;
output reg  main_0_x1_write_enable_a;
output reg [31:0] main_0_x1_in_a;
output  main_0_x1_byteena_a;
output reg  main_0_x1_enable_a;
output reg [4:0] main_0_x1_address_a;
input [31:0] main_0_x1_out_a;
output  main_0_x1_write_enable_b;
output [31:0] main_0_x1_in_b;
output  main_0_x1_byteena_b;
output  main_0_x1_enable_b;
output [4:0] main_0_x1_address_b;
input [31:0] main_0_x1_out_b;
output  main_0_y1_write_enable_a;
output [31:0] main_0_y1_in_a;
output  main_0_y1_byteena_a;
output reg  main_0_y1_enable_a;
output reg [4:0] main_0_y1_address_a;
input [31:0] main_0_y1_out_a;
output  main_0_y1_write_enable_b;
output [31:0] main_0_y1_in_b;
output  main_0_y1_byteena_b;
output  main_0_y1_enable_b;
output [4:0] main_0_y1_address_b;
input [31:0] main_0_y1_out_b;
output  main_0_A_write_enable_a;
output [31:0] main_0_A_in_a;
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
output reg  main_0_x2_write_enable_a;
output reg [31:0] main_0_x2_in_a;
output  main_0_x2_byteena_a;
output reg  main_0_x2_enable_a;
output reg [4:0] main_0_x2_address_a;
input [31:0] main_0_x2_out_a;
output  main_0_x2_write_enable_b;
output [31:0] main_0_x2_in_b;
output  main_0_x2_byteena_b;
output  main_0_x2_enable_b;
output [4:0] main_0_x2_address_b;
input [31:0] main_0_x2_out_b;
output  main_0_y2_write_enable_a;
output [31:0] main_0_y2_in_a;
output  main_0_y2_byteena_a;
output reg  main_0_y2_enable_a;
output reg [4:0] main_0_y2_address_a;
input [31:0] main_0_y2_out_a;
output  main_0_y2_write_enable_b;
output [31:0] main_0_y2_in_b;
output  main_0_y2_byteena_b;
output  main_0_y2_enable_b;
output [4:0] main_0_y2_address_b;
input [31:0] main_0_y2_out_b;
reg [4:0] cur_state;
reg [4:0] next_state;
reg [31:0] arg_A_reg;
reg [31:0] arg_x1_reg;
reg [31:0] arg_x2_reg;
reg [31:0] arg_y1_reg;
reg [31:0] arg_y2_reg;
reg  fsm_stall;
reg [5:0] mvt_1_i06;
reg [5:0] mvt_1_i06_reg;
reg [11:0] mvt_1_2;
reg [11:0] mvt_1_2_reg;
reg [31:0] mvt_1_scevgep11;
reg [31:0] mvt_1_scevgep11_reg;
reg [31:0] mvt_1_3;
reg [31:0] mvt_4_tmp05;
reg [31:0] mvt_4_tmp05_reg;
reg [31:0] mvt_4_j04;
reg [31:0] mvt_4_j04_reg;
reg [31:0] mvt_4_5;
reg [31:0] mvt_4_5_reg;
reg [31:0] mvt_4_scevgep8;
reg [31:0] mvt_4_scevgep7;
reg [31:0] mvt_4_6;
reg [31:0] mvt_4_7;
reg [31:0] mvt_4_7_reg;
reg [31:0] mvt_4_8;
reg [31:0] mvt_4_9;
reg [31:0] mvt_4_10;
reg [31:0] mvt_4_10_reg;
reg  mvt_4_exitcond;
reg  mvt_4_exitcond_reg;
reg [31:0] mvt_11_lcssa1;
reg [31:0] mvt_11_lcssa1_reg;
reg [6:0] mvt_11_12;
reg [6:0] mvt_11_12_reg;
reg  mvt_11_exitcond14;
reg [5:0] mvt_preheaderpreheader_i13;
reg [5:0] mvt_preheaderpreheader_i13_reg;
reg [31:0] mvt_preheaderpreheader_scevgep5;
reg [31:0] mvt_preheaderpreheader_scevgep5_reg;
reg [31:0] mvt_preheaderpreheader_13;
reg [31:0] mvt_14_tmp102;
reg [31:0] mvt_14_tmp102_reg;
reg [31:0] mvt_14_j11;
reg [31:0] mvt_14_j11_reg;
reg [31:0] mvt_14_15;
reg [31:0] mvt_14_16;
reg [31:0] mvt_14_16_reg;
reg [31:0] mvt_14_scevgep3;
reg [31:0] mvt_14_scevgep;
reg [31:0] mvt_14_17;
reg [31:0] mvt_14_18;
reg [31:0] mvt_14_18_reg;
reg [31:0] mvt_14_19;
reg [31:0] mvt_14_20;
reg [31:0] mvt_14_21;
reg [31:0] mvt_14_21_reg;
reg  mvt_14_exitcond3;
reg  mvt_14_exitcond3_reg;
reg [31:0] mvt_preheader_lcssa;
reg [31:0] mvt_preheader_lcssa_reg;
reg [6:0] mvt_preheader_22;
reg [6:0] mvt_preheader_22_reg;
reg  mvt_preheader_exitcond7;
reg  legup_mult_1_unsigned_32_32_1_0_clock;
reg  legup_mult_1_unsigned_32_32_1_0_aclr;
reg  legup_mult_1_unsigned_32_32_1_0_sum;
reg  legup_mult_1_unsigned_32_32_1_0_clken;
reg [31:0] legup_mult_1_unsigned_32_32_1_0_dataa;
reg [31:0] legup_mult_1_unsigned_32_32_1_0_datab;
wire [63:0] legup_mult_1_unsigned_32_32_1_0_result;
reg [63:0] legup_mult_mvt_4_8_out_actual;
reg [31:0] legup_mult_mvt_4_8_out;
reg  legup_mult_mvt_4_8_en;
reg  legup_mult_1_unsigned_32_32_1_1_clock;
reg  legup_mult_1_unsigned_32_32_1_1_aclr;
reg  legup_mult_1_unsigned_32_32_1_1_sum;
reg  legup_mult_1_unsigned_32_32_1_1_clken;
reg [31:0] legup_mult_1_unsigned_32_32_1_1_dataa;
reg [31:0] legup_mult_1_unsigned_32_32_1_1_datab;
wire [63:0] legup_mult_1_unsigned_32_32_1_1_result;
reg [63:0] legup_mult_mvt_14_19_out_actual;
reg [31:0] legup_mult_mvt_14_19_out;
reg  legup_mult_mvt_14_19_en;

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

// Commented out because it is not used in the CDFG extraction
/*
defparam
	legup_mult_1_unsigned_32_32_1_0.widtha = 32,
	legup_mult_1_unsigned_32_32_1_0.widthb = 32,
	legup_mult_1_unsigned_32_32_1_0.widthp = 64,
	legup_mult_1_unsigned_32_32_1_0.representation = "UNSIGNED";
*/
/*   %19 = mul nsw i32 %17, %18, !MSB !6, !LSB !3, !extendFrom !6*/
legup_mult_1 legup_mult_1_unsigned_32_32_1_1 (
	.clock (legup_mult_1_unsigned_32_32_1_1_clock),
	.aclr (legup_mult_1_unsigned_32_32_1_1_aclr),
	.sum (legup_mult_1_unsigned_32_32_1_1_sum),
	.clken (legup_mult_1_unsigned_32_32_1_1_clken),
	.dataa (legup_mult_1_unsigned_32_32_1_1_dataa),
	.datab (legup_mult_1_unsigned_32_32_1_1_datab),
	.result (legup_mult_1_unsigned_32_32_1_1_result)
);

// Commented out because it is not used in the CDFG extraction
/*
defparam
	legup_mult_1_unsigned_32_32_1_1.widtha = 32,
	legup_mult_1_unsigned_32_32_1_1.widthb = 32,
	legup_mult_1_unsigned_32_32_1_1.widthp = 64,
	legup_mult_1_unsigned_32_32_1_1.representation = "UNSIGNED";
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
		next_state = LEGUP_F_mvt_BB__1_1;
LEGUP_F_mvt_BB__11_7:
		next_state = LEGUP_F_mvt_BB__11_8;
LEGUP_F_mvt_BB__11_8:
	if ((fsm_stall == 1'd0) && (mvt_11_exitcond14 == 1'd1))
		next_state = LEGUP_F_mvt_BB_preheaderpreheaderpreheader_9;
	else if ((fsm_stall == 1'd0) && (mvt_11_exitcond14 == 1'd0))
		next_state = LEGUP_F_mvt_BB__1_1;
LEGUP_F_mvt_BB__14_12:
		next_state = LEGUP_F_mvt_BB__14_13;
LEGUP_F_mvt_BB__14_13:
		next_state = LEGUP_F_mvt_BB__14_14;
LEGUP_F_mvt_BB__14_14:
		next_state = LEGUP_F_mvt_BB__14_15;
LEGUP_F_mvt_BB__14_15:
	if ((fsm_stall == 1'd0) && (mvt_14_exitcond3_reg == 1'd1))
		next_state = LEGUP_F_mvt_BB_preheader_16;
	else if ((fsm_stall == 1'd0) && (mvt_14_exitcond3_reg == 1'd0))
		next_state = LEGUP_F_mvt_BB__14_12;
LEGUP_F_mvt_BB__1_1:
		next_state = LEGUP_F_mvt_BB__1_2;
LEGUP_F_mvt_BB__1_2:
		next_state = LEGUP_F_mvt_BB__4_3;
LEGUP_F_mvt_BB__23_18:
		next_state = LEGUP_0;
LEGUP_F_mvt_BB__4_3:
		next_state = LEGUP_F_mvt_BB__4_4;
LEGUP_F_mvt_BB__4_4:
		next_state = LEGUP_F_mvt_BB__4_5;
LEGUP_F_mvt_BB__4_5:
		next_state = LEGUP_F_mvt_BB__4_6;
LEGUP_F_mvt_BB__4_6:
	if ((fsm_stall == 1'd0) && (mvt_4_exitcond_reg == 1'd1))
		next_state = LEGUP_F_mvt_BB__11_7;
	else if ((fsm_stall == 1'd0) && (mvt_4_exitcond_reg == 1'd0))
		next_state = LEGUP_F_mvt_BB__4_3;
LEGUP_F_mvt_BB_preheader_16:
		next_state = LEGUP_F_mvt_BB_preheader_17;
LEGUP_F_mvt_BB_preheader_17:
	if ((fsm_stall == 1'd0) && (mvt_preheader_exitcond7 == 1'd1))
		next_state = LEGUP_F_mvt_BB__23_18;
	else if ((fsm_stall == 1'd0) && (mvt_preheader_exitcond7 == 1'd0))
		next_state = LEGUP_F_mvt_BB_preheaderpreheader_10;
LEGUP_F_mvt_BB_preheaderpreheader_10:
		next_state = LEGUP_F_mvt_BB_preheaderpreheader_11;
LEGUP_F_mvt_BB_preheaderpreheader_11:
		next_state = LEGUP_F_mvt_BB__14_12;
LEGUP_F_mvt_BB_preheaderpreheaderpreheader_9:
		next_state = LEGUP_F_mvt_BB_preheaderpreheader_10;
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
		arg_x1_reg <= arg_x1;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_x2_reg <= arg_x2;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_y1_reg <= arg_y1;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_y2_reg <= arg_y2;
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
	/* mvt: %1*/
	/*   %i.06 = phi i32 [ 0, %0 ], [ %12, %11 ], !MSB !4, !LSB !3, !extendFrom !4*/
	if ((((cur_state == LEGUP_0) & (fsm_stall == 1'd0)) & (start == 1'd1))) begin
		mvt_1_i06 = 32'd0;
	end
	/* mvt: %1*/
	/*   %i.06 = phi i32 [ 0, %0 ], [ %12, %11 ], !MSB !4, !LSB !3, !extendFrom !4*/
	else /* if ((((cur_state == LEGUP_F_mvt_BB__11_8) & (fsm_stall == 1'd0)) & (mvt_11_exitcond14 == 1'd0))) */ begin
		mvt_1_i06 = mvt_11_12_reg;
	end
end
always @(posedge clk) begin
	/* mvt: %1*/
	/*   %i.06 = phi i32 [ 0, %0 ], [ %12, %11 ], !MSB !4, !LSB !3, !extendFrom !4*/
	if ((((cur_state == LEGUP_0) & (fsm_stall == 1'd0)) & (start == 1'd1))) begin
		mvt_1_i06_reg <= mvt_1_i06;
	end
	/* mvt: %1*/
	/*   %i.06 = phi i32 [ 0, %0 ], [ %12, %11 ], !MSB !4, !LSB !3, !extendFrom !4*/
	if ((((cur_state == LEGUP_F_mvt_BB__11_8) & (fsm_stall == 1'd0)) & (mvt_11_exitcond14 == 1'd0))) begin
		mvt_1_i06_reg <= mvt_1_i06;
	end
end
always @(*) begin
	/* mvt: %1*/
	/*   %2 = mul i32 %i.06, 32, !MSB !5, !LSB !4, !extendFrom !5*/
		mvt_1_2 = ({6'd0,mvt_1_i06_reg} * 32'd32);
end
always @(posedge clk) begin
	/* mvt: %1*/
	/*   %2 = mul i32 %i.06, 32, !MSB !5, !LSB !4, !extendFrom !5*/
	if ((cur_state == LEGUP_F_mvt_BB__1_1)) begin
		mvt_1_2_reg <= mvt_1_2;
	end
end
always @(*) begin
	/* mvt: %1*/
	/*   %scevgep11 = getelementptr i32* %x1, i32 %i.06, !MSB !2, !LSB !3, !extendFrom !2*/
		mvt_1_scevgep11 = (arg_x1_reg + (4 * {26'd0,mvt_1_i06_reg}));
end
always @(posedge clk) begin
	/* mvt: %1*/
	/*   %scevgep11 = getelementptr i32* %x1, i32 %i.06, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_mvt_BB__1_1)) begin
		mvt_1_scevgep11_reg <= mvt_1_scevgep11;
	end
end
always @(*) begin
	/* mvt: %1*/
	/*   %3 = load i32* %scevgep11, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		mvt_1_3 = main_0_x1_out_a;
end
always @(*) begin
	/* mvt: %4*/
	/*   %tmp.05 = phi i32 [ %3, %1 ], [ %9, %4 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_mvt_BB__1_2) & (fsm_stall == 1'd0))) begin
		mvt_4_tmp05 = mvt_1_3;
	end
	/* mvt: %4*/
	/*   %tmp.05 = phi i32 [ %3, %1 ], [ %9, %4 ], !MSB !6, !LSB !3, !extendFrom !6*/
	else /* if ((((cur_state == LEGUP_F_mvt_BB__4_6) & (fsm_stall == 1'd0)) & (mvt_4_exitcond_reg == 1'd0))) */ begin
		mvt_4_tmp05 = mvt_4_9;
	end
end
always @(posedge clk) begin
	/* mvt: %4*/
	/*   %tmp.05 = phi i32 [ %3, %1 ], [ %9, %4 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_mvt_BB__1_2) & (fsm_stall == 1'd0))) begin
		mvt_4_tmp05_reg <= mvt_4_tmp05;
	end
	/* mvt: %4*/
	/*   %tmp.05 = phi i32 [ %3, %1 ], [ %9, %4 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_mvt_BB__4_6) & (fsm_stall == 1'd0)) & (mvt_4_exitcond_reg == 1'd0))) begin
		mvt_4_tmp05_reg <= mvt_4_tmp05;
	end
end
always @(*) begin
	/* mvt: %4*/
	/*   %j.04 = phi i32 [ 0, %1 ], [ %10, %4 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_mvt_BB__1_2) & (fsm_stall == 1'd0))) begin
		mvt_4_j04 = 32'd0;
	end
	/* mvt: %4*/
	/*   %j.04 = phi i32 [ 0, %1 ], [ %10, %4 ], !MSB !6, !LSB !3, !extendFrom !6*/
	else /* if ((((cur_state == LEGUP_F_mvt_BB__4_6) & (fsm_stall == 1'd0)) & (mvt_4_exitcond_reg == 1'd0))) */ begin
		mvt_4_j04 = mvt_4_10_reg;
	end
end
always @(posedge clk) begin
	/* mvt: %4*/
	/*   %j.04 = phi i32 [ 0, %1 ], [ %10, %4 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_mvt_BB__1_2) & (fsm_stall == 1'd0))) begin
		mvt_4_j04_reg <= mvt_4_j04;
	end
	/* mvt: %4*/
	/*   %j.04 = phi i32 [ 0, %1 ], [ %10, %4 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_mvt_BB__4_6) & (fsm_stall == 1'd0)) & (mvt_4_exitcond_reg == 1'd0))) begin
		mvt_4_j04_reg <= mvt_4_j04;
	end
end
always @(*) begin
	/* mvt: %4*/
	/*   %5 = add i32 %2, %j.04, !MSB !6, !LSB !3, !extendFrom !6*/
		mvt_4_5 = ({20'd0,mvt_1_2_reg} + mvt_4_j04_reg);
end
always @(posedge clk) begin
	/* mvt: %4*/
	/*   %5 = add i32 %2, %j.04, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_mvt_BB__4_3)) begin
		mvt_4_5_reg <= mvt_4_5;
	end
end
always @(*) begin
	/* mvt: %4*/
	/*   %scevgep8 = getelementptr i32* %A, i32 %5, !MSB !2, !LSB !3, !extendFrom !2*/
		mvt_4_scevgep8 = (arg_A_reg + (4 * mvt_4_5_reg));
end
always @(*) begin
	/* mvt: %4*/
	/*   %scevgep7 = getelementptr i32* %y1, i32 %j.04, !MSB !2, !LSB !3, !extendFrom !2*/
		mvt_4_scevgep7 = (arg_y1_reg + (4 * mvt_4_j04_reg));
end
always @(*) begin
	/* mvt: %4*/
	/*   %6 = load i32* %scevgep8, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		mvt_4_6 = main_0_A_out_a;
end
always @(*) begin
	/* mvt: %4*/
	/*   %7 = load i32* %scevgep7, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		mvt_4_7 = main_0_y1_out_a;
end
always @(posedge clk) begin
	/* mvt: %4*/
	/*   %7 = load i32* %scevgep7, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_mvt_BB__4_4)) begin
		mvt_4_7_reg <= mvt_4_7;
	end
end
always @(*) begin
	mvt_4_8 = legup_mult_mvt_4_8_out;
end
always @(*) begin
	/* mvt: %4*/
	/*   %9 = add nsw i32 %tmp.05, %8, !MSB !6, !LSB !3, !extendFrom !6*/
		mvt_4_9 = (mvt_4_tmp05_reg + mvt_4_8);
end
always @(*) begin
	/* mvt: %4*/
	/*   %10 = add nsw i32 %j.04, 1, !MSB !6, !LSB !3, !extendFrom !6*/
		mvt_4_10 = (mvt_4_j04_reg + 32'd1);
end
always @(posedge clk) begin
	/* mvt: %4*/
	/*   %10 = add nsw i32 %j.04, 1, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_mvt_BB__4_3)) begin
		mvt_4_10_reg <= mvt_4_10;
	end
end
always @(*) begin
	/* mvt: %4*/
	/*   %exitcond = icmp eq i32 %10, 32, !MSB !3, !LSB !3, !extendFrom !3*/
		mvt_4_exitcond = (mvt_4_10_reg == 32'd32);
end
always @(posedge clk) begin
	/* mvt: %4*/
	/*   %exitcond = icmp eq i32 %10, 32, !MSB !3, !LSB !3, !extendFrom !3*/
	if ((cur_state == LEGUP_F_mvt_BB__4_4)) begin
		mvt_4_exitcond_reg <= mvt_4_exitcond;
	end
end
always @(*) begin
	/* mvt: %11*/
	/*   %.lcssa1 = phi i32 [ %9, %4 ], !MSB !6, !LSB !3, !extendFrom !6*/
		mvt_11_lcssa1 = mvt_4_9;
end
always @(posedge clk) begin
	/* mvt: %11*/
	/*   %.lcssa1 = phi i32 [ %9, %4 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_mvt_BB__4_6) & (fsm_stall == 1'd0)) & (mvt_4_exitcond_reg == 1'd1))) begin
		mvt_11_lcssa1_reg <= mvt_11_lcssa1;
	end
end
always @(*) begin
	/* mvt: %11*/
	/*   %12 = add nsw i32 %i.06, 1, !MSB !7, !LSB !3, !extendFrom !7*/
		mvt_11_12 = ({1'd0,mvt_1_i06_reg} + 32'd1);
end
always @(posedge clk) begin
	/* mvt: %11*/
	/*   %12 = add nsw i32 %i.06, 1, !MSB !7, !LSB !3, !extendFrom !7*/
	if ((cur_state == LEGUP_F_mvt_BB__11_7)) begin
		mvt_11_12_reg <= mvt_11_12;
	end
end
always @(*) begin
	/* mvt: %11*/
	/*   %exitcond14 = icmp eq i32 %12, 32, !MSB !3, !LSB !3, !extendFrom !3*/
		mvt_11_exitcond14 = (mvt_11_12_reg == 32'd32);
end
always @(*) begin
	/* mvt: %.preheader.preheader*/
	/*   %i.13 = phi i32 [ %22, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	if (((cur_state == LEGUP_F_mvt_BB_preheaderpreheaderpreheader_9) & (fsm_stall == 1'd0))) begin
		mvt_preheaderpreheader_i13 = 32'd0;
	end
	/* mvt: %.preheader.preheader*/
	/*   %i.13 = phi i32 [ %22, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	else /* if ((((cur_state == LEGUP_F_mvt_BB_preheader_17) & (fsm_stall == 1'd0)) & (mvt_preheader_exitcond7 == 1'd0))) */ begin
		mvt_preheaderpreheader_i13 = mvt_preheader_22_reg;
	end
end
always @(posedge clk) begin
	/* mvt: %.preheader.preheader*/
	/*   %i.13 = phi i32 [ %22, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	if (((cur_state == LEGUP_F_mvt_BB_preheaderpreheaderpreheader_9) & (fsm_stall == 1'd0))) begin
		mvt_preheaderpreheader_i13_reg <= mvt_preheaderpreheader_i13;
	end
	/* mvt: %.preheader.preheader*/
	/*   %i.13 = phi i32 [ %22, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !4, !LSB !3, !extendFrom !4*/
	if ((((cur_state == LEGUP_F_mvt_BB_preheader_17) & (fsm_stall == 1'd0)) & (mvt_preheader_exitcond7 == 1'd0))) begin
		mvt_preheaderpreheader_i13_reg <= mvt_preheaderpreheader_i13;
	end
end
always @(*) begin
	/* mvt: %.preheader.preheader*/
	/*   %scevgep5 = getelementptr i32* %x2, i32 %i.13, !MSB !2, !LSB !3, !extendFrom !2*/
		mvt_preheaderpreheader_scevgep5 = (arg_x2_reg + (4 * {26'd0,mvt_preheaderpreheader_i13_reg}));
end
always @(posedge clk) begin
	/* mvt: %.preheader.preheader*/
	/*   %scevgep5 = getelementptr i32* %x2, i32 %i.13, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_mvt_BB_preheaderpreheader_10)) begin
		mvt_preheaderpreheader_scevgep5_reg <= mvt_preheaderpreheader_scevgep5;
	end
end
always @(*) begin
	/* mvt: %.preheader.preheader*/
	/*   %13 = load i32* %scevgep5, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		mvt_preheaderpreheader_13 = main_0_x2_out_a;
end
always @(*) begin
	/* mvt: %14*/
	/*   %tmp1.02 = phi i32 [ %13, %.preheader.preheader ], [ %20, %14 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_mvt_BB_preheaderpreheader_11) & (fsm_stall == 1'd0))) begin
		mvt_14_tmp102 = mvt_preheaderpreheader_13;
	end
	/* mvt: %14*/
	/*   %tmp1.02 = phi i32 [ %13, %.preheader.preheader ], [ %20, %14 ], !MSB !6, !LSB !3, !extendFrom !6*/
	else /* if ((((cur_state == LEGUP_F_mvt_BB__14_15) & (fsm_stall == 1'd0)) & (mvt_14_exitcond3_reg == 1'd0))) */ begin
		mvt_14_tmp102 = mvt_14_20;
	end
end
always @(posedge clk) begin
	/* mvt: %14*/
	/*   %tmp1.02 = phi i32 [ %13, %.preheader.preheader ], [ %20, %14 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_mvt_BB_preheaderpreheader_11) & (fsm_stall == 1'd0))) begin
		mvt_14_tmp102_reg <= mvt_14_tmp102;
	end
	/* mvt: %14*/
	/*   %tmp1.02 = phi i32 [ %13, %.preheader.preheader ], [ %20, %14 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_mvt_BB__14_15) & (fsm_stall == 1'd0)) & (mvt_14_exitcond3_reg == 1'd0))) begin
		mvt_14_tmp102_reg <= mvt_14_tmp102;
	end
end
always @(*) begin
	/* mvt: %14*/
	/*   %j.11 = phi i32 [ 0, %.preheader.preheader ], [ %21, %14 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_mvt_BB_preheaderpreheader_11) & (fsm_stall == 1'd0))) begin
		mvt_14_j11 = 32'd0;
	end
	/* mvt: %14*/
	/*   %j.11 = phi i32 [ 0, %.preheader.preheader ], [ %21, %14 ], !MSB !6, !LSB !3, !extendFrom !6*/
	else /* if ((((cur_state == LEGUP_F_mvt_BB__14_15) & (fsm_stall == 1'd0)) & (mvt_14_exitcond3_reg == 1'd0))) */ begin
		mvt_14_j11 = mvt_14_21_reg;
	end
end
always @(posedge clk) begin
	/* mvt: %14*/
	/*   %j.11 = phi i32 [ 0, %.preheader.preheader ], [ %21, %14 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if (((cur_state == LEGUP_F_mvt_BB_preheaderpreheader_11) & (fsm_stall == 1'd0))) begin
		mvt_14_j11_reg <= mvt_14_j11;
	end
	/* mvt: %14*/
	/*   %j.11 = phi i32 [ 0, %.preheader.preheader ], [ %21, %14 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_mvt_BB__14_15) & (fsm_stall == 1'd0)) & (mvt_14_exitcond3_reg == 1'd0))) begin
		mvt_14_j11_reg <= mvt_14_j11;
	end
end
always @(*) begin
	/* mvt: %14*/
	/*   %15 = mul i32 %j.11, 32, !MSB !6, !LSB !4, !extendFrom !6*/
		mvt_14_15 = (mvt_14_j11_reg * 32'd32);
end
always @(*) begin
	/* mvt: %14*/
	/*   %16 = add i32 %i.13, %15, !MSB !6, !LSB !3, !extendFrom !6*/
		mvt_14_16 = ({26'd0,mvt_preheaderpreheader_i13_reg} + mvt_14_15);
end
always @(posedge clk) begin
	/* mvt: %14*/
	/*   %16 = add i32 %i.13, %15, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_mvt_BB__14_12)) begin
		mvt_14_16_reg <= mvt_14_16;
	end
end
always @(*) begin
	/* mvt: %14*/
	/*   %scevgep3 = getelementptr i32* %A, i32 %16, !MSB !2, !LSB !3, !extendFrom !2*/
		mvt_14_scevgep3 = (arg_A_reg + (4 * mvt_14_16_reg));
end
always @(*) begin
	/* mvt: %14*/
	/*   %scevgep = getelementptr i32* %y2, i32 %j.11, !MSB !2, !LSB !3, !extendFrom !2*/
		mvt_14_scevgep = (arg_y2_reg + (4 * mvt_14_j11_reg));
end
always @(*) begin
	/* mvt: %14*/
	/*   %17 = load i32* %scevgep3, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		mvt_14_17 = main_0_A_out_a;
end
always @(*) begin
	/* mvt: %14*/
	/*   %18 = load i32* %scevgep, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
		mvt_14_18 = main_0_y2_out_a;
end
always @(posedge clk) begin
	/* mvt: %14*/
	/*   %18 = load i32* %scevgep, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_mvt_BB__14_13)) begin
		mvt_14_18_reg <= mvt_14_18;
	end
end
always @(*) begin
	mvt_14_19 = legup_mult_mvt_14_19_out;
end
always @(*) begin
	/* mvt: %14*/
	/*   %20 = add nsw i32 %tmp1.02, %19, !MSB !6, !LSB !3, !extendFrom !6*/
		mvt_14_20 = (mvt_14_tmp102_reg + mvt_14_19);
end
always @(*) begin
	/* mvt: %14*/
	/*   %21 = add nsw i32 %j.11, 1, !MSB !6, !LSB !3, !extendFrom !6*/
		mvt_14_21 = (mvt_14_j11_reg + 32'd1);
end
always @(posedge clk) begin
	/* mvt: %14*/
	/*   %21 = add nsw i32 %j.11, 1, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_mvt_BB__14_12)) begin
		mvt_14_21_reg <= mvt_14_21;
	end
end
always @(*) begin
	/* mvt: %14*/
	/*   %exitcond3 = icmp eq i32 %21, 32, !MSB !3, !LSB !3, !extendFrom !3*/
		mvt_14_exitcond3 = (mvt_14_21_reg == 32'd32);
end
always @(posedge clk) begin
	/* mvt: %14*/
	/*   %exitcond3 = icmp eq i32 %21, 32, !MSB !3, !LSB !3, !extendFrom !3*/
	if ((cur_state == LEGUP_F_mvt_BB__14_13)) begin
		mvt_14_exitcond3_reg <= mvt_14_exitcond3;
	end
end
always @(*) begin
	/* mvt: %.preheader*/
	/*   %.lcssa = phi i32 [ %20, %14 ], !MSB !6, !LSB !3, !extendFrom !6*/
		mvt_preheader_lcssa = mvt_14_20;
end
always @(posedge clk) begin
	/* mvt: %.preheader*/
	/*   %.lcssa = phi i32 [ %20, %14 ], !MSB !6, !LSB !3, !extendFrom !6*/
	if ((((cur_state == LEGUP_F_mvt_BB__14_15) & (fsm_stall == 1'd0)) & (mvt_14_exitcond3_reg == 1'd1))) begin
		mvt_preheader_lcssa_reg <= mvt_preheader_lcssa;
	end
end
always @(*) begin
	/* mvt: %.preheader*/
	/*   %22 = add nsw i32 %i.13, 1, !MSB !7, !LSB !3, !extendFrom !7*/
		mvt_preheader_22 = ({1'd0,mvt_preheaderpreheader_i13_reg} + 32'd1);
end
always @(posedge clk) begin
	/* mvt: %.preheader*/
	/*   %22 = add nsw i32 %i.13, 1, !MSB !7, !LSB !3, !extendFrom !7*/
	if ((cur_state == LEGUP_F_mvt_BB_preheader_16)) begin
		mvt_preheader_22_reg <= mvt_preheader_22;
	end
end
always @(*) begin
	/* mvt: %.preheader*/
	/*   %exitcond7 = icmp eq i32 %22, 32, !MSB !3, !LSB !3, !extendFrom !3*/
		mvt_preheader_exitcond7 = (mvt_preheader_22_reg == 32'd32);
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
	legup_mult_1_unsigned_32_32_1_0_clken = legup_mult_mvt_4_8_en;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_0_dataa = mvt_4_6;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_0_datab = mvt_4_7_reg;
end
always @(*) begin
	legup_mult_mvt_4_8_out_actual = legup_mult_1_unsigned_32_32_1_0_result;
end
always @(*) begin
	legup_mult_mvt_4_8_out = legup_mult_mvt_4_8_out_actual[31:0];
end
always @(*) begin
	legup_mult_mvt_4_8_en = ~(fsm_stall);
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
	legup_mult_1_unsigned_32_32_1_1_clken = legup_mult_mvt_14_19_en;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_1_dataa = mvt_14_17;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_1_datab = mvt_14_18_reg;
end
always @(*) begin
	legup_mult_mvt_14_19_out_actual = legup_mult_1_unsigned_32_32_1_1_result;
end
always @(*) begin
	legup_mult_mvt_14_19_out = legup_mult_mvt_14_19_out_actual[31:0];
end
always @(*) begin
	legup_mult_mvt_14_19_en = ~(fsm_stall);
end
always @(posedge clk) begin
	if ((cur_state == LEGUP_0)) begin
		finish <= 1'd0;
	end
	/* mvt: %23*/
	/*   ret void, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_mvt_BB__23_18)) begin
		finish <= (fsm_stall == 1'd0);
	end
end
always @(*) begin
	main_0_x1_write_enable_a = 1'd0;
	/* mvt: %11*/
	/*   store i32 %.lcssa1, i32* %scevgep11, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_mvt_BB__11_7)) begin
		main_0_x1_write_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_x1_in_a = 0;
	/* mvt: %11*/
	/*   store i32 %.lcssa1, i32* %scevgep11, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_mvt_BB__11_7)) begin
		main_0_x1_in_a = mvt_11_lcssa1_reg;
	end
end
assign main_0_x1_byteena_a = 1'd1;
always @(*) begin
	main_0_x1_enable_a = 1'd0;
	/* mvt: %1*/
	/*   %3 = load i32* %scevgep11, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_mvt_BB__1_1)) begin
		main_0_x1_enable_a = 1'd1;
	end
	/* mvt: %11*/
	/*   store i32 %.lcssa1, i32* %scevgep11, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_mvt_BB__11_7)) begin
		main_0_x1_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_x1_address_a = 5'd0;
	/* mvt: %1*/
	/*   %3 = load i32* %scevgep11, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_mvt_BB__1_1)) begin
		main_0_x1_address_a = (mvt_1_scevgep11 >>> 3'd2);
	end
	/* mvt: %11*/
	/*   store i32 %.lcssa1, i32* %scevgep11, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_mvt_BB__11_7)) begin
		main_0_x1_address_a = (mvt_1_scevgep11_reg >>> 3'd2);
	end
end
assign main_0_x1_write_enable_b = 1'd0;
assign main_0_x1_in_b = 0;
assign main_0_x1_byteena_b = 1'd1;
assign main_0_x1_enable_b = 1'd0;
assign main_0_x1_address_b = 5'd0;
assign main_0_y1_write_enable_a = 1'd0;
assign main_0_y1_in_a = 0;
assign main_0_y1_byteena_a = 1'd1;
always @(*) begin
	main_0_y1_enable_a = 1'd0;
	/* mvt: %4*/
	/*   %7 = load i32* %scevgep7, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_mvt_BB__4_3)) begin
		main_0_y1_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_y1_address_a = 5'd0;
	/* mvt: %4*/
	/*   %7 = load i32* %scevgep7, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_mvt_BB__4_3)) begin
		main_0_y1_address_a = (mvt_4_scevgep7 >>> 3'd2);
	end
end
assign main_0_y1_write_enable_b = 1'd0;
assign main_0_y1_in_b = 0;
assign main_0_y1_byteena_b = 1'd1;
assign main_0_y1_enable_b = 1'd0;
assign main_0_y1_address_b = 5'd0;
assign main_0_A_write_enable_a = 1'd0;
assign main_0_A_in_a = 0;
assign main_0_A_byteena_a = 1'd1;
always @(*) begin
	main_0_A_enable_a = 1'd0;
	/* mvt: %4*/
	/*   %6 = load i32* %scevgep8, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_mvt_BB__4_4)) begin
		main_0_A_enable_a = 1'd1;
	end
	/* mvt: %14*/
	/*   %17 = load i32* %scevgep3, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_mvt_BB__14_13)) begin
		main_0_A_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_A_address_a = 10'd0;
	/* mvt: %4*/
	/*   %6 = load i32* %scevgep8, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_mvt_BB__4_4)) begin
		main_0_A_address_a = (mvt_4_scevgep8 >>> 3'd2);
	end
	/* mvt: %14*/
	/*   %17 = load i32* %scevgep3, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_mvt_BB__14_13)) begin
		main_0_A_address_a = (mvt_14_scevgep3 >>> 3'd2);
	end
end
assign main_0_A_write_enable_b = 1'd0;
assign main_0_A_in_b = 0;
assign main_0_A_byteena_b = 1'd1;
assign main_0_A_enable_b = 1'd0;
assign main_0_A_address_b = 10'd0;
always @(*) begin
	main_0_x2_write_enable_a = 1'd0;
	/* mvt: %.preheader*/
	/*   store i32 %.lcssa, i32* %scevgep5, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_mvt_BB_preheader_16)) begin
		main_0_x2_write_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_x2_in_a = 0;
	/* mvt: %.preheader*/
	/*   store i32 %.lcssa, i32* %scevgep5, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_mvt_BB_preheader_16)) begin
		main_0_x2_in_a = mvt_preheader_lcssa_reg;
	end
end
assign main_0_x2_byteena_a = 1'd1;
always @(*) begin
	main_0_x2_enable_a = 1'd0;
	/* mvt: %.preheader.preheader*/
	/*   %13 = load i32* %scevgep5, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_mvt_BB_preheaderpreheader_10)) begin
		main_0_x2_enable_a = 1'd1;
	end
	/* mvt: %.preheader*/
	/*   store i32 %.lcssa, i32* %scevgep5, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_mvt_BB_preheader_16)) begin
		main_0_x2_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_x2_address_a = 5'd0;
	/* mvt: %.preheader.preheader*/
	/*   %13 = load i32* %scevgep5, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_mvt_BB_preheaderpreheader_10)) begin
		main_0_x2_address_a = (mvt_preheaderpreheader_scevgep5 >>> 3'd2);
	end
	/* mvt: %.preheader*/
	/*   store i32 %.lcssa, i32* %scevgep5, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_mvt_BB_preheader_16)) begin
		main_0_x2_address_a = (mvt_preheaderpreheader_scevgep5_reg >>> 3'd2);
	end
end
assign main_0_x2_write_enable_b = 1'd0;
assign main_0_x2_in_b = 0;
assign main_0_x2_byteena_b = 1'd1;
assign main_0_x2_enable_b = 1'd0;
assign main_0_x2_address_b = 5'd0;
assign main_0_y2_write_enable_a = 1'd0;
assign main_0_y2_in_a = 0;
assign main_0_y2_byteena_a = 1'd1;
always @(*) begin
	main_0_y2_enable_a = 1'd0;
	/* mvt: %14*/
	/*   %18 = load i32* %scevgep, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_mvt_BB__14_12)) begin
		main_0_y2_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_y2_address_a = 5'd0;
	/* mvt: %14*/
	/*   %18 = load i32* %scevgep, align 4, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_mvt_BB__14_12)) begin
		main_0_y2_address_a = (mvt_14_scevgep >>> 3'd2);
	end
end
assign main_0_y2_write_enable_b = 1'd0;
assign main_0_y2_in_b = 0;
assign main_0_y2_byteena_b = 1'd1;
assign main_0_y2_enable_b = 1'd0;
assign main_0_y2_address_b = 5'd0;

endmodule
