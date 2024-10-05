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

parameter [1:0] LEGUP_0 = 2'd0;
parameter [1:0] LEGUP_loop_pipeline_wait_loop_1_1 = 2'd1;
parameter [1:0] LEGUP_F_toy_BB__10_2 = 2'd2;

input  clk;
input  clk2x;
input  clk1x_follower;
input  reset;
input  memory_controller_waitrequest;
input  start;
output reg  finish;
input [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] arg_a;
input [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] arg_b;
input [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] arg_c;
output  main_0_a_write_enable_a;
output [31:0] main_0_a_in_a;
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
output  main_0_c_write_enable_a;
output [31:0] main_0_c_in_a;
output  main_0_c_byteena_a;
output reg  main_0_c_enable_a;
output reg [9:0] main_0_c_address_a;
input [31:0] main_0_c_out_a;
output reg  main_0_c_write_enable_b;
output reg [31:0] main_0_c_in_b;
output  main_0_c_byteena_b;
output reg  main_0_c_enable_b;
output reg [9:0] main_0_c_address_b;
input [31:0] main_0_c_out_b;
reg [1:0] cur_state;
reg [1:0] next_state;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] arg_a_reg;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] arg_b_reg;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] arg_c_reg;
reg  fsm_stall;
reg [10:0] toy_1_2;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] toy_1_scevgep2;
reg [10:0] toy_1_3;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] toy_1_scevgep4;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] toy_1_scevgep3;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] toy_1_scevgep;
reg [31:0] toy_1_5;
reg [31:0] toy_1_6;
reg [31:0] toy_1_7;
reg [31:0] toy_1_8;
reg [31:0] toy_1_9;
reg  loop_1_valid_bit_0;
reg  loop_1_state_stall_0;
reg  loop_1_state_enable_0;
reg  loop_1_valid_bit_1;
reg  loop_1_state_stall_1;
reg  loop_1_state_enable_1;
reg  loop_1_valid_bit_2;
reg  loop_1_state_stall_2;
reg  loop_1_state_enable_2;
reg  loop_1_valid_bit_3;
reg  loop_1_state_stall_3;
reg  loop_1_state_enable_3;
reg  loop_1_II_counter;
reg  loop_1_start;
reg  loop_1_activate_pipeline;
reg [31:0] toy_1_2_reg_stage1;
reg [31:0] toy_1_3_reg_stage1;
reg [`MEMORY_CONTROLLER_ADDR_SIZE-1:0] toy_1_scevgep_reg_stage2;
reg  loop_1_pipeline_exit_cond;
reg [31:0] loop_1_inductionVar_stage0;
reg  loop_1_active;
reg  loop_1_begin_pipeline;
reg  loop_1_epilogue;
reg  loop_1_pipeline_finish;
reg  loop_1_only_last_stage_enabled;
reg  loop_1_pipeline_finish_reg;

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
		next_state = LEGUP_loop_pipeline_wait_loop_1_1;
LEGUP_F_toy_BB__10_2:
		next_state = LEGUP_0;
LEGUP_loop_pipeline_wait_loop_1_1:
	if ((fsm_stall == 1'd0) && (loop_1_pipeline_finish == 1'd1))
		next_state = LEGUP_F_toy_BB__10_2;
	else if ((fsm_stall == 1'd0) && (loop_1_pipeline_finish == 1'd1))
		next_state = LEGUP_F_toy_BB__10_2;
default:
	next_state = cur_state;
endcase

end
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
	/*   %2 = add i32 %indvar, 2, !legup.pipeline.start_time !3, !legup.pipeline.avail_time !3, !legup.pipeline.stage !3, !MSB !6, !LSB !3, !extendFrom !6
	start_time: 0 avail_time: 0 stage: 0 II: 1 start_ii_state = 0 % 1 = 0 avail_ii_state = 0 % 1 = 0*/
		toy_1_2 = (loop_1_inductionVar_stage0 + 32'd2);
end
always @(*) begin
	/* toy: %1*/
	/*   %scevgep2 = getelementptr i32* %c, i32 %2, !legup.pipeline.start_time !4, !legup.pipeline.avail_time !4, !legup.pipeline.stage !4, !MSB !2, !LSB !3, !extendFrom !2
	start_time: 1 avail_time: 1 stage: 1 II: 1 start_ii_state = 1 % 1 = 0 avail_ii_state = 1 % 1 = 0*/
		toy_1_scevgep2 = (arg_c_reg + (4 * toy_1_2_reg_stage1));
end
always @(*) begin
	/* toy: %1*/
	/*   %3 = add i32 %indvar, 1, !legup.pipeline.start_time !3, !legup.pipeline.avail_time !3, !legup.pipeline.stage !3, !MSB !6, !LSB !3, !extendFrom !6
	start_time: 0 avail_time: 0 stage: 0 II: 1 start_ii_state = 0 % 1 = 0 avail_ii_state = 0 % 1 = 0*/
		toy_1_3 = (loop_1_inductionVar_stage0 + 32'd1);
end
always @(*) begin
	/* toy: %1*/
	/*   %scevgep4 = getelementptr i32* %a, i32 %3, !legup.pipeline.start_time !4, !legup.pipeline.avail_time !4, !legup.pipeline.stage !4, !MSB !2, !LSB !3, !extendFrom !2
	start_time: 1 avail_time: 1 stage: 1 II: 1 start_ii_state = 1 % 1 = 0 avail_ii_state = 1 % 1 = 0*/
		toy_1_scevgep4 = (arg_a_reg + (4 * toy_1_3_reg_stage1));
end
always @(*) begin
	/* toy: %1*/
	/*   %scevgep3 = getelementptr i32* %b, i32 %3, !legup.pipeline.start_time !4, !legup.pipeline.avail_time !4, !legup.pipeline.stage !4, !MSB !2, !LSB !3, !extendFrom !2
	start_time: 1 avail_time: 1 stage: 1 II: 1 start_ii_state = 1 % 1 = 0 avail_ii_state = 1 % 1 = 0*/
		toy_1_scevgep3 = (arg_b_reg + (4 * toy_1_3_reg_stage1));
end
always @(*) begin
	/* toy: %1*/
	/*   %scevgep = getelementptr i32* %c, i32 %3, !legup.pipeline.start_time !4, !legup.pipeline.avail_time !4, !legup.pipeline.stage !4, !MSB !2, !LSB !3, !extendFrom !2
	start_time: 1 avail_time: 1 stage: 1 II: 1 start_ii_state = 1 % 1 = 0 avail_ii_state = 1 % 1 = 0*/
		toy_1_scevgep = (arg_c_reg + (4 * toy_1_3_reg_stage1));
end
always @(*) begin
	/* toy: %1*/
	/*   %5 = load i32* %scevgep4, align 4, !legup.pipeline.start_time !4, !legup.pipeline.avail_time !7, !legup.pipeline.stage !4, !MSB !8, !LSB !3, !extendFrom !8
	start_time: 1 avail_time: 2 stage: 1 II: 1 start_ii_state = 1 % 1 = 0 avail_ii_state = 2 % 1 = 0*/
		toy_1_5 = main_0_a_out_a;
end
always @(*) begin
	/* toy: %1*/
	/*   %6 = load i32* %scevgep3, align 4, !legup.pipeline.start_time !4, !legup.pipeline.avail_time !7, !legup.pipeline.stage !4, !MSB !8, !LSB !3, !extendFrom !8
	start_time: 1 avail_time: 2 stage: 1 II: 1 start_ii_state = 1 % 1 = 0 avail_ii_state = 2 % 1 = 0*/
		toy_1_6 = main_0_b_out_a;
end
always @(*) begin
	/* toy: %1*/
	/*   %7 = add nsw i32 %5, %6, !legup.pipeline.start_time !7, !legup.pipeline.avail_time !7, !legup.pipeline.stage !7, !MSB !8, !LSB !3, !extendFrom !8
	start_time: 2 avail_time: 2 stage: 2 II: 1 start_ii_state = 2 % 1 = 0 avail_ii_state = 2 % 1 = 0*/
		toy_1_7 = (toy_1_5 + toy_1_6);
end
always @(*) begin
	/* toy: %1*/
	/*   %8 = load i32* %scevgep2, align 4, !legup.pipeline.start_time !4, !legup.pipeline.avail_time !7, !legup.pipeline.stage !4, !MSB !8, !LSB !3, !extendFrom !8
	start_time: 1 avail_time: 2 stage: 1 II: 1 start_ii_state = 1 % 1 = 0 avail_ii_state = 2 % 1 = 0*/
		toy_1_8 = main_0_c_out_a;
end
always @(*) begin
	/* toy: %1*/
	/*   %9 = add nsw i32 %7, %8, !legup.pipeline.start_time !7, !legup.pipeline.avail_time !7, !legup.pipeline.stage !7, !MSB !8, !LSB !3, !extendFrom !8
	start_time: 2 avail_time: 2 stage: 2 II: 1 start_ii_state = 2 % 1 = 0 avail_ii_state = 2 % 1 = 0*/
		toy_1_9 = (toy_1_7 + toy_1_8);
end
always @(posedge clk) begin
	if (~(loop_1_state_stall_0)) begin
		loop_1_valid_bit_0 <= ((loop_1_II_counter == 1'd0) & loop_1_start);
	end
	if (reset) begin
		loop_1_valid_bit_0 <= 1'd0;
	end
end
always @(*) begin
	loop_1_state_stall_0 = 1'd0;
	if (loop_1_state_stall_1) begin
		loop_1_state_stall_0 = 1'd1;
	end
end
always @(*) begin
	loop_1_state_enable_0 = (loop_1_valid_bit_0 & ~(loop_1_state_stall_0));
end
always @(posedge clk) begin
	if (~(loop_1_state_stall_1)) begin
		loop_1_valid_bit_1 <= loop_1_state_enable_0;
	end
	if (reset) begin
		loop_1_valid_bit_1 <= 1'd0;
	end
end
always @(*) begin
	loop_1_state_stall_1 = 1'd0;
	if (loop_1_state_stall_2) begin
		loop_1_state_stall_1 = 1'd1;
	end
end
always @(*) begin
	loop_1_state_enable_1 = (loop_1_valid_bit_1 & ~(loop_1_state_stall_1));
end
always @(posedge clk) begin
	if (~(loop_1_state_stall_2)) begin
		loop_1_valid_bit_2 <= loop_1_state_enable_1;
	end
	if (reset) begin
		loop_1_valid_bit_2 <= 1'd0;
	end
end
always @(*) begin
	loop_1_state_stall_2 = 1'd0;
	if (loop_1_state_stall_3) begin
		loop_1_state_stall_2 = 1'd1;
	end
end
always @(*) begin
	loop_1_state_enable_2 = (loop_1_valid_bit_2 & ~(loop_1_state_stall_2));
end
always @(posedge clk) begin
	if (~(loop_1_state_stall_3)) begin
		loop_1_valid_bit_3 <= loop_1_state_enable_2;
	end
	if (reset) begin
		loop_1_valid_bit_3 <= 1'd0;
	end
end
always @(*) begin
	loop_1_state_stall_3 = 1'd0;
	if (reset) begin
		loop_1_state_stall_3 = 1'd0;
	end
end
always @(*) begin
	loop_1_state_enable_3 = (loop_1_valid_bit_3 & ~(loop_1_state_stall_3));
end
always @(posedge clk) begin
	loop_1_II_counter <= (loop_1_II_counter + 1'd1);
	if (reset) begin
		loop_1_II_counter <= 1'd0;
	end
	if ((loop_1_II_counter == 1'd0)) begin
		loop_1_II_counter <= 1'd0;
	end
end
always @(*) begin
	loop_1_start = (loop_1_activate_pipeline | ((loop_1_active & ~(loop_1_epilogue)) & ~((loop_1_state_enable_0 & loop_1_pipeline_exit_cond))));
	if (reset) begin
		loop_1_start = 1'd0;
	end
end
always @(*) begin
	loop_1_activate_pipeline = (((fsm_stall == 1'd0) & loop_1_begin_pipeline) & ~(loop_1_active));
end
always @(posedge clk) begin
	if (loop_1_state_enable_0) begin
		toy_1_2_reg_stage1 <= {21'd0,toy_1_2};
	end
end
always @(posedge clk) begin
	if (loop_1_state_enable_0) begin
		toy_1_3_reg_stage1 <= {21'd0,toy_1_3};
	end
end
always @(posedge clk) begin
	if (loop_1_state_enable_1) begin
		toy_1_scevgep_reg_stage2 <= toy_1_scevgep;
	end
end
always @(*) begin
	loop_1_pipeline_exit_cond = (loop_1_inductionVar_stage0 == 998);
end
always @(posedge clk) begin
	if (reset) begin
		loop_1_inductionVar_stage0 <= 0;
	end
	if (loop_1_activate_pipeline) begin
		loop_1_inductionVar_stage0 <= 0;
	end
	if (((loop_1_II_counter == 1'd0) & loop_1_state_enable_0)) begin
		loop_1_inductionVar_stage0 <= (loop_1_inductionVar_stage0 + 1'd1);
	end
end
always @(posedge clk) begin
	if (reset) begin
		loop_1_active <= 1'd0;
	end
	if (loop_1_activate_pipeline) begin
		loop_1_active <= 1'd1;
	end
	if (((~(loop_1_state_stall_0) & loop_1_epilogue) & loop_1_only_last_stage_enabled)) begin
		loop_1_active <= 1'd0;
	end
end
always @(*) begin
	loop_1_begin_pipeline = 1'd0;
	if (reset) begin
		loop_1_begin_pipeline = 1'd0;
	end
	if ((((cur_state == LEGUP_0) & (fsm_stall == 1'd0)) & (start == 1'd1))) begin
		loop_1_begin_pipeline = 1'd1;
	end
end
always @(posedge clk) begin
	if (reset) begin
		loop_1_epilogue <= 1'd0;
	end
	if ((loop_1_state_enable_0 & loop_1_pipeline_exit_cond)) begin
		loop_1_epilogue <= 1'd1;
	end
	if (((~(loop_1_state_stall_0) & loop_1_epilogue) & loop_1_only_last_stage_enabled)) begin
		loop_1_epilogue <= 1'd0;
	end
end
always @(*) begin
	loop_1_pipeline_finish = (((~(loop_1_state_stall_0) & loop_1_epilogue) & loop_1_only_last_stage_enabled) | loop_1_pipeline_finish_reg);
end
always @(*) begin
	loop_1_only_last_stage_enabled = (((~(loop_1_state_enable_0) & ~(loop_1_state_enable_1)) & ~(loop_1_state_enable_2)) & loop_1_state_enable_3);
end
always @(posedge clk) begin
	loop_1_pipeline_finish_reg <= loop_1_pipeline_finish;
	if (reset) begin
		loop_1_pipeline_finish_reg <= 1'd0;
	end
	if (loop_1_activate_pipeline) begin
		loop_1_pipeline_finish_reg <= 1'd0;
	end
end
always @(posedge clk) begin
	if ((cur_state == LEGUP_0)) begin
		finish <= 1'd0;
	end
	/* toy: %10*/
	/*   ret void, !MSB !2, !LSB !3, !extendFrom !2*/
	if ((cur_state == LEGUP_F_toy_BB__10_2)) begin
		finish <= (fsm_stall == 1'd0);
	end
end
assign main_0_a_write_enable_a = 1'd0;
assign main_0_a_in_a = 0;
assign main_0_a_byteena_a = 1'd1;
always @(*) begin
	main_0_a_enable_a = 1'd0;
	/* toy: %1*/
	/*   %5 = load i32* %scevgep4, align 4, !legup.pipeline.start_time !4, !legup.pipeline.avail_time !7, !legup.pipeline.stage !4, !MSB !8, !LSB !3, !extendFrom !8
	start_time: 1 avail_time: 2 stage: 1 II: 1 start_ii_state = 1 % 1 = 0 avail_ii_state = 2 % 1 = 0*/
	if (loop_1_state_enable_1) begin
		main_0_a_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_a_address_a = 10'd0;
	if (loop_1_valid_bit_1) begin
		main_0_a_address_a = (toy_1_scevgep4 >>> 3'd2);
	end
end
assign main_0_a_write_enable_b = 1'd0;
assign main_0_a_in_b = 0;
assign main_0_a_byteena_b = 1'd1;
assign main_0_a_enable_b = 1'd0;
assign main_0_a_address_b = 10'd0;
assign main_0_b_write_enable_a = 1'd0;
assign main_0_b_in_a = 0;
assign main_0_b_byteena_a = 1'd1;
always @(*) begin
	main_0_b_enable_a = 1'd0;
	/* toy: %1*/
	/*   %6 = load i32* %scevgep3, align 4, !legup.pipeline.start_time !4, !legup.pipeline.avail_time !7, !legup.pipeline.stage !4, !MSB !8, !LSB !3, !extendFrom !8
	start_time: 1 avail_time: 2 stage: 1 II: 1 start_ii_state = 1 % 1 = 0 avail_ii_state = 2 % 1 = 0*/
	if (loop_1_state_enable_1) begin
		main_0_b_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_b_address_a = 10'd0;
	if (loop_1_valid_bit_1) begin
		main_0_b_address_a = (toy_1_scevgep3 >>> 3'd2);
	end
end
assign main_0_b_write_enable_b = 1'd0;
assign main_0_b_in_b = 0;
assign main_0_b_byteena_b = 1'd1;
assign main_0_b_enable_b = 1'd0;
assign main_0_b_address_b = 10'd0;
assign main_0_c_write_enable_a = 1'd0;
assign main_0_c_in_a = 0;
assign main_0_c_byteena_a = 1'd1;
always @(*) begin
	main_0_c_enable_a = 1'd0;
	/* toy: %1*/
	/*   %8 = load i32* %scevgep2, align 4, !legup.pipeline.start_time !4, !legup.pipeline.avail_time !7, !legup.pipeline.stage !4, !MSB !8, !LSB !3, !extendFrom !8
	start_time: 1 avail_time: 2 stage: 1 II: 1 start_ii_state = 1 % 1 = 0 avail_ii_state = 2 % 1 = 0*/
	if (loop_1_state_enable_1) begin
		main_0_c_enable_a = 1'd1;
	end
end
always @(*) begin
	main_0_c_address_a = 10'd0;
	if (loop_1_valid_bit_1) begin
		main_0_c_address_a = (toy_1_scevgep2 >>> 3'd2);
	end
end
always @(*) begin
	main_0_c_write_enable_b = 1'd0;
	if (loop_1_valid_bit_2) begin
		main_0_c_write_enable_b = 1'd1;
	end
end
always @(*) begin
	main_0_c_in_b = 0;
	if (loop_1_valid_bit_2) begin
		main_0_c_in_b = toy_1_9;
	end
end
assign main_0_c_byteena_b = 1'd1;
always @(*) begin
	main_0_c_enable_b = 1'd0;
	/* toy: %1*/
	/*   store i32 %9, i32* %scevgep, align 4, !legup.pipeline.start_time !7, !legup.pipeline.avail_time !9, !legup.pipeline.stage !7, !MSB !2, !LSB !3, !extendFrom !2
	start_time: 2 avail_time: 3 stage: 2 II: 1 start_ii_state = 2 % 1 = 0 avail_ii_state = 3 % 1 = 0*/
	if (loop_1_state_enable_2) begin
		main_0_c_enable_b = 1'd1;
	end
end
always @(*) begin
	main_0_c_address_b = 10'd0;
	if (loop_1_valid_bit_2) begin
		main_0_c_address_b = (toy_1_scevgep_reg_stage2 >>> 3'd2);
	end
end

endmodule