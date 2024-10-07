module main_tb;

    // Signals for module top
    reg clk;
    reg reset;
    reg start;
    reg B_ctrl_in0;
    wire s0_ctrl_out;
    wire s1_ctrl_out;
    wire s2_ctrl_out;
    wire s3_ctrl_out;
    wire s4_ctrl_out;
    wire s5_ctrl_out;
    wire s6_ctrl_out;
    wire finish;

    // Instantiate the DUT (Design Under Test)
    fsm uut (
        .clk(clk),
        .reset(reset),
        .start(start),
        .B_ctrl_in0(B_ctrl_in0),
        .s0_ctrl_out(s0_ctrl_out),
        .s1_ctrl_out(s1_ctrl_out),
        .s2_ctrl_out(s2_ctrl_out),
        .s3_ctrl_out(s3_ctrl_out),
        .s4_ctrl_out(s4_ctrl_out),
        .s5_ctrl_out(s5_ctrl_out),
        .s6_ctrl_out(s6_ctrl_out),
        .finish(finish)
    );

    // Generate clock signal
    always begin
        #5 clk = ~clk; // 10 time units per clock cycle (50 MHz clock)
    end

    // Test stimulus
    initial begin
        // Initialize signals
        clk = 0;
        reset = 0;
        start = 0;
        B_ctrl_in0 = 0;

        // Apply reset
        reset = 1;
        #10; // wait for 10 time units
        reset = 0;

        // Test Case 1: Start the state machine and transition through states
        start = 1;
        #20; // let it transition to s1
        start = 0; // Deassert start

        // Test Case 2: Let it transition through states s1 -> s2 -> s3 -> s4
        #40;

        // Test Case 3: Set B_ctrl_in0 to 0 and allow the state machine to transition to s5 and s6
        B_ctrl_in0 = 0;
        #40;

        // Test Case 5: Set B_ctrl_in0 to 1 and observe state transitions back to s1
        B_ctrl_in0 = 1;
        #20;

        // Test Case 6: Observe state transitions back to s4
        #60;

        // End the simulation
        $finish;
    end

endmodule
