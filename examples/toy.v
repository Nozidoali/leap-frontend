module toy_fsm
(
    clk,
    reset,
    /* handshake with the host machine */
    start,
    finish,

    /* stall signal from the resource */
    fsm_stall,

    /* fsm input */
    BB_1_EXIT,

    /* fsm output */
    is_STATE_0,
    is_STATE_1,
    is_STATE_2,
    is_STATE_3,
    is_STATE_4
);

parameter [5:0] STATE_0 = 5'd00001;
parameter [5:0] STATE_1 = 5'd00010;
parameter [5:0] STATE_2 = 5'd00100;
parameter [5:0] STATE_3 = 5'd01000;
parameter [5:0] STATE_4 = 5'd10000;

input  clk;
input  reset;
input  start;
input  fsm_stall;
input  BB_1_EXIT;
output reg  finish;
reg [4:0] cur_state;
reg [4:0] next_state;

output reg is_STATE_0;
output reg is_STATE_1;
output reg is_STATE_2;
output reg is_STATE_3;
output reg is_STATE_4;


always @(posedge clk) begin
if (reset == 1'b1)
	cur_state <= STATE_0;
else if (!fsm_stall)
	cur_state <= next_state;
end

always @(*)
begin
next_state = cur_state;
case(cur_state)  // synthesis parallel_case  
STATE_0:
	if ((fsm_stall == 1'd0) && (start == 1'd1))
		next_state = STATE_1;
STATE_1:
		next_state = STATE_2;
STATE_2:
		next_state = STATE_3;
STATE_3:
	if ((fsm_stall == 1'd0) && (BB_1_EXIT == 1'd1))
		next_state = STATE_4;
	else if ((fsm_stall == 1'd0) && (BB_1_EXIT == 1'd0))
		next_state = STATE_1;
STATE_4:
		next_state = STATE_0;
default:
	next_state = cur_state;
endcase

end

always @(*)
begin
	is_STATE_0 = cur_state[0];
	is_STATE_1 = cur_state[1];
	is_STATE_2 = cur_state[2];
	is_STATE_3 = cur_state[3];
	is_STATE_4 = cur_state[4];
end

always @(posedge clk) begin
	if ((is_STATE_0)) begin
		finish <= 1'd0;
	end
	/* toy: %9*/
	/*   ret void, !MSB !1, !LSB !2, !extendFrom !1*/
	if ((is_STATE_4)) begin
		finish <= (fsm_stall == 1'd0);
	end
end

endmodule