`define MEMORY_CONTROLLER_ADDR_SIZE 32
`define MEMORY_CONTROLLER_DATA_SIZE 64
// Number of RAM elements: 2
`define MEMORY_CONTROLLER_TAG_SIZE 9
`timescale 1 ns / 1 ns
module gaussian
(
	clk,
	clk2x,
	clk1x_follower,
	reset,
	memory_controller_waitrequest,
	start,
	finish,
	arg_c,
	arg_A,
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

parameter [3:0] LEGUP_0 = 4'd0;
parameter [3:0] LEGUP_F_gaussian_BB_loopexitloopexitloopexit_1 = 4'd1;
parameter [3:0] LEGUP_F_gaussian_BB_loopexitloopexit_2 = 4'd2;
parameter [3:0] LEGUP_F_gaussian_BB_loopexitloopexit_3 = 4'd3;
parameter [3:0] LEGUP_F_gaussian_BB_lrphpreheader_4 = 4'd4;
parameter [3:0] LEGUP_F_gaussian_BB_lrph_5 = 4'd5;
parameter [3:0] LEGUP_loop_pipeline_wait_LOOP22_1_6 = 4'd6;
parameter [3:0] LEGUP_F_gaussian_BB__20_7 = 4'd7;
parameter [3:0] LEGUP_F_gaussian_BB_loopexitloopexitthread_8 = 4'd8;

input  clk;
input  clk2x;
input  clk1x_follower;
input  reset;
input  memory_controller_waitrequest;
input  start;
output reg  finish;
input [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] arg_c;
input [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] arg_A;
output reg  main_0_A_write_enable_a;
output reg [31:0] main_0_A_in_a;
output  main_0_A_byteena_a;
output reg  main_0_A_enable_a;
output reg [7:0] main_0_A_address_a;
input [31:0] main_0_A_out_a;
output  main_0_A_write_enable_b;
output [31:0] main_0_A_in_b;
output  main_0_A_byteena_b;
output reg  main_0_A_enable_b;
output reg [7:0] main_0_A_address_b;
input [31:0] main_0_A_out_b;
output  main_0_c_write_enable_a;
output [31:0] main_0_c_in_a;
output  main_0_c_byteena_a;
output reg  main_0_c_enable_a;
output reg [3:0] main_0_c_address_a;
input [31:0] main_0_c_out_a;
output  main_0_c_write_enable_b;
output [31:0] main_0_c_in_b;
output  main_0_c_byteena_b;
output  main_0_c_enable_b;
output [3:0] main_0_c_address_b;
input [31:0] main_0_c_out_b;
reg [3:0] cur_state;
reg [3:0] next_state;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] arg_c_reg;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] arg_A_reg;
reg  fsm_stall;
reg [3:0] gaussian_loopexitloopexit_1;
reg [3:0] gaussian_loopexitloopexit_1_reg;
reg [8:0] gaussian_loopexitloopexit_2;
reg [9:0] gaussian_loopexitloopexit_3;
reg [9:0] gaussian_loopexitloopexit_3_reg;
reg [5:0] gaussian_loopexitloopexit_4;
reg [6:0] gaussian_loopexitloopexit_5;
reg [6:0] gaussian_loopexitloopexit_5_reg;
reg [9:0] gaussian_loopexitloopexit_6;
reg [9:0] gaussian_loopexitloopexit_6_reg;
reg [4:0] gaussian_loopexitloopexit_7;
reg [4:0] gaussian_loopexitloopexit_7_reg;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] gaussian_loopexitloopexit_scevgep11;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] gaussian_loopexitloopexit_scevgep11_reg;
reg [4:0] gaussian_loopexitloopexit_8;
reg [4:0] gaussian_loopexitloopexit_8_reg;
reg  gaussian_loopexitloopexit_exitcond;
reg  gaussian_loopexitloopexit_exitcond_reg;
reg [31:0] gaussian_lrph_indvar4;
reg [31:0] gaussian_lrph_indvar4_reg;
reg [31:0] gaussian_lrph_9;
reg [31:0] gaussian_lrph_10;
reg [31:0] gaussian_lrph_10_reg;
reg [31:0] gaussian_11_12;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] gaussian_11_scevgep6;
reg [31:0] gaussian_11_13;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] gaussian_11_scevgep;
reg [31:0] gaussian_11_14;
reg [31:0] gaussian_11_15;
reg [31:0] gaussian_11_16;
reg [31:0] gaussian_11_17;
reg [31:0] gaussian_11_18;
reg [31:0] gaussian_20_21;
reg  gaussian_20_exitcond5;
reg  LOOP22_1_valid_bit_0;
reg  LOOP22_1_state_stall_0;
reg  LOOP22_1_state_enable_0;
reg  LOOP22_1_state_stall_reg_0;
reg  LOOP22_1_valid_bit_1;
reg  LOOP22_1_state_stall_1;
reg  LOOP22_1_state_enable_1;
reg  LOOP22_1_state_stall_reg_1;
reg  LOOP22_1_valid_bit_2;
reg  LOOP22_1_state_stall_2;
reg  LOOP22_1_state_enable_2;
reg  LOOP22_1_state_stall_reg_2;
reg  LOOP22_1_valid_bit_3;
reg  LOOP22_1_state_stall_3;
reg  LOOP22_1_state_enable_3;
reg  LOOP22_1_state_stall_reg_3;
reg  LOOP22_1_valid_bit_4;
reg  LOOP22_1_state_stall_4;
reg  LOOP22_1_state_enable_4;
reg [1:0] LOOP22_1_II_counter;
reg  LOOP22_1_start;
reg  LOOP22_1_activate_pipeline;
reg [31:0] gaussian_11_12_reg_stage0;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] gaussian_11_scevgep6_reg_stage1;
reg [31:0] gaussian_11_13_reg_stage0;
reg [31:0] gaussian_11_15_reg_stage1;
reg  LOOP22_1_pipeline_exit_cond;
reg [31:0] LOOP22_1_inductionVar_stage0;
reg  LOOP22_1_active;
reg  LOOP22_1_begin_pipeline;
reg  LOOP22_1_epilogue;
reg  LOOP22_1_pipeline_finish;
reg  LOOP22_1_only_last_stage_enabled;
reg  LOOP22_1_pipeline_finish_reg;
reg  legup_mult_gaussian_loopexitloopexit_4_en;
reg [5:0] gaussian_loopexitloopexit_4_stage0_reg;
reg  legup_mult_1_unsigned_32_32_1_0_clock;
reg  legup_mult_1_unsigned_32_32_1_0_aclr;
reg  legup_mult_1_unsigned_32_32_1_0_sum;
reg  legup_mult_1_unsigned_32_32_1_0_clken;
reg [31:0] legup_mult_1_unsigned_32_32_1_0_dataa;
reg [31:0] legup_mult_1_unsigned_32_32_1_0_datab;
wire [63:0] legup_mult_1_unsigned_32_32_1_0_result;
reg [63:0] legup_mult_gaussian_11_17_out_actual;
reg [31:0] legup_mult_gaussian_11_17_out;
reg  legup_mult_gaussian_11_17_en;

