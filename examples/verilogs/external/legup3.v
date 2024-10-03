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

defparam
	legup_mult_1_unsigned_32_32_1_0.widtha = 32,
	legup_mult_1_unsigned_32_32_1_0.widthb = 32,
	legup_mult_1_unsigned_32_32_1_0.widthp = 64,
	legup_mult_1_unsigned_32_32_1_0.representation = "UNSIGNED";

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
		gaussian_loopexitloopexit_5 = ($signed({{1{gaussian_loopexitloopexit_4[5]}},gaussian_loopexitloopexit_4}) + 32'd14);
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
		gaussian_20_exitcond5 = (gaussian_20_21 == $signed(gaussian_loopexitloopexit_5_reg));
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
		gaussian_loopexitloopexit_4_stage0_reg <= ({2'd0,gaussian_loopexitloopexit_1_reg} * $signed(-32'd1));
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
`timescale 1 ns / 1 ns
module main
(
	clk,
	clk2x,
	clk1x_follower,
	reset,
	memory_controller_waitrequest,
	start,
	finish,
	return_val,
	gaussian_start,
	gaussian_finish,
	gaussian_arg_c,
	gaussian_arg_A,
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
	main_0_c_out_b,
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
	main_0_A_out_b
);

parameter [3:0] LEGUP_0 = 4'd0;
parameter [3:0] LEGUP_F_main_BB__0_1 = 4'd1;
parameter [3:0] LEGUP_F_main_BB__1_2 = 4'd2;
parameter [3:0] LEGUP_F_main_BB__1_3 = 4'd3;
parameter [3:0] LEGUP_loop_pipeline_wait_LOOP40_1_4 = 4'd4;
parameter [3:0] LEGUP_F_main_BB__6_5 = 4'd5;
parameter [3:0] LEGUP_F_main_BB__8_6 = 4'd6;
parameter [3:0] LEGUP_F_main_BB__8_8 = 4'd8;
parameter [3:0] LEGUP_F_main_BB__11_9 = 4'd9;
parameter [3:0] LEGUP_loop_pipeline_wait_LOOP50_1_10 = 4'd10;
parameter [3:0] LEGUP_F_main_BB__18_11 = 4'd11;
parameter [3:0] LEGUP_F_main_BB__21_12 = 4'd12;
parameter [3:0] LEGUP_function_call_7 = 4'd7;

input  clk;
input  clk2x;
input  clk1x_follower;
input  reset;
input  memory_controller_waitrequest;
input  start;
output reg  finish;
output reg [31:0] return_val;
output reg  gaussian_start;
input  gaussian_finish;
output reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] gaussian_arg_c;
output reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] gaussian_arg_A;
output reg  main_0_c_write_enable_a;
output reg [31:0] main_0_c_in_a;
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
output reg  main_0_A_write_enable_a;
output reg [31:0] main_0_A_in_a;
output  main_0_A_byteena_a;
output reg  main_0_A_enable_a;
output reg [7:0] main_0_A_address_a;
input [31:0] main_0_A_out_a;
output  main_0_A_write_enable_b;
output [31:0] main_0_A_in_b;
output  main_0_A_byteena_b;
output  main_0_A_enable_b;
output [7:0] main_0_A_address_b;
input [31:0] main_0_A_out_b;
reg [3:0] cur_state;
reg [3:0] next_state;
reg  fsm_stall;
reg [4:0] main_1_y04;
reg [4:0] main_1_y04_reg;
reg [9:0] main_1_2;
reg [9:0] main_1_2_reg;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] main_1_scevgep7;
reg [31:0] main_3_4;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] main_3_scevgep4;
reg [5:0] main_6_7;
reg  main_6_exitcond7;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] main_8_9;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] main_8_10;
reg [4:0] main_11_i202;
reg [4:0] main_11_i202_reg;
reg [9:0] main_11_12;
reg [9:0] main_11_12_reg;
reg [31:0] main_13_14;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] main_13_scevgep;
reg [31:0] main_13_15;
reg [5:0] main_18_20;
reg  main_18_exitcond4;
reg  LOOP40_1_valid_bit_0;
reg  LOOP40_1_state_stall_0;
reg  LOOP40_1_state_enable_0;
reg  LOOP40_1_valid_bit_1;
reg  LOOP40_1_state_stall_1;
reg  LOOP40_1_state_enable_1;
reg  LOOP40_1_valid_bit_2;
reg  LOOP40_1_state_stall_2;
reg  LOOP40_1_state_enable_2;
reg  LOOP40_1_II_counter;
reg  LOOP40_1_start;
reg  LOOP40_1_activate_pipeline;
reg [31:0] main_3_4_reg_stage1;
reg  LOOP40_1_pipeline_exit_cond;
reg [31:0] LOOP40_1_inductionVar_stage0;
reg  LOOP40_1_active;
reg  LOOP40_1_begin_pipeline;
reg  LOOP40_1_epilogue;
reg  LOOP40_1_pipeline_finish;
reg  LOOP40_1_only_last_stage_enabled;
reg  LOOP40_1_pipeline_finish_reg;
reg  LOOP50_1_valid_bit_0;
reg  LOOP50_1_state_stall_0;
reg  LOOP50_1_state_enable_0;
reg  LOOP50_1_valid_bit_1;
reg  LOOP50_1_state_stall_1;
reg  LOOP50_1_state_enable_1;
reg  LOOP50_1_valid_bit_2;
reg  LOOP50_1_state_stall_2;
reg  LOOP50_1_state_enable_2;
reg  LOOP50_1_II_counter;
reg  LOOP50_1_start;
reg  LOOP50_1_activate_pipeline;
reg [31:0] main_13_14_reg_stage1;
reg  LOOP50_1_pipeline_exit_cond;
reg [31:0] LOOP50_1_inductionVar_stage0;
reg  LOOP50_1_active;
reg  LOOP50_1_begin_pipeline;
reg  LOOP50_1_epilogue;
reg  LOOP50_1_pipeline_finish;
reg  LOOP50_1_only_last_stage_enabled;
reg  LOOP50_1_pipeline_finish_reg;

// Local Rams

// End Local Rams

/* Unsynthesizable Statements */
/* synthesis translate_off */
always @(posedge clk)
	if (!fsm_stall) begin
	/* main: %13*/
	/*   %16 = call i32 (i8*, ...)* @printf(i8* getelementptr inbounds ([4 x i8]* @.str8, i32 0, i32 0), i32 %15) #4, !legup.pipeline.start_time !9, !legup.pipeline.avail_time !9, !legup.pipeline.stage !9, !MSB !8, !LSB !4, !extendFrom !8
	start_time: 2 avail_time: 2 stage: 2 II: 1 start_ii_state = 2 % 1 = 0 avail_ii_state = 2 % 1 = 0*/
	if (LOOP50_1_state_enable_2) begin
		$write("%d ", $signed(main_13_15));
		// to fix quartus warning
		if (reset == 1'b0 && ^(main_13_15) === 1'bX) finish <= 0;
	end
	/* main: %18*/
	/*   %19 = call i32 (i8*, ...)* @printf(i8* getelementptr inbounds ([2 x i8]* @.str9, i32 0, i32 0)) #4, !MSB !8, !LSB !4, !extendFrom !8*/
	if ((cur_state == LEGUP_F_main_BB__18_11)) begin
		$write("\n");
	end
end
/* synthesis translate_on */
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
		next_state = LEGUP_F_main_BB__0_1;
LEGUP_F_main_BB__0_1:
		next_state = LEGUP_F_main_BB__1_2;
LEGUP_F_main_BB__11_9:
		next_state = LEGUP_loop_pipeline_wait_LOOP50_1_10;
LEGUP_F_main_BB__18_11:
	if ((fsm_stall == 1'd0) && (main_18_exitcond4 == 1'd1))
		next_state = LEGUP_F_main_BB__21_12;
	else if ((fsm_stall == 1'd0) && (main_18_exitcond4 == 1'd0))
		next_state = LEGUP_F_main_BB__11_9;
LEGUP_F_main_BB__1_2:
		next_state = LEGUP_F_main_BB__1_3;
LEGUP_F_main_BB__1_3:
		next_state = LEGUP_loop_pipeline_wait_LOOP40_1_4;
LEGUP_F_main_BB__21_12:
		next_state = LEGUP_0;
LEGUP_F_main_BB__6_5:
	if ((fsm_stall == 1'd0) && (main_6_exitcond7 == 1'd1))
		next_state = LEGUP_F_main_BB__8_6;
	else if ((fsm_stall == 1'd0) && (main_6_exitcond7 == 1'd0))
		next_state = LEGUP_F_main_BB__1_2;
LEGUP_F_main_BB__8_6:
		next_state = LEGUP_function_call_7;
LEGUP_F_main_BB__8_8:
		next_state = LEGUP_F_main_BB__11_9;
LEGUP_function_call_7:
	if ((fsm_stall == 1'd0) && (gaussian_finish == 1'd1))
		next_state = LEGUP_F_main_BB__8_8;
LEGUP_loop_pipeline_wait_LOOP40_1_4:
	if ((fsm_stall == 1'd0) && (LOOP40_1_pipeline_finish == 1'd1))
		next_state = LEGUP_F_main_BB__6_5;
	else if ((fsm_stall == 1'd0) && (LOOP40_1_pipeline_finish == 1'd1))
		next_state = LEGUP_F_main_BB__6_5;
LEGUP_loop_pipeline_wait_LOOP50_1_10:
	if ((fsm_stall == 1'd0) && (LOOP50_1_pipeline_finish == 1'd1))
		next_state = LEGUP_F_main_BB__18_11;
	else if ((fsm_stall == 1'd0) && (LOOP50_1_pipeline_finish == 1'd1))
		next_state = LEGUP_F_main_BB__18_11;
default:
	next_state = cur_state;
endcase

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
	/* main: %1*/
	/*   %y.04 = phi i32 [ 0, %0 ], [ %7, %6 ], !MSB !5, !LSB !4, !extendFrom !5*/
	if (((cur_state == LEGUP_F_main_BB__0_1) & (fsm_stall == 1'd0))) begin
		main_1_y04 = 32'd0;
	end
	/* main: %1*/
	/*   %y.04 = phi i32 [ 0, %0 ], [ %7, %6 ], !MSB !5, !LSB !4, !extendFrom !5*/
	else /* if ((((cur_state == LEGUP_F_main_BB__6_5) & (fsm_stall == 1'd0)) & (main_6_exitcond7 == 1'd0))) */ begin
		main_1_y04 = main_6_7;
	end
end
always @(posedge clk) begin
	/* main: %1*/
	/*   %y.04 = phi i32 [ 0, %0 ], [ %7, %6 ], !MSB !5, !LSB !4, !extendFrom !5*/
	if (((cur_state == LEGUP_F_main_BB__0_1) & (fsm_stall == 1'd0))) begin
		main_1_y04_reg <= main_1_y04;
	end
	/* main: %1*/
	/*   %y.04 = phi i32 [ 0, %0 ], [ %7, %6 ], !MSB !5, !LSB !4, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_main_BB__6_5) & (fsm_stall == 1'd0)) & (main_6_exitcond7 == 1'd0))) begin
		main_1_y04_reg <= main_1_y04;
	end
end
always @(*) begin
	/* main: %1*/
	/*   %2 = mul i32 %y.04, 16, !MSB !6, !LSB !5, !extendFrom !6*/
		main_1_2 = ({5'd0,main_1_y04_reg} * 32'd16);
end
always @(posedge clk) begin
	/* main: %1*/
	/*   %2 = mul i32 %y.04, 16, !MSB !6, !LSB !5, !extendFrom !6*/
	if ((cur_state == LEGUP_F_main_BB__1_2)) begin
		main_1_2_reg <= main_1_2;
	end
end
always @(*) begin
	/* main: %1*/
	/*   %scevgep7 = getelementptr [1 x [16 x i32]]* %c, i32 0, i32 0, i32 %y.04, !MSB !3, !LSB !4, !extendFrom !3*/
		main_1_scevgep7 = (1'd0 + (4 * {27'd0,main_1_y04_reg}));
end
always @(*) begin
	/* main: %3*/
	/*   %4 = add i32 %2, %x.03, !legup.pipeline.start_time !4, !legup.pipeline.avail_time !4, !legup.pipeline.stage !4, !MSB !8, !LSB !4, !extendFrom !8
	start_time: 0 avail_time: 0 stage: 0 II: 1 start_ii_state = 0 % 1 = 0 avail_ii_state = 0 % 1 = 0*/
		main_3_4 = ({22'd0,main_1_2_reg} + LOOP40_1_inductionVar_stage0);
end
always @(*) begin
	/* main: %3*/
	/*   %scevgep4 = getelementptr [1 x [256 x i32]]* %A, i32 0, i32 0, i32 %4, !legup.pipeline.start_time !7, !legup.pipeline.avail_time !7, !legup.pipeline.stage !7, !MSB !3, !LSB !4, !extendFrom !3
	start_time: 1 avail_time: 1 stage: 1 II: 1 start_ii_state = 1 % 1 = 0 avail_ii_state = 1 % 1 = 0*/
		main_3_scevgep4 = (1'd0 + (4 * main_3_4_reg_stage1));
end
always @(*) begin
	/* main: %6*/
	/*   %7 = add nsw i32 %y.04, 1, !MSB !13, !LSB !4, !extendFrom !13*/
		main_6_7 = ({1'd0,main_1_y04_reg} + 32'd1);
end
always @(*) begin
	/* main: %6*/
	/*   %exitcond7 = icmp eq i32 %7, 16, !MSB !4, !LSB !4, !extendFrom !4*/
		main_6_exitcond7 = (main_6_7 == 32'd16);
end
always @(*) begin
	/* main: %8*/
	/*   %9 = getelementptr inbounds [1 x [16 x i32]]* %c, i32 0, i32 0, i32 0, !MSB !3, !LSB !4, !extendFrom !3*/
if (reset) begin main_8_9 = 0; end
		main_8_9 = 1'd0;
end
always @(*) begin
	/* main: %8*/
	/*   %10 = getelementptr inbounds [1 x [256 x i32]]* %A, i32 0, i32 0, i32 0, !MSB !3, !LSB !4, !extendFrom !3*/
if (reset) begin main_8_10 = 0; end
		main_8_10 = 1'd0;
end
always @(*) begin
	/* main: %11*/
	/*   %i2.02 = phi i32 [ 0, %8 ], [ %20, %18 ], !MSB !5, !LSB !4, !extendFrom !5*/
	if (((cur_state == LEGUP_F_main_BB__8_8) & (fsm_stall == 1'd0))) begin
		main_11_i202 = 32'd0;
	end
	/* main: %11*/
	/*   %i2.02 = phi i32 [ 0, %8 ], [ %20, %18 ], !MSB !5, !LSB !4, !extendFrom !5*/
	else /* if ((((cur_state == LEGUP_F_main_BB__18_11) & (fsm_stall == 1'd0)) & (main_18_exitcond4 == 1'd0))) */ begin
		main_11_i202 = main_18_20;
	end
end
always @(posedge clk) begin
	/* main: %11*/
	/*   %i2.02 = phi i32 [ 0, %8 ], [ %20, %18 ], !MSB !5, !LSB !4, !extendFrom !5*/
	if (((cur_state == LEGUP_F_main_BB__8_8) & (fsm_stall == 1'd0))) begin
		main_11_i202_reg <= main_11_i202;
	end
	/* main: %11*/
	/*   %i2.02 = phi i32 [ 0, %8 ], [ %20, %18 ], !MSB !5, !LSB !4, !extendFrom !5*/
	if ((((cur_state == LEGUP_F_main_BB__18_11) & (fsm_stall == 1'd0)) & (main_18_exitcond4 == 1'd0))) begin
		main_11_i202_reg <= main_11_i202;
	end
end
always @(*) begin
	/* main: %11*/
	/*   %12 = mul i32 %i2.02, 16, !MSB !6, !LSB !5, !extendFrom !6*/
		main_11_12 = ({5'd0,main_11_i202_reg} * 32'd16);
end
always @(posedge clk) begin
	/* main: %11*/
	/*   %12 = mul i32 %i2.02, 16, !MSB !6, !LSB !5, !extendFrom !6*/
	if ((cur_state == LEGUP_F_main_BB__11_9)) begin
		main_11_12_reg <= main_11_12;
	end
end
always @(*) begin
	/* main: %13*/
	/*   %14 = add i32 %12, %j.01, !legup.pipeline.start_time !4, !legup.pipeline.avail_time !4, !legup.pipeline.stage !4, !MSB !8, !LSB !4, !extendFrom !8
	start_time: 0 avail_time: 0 stage: 0 II: 1 start_ii_state = 0 % 1 = 0 avail_ii_state = 0 % 1 = 0*/
		main_13_14 = ({22'd0,main_11_12_reg} + LOOP50_1_inductionVar_stage0);
end
always @(*) begin
	/* main: %13*/
	/*   %scevgep = getelementptr [1 x [256 x i32]]* %A, i32 0, i32 0, i32 %14, !legup.pipeline.start_time !7, !legup.pipeline.avail_time !7, !legup.pipeline.stage !7, !MSB !3, !LSB !4, !extendFrom !3
	start_time: 1 avail_time: 1 stage: 1 II: 1 start_ii_state = 1 % 1 = 0 avail_ii_state = 1 % 1 = 0*/
		main_13_scevgep = (1'd0 + (4 * main_13_14_reg_stage1));
end
always @(*) begin
	/* main: %13*/
	/*   %15 = load i32* %scevgep, align 4, !legup.pipeline.start_time !7, !legup.pipeline.avail_time !9, !legup.pipeline.stage !7, !MSB !8, !LSB !4, !extendFrom !8
	start_time: 1 avail_time: 2 stage: 1 II: 1 start_ii_state = 1 % 1 = 0 avail_ii_state = 2 % 1 = 0*/
		main_13_15 = main_0_A_out_a;
end
always @(*) begin
	/* main: %18*/
	/*   %20 = add nsw i32 %i2.02, 1, !MSB !13, !LSB !4, !extendFrom !13*/
		main_18_20 = ({1'd0,main_11_i202_reg} + 32'd1);
end
always @(*) begin
	/* main: %18*/
	/*   %exitcond4 = icmp eq i32 %20, 16, !MSB !4, !LSB !4, !extendFrom !4*/
		main_18_exitcond4 = (main_18_20 == 32'd16);
end
always @(posedge clk) begin
	if (~(LOOP40_1_state_stall_0)) begin
		LOOP40_1_valid_bit_0 <= ((LOOP40_1_II_counter == 1'd0) & LOOP40_1_start);
	end
	if (reset) begin
		LOOP40_1_valid_bit_0 <= 1'd0;
	end
end
always @(*) begin
	LOOP40_1_state_stall_0 = 1'd0;
	if (LOOP40_1_state_stall_1) begin
		LOOP40_1_state_stall_0 = 1'd1;
	end
end
always @(*) begin
	LOOP40_1_state_enable_0 = (LOOP40_1_valid_bit_0 & ~(LOOP40_1_state_stall_0));
end
always @(posedge clk) begin
	if (~(LOOP40_1_state_stall_1)) begin
		LOOP40_1_valid_bit_1 <= LOOP40_1_state_enable_0;
	end
	if (reset) begin
		LOOP40_1_valid_bit_1 <= 1'd0;
	end
end
always @(*) begin
	LOOP40_1_state_stall_1 = 1'd0;
	if (LOOP40_1_state_stall_2) begin
		LOOP40_1_state_stall_1 = 1'd1;
	end
end
always @(*) begin
	LOOP40_1_state_enable_1 = (LOOP40_1_valid_bit_1 & ~(LOOP40_1_state_stall_1));
end
always @(posedge clk) begin
	if (~(LOOP40_1_state_stall_2)) begin
		LOOP40_1_valid_bit_2 <= LOOP40_1_state_enable_1;
	end
	if (reset) begin
		LOOP40_1_valid_bit_2 <= 1'd0;
	end
end
always @(*) begin
	LOOP40_1_state_stall_2 = 1'd0;
	if (reset) begin
		LOOP40_1_state_stall_2 = 1'd0;
	end
end
always @(*) begin
	LOOP40_1_state_enable_2 = (LOOP40_1_valid_bit_2 & ~(LOOP40_1_state_stall_2));
end
always @(posedge clk) begin
	LOOP40_1_II_counter <= (LOOP40_1_II_counter + 1'd1);
	if (reset) begin
		LOOP40_1_II_counter <= 1'd0;
	end
	if ((LOOP40_1_II_counter == 1'd0)) begin
		LOOP40_1_II_counter <= 1'd0;
	end
end
always @(*) begin
	LOOP40_1_start = (LOOP40_1_activate_pipeline | ((LOOP40_1_active & ~(LOOP40_1_epilogue)) & ~((LOOP40_1_state_enable_0 & LOOP40_1_pipeline_exit_cond))));
	if (reset) begin
		LOOP40_1_start = 1'd0;
	end
end
always @(*) begin
	LOOP40_1_activate_pipeline = (((fsm_stall == 1'd0) & LOOP40_1_begin_pipeline) & ~(LOOP40_1_active));
end
always @(posedge clk) begin
	if (LOOP40_1_state_enable_0) begin
		main_3_4_reg_stage1 <= main_3_4;
	end
end
always @(*) begin
	LOOP40_1_pipeline_exit_cond = (LOOP40_1_inductionVar_stage0 == 15);
end
always @(posedge clk) begin
	if (reset) begin
		LOOP40_1_inductionVar_stage0 <= 0;
	end
	if (LOOP40_1_activate_pipeline) begin
		LOOP40_1_inductionVar_stage0 <= 0;
	end
	if (((LOOP40_1_II_counter == 1'd0) & LOOP40_1_state_enable_0)) begin
		LOOP40_1_inductionVar_stage0 <= (LOOP40_1_inductionVar_stage0 + 1'd1);
	end
end
always @(posedge clk) begin
	if (reset) begin
		LOOP40_1_active <= 1'd0;
	end
	if (LOOP40_1_activate_pipeline) begin
		LOOP40_1_active <= 1'd1;
	end
	if (((~(LOOP40_1_state_stall_0) & LOOP40_1_epilogue) & LOOP40_1_only_last_stage_enabled)) begin
		LOOP40_1_active <= 1'd0;
	end
end
always @(*) begin
	LOOP40_1_begin_pipeline = 1'd0;
	if (reset) begin
		LOOP40_1_begin_pipeline = 1'd0;
	end
	if (((cur_state == LEGUP_F_main_BB__1_3) & (fsm_stall == 1'd0))) begin
		LOOP40_1_begin_pipeline = 1'd1;
	end
end
always @(posedge clk) begin
	if (reset) begin
		LOOP40_1_epilogue <= 1'd0;
	end
	if ((LOOP40_1_state_enable_0 & LOOP40_1_pipeline_exit_cond)) begin
		LOOP40_1_epilogue <= 1'd1;
	end
	if (((~(LOOP40_1_state_stall_0) & LOOP40_1_epilogue) & LOOP40_1_only_last_stage_enabled)) begin
		LOOP40_1_epilogue <= 1'd0;
	end
end
always @(*) begin
	LOOP40_1_pipeline_finish = (((~(LOOP40_1_state_stall_0) & LOOP40_1_epilogue) & LOOP40_1_only_last_stage_enabled) | LOOP40_1_pipeline_finish_reg);
end
always @(*) begin
	LOOP40_1_only_last_stage_enabled = ((~(LOOP40_1_state_enable_0) & ~(LOOP40_1_state_enable_1)) & LOOP40_1_state_enable_2);
end
always @(posedge clk) begin
	LOOP40_1_pipeline_finish_reg <= LOOP40_1_pipeline_finish;
	if (reset) begin
		LOOP40_1_pipeline_finish_reg <= 1'd0;
	end
	if (LOOP40_1_activate_pipeline) begin
		LOOP40_1_pipeline_finish_reg <= 1'd0;
	end
end
always @(posedge clk) begin
	if (~(LOOP50_1_state_stall_0)) begin
		LOOP50_1_valid_bit_0 <= ((LOOP50_1_II_counter == 1'd0) & LOOP50_1_start);
	end
	if (reset) begin
		LOOP50_1_valid_bit_0 <= 1'd0;
	end
end
always @(*) begin
	LOOP50_1_state_stall_0 = 1'd0;
	if (LOOP50_1_state_stall_1) begin
		LOOP50_1_state_stall_0 = 1'd1;
	end
end
always @(*) begin
	LOOP50_1_state_enable_0 = (LOOP50_1_valid_bit_0 & ~(LOOP50_1_state_stall_0));
end
always @(posedge clk) begin
	if (~(LOOP50_1_state_stall_1)) begin
		LOOP50_1_valid_bit_1 <= LOOP50_1_state_enable_0;
	end
	if (reset) begin
		LOOP50_1_valid_bit_1 <= 1'd0;
	end
end
always @(*) begin
	LOOP50_1_state_stall_1 = 1'd0;
	if (LOOP50_1_state_stall_2) begin
		LOOP50_1_state_stall_1 = 1'd1;
	end
end
always @(*) begin
	LOOP50_1_state_enable_1 = (LOOP50_1_valid_bit_1 & ~(LOOP50_1_state_stall_1));
end
always @(posedge clk) begin
	if (~(LOOP50_1_state_stall_2)) begin
		LOOP50_1_valid_bit_2 <= LOOP50_1_state_enable_1;
	end
	if (reset) begin
		LOOP50_1_valid_bit_2 <= 1'd0;
	end
end
always @(*) begin
	LOOP50_1_state_stall_2 = 1'd0;
	if (reset) begin
		LOOP50_1_state_stall_2 = 1'd0;
	end
end
always @(*) begin
	LOOP50_1_state_enable_2 = (LOOP50_1_valid_bit_2 & ~(LOOP50_1_state_stall_2));
end
always @(posedge clk) begin
	LOOP50_1_II_counter <= (LOOP50_1_II_counter + 1'd1);
	if (reset) begin
		LOOP50_1_II_counter <= 1'd0;
	end
	if ((LOOP50_1_II_counter == 1'd0)) begin
		LOOP50_1_II_counter <= 1'd0;
	end
end
always @(*) begin
	LOOP50_1_start = (LOOP50_1_activate_pipeline | ((LOOP50_1_active & ~(LOOP50_1_epilogue)) & ~((LOOP50_1_state_enable_0 & LOOP50_1_pipeline_exit_cond))));
	if (reset) begin
		LOOP50_1_start = 1'd0;
	end
end
always @(*) begin
	LOOP50_1_activate_pipeline = (((fsm_stall == 1'd0) & LOOP50_1_begin_pipeline) & ~(LOOP50_1_active));
end
always @(posedge clk) begin
	if (LOOP50_1_state_enable_0) begin
		main_13_14_reg_stage1 <= main_13_14;
	end
end
always @(*) begin
	LOOP50_1_pipeline_exit_cond = (LOOP50_1_inductionVar_stage0 == 15);
end
always @(posedge clk) begin
	if (reset) begin
		LOOP50_1_inductionVar_stage0 <= 0;
	end
	if (LOOP50_1_activate_pipeline) begin
		LOOP50_1_inductionVar_stage0 <= 0;
	end
	if (((LOOP50_1_II_counter == 1'd0) & LOOP50_1_state_enable_0)) begin
		LOOP50_1_inductionVar_stage0 <= (LOOP50_1_inductionVar_stage0 + 1'd1);
	end
end
always @(posedge clk) begin
	if (reset) begin
		LOOP50_1_active <= 1'd0;
	end
	if (LOOP50_1_activate_pipeline) begin
		LOOP50_1_active <= 1'd1;
	end
	if (((~(LOOP50_1_state_stall_0) & LOOP50_1_epilogue) & LOOP50_1_only_last_stage_enabled)) begin
		LOOP50_1_active <= 1'd0;
	end
end
always @(*) begin
	LOOP50_1_begin_pipeline = 1'd0;
	if (reset) begin
		LOOP50_1_begin_pipeline = 1'd0;
	end
	if (((cur_state == LEGUP_F_main_BB__11_9) & (fsm_stall == 1'd0))) begin
		LOOP50_1_begin_pipeline = 1'd1;
	end
end
always @(posedge clk) begin
	if (reset) begin
		LOOP50_1_epilogue <= 1'd0;
	end
	if ((LOOP50_1_state_enable_0 & LOOP50_1_pipeline_exit_cond)) begin
		LOOP50_1_epilogue <= 1'd1;
	end
	if (((~(LOOP50_1_state_stall_0) & LOOP50_1_epilogue) & LOOP50_1_only_last_stage_enabled)) begin
		LOOP50_1_epilogue <= 1'd0;
	end
end
always @(*) begin
	LOOP50_1_pipeline_finish = (((~(LOOP50_1_state_stall_0) & LOOP50_1_epilogue) & LOOP50_1_only_last_stage_enabled) | LOOP50_1_pipeline_finish_reg);
end
always @(*) begin
	LOOP50_1_only_last_stage_enabled = ((~(LOOP50_1_state_enable_0) & ~(LOOP50_1_state_enable_1)) & LOOP50_1_state_enable_2);
end
always @(posedge clk) begin
	LOOP50_1_pipeline_finish_reg <= LOOP50_1_pipeline_finish;
	if (reset) begin
		LOOP50_1_pipeline_finish_reg <= 1'd0;
	end
	if (LOOP50_1_activate_pipeline) begin
		LOOP50_1_pipeline_finish_reg <= 1'd0;
	end
end
always @(posedge clk) begin
	if ((cur_state == LEGUP_0)) begin
		finish <= 1'd0;
	end
	/* main: %21*/
	/*   ret i32 0, !MSB !3, !LSB !4, !extendFrom !3*/
	if ((cur_state == LEGUP_F_main_BB__21_12)) begin
		finish <= (fsm_stall == 1'd0);
	end
end
always @(posedge clk) begin
	if ((cur_state == LEGUP_0)) begin
		return_val <= 0;
	end
	/* main: %21*/
	/*   ret i32 0, !MSB !3, !LSB !4, !extendFrom !3*/
	if ((cur_state == LEGUP_F_main_BB__21_12)) begin
		return_val <= 32'd0;
	end
end
always @(posedge clk) begin
	gaussian_start <= 1'd0;
	/* main: %8*/
	/*   call fastcc void @gaussian(i32* %9, i32* %10) #4, !MSB !3, !LSB !4, !extendFrom !3*/
	if ((cur_state == LEGUP_F_main_BB__8_6)) begin
		gaussian_start <= 1'd1;
	end
	if ((cur_state == LEGUP_F_main_BB__8_8)) begin
		gaussian_start <= 1'd0;
	end
end
always @(posedge clk) begin
	gaussian_arg_c <= 0;
	/* main: %8*/
	/*   call fastcc void @gaussian(i32* %9, i32* %10) #4, !MSB !3, !LSB !4, !extendFrom !3*/
	if ((cur_state == LEGUP_F_main_BB__8_6)) begin
		gaussian_arg_c <= main_8_9;
	end
end
always @(posedge clk) begin
	gaussian_arg_A <= 0;
	/* main: %8*/
	/*   call fastcc void @gaussian(i32* %9, i32* %10) #4, !MSB !3, !LSB !4, !extendFrom !3*/
	if ((cur_state == LEGUP_F_main_BB__8_6)) begin
		gaussian_arg_A <= main_8_10;
	end
end
always @(*) begin
	main_0_c_write_enable_a = 1'd0;
	/* main: %1*/
	/*   store i32 1, i32* %scevgep7, align 4, !MSB !3, !LSB !4, !extendFrom !3*/
	if ((cur_state == LEGUP_F_main_BB__1_2)) begin
		main_0_c_write_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_c_in_a = 0;
	/* main: %1*/
	/*   store i32 1, i32* %scevgep7, align 4, !MSB !3, !LSB !4, !extendFrom !3*/
	if ((cur_state == LEGUP_F_main_BB__1_2)) begin
		main_0_c_in_a = 32'd1;
	end
end
assign main_0_c_byteena_a = 1'd1;
always @(*) begin
	main_0_c_enable_a = 1'd0;
	/* main: %1*/
	/*   store i32 1, i32* %scevgep7, align 4, !MSB !3, !LSB !4, !extendFrom !3*/
	if ((cur_state == LEGUP_F_main_BB__1_2)) begin
		main_0_c_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_c_address_a = 4'd0;
	/* main: %1*/
	/*   store i32 1, i32* %scevgep7, align 4, !MSB !3, !LSB !4, !extendFrom !3*/
	if ((cur_state == LEGUP_F_main_BB__1_2)) begin
		main_0_c_address_a = (main_1_scevgep7 >>> 3'd2);
	end
end
assign main_0_c_write_enable_b = 1'd0;
assign main_0_c_in_b = 0;
assign main_0_c_byteena_b = 1'd1;
assign main_0_c_enable_b = 1'd0;
assign main_0_c_address_b = 4'd0;
always @(*) begin
	main_0_A_write_enable_a = 1'd0;
	if (LOOP40_1_valid_bit_1) begin
		main_0_A_write_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_A_in_a = 0;
	if (LOOP40_1_valid_bit_1) begin
		main_0_A_in_a = 32'd1;
	end
end
assign main_0_A_byteena_a = 1'd1;
always @(*) begin
	main_0_A_enable_a = 1'd0;
	/* main: %3*/
	/*   store i32 1, i32* %scevgep4, align 4, !legup.pipeline.start_time !7, !legup.pipeline.avail_time !9, !legup.pipeline.stage !7, !MSB !3, !LSB !4, !extendFrom !3
	start_time: 1 avail_time: 2 stage: 1 II: 1 start_ii_state = 1 % 1 = 0 avail_ii_state = 2 % 1 = 0*/
	if (LOOP40_1_state_enable_1) begin
		main_0_A_enable_a = 1'd1;
	end
	/* main: %13*/
	/*   %15 = load i32* %scevgep, align 4, !legup.pipeline.start_time !7, !legup.pipeline.avail_time !9, !legup.pipeline.stage !7, !MSB !8, !LSB !4, !extendFrom !8
	start_time: 1 avail_time: 2 stage: 1 II: 1 start_ii_state = 1 % 1 = 0 avail_ii_state = 2 % 1 = 0*/
	if (LOOP50_1_state_enable_1) begin
		main_0_A_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_A_address_a = 8'd0;
	if (LOOP40_1_valid_bit_1) begin
		main_0_A_address_a = (main_3_scevgep4 >>> 3'd2);
	end
	if (LOOP50_1_valid_bit_1) begin
		main_0_A_address_a = (main_13_scevgep >>> 3'd2);
	end
end
assign main_0_A_write_enable_b = 1'd0;
assign main_0_A_in_b = 0;
assign main_0_A_byteena_b = 1'd1;
assign main_0_A_enable_b = 1'd0;
assign main_0_A_address_b = 8'd0;

endmodule
module ram_dual_port
(
	clk,
	clken,
	address_a,
	address_b,
	wren_a,
	wren_b,
	data_a,
	data_b,
	byteena_a,
	byteena_b,
	q_a,
	q_b
);

parameter  width_a = 1'd0;
parameter  width_b = 1'd0;
parameter  widthad_a = 1'd0;
parameter  widthad_b = 1'd0;
parameter  numwords_a = 1'd0;
parameter  numwords_b = 1'd0;
parameter  latency = 1;
parameter  init_file = "UNUSED";
parameter  width_be_a = 1'd0;
parameter  width_be_b = 1'd0;
input  clk;
input  clken;
input [(widthad_a-1):0] address_a;
input [(widthad_b-1):0] address_b;
output wire [(width_a-1):0] q_a;
output wire [(width_b-1):0] q_b;
wire [(width_a-1):0] q_a_wire;
wire [(width_b-1):0] q_b_wire;
input  wren_a;
input  wren_b;
input [(width_a-1):0] data_a;
input [(width_b-1):0] data_b;
input [width_be_a-1:0] byteena_a;
input [width_be_b-1:0] byteena_b;
reg  clk_wire;

altsyncram altsyncram_component (
	.address_a (address_a),
	.address_b (address_b),
    .clock0 (clk_wire),
    .clock1 (1'd1),
    .clocken0 (clken),
    .clocken1 (1'd1),
    .clocken2 (1'd1),
    .clocken3 (1'd1),
    .aclr0 (1'd0),
    .aclr1 (1'd0),
    .addressstall_a (1'd0),
    .addressstall_b (1'd0),
    .eccstatus (),
    .rden_a (clken),
    .rden_b (clken),
    .q_a (q_a_wire),
    .q_b (q_b_wire),
    .wren_a (wren_a),
    .wren_b (wren_b),
    .data_a (data_a),
    .data_b (data_b),
    .byteena_a (byteena_a),
    .byteena_b (byteena_b)
);
defparam
    altsyncram_component.width_byteena_a = width_be_a,
    altsyncram_component.width_byteena_b = width_be_b,
    altsyncram_component.operation_mode = "BIDIR_DUAL_PORT",
    altsyncram_component.read_during_write_mode_mixed_ports = "OLD_DATA",
    altsyncram_component.init_file = init_file,
    altsyncram_component.lpm_hint = "ENABLE_RUNTIME_MOD=NO",
    altsyncram_component.lpm_type = "altsyncram",
    altsyncram_component.power_up_uninitialized = "FALSE",
    altsyncram_component.intended_device_family = "Cyclone V",
    altsyncram_component.clock_enable_input_a = "BYPASS",
    altsyncram_component.clock_enable_input_b = "BYPASS",
    altsyncram_component.clock_enable_output_a = "BYPASS",
    altsyncram_component.clock_enable_output_b = "BYPASS",
    altsyncram_component.outdata_aclr_a = "NONE",
    altsyncram_component.outdata_aclr_b = "NONE",
    altsyncram_component.outdata_reg_a = "UNREGISTERED",
    altsyncram_component.outdata_reg_b = "UNREGISTERED",
    altsyncram_component.numwords_a = numwords_a,
    altsyncram_component.numwords_b = numwords_b,
    altsyncram_component.widthad_a = widthad_a,
    altsyncram_component.widthad_b = widthad_b,
    altsyncram_component.width_a = width_a,
    altsyncram_component.width_b = width_b,
    altsyncram_component.address_reg_b = "CLOCK0",
    altsyncram_component.byteena_reg_b = "CLOCK0",
    altsyncram_component.indata_reg_b = "CLOCK0",
    altsyncram_component.wrcontrol_wraddress_reg_b = "CLOCK0";
always @(*) begin
    clk_wire = clk;
end




integer j;
reg [(width_a-1):0] q_a_reg[latency:1], q_b_reg[latency:1];

always @(*)
begin
   q_a_reg[1] <= q_a_wire;
   q_b_reg[1] <= q_b_wire;
end

always @(posedge clk)
if (clken)
begin
   for (j = 1; j < latency; j=j+1)
   begin
       q_a_reg[j+1] <= q_a_reg[j];
       q_b_reg[j+1] <= q_b_reg[j];
   end
end

assign q_a = (clken) ? q_a_reg[latency] : 0;
assign q_b = (clken) ? q_b_reg[latency] : 0;


endmodule
module rom_dual_port
(
	clk,
	clken,
	address_a,
	address_b,
	q_a,
	q_b
);

parameter  width_a = 1'd0;
parameter  width_b = 1'd0;
parameter  widthad_a = 1'd0;
parameter  widthad_b = 1'd0;
parameter  numwords_a = 1'd0;
parameter  numwords_b = 1'd0;
parameter  latency = 1;
parameter  init_file = "UNUSED";
input  clk;
input  clken;
input [(widthad_a-1):0] address_a;
input [(widthad_b-1):0] address_b;
output wire [(width_a-1):0] q_a;
output wire [(width_b-1):0] q_b;
wire [(width_a-1):0] q_a_wire;
wire [(width_b-1):0] q_b_wire;
reg  clk_wire;

altsyncram altsyncram_component (
	.address_a (address_a),
	.address_b (address_b),
    .clock0 (clk_wire),
    .clock1 (1'd1),
    .clocken0 (clken),
    .clocken1 (1'd1),
    .clocken2 (1'd1),
    .clocken3 (1'd1),
    .aclr0 (1'd0),
    .aclr1 (1'd0),
    .addressstall_a (1'd0),
    .addressstall_b (1'd0),
    .eccstatus (),
    .rden_a (clken),
    .rden_b (clken),
    .q_a (q_a_wire),
    .q_b (q_b_wire),
    .wren_a (1'd0),
    .wren_b (1'd0),
    .data_a (),
    .data_b (),
    .byteena_a (),
    .byteena_b ()
);
defparam
    altsyncram_component.operation_mode = "BIDIR_DUAL_PORT",
    altsyncram_component.read_during_write_mode_mixed_ports = "OLD_DATA",
    altsyncram_component.init_file = init_file,
    altsyncram_component.lpm_hint = "ENABLE_RUNTIME_MOD=NO",
    altsyncram_component.lpm_type = "altsyncram",
    altsyncram_component.power_up_uninitialized = "FALSE",
    altsyncram_component.intended_device_family = "Cyclone V",
    altsyncram_component.clock_enable_input_a = "BYPASS",
    altsyncram_component.clock_enable_input_b = "BYPASS",
    altsyncram_component.clock_enable_output_a = "BYPASS",
    altsyncram_component.clock_enable_output_b = "BYPASS",
    altsyncram_component.outdata_aclr_a = "NONE",
    altsyncram_component.outdata_aclr_b = "NONE",
    altsyncram_component.outdata_reg_a = "UNREGISTERED",
    altsyncram_component.outdata_reg_b = "UNREGISTERED",
    altsyncram_component.numwords_a = numwords_a,
    altsyncram_component.numwords_b = numwords_b,
    altsyncram_component.widthad_a = widthad_a,
    altsyncram_component.widthad_b = widthad_b,
    altsyncram_component.width_a = width_a,
    altsyncram_component.width_b = width_b,
    altsyncram_component.address_reg_b = "CLOCK0",
    altsyncram_component.byteena_reg_b = "CLOCK0",
    altsyncram_component.indata_reg_b = "CLOCK0",
    altsyncram_component.wrcontrol_wraddress_reg_b = "CLOCK0";
always @(*) begin
    clk_wire = clk;
end




integer j;
reg [(width_a-1):0] q_a_reg[latency:1], q_b_reg[latency:1];

always @(*)
begin
   q_a_reg[1] <= q_a_wire;
   q_b_reg[1] <= q_b_wire;
end

always @(posedge clk)
if (clken)
begin
   for (j = 1; j < latency; j=j+1)
   begin
       q_a_reg[j+1] <= q_a_reg[j];
       q_b_reg[j+1] <= q_b_reg[j];
   end
end

assign q_a = (clken) ? q_a_reg[latency] : 0;
assign q_b = (clken) ? q_b_reg[latency] : 0;


endmodule
module hex_digits(x, hex_LEDs);
    input [3:0] x;
    output [6:0] hex_LEDs;
    
    assign hex_LEDs[0] = (~x[3] & ~x[2] & ~x[1] & x[0]) |
                            (~x[3] & x[2] & ~x[1] & ~x[0]) |
                            (x[3] & x[2] & ~x[1] & x[0]) |
                            (x[3] & ~x[2] & x[1] & x[0]);
    assign hex_LEDs[1] = (~x[3] & x[2] & ~x[1] & x[0]) |
                            (x[3] & x[1] & x[0]) |
                            (x[3] & x[2] & ~x[0]) |
                            (x[2] & x[1] & ~x[0]);
    assign hex_LEDs[2] = (x[3] & x[2] & ~x[0]) |
                            (x[3] & x[2] & x[1]) |
                            (~x[3] & ~x[2] & x[1] & ~x[0]);
    assign hex_LEDs[3] = (~x[3] & ~x[2] & ~x[1] & x[0]) | 
                            (~x[3] & x[2] & ~x[1] & ~x[0]) | 
                            (x[2] & x[1] & x[0]) | 
                            (x[3] & ~x[2] & x[1] & ~x[0]);
    assign hex_LEDs[4] = (~x[3] & x[0]) |
                            (~x[3] & x[2] & ~x[1]) |
                            (~x[2] & ~x[1] & x[0]);
    assign hex_LEDs[5] = (~x[3] & ~x[2] & x[0]) | 
                            (~x[3] & ~x[2] & x[1]) | 
                            (~x[3] & x[1] & x[0]) | 
                            (x[3] & x[2] & ~x[1] & x[0]);
    assign hex_LEDs[6] = (~x[3] & ~x[2] & ~x[1]) | 
                            (x[3] & x[2] & ~x[1] & ~x[0]) | 
                            (~x[3] & x[2] & x[1] & x[0]);
    
endmodule
`timescale 1 ns / 1 ns
module main_tb
(
);

reg  clk;
reg  reset;
reg  start;
reg  waitrequest;
wire [31:0] return_val;
wire  finish;
wire  clk2x;
wire  clk1x_follower;


top top_inst (
	.clk (clk),
	.clk2x (clk2x),
	.clk1x_follower (clk1x_follower),
	.reset (reset),
	.memory_controller_waitrequest (waitrequest),
	.start (start),
	.finish (finish),
	.return_val (return_val)
);


// Local Rams

// End Local Rams


initial 
    clk = 0;
always @(clk)
    clk <= #10 ~clk;

initial begin
//$monitor("At t=%t clk=%b %b %b %b %d", $time, clk, reset, start, finish, return_val);
reset <= 1;
@(negedge clk);
reset <= 0;
start <= 1;
@(negedge clk);
start <= 0;
end

always@(finish) begin
    if (finish == 1) begin
        $display("At t=%t clk=%b finish=%b return_val=%d", $time, clk, finish, return_val);
        $display("Cycles: %d", ($time-50)/20);
        $finish;
    end
end

initial begin
waitrequest <= 1;
@(negedge clk);
waitrequest <= 0;
end


endmodule
`timescale 1 ns / 1 ns
module top
(
	clk,
	clk2x,
	clk1x_follower,
	reset,
	memory_controller_waitrequest,
	start,
	finish,
	return_val
);

input  clk;
input  clk2x;
input  clk1x_follower;
input  reset;
input  memory_controller_waitrequest;
input  start;
output reg  finish;
output reg [31:0] return_val;
reg  main_inst_clk;
reg  main_inst_clk2x;
reg  main_inst_clk1x_follower;
reg  main_inst_reset;
reg  main_inst_memory_controller_waitrequest;
reg  main_inst_start;
wire  main_inst_finish;
wire [31:0] main_inst_return_val;
wire  main_inst_gaussian_start;
reg  main_inst_gaussian_finish;
wire [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] main_inst_gaussian_arg_c;
wire [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] main_inst_gaussian_arg_A;
wire  main_inst_main_0_c_write_enable_a;
wire [31:0] main_inst_main_0_c_in_a;
wire  main_inst_main_0_c_byteena_a;
wire  main_inst_main_0_c_enable_a;
wire [3:0] main_inst_main_0_c_address_a;
reg [31:0] main_inst_main_0_c_out_a;
wire  main_inst_main_0_c_write_enable_b;
wire [31:0] main_inst_main_0_c_in_b;
wire  main_inst_main_0_c_byteena_b;
wire  main_inst_main_0_c_enable_b;
wire [3:0] main_inst_main_0_c_address_b;
reg [31:0] main_inst_main_0_c_out_b;
wire  main_inst_main_0_A_write_enable_a;
wire [31:0] main_inst_main_0_A_in_a;
wire  main_inst_main_0_A_byteena_a;
wire  main_inst_main_0_A_enable_a;
wire [7:0] main_inst_main_0_A_address_a;
reg [31:0] main_inst_main_0_A_out_a;
wire  main_inst_main_0_A_write_enable_b;
wire [31:0] main_inst_main_0_A_in_b;
wire  main_inst_main_0_A_byteena_b;
wire  main_inst_main_0_A_enable_b;
wire [7:0] main_inst_main_0_A_address_b;
reg [31:0] main_inst_main_0_A_out_b;
reg  main_inst_finish_reg;
reg [31:0] main_inst_return_val_reg;
reg  main_0_c_inst_clk;
reg  main_0_c_inst_clken;
reg [3:0] main_0_c_inst_address_a;
reg  main_0_c_inst_wren_a;
reg [31:0] main_0_c_inst_data_a;
wire  main_0_c_inst_byteena_a;
wire [31:0] main_0_c_inst_q_a;
reg [3:0] main_0_c_inst_address_b;
reg  main_0_c_inst_wren_b;
reg [31:0] main_0_c_inst_data_b;
wire  main_0_c_inst_byteena_b;
wire [31:0] main_0_c_inst_q_b;
reg  main_0_A_inst_clk;
reg  main_0_A_inst_clken;
reg [7:0] main_0_A_inst_address_a;
reg  main_0_A_inst_wren_a;
reg [31:0] main_0_A_inst_data_a;
wire  main_0_A_inst_byteena_a;
wire [31:0] main_0_A_inst_q_a;
reg [7:0] main_0_A_inst_address_b;
reg  main_0_A_inst_wren_b;
reg [31:0] main_0_A_inst_data_b;
wire  main_0_A_inst_byteena_b;
wire [31:0] main_0_A_inst_q_b;
reg  gaussian_inst_clk;
reg  gaussian_inst_clk2x;
reg  gaussian_inst_clk1x_follower;
reg  gaussian_inst_reset;
reg  gaussian_inst_memory_controller_waitrequest;
reg  gaussian_inst_start;
wire  gaussian_inst_finish;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] gaussian_inst_arg_c;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] gaussian_inst_arg_A;
wire  gaussian_inst_main_0_A_write_enable_a;
wire [31:0] gaussian_inst_main_0_A_in_a;
wire  gaussian_inst_main_0_A_byteena_a;
wire  gaussian_inst_main_0_A_enable_a;
wire [7:0] gaussian_inst_main_0_A_address_a;
reg [31:0] gaussian_inst_main_0_A_out_a;
wire  gaussian_inst_main_0_A_write_enable_b;
wire [31:0] gaussian_inst_main_0_A_in_b;
wire  gaussian_inst_main_0_A_byteena_b;
wire  gaussian_inst_main_0_A_enable_b;
wire [7:0] gaussian_inst_main_0_A_address_b;
reg [31:0] gaussian_inst_main_0_A_out_b;
wire  gaussian_inst_main_0_c_write_enable_a;
wire [31:0] gaussian_inst_main_0_c_in_a;
wire  gaussian_inst_main_0_c_byteena_a;
wire  gaussian_inst_main_0_c_enable_a;
wire [3:0] gaussian_inst_main_0_c_address_a;
reg [31:0] gaussian_inst_main_0_c_out_a;
wire  gaussian_inst_main_0_c_write_enable_b;
wire [31:0] gaussian_inst_main_0_c_in_b;
wire  gaussian_inst_main_0_c_byteena_b;
wire  gaussian_inst_main_0_c_enable_b;
wire [3:0] gaussian_inst_main_0_c_address_b;
reg [31:0] gaussian_inst_main_0_c_out_b;
reg  gaussian_inst_finish_reg;


main main_inst (
	.clk (main_inst_clk),
	.clk2x (main_inst_clk2x),
	.clk1x_follower (main_inst_clk1x_follower),
	.reset (main_inst_reset),
	.memory_controller_waitrequest (main_inst_memory_controller_waitrequest),
	.start (main_inst_start),
	.finish (main_inst_finish),
	.return_val (main_inst_return_val),
	.gaussian_start (main_inst_gaussian_start),
	.gaussian_finish (main_inst_gaussian_finish),
	.gaussian_arg_c (main_inst_gaussian_arg_c),
	.gaussian_arg_A (main_inst_gaussian_arg_A),
	.main_0_c_write_enable_a (main_inst_main_0_c_write_enable_a),
	.main_0_c_in_a (main_inst_main_0_c_in_a),
	.main_0_c_byteena_a (main_inst_main_0_c_byteena_a),
	.main_0_c_enable_a (main_inst_main_0_c_enable_a),
	.main_0_c_address_a (main_inst_main_0_c_address_a),
	.main_0_c_out_a (main_inst_main_0_c_out_a),
	.main_0_c_write_enable_b (main_inst_main_0_c_write_enable_b),
	.main_0_c_in_b (main_inst_main_0_c_in_b),
	.main_0_c_byteena_b (main_inst_main_0_c_byteena_b),
	.main_0_c_enable_b (main_inst_main_0_c_enable_b),
	.main_0_c_address_b (main_inst_main_0_c_address_b),
	.main_0_c_out_b (main_inst_main_0_c_out_b),
	.main_0_A_write_enable_a (main_inst_main_0_A_write_enable_a),
	.main_0_A_in_a (main_inst_main_0_A_in_a),
	.main_0_A_byteena_a (main_inst_main_0_A_byteena_a),
	.main_0_A_enable_a (main_inst_main_0_A_enable_a),
	.main_0_A_address_a (main_inst_main_0_A_address_a),
	.main_0_A_out_a (main_inst_main_0_A_out_a),
	.main_0_A_write_enable_b (main_inst_main_0_A_write_enable_b),
	.main_0_A_in_b (main_inst_main_0_A_in_b),
	.main_0_A_byteena_b (main_inst_main_0_A_byteena_b),
	.main_0_A_enable_b (main_inst_main_0_A_enable_b),
	.main_0_A_address_b (main_inst_main_0_A_address_b),
	.main_0_A_out_b (main_inst_main_0_A_out_b)
);



ram_dual_port main_0_c_inst (
	.clk (main_0_c_inst_clk),
	.clken (main_0_c_inst_clken),
	.address_a (main_0_c_inst_address_a),
	.wren_a (main_0_c_inst_wren_a),
	.data_a (main_0_c_inst_data_a),
	.byteena_a (main_0_c_inst_byteena_a),
	.q_a (main_0_c_inst_q_a),
	.address_b (main_0_c_inst_address_b),
	.wren_b (main_0_c_inst_wren_b),
	.data_b (main_0_c_inst_data_b),
	.byteena_b (main_0_c_inst_byteena_b),
	.q_b (main_0_c_inst_q_b)
);

defparam
	main_0_c_inst.width_a = 32,
	main_0_c_inst.width_b = 32,
	main_0_c_inst.widthad_a = 4,
	main_0_c_inst.widthad_b = 4,
	main_0_c_inst.width_be_a = 1,
	main_0_c_inst.width_be_b = 1,
	main_0_c_inst.numwords_a = 16,
	main_0_c_inst.numwords_b = 16,
	main_0_c_inst.latency = 1;


ram_dual_port main_0_A_inst (
	.clk (main_0_A_inst_clk),
	.clken (main_0_A_inst_clken),
	.address_a (main_0_A_inst_address_a),
	.wren_a (main_0_A_inst_wren_a),
	.data_a (main_0_A_inst_data_a),
	.byteena_a (main_0_A_inst_byteena_a),
	.q_a (main_0_A_inst_q_a),
	.address_b (main_0_A_inst_address_b),
	.wren_b (main_0_A_inst_wren_b),
	.data_b (main_0_A_inst_data_b),
	.byteena_b (main_0_A_inst_byteena_b),
	.q_b (main_0_A_inst_q_b)
);

defparam
	main_0_A_inst.width_a = 32,
	main_0_A_inst.width_b = 32,
	main_0_A_inst.widthad_a = 8,
	main_0_A_inst.widthad_b = 8,
	main_0_A_inst.width_be_a = 1,
	main_0_A_inst.width_be_b = 1,
	main_0_A_inst.numwords_a = 256,
	main_0_A_inst.numwords_b = 256,
	main_0_A_inst.latency = 1;


gaussian gaussian_inst (
	.clk (gaussian_inst_clk),
	.clk2x (gaussian_inst_clk2x),
	.clk1x_follower (gaussian_inst_clk1x_follower),
	.reset (gaussian_inst_reset),
	.memory_controller_waitrequest (gaussian_inst_memory_controller_waitrequest),
	.start (gaussian_inst_start),
	.finish (gaussian_inst_finish),
	.arg_c (gaussian_inst_arg_c),
	.arg_A (gaussian_inst_arg_A),
	.main_0_A_write_enable_a (gaussian_inst_main_0_A_write_enable_a),
	.main_0_A_in_a (gaussian_inst_main_0_A_in_a),
	.main_0_A_byteena_a (gaussian_inst_main_0_A_byteena_a),
	.main_0_A_enable_a (gaussian_inst_main_0_A_enable_a),
	.main_0_A_address_a (gaussian_inst_main_0_A_address_a),
	.main_0_A_out_a (gaussian_inst_main_0_A_out_a),
	.main_0_A_write_enable_b (gaussian_inst_main_0_A_write_enable_b),
	.main_0_A_in_b (gaussian_inst_main_0_A_in_b),
	.main_0_A_byteena_b (gaussian_inst_main_0_A_byteena_b),
	.main_0_A_enable_b (gaussian_inst_main_0_A_enable_b),
	.main_0_A_address_b (gaussian_inst_main_0_A_address_b),
	.main_0_A_out_b (gaussian_inst_main_0_A_out_b),
	.main_0_c_write_enable_a (gaussian_inst_main_0_c_write_enable_a),
	.main_0_c_in_a (gaussian_inst_main_0_c_in_a),
	.main_0_c_byteena_a (gaussian_inst_main_0_c_byteena_a),
	.main_0_c_enable_a (gaussian_inst_main_0_c_enable_a),
	.main_0_c_address_a (gaussian_inst_main_0_c_address_a),
	.main_0_c_out_a (gaussian_inst_main_0_c_out_a),
	.main_0_c_write_enable_b (gaussian_inst_main_0_c_write_enable_b),
	.main_0_c_in_b (gaussian_inst_main_0_c_in_b),
	.main_0_c_byteena_b (gaussian_inst_main_0_c_byteena_b),
	.main_0_c_enable_b (gaussian_inst_main_0_c_enable_b),
	.main_0_c_address_b (gaussian_inst_main_0_c_address_b),
	.main_0_c_out_b (gaussian_inst_main_0_c_out_b)
);


// Local Rams

// End Local Rams

always @(*) begin
	main_inst_clk = clk;
end
always @(*) begin
	main_inst_clk2x = clk2x;
end
always @(*) begin
	main_inst_clk1x_follower = clk1x_follower;
end
always @(*) begin
	main_inst_reset = reset;
end
always @(*) begin
	main_inst_memory_controller_waitrequest = memory_controller_waitrequest;
end
always @(*) begin
	main_inst_start = start;
end
always @(*) begin
	main_inst_gaussian_finish = (~(gaussian_inst_start) & gaussian_inst_finish_reg);
end
always @(*) begin
	main_inst_main_0_c_out_a = main_0_c_inst_q_a;
end
always @(*) begin
	main_inst_main_0_c_out_b = main_0_c_inst_q_b;
end
always @(*) begin
	main_inst_main_0_A_out_a = main_0_A_inst_q_a;
end
always @(*) begin
	main_inst_main_0_A_out_b = main_0_A_inst_q_b;
end
always @(posedge clk) begin
	if ((reset | main_inst_start)) begin
		main_inst_finish_reg <= 1'd0;
	end
	if (main_inst_finish) begin
		main_inst_finish_reg <= 1'd1;
	end
end
always @(posedge clk) begin
	if ((reset | main_inst_start)) begin
		main_inst_return_val_reg <= 0;
	end
	if (main_inst_finish) begin
		main_inst_return_val_reg <= main_inst_return_val;
	end
end
always @(*) begin
	main_0_c_inst_clk = clk;
end
always @(*) begin
	main_0_c_inst_clken = ~(memory_controller_waitrequest);
end
always @(*) begin
	main_0_c_inst_address_a = (main_inst_main_0_c_address_a | gaussian_inst_main_0_c_address_a);
end
always @(*) begin
	main_0_c_inst_wren_a = (main_inst_main_0_c_write_enable_a | gaussian_inst_main_0_c_write_enable_a);
end
always @(*) begin
	main_0_c_inst_data_a = (main_inst_main_0_c_in_a | gaussian_inst_main_0_c_in_a);
end
always @(*) begin
	main_0_c_inst_address_b = (main_inst_main_0_c_address_b | gaussian_inst_main_0_c_address_b);
end
always @(*) begin
	main_0_c_inst_wren_b = (main_inst_main_0_c_write_enable_b | gaussian_inst_main_0_c_write_enable_b);
end
always @(*) begin
	main_0_c_inst_data_b = (main_inst_main_0_c_in_b | gaussian_inst_main_0_c_in_b);
end
always @(*) begin
	main_0_A_inst_clk = clk;
end
always @(*) begin
	main_0_A_inst_clken = ~(memory_controller_waitrequest);
end
always @(*) begin
	main_0_A_inst_address_a = (main_inst_main_0_A_address_a | gaussian_inst_main_0_A_address_a);
end
always @(*) begin
	main_0_A_inst_wren_a = (main_inst_main_0_A_write_enable_a | gaussian_inst_main_0_A_write_enable_a);
end
always @(*) begin
	main_0_A_inst_data_a = (main_inst_main_0_A_in_a | gaussian_inst_main_0_A_in_a);
end
always @(*) begin
	main_0_A_inst_address_b = (main_inst_main_0_A_address_b | gaussian_inst_main_0_A_address_b);
end
always @(*) begin
	main_0_A_inst_wren_b = (main_inst_main_0_A_write_enable_b | gaussian_inst_main_0_A_write_enable_b);
end
always @(*) begin
	main_0_A_inst_data_b = (main_inst_main_0_A_in_b | gaussian_inst_main_0_A_in_b);
end
always @(*) begin
	gaussian_inst_clk = clk;
end
always @(*) begin
	gaussian_inst_clk2x = clk2x;
end
always @(*) begin
	gaussian_inst_clk1x_follower = clk1x_follower;
end
always @(*) begin
	gaussian_inst_reset = reset;
end
always @(*) begin
	gaussian_inst_memory_controller_waitrequest = memory_controller_waitrequest;
end
always @(*) begin
	gaussian_inst_start = main_inst_gaussian_start;
end
always @(*) begin
	gaussian_inst_arg_c = main_inst_gaussian_arg_c;
end
always @(*) begin
	gaussian_inst_arg_A = main_inst_gaussian_arg_A;
end
always @(*) begin
	gaussian_inst_main_0_A_out_a = main_0_A_inst_q_a;
end
always @(*) begin
	gaussian_inst_main_0_A_out_b = main_0_A_inst_q_b;
end
always @(*) begin
	gaussian_inst_main_0_c_out_a = main_0_c_inst_q_a;
end
always @(*) begin
	gaussian_inst_main_0_c_out_b = main_0_c_inst_q_b;
end
always @(posedge clk) begin
	if ((reset | gaussian_inst_start)) begin
		gaussian_inst_finish_reg <= 1'd0;
	end
	if (gaussian_inst_finish) begin
		gaussian_inst_finish_reg <= 1'd1;
	end
end
always @(posedge clk) begin
	finish <= main_inst_finish;
end
always @(posedge clk) begin
	return_val <= main_inst_return_val;
end

endmodule
