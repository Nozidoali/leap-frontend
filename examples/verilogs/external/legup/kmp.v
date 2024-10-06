//----------------------------------------------------------------------------
// LegUp High-Level Synthesis Tool Version 5.0 (http://legup.org)
// Copyright (c) 2009-23 University of Toronto. All Rights Reserved.
// For research and academic purposes only. Commercial use is prohibited.
// Please report bugs at: http://legup.org/bugs
// Please email questions to: legup@eecg.toronto.edu
// Date: Sun Oct  6 18:16:47 2024
// ----------------------------------------------------------------------------
`timescale 1 ns / 1 ns
module kmp
(
	clk,
	clk2x,
	clk1x_follower,
	reset,
	memory_controller_waitrequest,
	start,
	finish,
	arg_pattern,
	arg_input,
	arg_kmpNext,
	main_0_kmpNext_write_enable_a,
	main_0_kmpNext_in_a,
	main_0_kmpNext_byteena_a,
	main_0_kmpNext_enable_a,
	main_0_kmpNext_address_a,
	main_0_kmpNext_out_a,
	main_0_kmpNext_write_enable_b,
	main_0_kmpNext_in_b,
	main_0_kmpNext_byteena_b,
	main_0_kmpNext_enable_b,
	main_0_kmpNext_address_b,
	main_0_kmpNext_out_b,
	main_0_pattern_write_enable_a,
	main_0_pattern_in_a,
	main_0_pattern_byteena_a,
	main_0_pattern_enable_a,
	main_0_pattern_address_a,
	main_0_pattern_out_a,
	main_0_pattern_write_enable_b,
	main_0_pattern_in_b,
	main_0_pattern_byteena_b,
	main_0_pattern_enable_b,
	main_0_pattern_address_b,
	main_0_pattern_out_b,
	main_0_input_write_enable_a,
	main_0_input_in_a,
	main_0_input_byteena_a,
	main_0_input_enable_a,
	main_0_input_address_a,
	main_0_input_out_a,
	main_0_input_write_enable_b,
	main_0_input_in_b,
	main_0_input_byteena_b,
	main_0_input_enable_b,
	main_0_input_address_b,
	main_0_input_out_b
);

parameter [5:0] LEGUP_0 = 6'd0;
parameter [5:0] LEGUP_F_kmp_BB__0_1 = 6'd1;
parameter [5:0] LEGUP_F_kmp_BB__0_2 = 6'd2;
parameter [5:0] LEGUP_F_kmp_BB__1_3 = 6'd3;
parameter [5:0] LEGUP_F_kmp_BB__1_4 = 6'd4;
parameter [5:0] LEGUP_F_kmp_BB_lrph14preheader_5 = 6'd5;
parameter [5:0] LEGUP_F_kmp_BB_lrph14_6 = 6'd6;
parameter [5:0] LEGUP_F_kmp_BB_lrph14_7 = 6'd7;
parameter [5:0] LEGUP_F_kmp_BB__9_8 = 6'd8;
parameter [5:0] LEGUP_F_kmp_BB__9_9 = 6'd9;
parameter [5:0] LEGUP_F_kmp_BB_threadloopexit_10 = 6'd10;
parameter [5:0] LEGUP_F_kmp_BB_thread_11 = 6'd11;
parameter [5:0] LEGUP_F_kmp_BB_thread_12 = 6'd12;
parameter [5:0] LEGUP_F_kmp_BB_threadthreadloopexit_13 = 6'd13;
parameter [5:0] LEGUP_F_kmp_BB_threadthread_14 = 6'd14;
parameter [5:0] LEGUP_F_kmp_BB__14_15 = 6'd15;
parameter [5:0] LEGUP_F_kmp_BB__14_16 = 6'd16;
parameter [5:0] LEGUP_F_kmp_BB_preheaderpreheaderpreheader_17 = 6'd17;
parameter [5:0] LEGUP_F_kmp_BB_preheaderpreheader_18 = 6'd18;
parameter [5:0] LEGUP_F_kmp_BB_preheaderpreheader_19 = 6'd19;
parameter [5:0] LEGUP_F_kmp_BB_lrphpreheader_20 = 6'd20;
parameter [5:0] LEGUP_F_kmp_BB_lrph_21 = 6'd21;
parameter [5:0] LEGUP_F_kmp_BB_lrph_22 = 6'd22;
parameter [5:0] LEGUP_F_kmp_BB__20_23 = 6'd23;
parameter [5:0] LEGUP_F_kmp_BB__20_24 = 6'd24;
parameter [5:0] LEGUP_F_kmp_BB_thread2loopexit_25 = 6'd25;
parameter [5:0] LEGUP_F_kmp_BB_thread2_26 = 6'd26;
parameter [5:0] LEGUP_F_kmp_BB_thread2_27 = 6'd27;
parameter [5:0] LEGUP_F_kmp_BB_threadpresplitloopexit_28 = 6'd28;
parameter [5:0] LEGUP_F_kmp_BB_threadpresplit_29 = 6'd29;
parameter [5:0] LEGUP_F_kmp_BB__27_30 = 6'd30;
parameter [5:0] LEGUP_F_kmp_BB__27_31 = 6'd31;
parameter [5:0] LEGUP_F_kmp_BB_preheader_32 = 6'd32;
parameter [5:0] LEGUP_F_kmp_BB__32_33 = 6'd33;

input  clk;
input  clk2x;
input  clk1x_follower;
input  reset;
input  memory_controller_waitrequest;
input  start;
output reg  finish;
input [31:0] arg_pattern;
input [31:0] arg_input;
input [31:0] arg_kmpNext;
output reg  main_0_kmpNext_write_enable_a;
output reg [31:0] main_0_kmpNext_in_a;
output  main_0_kmpNext_byteena_a;
output reg  main_0_kmpNext_enable_a;
output reg [1:0] main_0_kmpNext_address_a;
input [31:0] main_0_kmpNext_out_a;
output  main_0_kmpNext_write_enable_b;
output [31:0] main_0_kmpNext_in_b;
output  main_0_kmpNext_byteena_b;
output  main_0_kmpNext_enable_b;
output [1:0] main_0_kmpNext_address_b;
input [31:0] main_0_kmpNext_out_b;
output  main_0_pattern_write_enable_a;
output [31:0] main_0_pattern_in_a;
output  main_0_pattern_byteena_a;
output reg  main_0_pattern_enable_a;
output reg [1:0] main_0_pattern_address_a;
input [31:0] main_0_pattern_out_a;
output  main_0_pattern_write_enable_b;
output [31:0] main_0_pattern_in_b;
output  main_0_pattern_byteena_b;
output  main_0_pattern_enable_b;
output [1:0] main_0_pattern_address_b;
input [31:0] main_0_pattern_out_b;
output  main_0_input_write_enable_a;
output [31:0] main_0_input_in_a;
output  main_0_input_byteena_a;
output reg  main_0_input_enable_a;
output reg [9:0] main_0_input_address_a;
input [31:0] main_0_input_out_a;
output  main_0_input_write_enable_b;
output [31:0] main_0_input_in_b;
output  main_0_input_byteena_b;
output  main_0_input_enable_b;
output [9:0] main_0_input_address_b;
input [31:0] main_0_input_out_b;
reg [5:0] cur_state;
reg [5:0] next_state;
reg [31:0] arg_pattern_reg;
reg [31:0] arg_input_reg;
reg [31:0] arg_kmpNext_reg;
reg  fsm_stall;
reg [1:0] kmp_1_indvar;
reg [1:0] kmp_1_indvar_reg;
reg [31:0] kmp_1_k016;
reg [31:0] kmp_1_k016_reg;
reg [2:0] kmp_1_2;
reg [31:0] kmp_1_scevgep6;
reg [31:0] kmp_1_scevgep5;
reg [31:0] kmp_1_scevgep5_reg;
reg [2:0] kmp_1_3;
reg [2:0] kmp_1_3_reg;
reg [31:0] kmp_1_4;
reg [31:0] kmp_1_4_reg;
reg  kmp_1_5;
reg  kmp_1_5_reg;
reg [31:0] kmp_lrph14_k113;
reg [31:0] kmp_lrph14_k113_reg;
reg [31:0] kmp_lrph14_6;
reg [31:0] kmp_lrph14_7;
reg  kmp_lrph14_8;
reg [31:0] kmp_9_10;
reg  kmp_9_11;
reg [31:0] kmp_threadloopexit_lcssa3;
reg [31:0] kmp_threadloopexit_lcssa3_reg;
reg [31:0] kmp_thread_k1lcssa;
reg [31:0] kmp_thread_k1lcssa_reg;
reg [31:0] kmp_thread_phitransinsert;
reg [31:0] kmp_thread_pre;
reg  kmp_thread_12;
reg [31:0] kmp_threadthreadloopexit_k113lcssa;
reg [31:0] kmp_threadthreadloopexit_k113lcssa_reg;
reg [31:0] kmp_threadthread_k13739;
reg [31:0] kmp_threadthread_k13739_reg;
reg [31:0] kmp_threadthread_13;
reg [31:0] kmp_14_k2;
reg [31:0] kmp_14_k2_reg;
reg  kmp_14_exitcond8;
reg  kmp_14_exitcond8_reg;
reg [9:0] kmp_preheaderpreheader_i012;
reg [9:0] kmp_preheaderpreheader_i012_reg;
reg [31:0] kmp_preheaderpreheader_q111;
reg [31:0] kmp_preheaderpreheader_q111_reg;
reg [31:0] kmp_preheaderpreheader_scevgep;
reg [31:0] kmp_preheaderpreheader_15;
reg [31:0] kmp_preheaderpreheader_15_reg;
reg  kmp_preheaderpreheader_16;
reg  kmp_preheaderpreheader_16_reg;
reg [31:0] kmp_lrph_q29;
reg [31:0] kmp_lrph_q29_reg;
reg [31:0] kmp_lrph_17;
reg [31:0] kmp_lrph_18;
reg  kmp_lrph_19;
reg [31:0] kmp_20_21;
reg [31:0] kmp_20_22;
reg  kmp_20_23;
reg [31:0] kmp_thread2loopexit_lcssa;
reg [31:0] kmp_thread2loopexit_lcssa_reg;
reg [31:0] kmp_thread2_q2lcssa;
reg [31:0] kmp_thread2_q2lcssa_reg;
reg [31:0] kmp_thread2_phitransinsert32;
reg [31:0] kmp_thread2_pre33;
reg  kmp_thread2_24;
reg [31:0] kmp_threadpresplitloopexit_q29lcssa;
reg [31:0] kmp_threadpresplitloopexit_q29lcssa_reg;
reg [31:0] kmp_threadpresplit_q23540;
reg [31:0] kmp_threadpresplit_q23540_reg;
reg [31:0] kmp_threadpresplit_25;
reg  kmp_threadpresplit_26;
reg [31:0] kmp_27_29;
reg [31:0] kmp_27_30;
reg [31:0] kmp_preheader_q4;
reg [31:0] kmp_preheader_q4_reg;
reg [10:0] kmp_preheader_31;
reg  kmp_preheader_exitcond5;
reg [1:0] kmp_1_5_op1_temp;
reg [1:0] kmp_9_11_op1_temp;
reg [1:0] kmp_preheaderpreheader_16_op1_temp;
reg [1:0] kmp_20_23_op1_temp;
reg [2:0] kmp_threadpresplit_26_op1_temp;

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
		next_state = LEGUP_F_kmp_BB__0_1;
LEGUP_F_kmp_BB__0_1:
		next_state = LEGUP_F_kmp_BB__0_2;
LEGUP_F_kmp_BB__0_2:
		next_state = LEGUP_F_kmp_BB__1_3;
LEGUP_F_kmp_BB__14_15:
		next_state = LEGUP_F_kmp_BB__14_16;
LEGUP_F_kmp_BB__14_16:
	if ((fsm_stall == 1'd0) && (kmp_14_exitcond8_reg == 1'd1))
		next_state = LEGUP_F_kmp_BB_preheaderpreheaderpreheader_17;
	else if ((fsm_stall == 1'd0) && (kmp_14_exitcond8_reg == 1'd0))
		next_state = LEGUP_F_kmp_BB__1_3;
LEGUP_F_kmp_BB__1_3:
		next_state = LEGUP_F_kmp_BB__1_4;
LEGUP_F_kmp_BB__1_4:
	if ((fsm_stall == 1'd0) && (kmp_1_5_reg == 1'd1))
		next_state = LEGUP_F_kmp_BB_lrph14preheader_5;
	else if ((fsm_stall == 1'd0) && (kmp_1_5_reg == 1'd0))
		next_state = LEGUP_F_kmp_BB_thread_11;
LEGUP_F_kmp_BB__20_23:
		next_state = LEGUP_F_kmp_BB__20_24;
LEGUP_F_kmp_BB__20_24:
	if ((fsm_stall == 1'd0) && (kmp_20_23 == 1'd1))
		next_state = LEGUP_F_kmp_BB_lrph_21;
	else if ((fsm_stall == 1'd0) && (kmp_20_23 == 1'd0))
		next_state = LEGUP_F_kmp_BB_thread2loopexit_25;
LEGUP_F_kmp_BB__27_30:
		next_state = LEGUP_F_kmp_BB__27_31;
LEGUP_F_kmp_BB__27_31:
		next_state = LEGUP_F_kmp_BB_preheader_32;
LEGUP_F_kmp_BB__32_33:
		next_state = LEGUP_0;
LEGUP_F_kmp_BB__9_8:
		next_state = LEGUP_F_kmp_BB__9_9;
LEGUP_F_kmp_BB__9_9:
	if ((fsm_stall == 1'd0) && (kmp_9_11 == 1'd1))
		next_state = LEGUP_F_kmp_BB_lrph14_6;
	else if ((fsm_stall == 1'd0) && (kmp_9_11 == 1'd0))
		next_state = LEGUP_F_kmp_BB_threadloopexit_10;
LEGUP_F_kmp_BB_lrph14_6:
		next_state = LEGUP_F_kmp_BB_lrph14_7;
LEGUP_F_kmp_BB_lrph14_7:
	if ((fsm_stall == 1'd0) && (kmp_lrph14_8 == 1'd1))
		next_state = LEGUP_F_kmp_BB_threadthreadloopexit_13;
	else if ((fsm_stall == 1'd0) && (kmp_lrph14_8 == 1'd0))
		next_state = LEGUP_F_kmp_BB__9_8;
LEGUP_F_kmp_BB_lrph14preheader_5:
		next_state = LEGUP_F_kmp_BB_lrph14_6;
LEGUP_F_kmp_BB_lrph_21:
		next_state = LEGUP_F_kmp_BB_lrph_22;
LEGUP_F_kmp_BB_lrph_22:
	if ((fsm_stall == 1'd0) && (kmp_lrph_19 == 1'd1))
		next_state = LEGUP_F_kmp_BB_threadpresplitloopexit_28;
	else if ((fsm_stall == 1'd0) && (kmp_lrph_19 == 1'd0))
		next_state = LEGUP_F_kmp_BB__20_23;
LEGUP_F_kmp_BB_lrphpreheader_20:
		next_state = LEGUP_F_kmp_BB_lrph_21;
LEGUP_F_kmp_BB_preheader_32:
	if ((fsm_stall == 1'd0) && (kmp_preheader_exitcond5 == 1'd1))
		next_state = LEGUP_F_kmp_BB__32_33;
	else if ((fsm_stall == 1'd0) && (kmp_preheader_exitcond5 == 1'd0))
		next_state = LEGUP_F_kmp_BB_preheaderpreheader_18;
LEGUP_F_kmp_BB_preheaderpreheader_18:
		next_state = LEGUP_F_kmp_BB_preheaderpreheader_19;
LEGUP_F_kmp_BB_preheaderpreheader_19:
	if ((fsm_stall == 1'd0) && (kmp_preheaderpreheader_16_reg == 1'd1))
		next_state = LEGUP_F_kmp_BB_lrphpreheader_20;
	else if ((fsm_stall == 1'd0) && (kmp_preheaderpreheader_16_reg == 1'd0))
		next_state = LEGUP_F_kmp_BB_thread2_26;
LEGUP_F_kmp_BB_preheaderpreheaderpreheader_17:
		next_state = LEGUP_F_kmp_BB_preheaderpreheader_18;
LEGUP_F_kmp_BB_thread2_26:
		next_state = LEGUP_F_kmp_BB_thread2_27;
LEGUP_F_kmp_BB_thread2_27:
	if ((fsm_stall == 1'd0) && (kmp_thread2_24 == 1'd1))
		next_state = LEGUP_F_kmp_BB_threadpresplit_29;
	else if ((fsm_stall == 1'd0) && (kmp_thread2_24 == 1'd0))
		next_state = LEGUP_F_kmp_BB_preheader_32;
LEGUP_F_kmp_BB_thread2loopexit_25:
		next_state = LEGUP_F_kmp_BB_thread2_26;
LEGUP_F_kmp_BB_thread_11:
		next_state = LEGUP_F_kmp_BB_thread_12;
LEGUP_F_kmp_BB_thread_12:
	if ((fsm_stall == 1'd0) && (kmp_thread_12 == 1'd1))
		next_state = LEGUP_F_kmp_BB_threadthread_14;
	else if ((fsm_stall == 1'd0) && (kmp_thread_12 == 1'd0))
		next_state = LEGUP_F_kmp_BB__14_15;
LEGUP_F_kmp_BB_threadloopexit_10:
		next_state = LEGUP_F_kmp_BB_thread_11;
LEGUP_F_kmp_BB_threadpresplit_29:
	if ((fsm_stall == 1'd0) && (kmp_threadpresplit_26 == 1'd1))
		next_state = LEGUP_F_kmp_BB__27_30;
	else if ((fsm_stall == 1'd0) && (kmp_threadpresplit_26 == 1'd0))
		next_state = LEGUP_F_kmp_BB_preheader_32;
LEGUP_F_kmp_BB_threadpresplitloopexit_28:
		next_state = LEGUP_F_kmp_BB_threadpresplit_29;
LEGUP_F_kmp_BB_threadthread_14:
		next_state = LEGUP_F_kmp_BB__14_15;
LEGUP_F_kmp_BB_threadthreadloopexit_13:
		next_state = LEGUP_F_kmp_BB_threadthread_14;
default:
	next_state = cur_state;
endcase

end
always @(posedge clk) begin
	if (start) begin
		arg_pattern_reg <= arg_pattern;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_input_reg <= arg_input;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_kmpNext_reg <= arg_kmpNext;
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
	/* kmp: %1*/
	/*   %indvar = phi i32 [ %3, %14 ], [ 0, %0 ], !MSB !4, !LSB !3, !extendFrom !4*/
	if (((cur_state == LEGUP_F_kmp_BB__0_2) & (fsm_stall == 1'd0))) begin
		kmp_1_indvar = 32'd0;
	end
	/* kmp: %1*/
	/*   %indvar = phi i32 [ %3, %14 ], [ 0, %0 ], !MSB !4, !LSB !3, !extendFrom !4*/
	else /* if ((((cur_state == LEGUP_F_kmp_BB__14_16) & (fsm_stall == 1'd0)) & (kmp_14_exitcond8_reg == 1'd0))) */ begin
		kmp_1_indvar = kmp_1_3_reg;
	end
end
always @(posedge clk) begin
	/* kmp: %1*/
	/*   %indvar = phi i32 [ %3, %14 ], [ 0, %0 ], !MSB !4, !LSB !3, !extendFrom !4*/
	if (((cur_state == LEGUP_F_kmp_BB__0_2) & (fsm_stall == 1'd0))) begin
		kmp_1_indvar_reg <= kmp_1_indvar;
	end
	/* kmp: %1*/
	/*   %indvar = phi i32 [ %3, %14 ], [ 0, %0 ], !MSB !4, !LSB !3, !extendFrom !4*/
	if ((((cur_state == LEGUP_F_kmp_BB__14_16) & (fsm_stall == 1'd0)) & (kmp_14_exitcond8_reg == 1'd0))) begin
		kmp_1_indvar_reg <= kmp_1_indvar;
	end
end
always @(*) begin
	/* kmp: %1*/
	/*   %k.016 = phi i32 [ 0, %0 ], [ %k.2, %14 ], !MSB !5, !LSB !3, !extendFrom !5*/
	if (((cur_state == LEGUP_F_kmp_BB__0_2) & (fsm_stall == 1'd0))) begin
		kmp_1_k016 = 32'd0;
	end
	/* kmp: %1*/
	/*   %k.016 = phi i32 [ 0, %0 ], [ %k.2, %14 ], !MSB !5, !LSB !3, !extendFrom !5*/
	else /* if ((((cur_state == LEGUP_F_kmp_BB__14_16) & (fsm_stall == 1'd0)) & (kmp_14_exitcond8_reg == 1'd0))) */ begin
		kmp_1_k016 = kmp_14_k2_reg;
	end
end
always @(posedge clk) begin
	/* kmp: %1*/
	/*   %k.016 = phi i32 [ 0, %0 ], [ %k.2, %14 ], !MSB !5, !LSB !3, !extendFrom !5*/
	if (((cur_state == LEGUP_F_kmp_BB__0_2) & (fsm_stall == 1'd0))) begin
		kmp_1_k016_reg <= kmp_1_k016;
	end
	/* kmp: %1*/
	/*   %k.016 = phi i32 [ 0, %0 ], [ %k.2, %14 ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB__14_16) & (fsm_stall == 1'd0)) & (kmp_14_exitcond8_reg == 1'd0))) begin
		kmp_1_k016_reg <= kmp_1_k016;
	end
end
always @(*) begin
	/* kmp: %1*/
	/*   %2 = add i32 %indvar, 1, !MSB !6, !LSB !3, !extendFrom !6*/
		kmp_1_2 = ({1'd0,kmp_1_indvar_reg} + 32'd1);
end
always @(*) begin
	/* kmp: %1*/
	/*   %scevgep6 = getelementptr i32* %pattern, i32 %2, !MSB !2, !LSB !3, !extendFrom !2*/
		kmp_1_scevgep6 = (arg_pattern_reg + (4 * {29'd0,kmp_1_2}));
end
always @(*) begin
	/* kmp: %1*/
	/*   %scevgep5 = getelementptr i32* %kmpNext, i32 %2, !MSB !2, !LSB !3, !extendFrom !2*/
		kmp_1_scevgep5 = (arg_kmpNext_reg + (4 * {29'd0,kmp_1_2}));
end
always @(posedge clk) begin
	/* kmp: %1*/
	/*   %scevgep5 = getelementptr i32* %kmpNext, i32 %2, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kmp_BB__1_3)) begin
		kmp_1_scevgep5_reg <= kmp_1_scevgep5;
	end
end
always @(*) begin
	/* kmp: %1*/
	/*   %3 = add i32 %indvar, 1, !MSB !6, !LSB !3, !extendFrom !6*/
		kmp_1_3 = ({1'd0,kmp_1_indvar_reg} + 32'd1);
end
always @(posedge clk) begin
	/* kmp: %1*/
	/*   %3 = add i32 %indvar, 1, !MSB !6, !LSB !3, !extendFrom !6*/
	if ((cur_state == LEGUP_F_kmp_BB__1_3)) begin
		kmp_1_3_reg <= kmp_1_3;
	end
end
always @(*) begin
	/* kmp: %1*/
	/*   %4 = load i32* %scevgep6, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
		kmp_1_4 = main_0_pattern_out_a;
end
always @(posedge clk) begin
	/* kmp: %1*/
	/*   %4 = load i32* %scevgep6, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB__1_4)) begin
		kmp_1_4_reg <= kmp_1_4;
	end
end
always @(*) begin
	/* kmp: %1*/
	/*   %5 = icmp sgt i32 %k.016, 0, !MSB !3, !LSB !3, !extendFrom !3*/
		kmp_1_5 = ((kmp_1_k016_reg) > ({30'd0,kmp_1_5_op1_temp}));
end
always @(posedge clk) begin
	/* kmp: %1*/
	/*   %5 = icmp sgt i32 %k.016, 0, !MSB !3, !LSB !3, !extendFrom !3*/
	if ((cur_state == LEGUP_F_kmp_BB__1_3)) begin
		kmp_1_5_reg <= kmp_1_5;
	end
end
always @(*) begin
	/* kmp: %.lr.ph14*/
	/*   %k.113 = phi i32 [ %10, %9 ], [ %k.016, %.lr.ph14.preheader ], !MSB !5, !LSB !3, !extendFrom !5*/
	if (((cur_state == LEGUP_F_kmp_BB_lrph14preheader_5) & (fsm_stall == 1'd0))) begin
		kmp_lrph14_k113 = kmp_1_k016_reg;
	end
	/* kmp: %.lr.ph14*/
	/*   %k.113 = phi i32 [ %10, %9 ], [ %k.016, %.lr.ph14.preheader ], !MSB !5, !LSB !3, !extendFrom !5*/
	else /* if ((((cur_state == LEGUP_F_kmp_BB__9_9) & (fsm_stall == 1'd0)) & (kmp_9_11 == 1'd1))) */ begin
		kmp_lrph14_k113 = kmp_9_10;
	end
end
always @(posedge clk) begin
	/* kmp: %.lr.ph14*/
	/*   %k.113 = phi i32 [ %10, %9 ], [ %k.016, %.lr.ph14.preheader ], !MSB !5, !LSB !3, !extendFrom !5*/
	if (((cur_state == LEGUP_F_kmp_BB_lrph14preheader_5) & (fsm_stall == 1'd0))) begin
		kmp_lrph14_k113_reg <= kmp_lrph14_k113;
	end
	/* kmp: %.lr.ph14*/
	/*   %k.113 = phi i32 [ %10, %9 ], [ %k.016, %.lr.ph14.preheader ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB__9_9) & (fsm_stall == 1'd0)) & (kmp_9_11 == 1'd1))) begin
		kmp_lrph14_k113_reg <= kmp_lrph14_k113;
	end
end
always @(*) begin
	/* kmp: %.lr.ph14*/
	/*   %6 = getelementptr inbounds i32* %pattern, i32 %k.113, !MSB !2, !LSB !3, !extendFrom !2*/
		kmp_lrph14_6 = (arg_pattern_reg + (4 * kmp_lrph14_k113_reg));
end
always @(*) begin
	/* kmp: %.lr.ph14*/
	/*   %7 = load i32* %6, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
		kmp_lrph14_7 = main_0_pattern_out_a;
end
always @(*) begin
	/* kmp: %.lr.ph14*/
	/*   %8 = icmp eq i32 %7, %4, !MSB !3, !LSB !3, !extendFrom !3*/
		kmp_lrph14_8 = (kmp_lrph14_7 == kmp_1_4_reg);
end
always @(*) begin
	/* kmp: %9*/
	/*   %10 = load i32* %scevgep5, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
		kmp_9_10 = main_0_kmpNext_out_a;
end
always @(*) begin
	/* kmp: %9*/
	/*   %11 = icmp sgt i32 %10, 0, !MSB !3, !LSB !3, !extendFrom !3*/
		kmp_9_11 = ((kmp_9_10) > ({30'd0,kmp_9_11_op1_temp}));
end
always @(*) begin
	/* kmp: %.thread.loopexit*/
	/*   %.lcssa3 = phi i32 [ %10, %9 ], !MSB !5, !LSB !3, !extendFrom !5*/
		kmp_threadloopexit_lcssa3 = kmp_9_10;
end
always @(posedge clk) begin
	/* kmp: %.thread.loopexit*/
	/*   %.lcssa3 = phi i32 [ %10, %9 ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB__9_9) & (fsm_stall == 1'd0)) & (kmp_9_11 == 1'd0))) begin
		kmp_threadloopexit_lcssa3_reg <= kmp_threadloopexit_lcssa3;
	end
end
always @(*) begin
	/* kmp: %.thread*/
	/*   %k.1.lcssa = phi i32 [ %k.016, %1 ], [ %.lcssa3, %.thread.loopexit ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB__1_4) & (fsm_stall == 1'd0)) & (kmp_1_5_reg == 1'd0))) begin
		kmp_thread_k1lcssa = kmp_1_k016_reg;
	end
	/* kmp: %.thread*/
	/*   %k.1.lcssa = phi i32 [ %k.016, %1 ], [ %.lcssa3, %.thread.loopexit ], !MSB !5, !LSB !3, !extendFrom !5*/
	else /* if (((cur_state == LEGUP_F_kmp_BB_threadloopexit_10) & (fsm_stall == 1'd0))) */ begin
		kmp_thread_k1lcssa = kmp_threadloopexit_lcssa3_reg;
	end
end
always @(posedge clk) begin
	/* kmp: %.thread*/
	/*   %k.1.lcssa = phi i32 [ %k.016, %1 ], [ %.lcssa3, %.thread.loopexit ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB__1_4) & (fsm_stall == 1'd0)) & (kmp_1_5_reg == 1'd0))) begin
		kmp_thread_k1lcssa_reg <= kmp_thread_k1lcssa;
	end
	/* kmp: %.thread*/
	/*   %k.1.lcssa = phi i32 [ %k.016, %1 ], [ %.lcssa3, %.thread.loopexit ], !MSB !5, !LSB !3, !extendFrom !5*/
	if (((cur_state == LEGUP_F_kmp_BB_threadloopexit_10) & (fsm_stall == 1'd0))) begin
		kmp_thread_k1lcssa_reg <= kmp_thread_k1lcssa;
	end
end
always @(*) begin
	/* kmp: %.thread*/
	/*   %.phi.trans.insert = getelementptr inbounds i32* %pattern, i32 %k.1.lcssa, !MSB !2, !LSB !3, !extendFrom !2*/
		kmp_thread_phitransinsert = (arg_pattern_reg + (4 * kmp_thread_k1lcssa_reg));
end
always @(*) begin
	/* kmp: %.thread*/
	/*   %.pre = load i32* %.phi.trans.insert, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
		kmp_thread_pre = main_0_pattern_out_a;
end
always @(*) begin
	/* kmp: %.thread*/
	/*   %12 = icmp eq i32 %.pre, %4, !MSB !3, !LSB !3, !extendFrom !3*/
		kmp_thread_12 = (kmp_thread_pre == kmp_1_4_reg);
end
always @(*) begin
	/* kmp: %.thread.thread.loopexit*/
	/*   %k.113.lcssa = phi i32 [ %k.113, %.lr.ph14 ], !MSB !5, !LSB !3, !extendFrom !5*/
		kmp_threadthreadloopexit_k113lcssa = kmp_lrph14_k113_reg;
end
always @(posedge clk) begin
	/* kmp: %.thread.thread.loopexit*/
	/*   %k.113.lcssa = phi i32 [ %k.113, %.lr.ph14 ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB_lrph14_7) & (fsm_stall == 1'd0)) & (kmp_lrph14_8 == 1'd1))) begin
		kmp_threadthreadloopexit_k113lcssa_reg <= kmp_threadthreadloopexit_k113lcssa;
	end
end
always @(*) begin
	/* kmp: %.thread.thread*/
	/*   %k.13739 = phi i32 [ %k.1.lcssa, %.thread ], [ %k.113.lcssa, %.thread.thread.loopexit ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB_thread_12) & (fsm_stall == 1'd0)) & (kmp_thread_12 == 1'd1))) begin
		kmp_threadthread_k13739 = kmp_thread_k1lcssa_reg;
	end
	/* kmp: %.thread.thread*/
	/*   %k.13739 = phi i32 [ %k.1.lcssa, %.thread ], [ %k.113.lcssa, %.thread.thread.loopexit ], !MSB !5, !LSB !3, !extendFrom !5*/
	else /* if (((cur_state == LEGUP_F_kmp_BB_threadthreadloopexit_13) & (fsm_stall == 1'd0))) */ begin
		kmp_threadthread_k13739 = kmp_threadthreadloopexit_k113lcssa_reg;
	end
end
always @(posedge clk) begin
	/* kmp: %.thread.thread*/
	/*   %k.13739 = phi i32 [ %k.1.lcssa, %.thread ], [ %k.113.lcssa, %.thread.thread.loopexit ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB_thread_12) & (fsm_stall == 1'd0)) & (kmp_thread_12 == 1'd1))) begin
		kmp_threadthread_k13739_reg <= kmp_threadthread_k13739;
	end
	/* kmp: %.thread.thread*/
	/*   %k.13739 = phi i32 [ %k.1.lcssa, %.thread ], [ %k.113.lcssa, %.thread.thread.loopexit ], !MSB !5, !LSB !3, !extendFrom !5*/
	if (((cur_state == LEGUP_F_kmp_BB_threadthreadloopexit_13) & (fsm_stall == 1'd0))) begin
		kmp_threadthread_k13739_reg <= kmp_threadthread_k13739;
	end
end
always @(*) begin
	/* kmp: %.thread.thread*/
	/*   %13 = add nsw i32 %k.13739, 1, !MSB !5, !LSB !3, !extendFrom !5*/
		kmp_threadthread_13 = (kmp_threadthread_k13739_reg + 32'd1);
end
always @(*) begin
	/* kmp: %14*/
	/*   %k.2 = phi i32 [ %13, %.thread.thread ], [ %k.1.lcssa, %.thread ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB_thread_12) & (fsm_stall == 1'd0)) & (kmp_thread_12 == 1'd0))) begin
		kmp_14_k2 = kmp_thread_k1lcssa_reg;
	end
	/* kmp: %14*/
	/*   %k.2 = phi i32 [ %13, %.thread.thread ], [ %k.1.lcssa, %.thread ], !MSB !5, !LSB !3, !extendFrom !5*/
	else /* if (((cur_state == LEGUP_F_kmp_BB_threadthread_14) & (fsm_stall == 1'd0))) */ begin
		kmp_14_k2 = kmp_threadthread_13;
	end
end
always @(posedge clk) begin
	/* kmp: %14*/
	/*   %k.2 = phi i32 [ %13, %.thread.thread ], [ %k.1.lcssa, %.thread ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB_thread_12) & (fsm_stall == 1'd0)) & (kmp_thread_12 == 1'd0))) begin
		kmp_14_k2_reg <= kmp_14_k2;
	end
	/* kmp: %14*/
	/*   %k.2 = phi i32 [ %13, %.thread.thread ], [ %k.1.lcssa, %.thread ], !MSB !5, !LSB !3, !extendFrom !5*/
	if (((cur_state == LEGUP_F_kmp_BB_threadthread_14) & (fsm_stall == 1'd0))) begin
		kmp_14_k2_reg <= kmp_14_k2;
	end
end
always @(*) begin
	/* kmp: %14*/
	/*   %exitcond8 = icmp eq i32 %3, 3, !MSB !3, !LSB !3, !extendFrom !3*/
		kmp_14_exitcond8 = (kmp_1_3_reg == 32'd3);
end
always @(posedge clk) begin
	/* kmp: %14*/
	/*   %exitcond8 = icmp eq i32 %3, 3, !MSB !3, !LSB !3, !extendFrom !3*/
	if ((cur_state == LEGUP_F_kmp_BB__14_15)) begin
		kmp_14_exitcond8_reg <= kmp_14_exitcond8;
	end
end
always @(*) begin
	/* kmp: %.preheader.preheader*/
	/*   %i.012 = phi i32 [ %31, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !7, !LSB !3, !extendFrom !7*/
	if (((cur_state == LEGUP_F_kmp_BB_preheaderpreheaderpreheader_17) & (fsm_stall == 1'd0))) begin
		kmp_preheaderpreheader_i012 = 32'd0;
	end
	/* kmp: %.preheader.preheader*/
	/*   %i.012 = phi i32 [ %31, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !7, !LSB !3, !extendFrom !7*/
	else /* if ((((cur_state == LEGUP_F_kmp_BB_preheader_32) & (fsm_stall == 1'd0)) & (kmp_preheader_exitcond5 == 1'd0))) */ begin
		kmp_preheaderpreheader_i012 = kmp_preheader_31;
	end
end
always @(posedge clk) begin
	/* kmp: %.preheader.preheader*/
	/*   %i.012 = phi i32 [ %31, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !7, !LSB !3, !extendFrom !7*/
	if (((cur_state == LEGUP_F_kmp_BB_preheaderpreheaderpreheader_17) & (fsm_stall == 1'd0))) begin
		kmp_preheaderpreheader_i012_reg <= kmp_preheaderpreheader_i012;
	end
	/* kmp: %.preheader.preheader*/
	/*   %i.012 = phi i32 [ %31, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !7, !LSB !3, !extendFrom !7*/
	if ((((cur_state == LEGUP_F_kmp_BB_preheader_32) & (fsm_stall == 1'd0)) & (kmp_preheader_exitcond5 == 1'd0))) begin
		kmp_preheaderpreheader_i012_reg <= kmp_preheaderpreheader_i012;
	end
end
always @(*) begin
	/* kmp: %.preheader.preheader*/
	/*   %q.111 = phi i32 [ %q.4, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !5, !LSB !3, !extendFrom !5*/
	if (((cur_state == LEGUP_F_kmp_BB_preheaderpreheaderpreheader_17) & (fsm_stall == 1'd0))) begin
		kmp_preheaderpreheader_q111 = 32'd0;
	end
	/* kmp: %.preheader.preheader*/
	/*   %q.111 = phi i32 [ %q.4, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !5, !LSB !3, !extendFrom !5*/
	else /* if ((((cur_state == LEGUP_F_kmp_BB_preheader_32) & (fsm_stall == 1'd0)) & (kmp_preheader_exitcond5 == 1'd0))) */ begin
		kmp_preheaderpreheader_q111 = kmp_preheader_q4_reg;
	end
end
always @(posedge clk) begin
	/* kmp: %.preheader.preheader*/
	/*   %q.111 = phi i32 [ %q.4, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !5, !LSB !3, !extendFrom !5*/
	if (((cur_state == LEGUP_F_kmp_BB_preheaderpreheaderpreheader_17) & (fsm_stall == 1'd0))) begin
		kmp_preheaderpreheader_q111_reg <= kmp_preheaderpreheader_q111;
	end
	/* kmp: %.preheader.preheader*/
	/*   %q.111 = phi i32 [ %q.4, %.preheader ], [ 0, %.preheader.preheader.preheader ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB_preheader_32) & (fsm_stall == 1'd0)) & (kmp_preheader_exitcond5 == 1'd0))) begin
		kmp_preheaderpreheader_q111_reg <= kmp_preheaderpreheader_q111;
	end
end
always @(*) begin
	/* kmp: %.preheader.preheader*/
	/*   %scevgep = getelementptr i32* %input, i32 %i.012, !MSB !2, !LSB !3, !extendFrom !2*/
		kmp_preheaderpreheader_scevgep = (arg_input_reg + (4 * {22'd0,kmp_preheaderpreheader_i012_reg}));
end
always @(*) begin
	/* kmp: %.preheader.preheader*/
	/*   %15 = load i32* %scevgep, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
		kmp_preheaderpreheader_15 = main_0_input_out_a;
end
always @(posedge clk) begin
	/* kmp: %.preheader.preheader*/
	/*   %15 = load i32* %scevgep, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB_preheaderpreheader_19)) begin
		kmp_preheaderpreheader_15_reg <= kmp_preheaderpreheader_15;
	end
end
always @(*) begin
	/* kmp: %.preheader.preheader*/
	/*   %16 = icmp sgt i32 %q.111, 0, !MSB !3, !LSB !3, !extendFrom !3*/
		kmp_preheaderpreheader_16 = ((kmp_preheaderpreheader_q111_reg) > ({30'd0,kmp_preheaderpreheader_16_op1_temp}));
end
always @(posedge clk) begin
	/* kmp: %.preheader.preheader*/
	/*   %16 = icmp sgt i32 %q.111, 0, !MSB !3, !LSB !3, !extendFrom !3*/
	if ((cur_state == LEGUP_F_kmp_BB_preheaderpreheader_18)) begin
		kmp_preheaderpreheader_16_reg <= kmp_preheaderpreheader_16;
	end
end
always @(*) begin
	/* kmp: %.lr.ph*/
	/*   %q.29 = phi i32 [ %22, %20 ], [ %q.111, %.lr.ph.preheader ], !MSB !5, !LSB !3, !extendFrom !5*/
	if (((cur_state == LEGUP_F_kmp_BB_lrphpreheader_20) & (fsm_stall == 1'd0))) begin
		kmp_lrph_q29 = kmp_preheaderpreheader_q111_reg;
	end
	/* kmp: %.lr.ph*/
	/*   %q.29 = phi i32 [ %22, %20 ], [ %q.111, %.lr.ph.preheader ], !MSB !5, !LSB !3, !extendFrom !5*/
	else /* if ((((cur_state == LEGUP_F_kmp_BB__20_24) & (fsm_stall == 1'd0)) & (kmp_20_23 == 1'd1))) */ begin
		kmp_lrph_q29 = kmp_20_22;
	end
end
always @(posedge clk) begin
	/* kmp: %.lr.ph*/
	/*   %q.29 = phi i32 [ %22, %20 ], [ %q.111, %.lr.ph.preheader ], !MSB !5, !LSB !3, !extendFrom !5*/
	if (((cur_state == LEGUP_F_kmp_BB_lrphpreheader_20) & (fsm_stall == 1'd0))) begin
		kmp_lrph_q29_reg <= kmp_lrph_q29;
	end
	/* kmp: %.lr.ph*/
	/*   %q.29 = phi i32 [ %22, %20 ], [ %q.111, %.lr.ph.preheader ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB__20_24) & (fsm_stall == 1'd0)) & (kmp_20_23 == 1'd1))) begin
		kmp_lrph_q29_reg <= kmp_lrph_q29;
	end
end
always @(*) begin
	/* kmp: %.lr.ph*/
	/*   %17 = getelementptr inbounds i32* %pattern, i32 %q.29, !MSB !2, !LSB !3, !extendFrom !2*/
		kmp_lrph_17 = (arg_pattern_reg + (4 * kmp_lrph_q29_reg));
end
always @(*) begin
	/* kmp: %.lr.ph*/
	/*   %18 = load i32* %17, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
		kmp_lrph_18 = main_0_pattern_out_a;
end
always @(*) begin
	/* kmp: %.lr.ph*/
	/*   %19 = icmp eq i32 %18, %15, !MSB !3, !LSB !3, !extendFrom !3*/
		kmp_lrph_19 = (kmp_lrph_18 == kmp_preheaderpreheader_15_reg);
end
always @(*) begin
	/* kmp: %20*/
	/*   %21 = getelementptr inbounds i32* %kmpNext, i32 %q.29, !MSB !2, !LSB !3, !extendFrom !2*/
		kmp_20_21 = (arg_kmpNext_reg + (4 * kmp_lrph_q29_reg));
end
always @(*) begin
	/* kmp: %20*/
	/*   %22 = load i32* %21, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
		kmp_20_22 = main_0_kmpNext_out_a;
end
always @(*) begin
	/* kmp: %20*/
	/*   %23 = icmp sgt i32 %22, 0, !MSB !3, !LSB !3, !extendFrom !3*/
		kmp_20_23 = ((kmp_20_22) > ({30'd0,kmp_20_23_op1_temp}));
end
always @(*) begin
	/* kmp: %.thread2.loopexit*/
	/*   %.lcssa = phi i32 [ %22, %20 ], !MSB !5, !LSB !3, !extendFrom !5*/
		kmp_thread2loopexit_lcssa = kmp_20_22;
end
always @(posedge clk) begin
	/* kmp: %.thread2.loopexit*/
	/*   %.lcssa = phi i32 [ %22, %20 ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB__20_24) & (fsm_stall == 1'd0)) & (kmp_20_23 == 1'd0))) begin
		kmp_thread2loopexit_lcssa_reg <= kmp_thread2loopexit_lcssa;
	end
end
always @(*) begin
	/* kmp: %.thread2*/
	/*   %q.2.lcssa = phi i32 [ %q.111, %.preheader.preheader ], [ %.lcssa, %.thread2.loopexit ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB_preheaderpreheader_19) & (fsm_stall == 1'd0)) & (kmp_preheaderpreheader_16_reg == 1'd0))) begin
		kmp_thread2_q2lcssa = kmp_preheaderpreheader_q111_reg;
	end
	/* kmp: %.thread2*/
	/*   %q.2.lcssa = phi i32 [ %q.111, %.preheader.preheader ], [ %.lcssa, %.thread2.loopexit ], !MSB !5, !LSB !3, !extendFrom !5*/
	else /* if (((cur_state == LEGUP_F_kmp_BB_thread2loopexit_25) & (fsm_stall == 1'd0))) */ begin
		kmp_thread2_q2lcssa = kmp_thread2loopexit_lcssa_reg;
	end
end
always @(posedge clk) begin
	/* kmp: %.thread2*/
	/*   %q.2.lcssa = phi i32 [ %q.111, %.preheader.preheader ], [ %.lcssa, %.thread2.loopexit ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB_preheaderpreheader_19) & (fsm_stall == 1'd0)) & (kmp_preheaderpreheader_16_reg == 1'd0))) begin
		kmp_thread2_q2lcssa_reg <= kmp_thread2_q2lcssa;
	end
	/* kmp: %.thread2*/
	/*   %q.2.lcssa = phi i32 [ %q.111, %.preheader.preheader ], [ %.lcssa, %.thread2.loopexit ], !MSB !5, !LSB !3, !extendFrom !5*/
	if (((cur_state == LEGUP_F_kmp_BB_thread2loopexit_25) & (fsm_stall == 1'd0))) begin
		kmp_thread2_q2lcssa_reg <= kmp_thread2_q2lcssa;
	end
end
always @(*) begin
	/* kmp: %.thread2*/
	/*   %.phi.trans.insert32 = getelementptr inbounds i32* %pattern, i32 %q.2.lcssa, !MSB !2, !LSB !3, !extendFrom !2*/
		kmp_thread2_phitransinsert32 = (arg_pattern_reg + (4 * kmp_thread2_q2lcssa_reg));
end
always @(*) begin
	/* kmp: %.thread2*/
	/*   %.pre33 = load i32* %.phi.trans.insert32, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
		kmp_thread2_pre33 = main_0_pattern_out_a;
end
always @(*) begin
	/* kmp: %.thread2*/
	/*   %24 = icmp eq i32 %.pre33, %15, !MSB !3, !LSB !3, !extendFrom !3*/
		kmp_thread2_24 = (kmp_thread2_pre33 == kmp_preheaderpreheader_15_reg);
end
always @(*) begin
	/* kmp: %thread-pre-split.loopexit*/
	/*   %q.29.lcssa = phi i32 [ %q.29, %.lr.ph ], !MSB !5, !LSB !3, !extendFrom !5*/
		kmp_threadpresplitloopexit_q29lcssa = kmp_lrph_q29_reg;
end
always @(posedge clk) begin
	/* kmp: %thread-pre-split.loopexit*/
	/*   %q.29.lcssa = phi i32 [ %q.29, %.lr.ph ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB_lrph_22) & (fsm_stall == 1'd0)) & (kmp_lrph_19 == 1'd1))) begin
		kmp_threadpresplitloopexit_q29lcssa_reg <= kmp_threadpresplitloopexit_q29lcssa;
	end
end
always @(*) begin
	/* kmp: %thread-pre-split*/
	/*   %q.23540 = phi i32 [ %q.2.lcssa, %.thread2 ], [ %q.29.lcssa, %thread-pre-split.loopexit ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB_thread2_27) & (fsm_stall == 1'd0)) & (kmp_thread2_24 == 1'd1))) begin
		kmp_threadpresplit_q23540 = kmp_thread2_q2lcssa_reg;
	end
	/* kmp: %thread-pre-split*/
	/*   %q.23540 = phi i32 [ %q.2.lcssa, %.thread2 ], [ %q.29.lcssa, %thread-pre-split.loopexit ], !MSB !5, !LSB !3, !extendFrom !5*/
	else /* if (((cur_state == LEGUP_F_kmp_BB_threadpresplitloopexit_28) & (fsm_stall == 1'd0))) */ begin
		kmp_threadpresplit_q23540 = kmp_threadpresplitloopexit_q29lcssa_reg;
	end
end
always @(posedge clk) begin
	/* kmp: %thread-pre-split*/
	/*   %q.23540 = phi i32 [ %q.2.lcssa, %.thread2 ], [ %q.29.lcssa, %thread-pre-split.loopexit ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB_thread2_27) & (fsm_stall == 1'd0)) & (kmp_thread2_24 == 1'd1))) begin
		kmp_threadpresplit_q23540_reg <= kmp_threadpresplit_q23540;
	end
	/* kmp: %thread-pre-split*/
	/*   %q.23540 = phi i32 [ %q.2.lcssa, %.thread2 ], [ %q.29.lcssa, %thread-pre-split.loopexit ], !MSB !5, !LSB !3, !extendFrom !5*/
	if (((cur_state == LEGUP_F_kmp_BB_threadpresplitloopexit_28) & (fsm_stall == 1'd0))) begin
		kmp_threadpresplit_q23540_reg <= kmp_threadpresplit_q23540;
	end
end
always @(*) begin
	/* kmp: %thread-pre-split*/
	/*   %25 = add nsw i32 %q.23540, 1, !MSB !5, !LSB !3, !extendFrom !5*/
		kmp_threadpresplit_25 = (kmp_threadpresplit_q23540_reg + 32'd1);
end
always @(*) begin
	/* kmp: %thread-pre-split*/
	/*   %26 = icmp sgt i32 %q.23540, 2, !MSB !3, !LSB !3, !extendFrom !3*/
		kmp_threadpresplit_26 = ((kmp_threadpresplit_q23540_reg) > ({29'd0,kmp_threadpresplit_26_op1_temp}));
end
always @(*) begin
	/* kmp: %27*/
	/*   %29 = getelementptr inbounds i32* %kmpNext, i32 %q.23540, !MSB !2, !LSB !3, !extendFrom !2*/
		kmp_27_29 = (arg_kmpNext_reg + (4 * kmp_threadpresplit_q23540_reg));
end
always @(*) begin
	/* kmp: %27*/
	/*   %30 = load i32* %29, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
		kmp_27_30 = main_0_kmpNext_out_a;
end
always @(*) begin
	/* kmp: %.preheader*/
	/*   %q.4 = phi i32 [ %30, %27 ], [ %25, %thread-pre-split ], [ %q.2.lcssa, %.thread2 ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB_thread2_27) & (fsm_stall == 1'd0)) & (kmp_thread2_24 == 1'd0))) begin
		kmp_preheader_q4 = kmp_thread2_q2lcssa_reg;
	end
	/* kmp: %.preheader*/
	/*   %q.4 = phi i32 [ %30, %27 ], [ %25, %thread-pre-split ], [ %q.2.lcssa, %.thread2 ], !MSB !5, !LSB !3, !extendFrom !5*/
	else if ((((cur_state == LEGUP_F_kmp_BB_threadpresplit_29) & (fsm_stall == 1'd0)) & (kmp_threadpresplit_26 == 1'd0))) begin
		kmp_preheader_q4 = kmp_threadpresplit_25;
	end
	/* kmp: %.preheader*/
	/*   %q.4 = phi i32 [ %30, %27 ], [ %25, %thread-pre-split ], [ %q.2.lcssa, %.thread2 ], !MSB !5, !LSB !3, !extendFrom !5*/
	else /* if (((cur_state == LEGUP_F_kmp_BB__27_31) & (fsm_stall == 1'd0))) */ begin
		kmp_preheader_q4 = kmp_27_30;
	end
end
always @(posedge clk) begin
	/* kmp: %.preheader*/
	/*   %q.4 = phi i32 [ %30, %27 ], [ %25, %thread-pre-split ], [ %q.2.lcssa, %.thread2 ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB_thread2_27) & (fsm_stall == 1'd0)) & (kmp_thread2_24 == 1'd0))) begin
		kmp_preheader_q4_reg <= kmp_preheader_q4;
	end
	/* kmp: %.preheader*/
	/*   %q.4 = phi i32 [ %30, %27 ], [ %25, %thread-pre-split ], [ %q.2.lcssa, %.thread2 ], !MSB !5, !LSB !3, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_kmp_BB_threadpresplit_29) & (fsm_stall == 1'd0)) & (kmp_threadpresplit_26 == 1'd0))) begin
		kmp_preheader_q4_reg <= kmp_preheader_q4;
	end
	/* kmp: %.preheader*/
	/*   %q.4 = phi i32 [ %30, %27 ], [ %25, %thread-pre-split ], [ %q.2.lcssa, %.thread2 ], !MSB !5, !LSB !3, !extendFrom !5*/
	if (((cur_state == LEGUP_F_kmp_BB__27_31) & (fsm_stall == 1'd0))) begin
		kmp_preheader_q4_reg <= kmp_preheader_q4;
	end
end
always @(*) begin
	/* kmp: %.preheader*/
	/*   %31 = add nsw i32 %i.012, 1, !MSB !8, !LSB !3, !extendFrom !8*/
		kmp_preheader_31 = ({1'd0,kmp_preheaderpreheader_i012_reg} + 32'd1);
end
always @(*) begin
	/* kmp: %.preheader*/
	/*   %exitcond5 = icmp eq i32 %31, 1000, !MSB !3, !LSB !3, !extendFrom !3*/
		kmp_preheader_exitcond5 = (kmp_preheader_31 == 32'd1000);
end
always @(*) begin
	kmp_1_5_op1_temp = 32'd0;
if (reset) begin kmp_1_5_op1_temp = 0; end
end
always @(*) begin
	kmp_9_11_op1_temp = 32'd0;
if (reset) begin kmp_9_11_op1_temp = 0; end
end
always @(*) begin
	kmp_preheaderpreheader_16_op1_temp = 32'd0;
if (reset) begin kmp_preheaderpreheader_16_op1_temp = 0; end
end
always @(*) begin
	kmp_20_23_op1_temp = 32'd0;
if (reset) begin kmp_20_23_op1_temp = 0; end
end
always @(*) begin
	kmp_threadpresplit_26_op1_temp = 32'd2;
if (reset) begin kmp_threadpresplit_26_op1_temp = 0; end
end
always @(posedge clk) begin
	if ((cur_state == LEGUP_0)) begin
		finish <= 1'd0;
	end
	/* kmp: %32*/
	/*   ret void, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kmp_BB__32_33)) begin
		finish <= (fsm_stall == 1'd0);
	end
end
always @(*) begin
	main_0_kmpNext_write_enable_a = 1'd0;
	/* kmp: %0*/
	/*   store i32 0, i32* %kmpNext, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kmp_BB__0_1)) begin
		main_0_kmpNext_write_enable_a = 1'd1;
	end
	/* kmp: %14*/
	/*   store i32 %k.2, i32* %scevgep5, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kmp_BB__14_15)) begin
		main_0_kmpNext_write_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_kmpNext_in_a = 0;
	/* kmp: %0*/
	/*   store i32 0, i32* %kmpNext, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kmp_BB__0_1)) begin
		main_0_kmpNext_in_a = 32'd0;
	end
	/* kmp: %14*/
	/*   store i32 %k.2, i32* %scevgep5, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kmp_BB__14_15)) begin
		main_0_kmpNext_in_a = kmp_14_k2_reg;
	end
end
assign main_0_kmpNext_byteena_a = 1'd1;
always @(*) begin
	main_0_kmpNext_enable_a = 1'd0;
	/* kmp: %0*/
	/*   store i32 0, i32* %kmpNext, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kmp_BB__0_1)) begin
		main_0_kmpNext_enable_a = 1'd1;
	end
	/* kmp: %9*/
	/*   %10 = load i32* %scevgep5, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB__9_8)) begin
		main_0_kmpNext_enable_a = 1'd1;
	end
	/* kmp: %14*/
	/*   store i32 %k.2, i32* %scevgep5, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kmp_BB__14_15)) begin
		main_0_kmpNext_enable_a = 1'd1;
	end
	/* kmp: %20*/
	/*   %22 = load i32* %21, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB__20_23)) begin
		main_0_kmpNext_enable_a = 1'd1;
	end
	/* kmp: %27*/
	/*   %30 = load i32* %29, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB__27_30)) begin
		main_0_kmpNext_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_kmpNext_address_a = 2'd0;
	/* kmp: %0*/
	/*   store i32 0, i32* %kmpNext, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kmp_BB__0_1)) begin
		main_0_kmpNext_address_a = (arg_kmpNext_reg >>> 3'd2);
	end
	/* kmp: %9*/
	/*   %10 = load i32* %scevgep5, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB__9_8)) begin
		main_0_kmpNext_address_a = (kmp_1_scevgep5_reg >>> 3'd2);
	end
	/* kmp: %14*/
	/*   store i32 %k.2, i32* %scevgep5, align 4, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_kmp_BB__14_15)) begin
		main_0_kmpNext_address_a = (kmp_1_scevgep5_reg >>> 3'd2);
	end
	/* kmp: %20*/
	/*   %22 = load i32* %21, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB__20_23)) begin
		main_0_kmpNext_address_a = (kmp_20_21 >>> 3'd2);
	end
	/* kmp: %27*/
	/*   %30 = load i32* %29, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB__27_30)) begin
		main_0_kmpNext_address_a = (kmp_27_29 >>> 3'd2);
	end
end
assign main_0_kmpNext_write_enable_b = 1'd0;
assign main_0_kmpNext_in_b = 0;
assign main_0_kmpNext_byteena_b = 1'd1;
assign main_0_kmpNext_enable_b = 1'd0;
assign main_0_kmpNext_address_b = 2'd0;
assign main_0_pattern_write_enable_a = 1'd0;
assign main_0_pattern_in_a = 0;
assign main_0_pattern_byteena_a = 1'd1;
always @(*) begin
	main_0_pattern_enable_a = 1'd0;
	/* kmp: %1*/
	/*   %4 = load i32* %scevgep6, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB__1_3)) begin
		main_0_pattern_enable_a = 1'd1;
	end
	/* kmp: %.lr.ph14*/
	/*   %7 = load i32* %6, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB_lrph14_6)) begin
		main_0_pattern_enable_a = 1'd1;
	end
	/* kmp: %.thread*/
	/*   %.pre = load i32* %.phi.trans.insert, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB_thread_11)) begin
		main_0_pattern_enable_a = 1'd1;
	end
	/* kmp: %.lr.ph*/
	/*   %18 = load i32* %17, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB_lrph_21)) begin
		main_0_pattern_enable_a = 1'd1;
	end
	/* kmp: %.thread2*/
	/*   %.pre33 = load i32* %.phi.trans.insert32, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB_thread2_26)) begin
		main_0_pattern_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_pattern_address_a = 2'd0;
	/* kmp: %1*/
	/*   %4 = load i32* %scevgep6, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB__1_3)) begin
		main_0_pattern_address_a = (kmp_1_scevgep6 >>> 3'd2);
	end
	/* kmp: %.lr.ph14*/
	/*   %7 = load i32* %6, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB_lrph14_6)) begin
		main_0_pattern_address_a = (kmp_lrph14_6 >>> 3'd2);
	end
	/* kmp: %.thread*/
	/*   %.pre = load i32* %.phi.trans.insert, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB_thread_11)) begin
		main_0_pattern_address_a = (kmp_thread_phitransinsert >>> 3'd2);
	end
	/* kmp: %.lr.ph*/
	/*   %18 = load i32* %17, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB_lrph_21)) begin
		main_0_pattern_address_a = (kmp_lrph_17 >>> 3'd2);
	end
	/* kmp: %.thread2*/
	/*   %.pre33 = load i32* %.phi.trans.insert32, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB_thread2_26)) begin
		main_0_pattern_address_a = (kmp_thread2_phitransinsert32 >>> 3'd2);
	end
end
assign main_0_pattern_write_enable_b = 1'd0;
assign main_0_pattern_in_b = 0;
assign main_0_pattern_byteena_b = 1'd1;
assign main_0_pattern_enable_b = 1'd0;
assign main_0_pattern_address_b = 2'd0;
assign main_0_input_write_enable_a = 1'd0;
assign main_0_input_in_a = 0;
assign main_0_input_byteena_a = 1'd1;
always @(*) begin
	main_0_input_enable_a = 1'd0;
	/* kmp: %.preheader.preheader*/
	/*   %15 = load i32* %scevgep, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB_preheaderpreheader_18)) begin
		main_0_input_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_input_address_a = 10'd0;
	/* kmp: %.preheader.preheader*/
	/*   %15 = load i32* %scevgep, align 4, !MSB !5, !LSB !3, !extendFrom !5*/
	if ((cur_state == LEGUP_F_kmp_BB_preheaderpreheader_18)) begin
		main_0_input_address_a = (kmp_preheaderpreheader_scevgep >>> 3'd2);
	end
end
assign main_0_input_write_enable_b = 1'd0;
assign main_0_input_in_b = 0;
assign main_0_input_byteena_b = 1'd1;
assign main_0_input_enable_b = 1'd0;
assign main_0_input_address_b = 10'd0;

endmodule