/*   %17 = mul nsw i32 %15, %16, !legup.pipeline.start_time !13, !legup.pipeline.avail_time !5, !legup.pipeline.stage !12, !MSB !9, !LSB !4, !extendFrom !9*/
legup_mult_1 legup_mult_1_unsigned_32_32_1_0 (
	.clock (legup_mult_1_unsigned_32_32_1_0_clock),
	.aclr (legup_mult_1_unsigned_32_32_1_0_aclr),
	.sum (legup_mult_1_unsigned_32_32_1_0_sum),
	.clken (legup_mult_1_unsigned_32_32_1_0_clken),
	.dataa (legup_mult_1_unsigned_32_32_1_0_dataa),
	.datab (legup_mult_1_unsigned_32_32_1_0_datab),
	.result (legup_mult_1_unsigned_32_32_1_0_result)
);

// Commented out since it is not essential for CDFG extraction 
//defparam
//	legup_mult_1_unsigned_32_32_1_0.widtha = 32,
//	legup_mult_1_unsigned_32_32_1_0.widthb = 32,
//	legup_mult_1_unsigned_32_32_1_0.widthp = 64,
//	legup_mult_1_unsigned_32_32_1_0.representation = "UNSIGNED";

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
		next_state = LEGUP_F_gaussian_BB_loopexitloopexit_2;
LEGUP_F_gaussian_BB__20_7:
	if ((fsm_stall == 1'd0) && (gaussian_20_exitcond5 == 1'd1))
		next_state = LEGUP_F_gaussian_BB_loopexitloopexitloopexit_1;
	else if ((fsm_stall == 1'd0) && (gaussian_20_exitcond5 == 1'd0))
		next_state = LEGUP_F_gaussian_BB_lrph_5;
LEGUP_F_gaussian_BB_loopexitloopexit_2:
		next_state = LEGUP_F_gaussian_BB_loopexitloopexit_3;
LEGUP_F_gaussian_BB_loopexitloopexit_3:
	if ((fsm_stall == 1'd0) && (gaussian_loopexitloopexit_exitcond_reg == 1'd1))
		next_state = LEGUP_F_gaussian_BB_loopexitloopexitthread_8;
	else if ((fsm_stall == 1'd0) && (gaussian_loopexitloopexit_exitcond_reg == 1'd0))
		next_state = LEGUP_F_gaussian_BB_lrphpreheader_4;
LEGUP_F_gaussian_BB_loopexitloopexitloopexit_1:
		next_state = LEGUP_F_gaussian_BB_loopexitloopexit_2;
LEGUP_F_gaussian_BB_loopexitloopexitthread_8:
		next_state = LEGUP_0;
LEGUP_F_gaussian_BB_lrph_5:
		next_state = LEGUP_loop_pipeline_wait_LOOP22_1_6;
LEGUP_F_gaussian_BB_lrphpreheader_4:
		next_state = LEGUP_F_gaussian_BB_lrph_5;
