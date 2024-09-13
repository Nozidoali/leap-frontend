//------------------------------------------------------------------------------
// Generated by LeaP compiler
// Author: Hanyu Wang
// Date: 2024-09-13 02:50:00
//------------------------------------------------------------------------------
module toy_fsm
(
	is_STATE_1,
	is_STATE_3,
	is_STATE_4,
	reset,
	BB_1_EXIT,
	clk,
	fsm_stall,
	is_STATE_0,
	is_STATE_2,
	finish,
	start
);

parameter [4:0] STATE_0 = 5'd00001;
parameter [4:0] STATE_1 = 5'd00010;
parameter [4:0] STATE_2 = 5'd00100;
parameter [4:0] STATE_3 = 5'd01000;
parameter [4:0] STATE_4 = 5'd10000;

input  clk;
input  reset;
input  start;
output reg  finish;
input  fsm_stall;
input  BB_1_EXIT;
output reg  is_STATE_0;
output reg  is_STATE_1;
output reg  is_STATE_2;
output reg  is_STATE_3;
output reg  is_STATE_4;
reg [4:0] cur_state;
reg [4:0] next_state;


always @(posedge clk) begin
if (reset == 1'b1) begin
	cur_state <= STATE_0;
end
else if (!(fsm_stall)) begin
	cur_state <= next_state;
end
end
always @(*) begin
	next_state = cur_state;
	next_state = cur_state;
if (((fsm_stall == 1'd0) && (start == 1'd1)) && (cur_state == STATE_0)) begin
	next_state = STATE_1;
end
else if (cur_state == STATE_1) begin
	next_state = STATE_2;
end
else if (cur_state == STATE_2) begin
	next_state = STATE_3;
end
else if (((fsm_stall == 1'd0) && (BB_1_EXIT == 1'd1)) && (cur_state == STATE_3)) begin
	next_state = STATE_4;
end
else if (((fsm_stall == 1'd0) && (BB_1_EXIT == 1'd0)) && (cur_state == STATE_3)) begin
	next_state = STATE_1;
end
else if (cur_state == STATE_4) begin
	next_state = STATE_0;
end
end
always @(*) begin
	is_STATE_0 = cur_state[0];
end
always @(*) begin
	is_STATE_1 = cur_state[1];
end
always @(*) begin
	is_STATE_2 = cur_state[2];
end
always @(*) begin
	is_STATE_3 = cur_state[3];
end
always @(*) begin
	is_STATE_4 = cur_state[4];
end
always @(posedge clk) begin
if (is_STATE_0) begin
	finish <= 1'd0;
end
else if (is_STATE_4) begin
	finish <= fsm_stall == 1'd0;
end
end
endmodule
