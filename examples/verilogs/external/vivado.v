module toy (
        ap_clk,
        ap_rst,
        ap_start,
        ap_done,
        ap_idle,
        ap_ready,
        a_address0,
        a_ce0,
        a_q0,
        b_address0,
        b_ce0,
        b_q0,
        c_address0,
        c_ce0,
        c_we0,
        c_d0,
        c_q0
);

parameter    ap_ST_fsm_state1 = 3'd1;
parameter    ap_ST_fsm_state2 = 3'd2;
parameter    ap_ST_fsm_state3 = 3'd4;

input   ap_clk;
input   ap_rst;
input   ap_start;
output   ap_done;
output   ap_idle;
output   ap_ready;
output  [6:0] a_address0;
output   a_ce0;
input  [31:0] a_q0;
output  [6:0] b_address0;
output   b_ce0;
input  [31:0] b_q0;
output  [6:0] c_address0;
output   c_ce0;
output   c_we0;
output  [31:0] c_d0;
input  [31:0] c_q0;

reg ap_done;
reg ap_idle;
reg ap_ready;
reg a_ce0;
reg b_ce0;
reg[6:0] c_address0;
reg c_ce0;
reg c_we0;

reg   [2:0] ap_CS_fsm;
wire    ap_CS_fsm_state1;
wire   [63:0] zext_ln8_fu_92_p1;
reg   [63:0] zext_ln8_reg_131;
wire    ap_CS_fsm_state2;
wire   [0:0] icmp_ln6_fu_86_p2;
wire   [6:0] i_fu_109_p2;
reg   [6:0] i_reg_151;
reg   [6:0] i_0_reg_75;
wire    ap_CS_fsm_state3;
wire   [63:0] zext_ln8_1_fu_104_p1;
wire   [6:0] add_ln8_fu_98_p2;
wire   [31:0] add_ln8_1_fu_115_p2;
reg   [2:0] ap_NS_fsm;

// power-on initialization
initial begin
#0 ap_CS_fsm = 3'd1;
end

always @ (posedge ap_clk) begin
    if (ap_rst == 1'b1) begin
        ap_CS_fsm <= ap_ST_fsm_state1;
    end else begin
        ap_CS_fsm <= ap_NS_fsm;
    end
end

always @ (posedge ap_clk) begin
    if ((1'b1 == ap_CS_fsm_state3)) begin
        i_0_reg_75 <= i_reg_151;
    end else if (((ap_start == 1'b1) & (1'b1 == ap_CS_fsm_state1))) begin
        i_0_reg_75 <= 7'd1;
    end
end

always @ (posedge ap_clk) begin
    if (((icmp_ln6_fu_86_p2 == 1'd0) & (1'b1 == ap_CS_fsm_state2))) begin
        i_reg_151 <= i_fu_109_p2;
        zext_ln8_reg_131[6 : 0] <= zext_ln8_fu_92_p1[6 : 0];
    end
end

always @ (*) begin
    if ((1'b1 == ap_CS_fsm_state2)) begin
        a_ce0 = 1'b1;
    end else begin
        a_ce0 = 1'b0;
    end
end

always @ (*) begin
    if (((icmp_ln6_fu_86_p2 == 1'd1) & (1'b1 == ap_CS_fsm_state2))) begin
        ap_done = 1'b1;
    end else begin
        ap_done = 1'b0;
    end
end

always @ (*) begin
    if (((ap_start == 1'b0) & (1'b1 == ap_CS_fsm_state1))) begin
        ap_idle = 1'b1;
    end else begin
        ap_idle = 1'b0;
    end
end

always @ (*) begin
    if (((icmp_ln6_fu_86_p2 == 1'd1) & (1'b1 == ap_CS_fsm_state2))) begin
        ap_ready = 1'b1;
    end else begin
        ap_ready = 1'b0;
    end
end

always @ (*) begin
    if ((1'b1 == ap_CS_fsm_state2)) begin
        b_ce0 = 1'b1;
    end else begin
        b_ce0 = 1'b0;
    end
end

always @ (*) begin
    if ((1'b1 == ap_CS_fsm_state3)) begin
        c_address0 = zext_ln8_reg_131;
    end else if ((1'b1 == ap_CS_fsm_state2)) begin
        c_address0 = zext_ln8_1_fu_104_p1;
    end else begin
        c_address0 = 'bx;
    end
end

always @ (*) begin
    if (((1'b1 == ap_CS_fsm_state3) | (1'b1 == ap_CS_fsm_state2))) begin
        c_ce0 = 1'b1;
    end else begin
        c_ce0 = 1'b0;
    end
end

always @ (*) begin
    if ((1'b1 == ap_CS_fsm_state3)) begin
        c_we0 = 1'b1;
    end else begin
        c_we0 = 1'b0;
    end
end

always @ (*) begin
    case (ap_CS_fsm)
        ap_ST_fsm_state1 : begin
            if (((ap_start == 1'b1) & (1'b1 == ap_CS_fsm_state1))) begin
                ap_NS_fsm = ap_ST_fsm_state2;
            end else begin
                ap_NS_fsm = ap_ST_fsm_state1;
            end
        end
        ap_ST_fsm_state2 : begin
            if (((icmp_ln6_fu_86_p2 == 1'd1) & (1'b1 == ap_CS_fsm_state2))) begin
                ap_NS_fsm = ap_ST_fsm_state1;
            end else begin
                ap_NS_fsm = ap_ST_fsm_state3;
            end
        end
        ap_ST_fsm_state3 : begin
            ap_NS_fsm = ap_ST_fsm_state2;
        end
        default : begin
            ap_NS_fsm = 'bx;
        end
    endcase
end

assign a_address0 = zext_ln8_fu_92_p1;

assign add_ln8_1_fu_115_p2 = (b_q0 + c_q0);

assign add_ln8_fu_98_p2 = (i_0_reg_75) + 7'd127;

assign ap_CS_fsm_state1 = ap_CS_fsm[32'd0];

assign ap_CS_fsm_state2 = ap_CS_fsm[32'd1];

assign ap_CS_fsm_state3 = ap_CS_fsm[32'd2];

assign b_address0 = zext_ln8_fu_92_p1;

assign c_d0 = (add_ln8_1_fu_115_p2 + a_q0);

assign i_fu_109_p2 = (i_0_reg_75 + 7'd1);

assign icmp_ln6_fu_86_p2 = ((i_0_reg_75 == 7'd100) ? 1'b1 : 1'b0);

assign zext_ln8_1_fu_104_p1 = add_ln8_fu_98_p2;

assign zext_ln8_fu_92_p1 = i_0_reg_75;

always @ (posedge ap_clk) begin
    zext_ln8_reg_131[63:7] <= 57'b000000000000000000000000000000000000000000000000000000000;
end

endmodule