LEGUP_loop_pipeline_wait_LOOP22_1_6:
	if ((fsm_stall == 1'd0) && (LOOP22_1_pipeline_finish == 1'd1))
		next_state = LEGUP_F_gaussian_BB__20_7;
	else if ((fsm_stall == 1'd0) && (LOOP22_1_pipeline_finish == 1'd1))
		next_state = LEGUP_F_gaussian_BB__20_7;
default:
	next_state = cur_state;
endcase

end
always @(posedge clk) begin
	if (start) begin
		arg_c_reg <= arg_c;
	end
end
always @(posedge clk) begin
	if (start) begin
		arg_A_reg <= arg_A;
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
	/* gaussian: %.loopexit.loopexit*/
	/*   %1 = phi i32 [ 0, %0 ], [ %8, %.loopexit.loopexit.loopexit ], !MSB !5, !LSB !4, !extendFrom !5*/
	if ((((cur_state == LEGUP_0) & (fsm_stall == 1'd0)) & (start == 1'd1))) begin
		gaussian_loopexitloopexit_1 = 32'd0;
	end
	/* gaussian: %.loopexit.loopexit*/
	/*   %1 = phi i32 [ 0, %0 ], [ %8, %.loopexit.loopexit.loopexit ], !MSB !5, !LSB !4, !extendFrom !5*/
	else /* if (((cur_state == LEGUP_F_gaussian_BB_loopexitloopexitloopexit_1) & (fsm_stall == 1'd0))) */ begin
		gaussian_loopexitloopexit_1 = gaussian_loopexitloopexit_8_reg;
	end
end
always @(posedge clk) begin
	/* gaussian: %.loopexit.loopexit*/
	/*   %1 = phi i32 [ 0, %0 ], [ %8, %.loopexit.loopexit.loopexit ], !MSB !5, !LSB !4, !extendFrom !5*/
	if ((((cur_state == LEGUP_0) & (fsm_stall == 1'd0)) & (start == 1'd1))) begin
		gaussian_loopexitloopexit_1_reg <= gaussian_loopexitloopexit_1;
	end
	/* gaussian: %.loopexit.loopexit*/
	/*   %1 = phi i32 [ 0, %0 ], [ %8, %.loopexit.loopexit.loopexit ], !MSB !5, !LSB !4, !extendFrom !5*/
	if (((cur_state == LEGUP_F_gaussian_BB_loopexitloopexitloopexit_1) & (fsm_stall == 1'd0))) begin
		gaussian_loopexitloopexit_1_reg <= gaussian_loopexitloopexit_1;
	end
end
always @(*) begin
	/* gaussian: %.loopexit.loopexit*/
	/*   %2 = mul i32 %1, 16, !MSB !6, !LSB !7, !extendFrom !6*/
		gaussian_loopexitloopexit_2 = ({5'd0,gaussian_loopexitloopexit_1_reg} * 32'd16);
end
always @(*) begin
	/* gaussian: %.loopexit.loopexit*/
	/*   %3 = add i32 %2, 33, !MSB !8, !LSB !4, !extendFrom !8*/
		gaussian_loopexitloopexit_3 = ({1'd0,gaussian_loopexitloopexit_2} + 32'd33);
end
always @(posedge clk) begin
	/* gaussian: %.loopexit.loopexit*/
	/*   %3 = add i32 %2, 33, !MSB !8, !LSB !4, !extendFrom !8*/
	if ((cur_state == LEGUP_F_gaussian_BB_loopexitloopexit_2)) begin
		gaussian_loopexitloopexit_3_reg <= gaussian_loopexitloopexit_3;
	end
end
always @(*) begin
	gaussian_loopexitloopexit_4 = gaussian_loopexitloopexit_4_stage0_reg;
end
always @(*) begin
	/* gaussian: %.loopexit.loopexit*/
	/*   %5 = add i32 %4, 14, !MSB !9, !LSB !4, !extendFrom !11*/
		gaussian_loopexitloopexit_5 = (({{1{gaussian_loopexitloopexit_4[5]}},gaussian_loopexitloopexit_4}) + 32'd14);
end
always @(posedge clk) begin
	/* gaussian: %.loopexit.loopexit*/
	/*   %5 = add i32 %4, 14, !MSB !9, !LSB !4, !extendFrom !11*/
	if ((cur_state == LEGUP_F_gaussian_BB_loopexitloopexit_3)) begin
		gaussian_loopexitloopexit_5_reg <= gaussian_loopexitloopexit_5;
	end
end
always @(*) begin
	/* gaussian: %.loopexit.loopexit*/
	/*   %6 = add i32 %2, 17, !MSB !8, !LSB !4, !extendFrom !8*/
		gaussian_loopexitloopexit_6 = ({1'd0,gaussian_loopexitloopexit_2} + 32'd17);
end
always @(posedge clk) begin
	/* gaussian: %.loopexit.loopexit*/
	/*   %6 = add i32 %2, 17, !MSB !8, !LSB !4, !extendFrom !8*/
	if ((cur_state == LEGUP_F_gaussian_BB_loopexitloopexit_2)) begin
		gaussian_loopexitloopexit_6_reg <= gaussian_loopexitloopexit_6;
	end
end
always @(*) begin
	/* gaussian: %.loopexit.loopexit*/
	/*   %7 = add i32 %1, 1, !MSB !7, !LSB !4, !extendFrom !7*/
		gaussian_loopexitloopexit_7 = ({1'd0,gaussian_loopexitloopexit_1_reg} + 32'd1);
end
always @(posedge clk) begin
	/* gaussian: %.loopexit.loopexit*/
	/*   %7 = add i32 %1, 1, !MSB !7, !LSB !4, !extendFrom !7*/
	if ((cur_state == LEGUP_F_gaussian_BB_loopexitloopexit_2)) begin
		gaussian_loopexitloopexit_7_reg <= gaussian_loopexitloopexit_7;
	end
end
always @(*) begin
	/* gaussian: %.loopexit.loopexit*/
	/*   %scevgep11 = getelementptr i32* %c, i32 %7, !MSB !3, !LSB !4, !extendFrom !3*/
		gaussian_loopexitloopexit_scevgep11 = (arg_c_reg + (4 * {27'd0,gaussian_loopexitloopexit_7_reg}));
end
always @(posedge clk) begin
	/* gaussian: %.loopexit.loopexit*/
	/*   %scevgep11 = getelementptr i32* %c, i32 %7, !MSB !3, !LSB !4, !extendFrom !3*/
	if ((cur_state == LEGUP_F_gaussian_BB_loopexitloopexit_3)) begin
		gaussian_loopexitloopexit_scevgep11_reg <= gaussian_loopexitloopexit_scevgep11;
	end
end
always @(*) begin
	/* gaussian: %.loopexit.loopexit*/
	/*   %8 = add i32 %1, 1, !MSB !7, !LSB !4, !extendFrom !7*/
		gaussian_loopexitloopexit_8 = ({1'd0,gaussian_loopexitloopexit_1_reg} + 32'd1);
end
always @(posedge clk) begin
	/* gaussian: %.loopexit.loopexit*/
	/*   %8 = add i32 %1, 1, !MSB !7, !LSB !4, !extendFrom !7*/
	if ((cur_state == LEGUP_F_gaussian_BB_loopexitloopexit_2)) begin
		gaussian_loopexitloopexit_8_reg <= gaussian_loopexitloopexit_8;
	end
end
always @(*) begin
	/* gaussian: %.loopexit.loopexit*/
	/*   %exitcond = icmp eq i32 %1, 14, !MSB !4, !LSB !4, !extendFrom !4*/
		gaussian_loopexitloopexit_exitcond = (gaussian_loopexitloopexit_1_reg == 32'd14);
end
always @(posedge clk) begin
	/* gaussian: %.loopexit.loopexit*/
	/*   %exitcond = icmp eq i32 %1, 14, !MSB !4, !LSB !4, !extendFrom !4*/
	if ((cur_state == LEGUP_F_gaussian_BB_loopexitloopexit_2)) begin
		gaussian_loopexitloopexit_exitcond_reg <= gaussian_loopexitloopexit_exitcond;
	end
end
always @(*) begin
	/* gaussian: %.lr.ph*/
	/*   %indvar4 = phi i32 [ %21, %20 ], [ 0, %.lr.ph.preheader ], !MSB !9, !LSB !4, !extendFrom !9*/
	if (((cur_state == LEGUP_F_gaussian_BB_lrphpreheader_4) & (fsm_stall == 1'd0))) begin
		gaussian_lrph_indvar4 = 32'd0;
	end
	/* gaussian: %.lr.ph*/
	/*   %indvar4 = phi i32 [ %21, %20 ], [ 0, %.lr.ph.preheader ], !MSB !9, !LSB !4, !extendFrom !9*/
	else /* if ((((cur_state == LEGUP_F_gaussian_BB__20_7) & (fsm_stall == 1'd0)) & (gaussian_20_exitcond5 == 1'd0))) */ begin
		gaussian_lrph_indvar4 = gaussian_20_21;
	end
end
always @(posedge clk) begin
	/* gaussian: %.lr.ph*/
	/*   %indvar4 = phi i32 [ %21, %20 ], [ 0, %.lr.ph.preheader ], !MSB !9, !LSB !4, !extendFrom !9*/
	if (((cur_state == LEGUP_F_gaussian_BB_lrphpreheader_4) & (fsm_stall == 1'd0))) begin
		gaussian_lrph_indvar4_reg <= gaussian_lrph_indvar4;
	end
	/* gaussian: %.lr.ph*/
	/*   %indvar4 = phi i32 [ %21, %20 ], [ 0, %.lr.ph.preheader ], !MSB !9, !LSB !4, !extendFrom !9*/
	if ((((cur_state == LEGUP_F_gaussian_BB__20_7) & (fsm_stall == 1'd0)) & (gaussian_20_exitcond5 == 1'd0))) begin
		gaussian_lrph_indvar4_reg <= gaussian_lrph_indvar4;
	end
end
always @(*) begin
	/* gaussian: %.lr.ph*/
	/*   %9 = mul i32 %indvar4, 16, !MSB !9, !LSB !7, !extendFrom !9*/
		gaussian_lrph_9 = (gaussian_lrph_indvar4_reg * 32'd16);
end
always @(*) begin
	/* gaussian: %.lr.ph*/
	/*   %10 = add i32 %3, %9, !MSB !9, !LSB !4, !extendFrom !9*/
		gaussian_lrph_10 = ({22'd0,gaussian_loopexitloopexit_3_reg} + gaussian_lrph_9);
end
always @(posedge clk) begin
	/* gaussian: %.lr.ph*/
	/*   %10 = add i32 %3, %9, !MSB !9, !LSB !4, !extendFrom !9*/
	if ((cur_state == LEGUP_F_gaussian_BB_lrph_5)) begin
		gaussian_lrph_10_reg <= gaussian_lrph_10;
	end
end
always @(*) begin
	/* gaussian: %11*/
	/*   %12 = add i32 %10, %indvar, !legup.pipeline.start_time !4, !legup.pipeline.avail_time !4, !legup.pipeline.stage !4, !MSB !9, !LSB !4, !extendFrom !9
	start_time: 0 avail_time: 0 stage: 0 II: 2 start_ii_state = 0 % 2 = 0 avail_ii_state = 0 % 2 = 0*/
		gaussian_11_12 = (gaussian_lrph_10_reg + LOOP22_1_inductionVar_stage0);
end
always @(*) begin
	/* gaussian: %11*/
	/*   %scevgep6 = getelementptr i32* %A, i32 %12, !legup.pipeline.start_time !12, !legup.pipeline.avail_time !12, !legup.pipeline.stage !4, !MSB !3, !LSB !4, !extendFrom !3
	start_time: 1 avail_time: 1 stage: 0 II: 2 start_ii_state = 1 % 2 = 1 avail_ii_state = 1 % 2 = 1*/
		gaussian_11_scevgep6 = (arg_A_reg + (4 * gaussian_11_12_reg_stage0));
end
always @(*) begin
	/* gaussian: %11*/
	/*   %13 = add i32 %6, %indvar, !legup.pipeline.start_time !4, !legup.pipeline.avail_time !4, !legup.pipeline.stage !4, !MSB !9, !LSB !4, !extendFrom !9
	start_time: 0 avail_time: 0 stage: 0 II: 2 start_ii_state = 0 % 2 = 0 avail_ii_state = 0 % 2 = 0*/
		gaussian_11_13 = ({22'd0,gaussian_loopexitloopexit_6_reg} + LOOP22_1_inductionVar_stage0);
end
always @(*) begin
	/* gaussian: %11*/
	/*   %scevgep = getelementptr i32* %A, i32 %13, !legup.pipeline.start_time !12, !legup.pipeline.avail_time !12, !legup.pipeline.stage !4, !MSB !3, !LSB !4, !extendFrom !3
	start_time: 1 avail_time: 1 stage: 0 II: 2 start_ii_state = 1 % 2 = 1 avail_ii_state = 1 % 2 = 1*/
		gaussian_11_scevgep = (arg_A_reg + (4 * gaussian_11_13_reg_stage0));
end
always @(*) begin
	/* gaussian: %11*/
	/*   %14 = load i32* %scevgep6, align 4, !legup.pipeline.start_time !13, !legup.pipeline.avail_time !5, !legup.pipeline.stage !12, !MSB !9, !LSB !4, !extendFrom !9
	start_time: 2 avail_time: 3 stage: 1 II: 2 start_ii_state = 2 % 2 = 0 avail_ii_state = 3 % 2 = 1*/
		gaussian_11_14 = main_0_A_out_a;
end
always @(*) begin
	/* gaussian: %11*/
	/*   %15 = load i32* %scevgep11, align 4, !legup.pipeline.start_time !4, !legup.pipeline.avail_time !12, !legup.pipeline.stage !4, !MSB !9, !LSB !4, !extendFrom !9
	start_time: 0 avail_time: 1 stage: 0 II: 2 start_ii_state = 0 % 2 = 0 avail_ii_state = 1 % 2 = 1*/
		gaussian_11_15 = main_0_c_out_a;
end
always @(*) begin
	/* gaussian: %11*/
	/*   %16 = load i32* %scevgep, align 4, !legup.pipeline.start_time !12, !legup.pipeline.avail_time !13, !legup.pipeline.stage !4, !MSB !9, !LSB !4, !extendFrom !9
	start_time: 1 avail_time: 2 stage: 0 II: 2 start_ii_state = 1 % 2 = 1 avail_ii_state = 2 % 2 = 0*/
		gaussian_11_16 = main_0_A_out_b;
end
always @(*) begin
	gaussian_11_17 = legup_mult_gaussian_11_17_out;
end
always @(*) begin
	/* gaussian: %11*/
	/*   %18 = sub nsw i32 %14, %17, !legup.pipeline.start_time !5, !legup.pipeline.avail_time !5, !legup.pipeline.stage !12, !MSB !9, !LSB !4, !extendFrom !9
	start_time: 3 avail_time: 3 stage: 1 II: 2 start_ii_state = 3 % 2 = 1 avail_ii_state = 3 % 2 = 1*/
		gaussian_11_18 = (gaussian_11_14 - gaussian_11_17);
end
always @(*) begin
	/* gaussian: %20*/
	/*   %21 = add i32 %indvar4, 1, !MSB !9, !LSB !4, !extendFrom !9*/
		gaussian_20_21 = (gaussian_lrph_indvar4_reg + 32'd1);
end
always @(*) begin
	/* gaussian: %20*/
	/*   %exitcond5 = icmp eq i32 %21, %5, !MSB !4, !LSB !4, !extendFrom !4*/
		gaussian_20_exitcond5 = (gaussian_20_21 == (gaussian_loopexitloopexit_5_reg));
end
always @(posedge clk) begin
	if (~(LOOP22_1_state_stall_0)) begin
		LOOP22_1_valid_bit_0 <= ((LOOP22_1_II_counter == 2'd1) & LOOP22_1_start);
	end
	if (reset) begin
		LOOP22_1_valid_bit_0 <= 1'd0;
	end
end
always @(*) begin
	LOOP22_1_state_stall_0 = 1'd0;
	if ((LOOP22_1_state_stall_reg_0 & (LOOP22_1_II_counter != 2'd0))) begin
		LOOP22_1_state_stall_0 = 1'd1;
	end
	if (LOOP22_1_state_stall_1) begin
		LOOP22_1_state_stall_0 = 1'd1;
	end
end
always @(*) begin
	LOOP22_1_state_enable_0 = (LOOP22_1_valid_bit_0 & ~(LOOP22_1_state_stall_0));
end
always @(posedge clk) begin
	LOOP22_1_state_stall_reg_0 <= LOOP22_1_state_stall_0;
	if (reset) begin
		LOOP22_1_state_stall_reg_0 <= 1'd0;
	end
end
always @(posedge clk) begin
	if (~(LOOP22_1_state_stall_1)) begin
		LOOP22_1_valid_bit_1 <= LOOP22_1_state_enable_0;
	end
	if (reset) begin
		LOOP22_1_valid_bit_1 <= 1'd0;
	end
end
always @(*) begin
	LOOP22_1_state_stall_1 = 1'd0;
	if ((LOOP22_1_state_stall_reg_1 & (LOOP22_1_II_counter != 2'd1))) begin
		LOOP22_1_state_stall_1 = 1'd1;
	end
	if (LOOP22_1_state_stall_2) begin
		LOOP22_1_state_stall_1 = 1'd1;
	end
end
always @(*) begin
	LOOP22_1_state_enable_1 = (LOOP22_1_valid_bit_1 & ~(LOOP22_1_state_stall_1));
end
always @(posedge clk) begin
	LOOP22_1_state_stall_reg_1 <= LOOP22_1_state_stall_1;
	if (reset) begin
		LOOP22_1_state_stall_reg_1 <= 1'd0;
	end
end
always @(posedge clk) begin
	if (~(LOOP22_1_state_stall_2)) begin
		LOOP22_1_valid_bit_2 <= LOOP22_1_state_enable_1;
	end
	if (reset) begin
		LOOP22_1_valid_bit_2 <= 1'd0;
	end
end
always @(*) begin
	LOOP22_1_state_stall_2 = 1'd0;
	if ((LOOP22_1_state_stall_reg_2 & (LOOP22_1_II_counter != 2'd0))) begin
		LOOP22_1_state_stall_2 = 1'd1;
	end
	if (LOOP22_1_state_stall_3) begin
		LOOP22_1_state_stall_2 = 1'd1;
	end
end
always @(*) begin
	LOOP22_1_state_enable_2 = (LOOP22_1_valid_bit_2 & ~(LOOP22_1_state_stall_2));
end
always @(posedge clk) begin
	LOOP22_1_state_stall_reg_2 <= LOOP22_1_state_stall_2;
	if (reset) begin
		LOOP22_1_state_stall_reg_2 <= 1'd0;
	end
end
always @(posedge clk) begin
	if (~(LOOP22_1_state_stall_3)) begin
		LOOP22_1_valid_bit_3 <= LOOP22_1_state_enable_2;
	end
	if (reset) begin
		LOOP22_1_valid_bit_3 <= 1'd0;
	end
end
always @(*) begin
	LOOP22_1_state_stall_3 = 1'd0;
	if ((LOOP22_1_state_stall_reg_3 & (LOOP22_1_II_counter != 2'd1))) begin
		LOOP22_1_state_stall_3 = 1'd1;
	end
	if (LOOP22_1_state_stall_4) begin
		LOOP22_1_state_stall_3 = 1'd1;
	end
end
always @(*) begin
	LOOP22_1_state_enable_3 = (LOOP22_1_valid_bit_3 & ~(LOOP22_1_state_stall_3));
end
always @(posedge clk) begin
	LOOP22_1_state_stall_reg_3 <= LOOP22_1_state_stall_3;
	if (reset) begin
		LOOP22_1_state_stall_reg_3 <= 1'd0;
	end
end
always @(posedge clk) begin
	if (~(LOOP22_1_state_stall_4)) begin
		LOOP22_1_valid_bit_4 <= LOOP22_1_state_enable_3;
	end
	if (reset) begin
		LOOP22_1_valid_bit_4 <= 1'd0;
	end
end
always @(*) begin
	LOOP22_1_state_stall_4 = 1'd0;
	if (reset) begin
		LOOP22_1_state_stall_4 = 1'd0;
	end
end
always @(*) begin
	LOOP22_1_state_enable_4 = (LOOP22_1_valid_bit_4 & ~(LOOP22_1_state_stall_4));
end
always @(posedge clk) begin
	LOOP22_1_II_counter <= (LOOP22_1_II_counter + 2'd1);
	if (reset) begin
		LOOP22_1_II_counter <= 2'd0;
	end
	if ((LOOP22_1_II_counter == 2'd1)) begin
		LOOP22_1_II_counter <= 2'd0;
	end
end
always @(*) begin
	LOOP22_1_start = (LOOP22_1_activate_pipeline | ((LOOP22_1_active & ~(LOOP22_1_epilogue)) & ~((LOOP22_1_state_enable_0 & LOOP22_1_pipeline_exit_cond))));
	if (reset) begin
		LOOP22_1_start = 1'd0;
	end
end
always @(*) begin
	LOOP22_1_activate_pipeline = (((fsm_stall == 1'd0) & LOOP22_1_begin_pipeline) & ~(LOOP22_1_active));
end
always @(posedge clk) begin
	if (LOOP22_1_state_enable_0) begin
		gaussian_11_12_reg_stage0 <= gaussian_11_12;
	end
end
always @(posedge clk) begin
	if (LOOP22_1_state_enable_1) begin
		gaussian_11_scevgep6_reg_stage1 <= gaussian_11_scevgep6;
	end
end
always @(posedge clk) begin
	if (LOOP22_1_state_enable_0) begin
		gaussian_11_13_reg_stage0 <= gaussian_11_13;
	end
end
always @(posedge clk) begin
	if (LOOP22_1_state_enable_1) begin
		gaussian_11_15_reg_stage1 <= gaussian_11_15;
	end
end
always @(*) begin
	LOOP22_1_pipeline_exit_cond = (LOOP22_1_inductionVar_stage0 == 14);
end
always @(posedge clk) begin
	if (reset) begin
		LOOP22_1_inductionVar_stage0 <= 0;
	end
	if (LOOP22_1_activate_pipeline) begin
		LOOP22_1_inductionVar_stage0 <= 0;
	end
	if (((LOOP22_1_II_counter == 1'd1) & LOOP22_1_state_enable_1)) begin
		LOOP22_1_inductionVar_stage0 <= (LOOP22_1_inductionVar_stage0 + 1'd1);
	end
end
always @(posedge clk) begin
	if (reset) begin
		LOOP22_1_active <= 1'd0;
	end
	if (LOOP22_1_activate_pipeline) begin
		LOOP22_1_active <= 1'd1;
	end
	if (((~(LOOP22_1_state_stall_0) & LOOP22_1_epilogue) & LOOP22_1_only_last_stage_enabled)) begin
		LOOP22_1_active <= 1'd0;
	end
end
always @(*) begin
	LOOP22_1_begin_pipeline = 1'd0;
	if (reset) begin
		LOOP22_1_begin_pipeline = 1'd0;
	end
	if (((cur_state == LEGUP_F_gaussian_BB_lrph_5) & (fsm_stall == 1'd0))) begin
		LOOP22_1_begin_pipeline = 1'd1;
	end
end
always @(posedge clk) begin
	if (reset) begin
		LOOP22_1_epilogue <= 1'd0;
	end
	if ((LOOP22_1_state_enable_0 & LOOP22_1_pipeline_exit_cond)) begin
		LOOP22_1_epilogue <= 1'd1;
	end
	if (((~(LOOP22_1_state_stall_0) & LOOP22_1_epilogue) & LOOP22_1_only_last_stage_enabled)) begin
		LOOP22_1_epilogue <= 1'd0;
	end
end
always @(*) begin
	LOOP22_1_pipeline_finish = (((~(LOOP22_1_state_stall_0) & LOOP22_1_epilogue) & LOOP22_1_only_last_stage_enabled) | LOOP22_1_pipeline_finish_reg);
end
always @(*) begin
	LOOP22_1_only_last_stage_enabled = ((((~(LOOP22_1_state_enable_0) & ~(LOOP22_1_state_enable_1)) & ~(LOOP22_1_state_enable_2)) & ~(LOOP22_1_state_enable_3)) & LOOP22_1_state_enable_4);
end
always @(posedge clk) begin
	LOOP22_1_pipeline_finish_reg <= LOOP22_1_pipeline_finish;
	if (reset) begin
		LOOP22_1_pipeline_finish_reg <= 1'd0;
	end
	if (LOOP22_1_activate_pipeline) begin
		LOOP22_1_pipeline_finish_reg <= 1'd0;
	end
end
always @(*) begin
	legup_mult_gaussian_loopexitloopexit_4_en = ~(fsm_stall);
end
always @(posedge clk) begin
	/* gaussian: %.loopexit.loopexit*/
	/*   %4 = mul i32 %1, -1, !MSB !9, !LSB !4, !extendFrom !10*/
	if ((legup_mult_gaussian_loopexitloopexit_4_en == 1'd1)) begin
		gaussian_loopexitloopexit_4_stage0_reg <= ({2'd0,gaussian_loopexitloopexit_1_reg} * (-32'd1));
	end
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
	legup_mult_1_unsigned_32_32_1_0_clken = legup_mult_gaussian_11_17_en;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_0_dataa = gaussian_11_15_reg_stage1;
end
always @(*) begin
	legup_mult_1_unsigned_32_32_1_0_datab = gaussian_11_16;
end
always @(*) begin
	legup_mult_gaussian_11_17_out_actual = legup_mult_1_unsigned_32_32_1_0_result;
end
always @(*) begin
	legup_mult_gaussian_11_17_out = legup_mult_gaussian_11_17_out_actual[31:0];
end
always @(*) begin
	legup_mult_gaussian_11_17_en = ~(LOOP22_1_state_stall_2);
end
always @(posedge clk) begin
	if ((cur_state == LEGUP_0)) begin
		finish <= 1'd0;
	end
	/* gaussian: %.loopexit.loopexit.thread*/
	/*   ret void, !MSB !3, !LSB !4, !extendFrom !3*/
	if ((cur_state == LEGUP_F_gaussian_BB_loopexitloopexitthread_8)) begin
		finish <= (fsm_stall == 1'd0);
	end
end
always @(*) begin
	main_0_A_write_enable_a = 1'd0;
	if (LOOP22_1_valid_bit_3) begin
		main_0_A_write_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_A_in_a = 0;
	if (LOOP22_1_valid_bit_3) begin
		main_0_A_in_a = gaussian_11_18;
	end
end
assign main_0_A_byteena_a = 1'd1;
always @(*) begin
	main_0_A_enable_a = 1'd0;
	/* gaussian: %11*/
	/*   %14 = load i32* %scevgep6, align 4, !legup.pipeline.start_time !13, !legup.pipeline.avail_time !5, !legup.pipeline.stage !12, !MSB !9, !LSB !4, !extendFrom !9
	start_time: 2 avail_time: 3 stage: 1 II: 2 start_ii_state = 2 % 2 = 0 avail_ii_state = 3 % 2 = 1*/
	if (LOOP22_1_state_enable_2) begin
		main_0_A_enable_a = 1'd1;
	end
	/* gaussian: %11*/
	/*   store i32 %18, i32* %scevgep6, align 4, !legup.pipeline.start_time !5, !legup.pipeline.avail_time !7, !legup.pipeline.stage !12, !MSB !3, !LSB !4, !extendFrom !3
	start_time: 3 avail_time: 4 stage: 1 II: 2 start_ii_state = 3 % 2 = 1 avail_ii_state = 4 % 2 = 0*/
	if (LOOP22_1_state_enable_3) begin
		main_0_A_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_A_address_a = 8'd0;
	if (LOOP22_1_valid_bit_2) begin
		main_0_A_address_a = (gaussian_11_scevgep6_reg_stage1 >>> 3'd2);
	end
	if (LOOP22_1_valid_bit_3) begin
		main_0_A_address_a = (gaussian_11_scevgep6_reg_stage1 >>> 3'd2);
	end
end
assign main_0_A_write_enable_b = 1'd0;
assign main_0_A_in_b = 0;
assign main_0_A_byteena_b = 1'd1;
always @(*) begin
	main_0_A_enable_b = 1'd0;
	/* gaussian: %11*/
	/*   %16 = load i32* %scevgep, align 4, !legup.pipeline.start_time !12, !legup.pipeline.avail_time !13, !legup.pipeline.stage !4, !MSB !9, !LSB !4, !extendFrom !9
	start_time: 1 avail_time: 2 stage: 0 II: 2 start_ii_state = 1 % 2 = 1 avail_ii_state = 2 % 2 = 0*/
	if (LOOP22_1_state_enable_1) begin
		main_0_A_enable_b = 1'd1;
	end
end
always @(*) begin
	main_0_A_address_b = 8'd0;
	if (LOOP22_1_valid_bit_1) begin
		main_0_A_address_b = (gaussian_11_scevgep >>> 3'd2);
	end
end
assign main_0_c_write_enable_a = 1'd0;
assign main_0_c_in_a = 0;
assign main_0_c_byteena_a = 1'd1;
always @(*) begin
	main_0_c_enable_a = 1'd0;
	/* gaussian: %11*/
	/*   %15 = load i32* %scevgep11, align 4, !legup.pipeline.start_time !4, !legup.pipeline.avail_time !12, !legup.pipeline.stage !4, !MSB !9, !LSB !4, !extendFrom !9
	start_time: 0 avail_time: 1 stage: 0 II: 2 start_ii_state = 0 % 2 = 0 avail_ii_state = 1 % 2 = 1*/
	if (LOOP22_1_state_enable_0) begin
		main_0_c_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_c_address_a = 4'd0;
	if (LOOP22_1_valid_bit_0) begin
		main_0_c_address_a = (gaussian_loopexitloopexit_scevgep11_reg >>> 3'd2);
	end
end
assign main_0_c_write_enable_b = 1'd0;
assign main_0_c_in_b = 0;
assign main_0_c_byteena_b = 1'd1;
assign main_0_c_enable_b = 1'd0;
assign main_0_c_address_b = 4'd0;

endmodule
