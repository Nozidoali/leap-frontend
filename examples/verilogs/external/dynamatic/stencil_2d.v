module stencil_2d(
  // inputs
  input [31:0] orig_loadData,
  input [31:0] filter_loadData,
  input [31:0] sol_loadData,
  input  orig_start_valid,
  input  filter_start_valid,
  input  sol_start_valid,
  input  start_valid,
  input  clk,
  input  rst,
  input  out0_ready,
  input  orig_end_ready,
  input  filter_end_ready,
  input  sol_end_ready,
  input  end_ready,
  // outputs
  output  orig_start_ready,
  output  filter_start_ready,
  output  sol_start_ready,
  output  start_ready,
  output [31:0] out0,
  output  out0_valid,
  output  orig_end_valid,
  output  filter_end_valid,
  output  sol_end_valid,
  output  end_valid,
  output  orig_loadEn,
  output [31:0] orig_loadAddr,
  output  orig_storeEn,
  output [31:0] orig_storeAddr,
  output [31:0] orig_storeData,
  output  filter_loadEn,
  output [31:0] filter_loadAddr,
  output  filter_storeEn,
  output [31:0] filter_storeAddr,
  output [31:0] filter_storeData,
  output  sol_loadEn,
  output [31:0] sol_loadAddr,
  output  sol_storeEn,
  output [31:0] sol_storeAddr,
  output [31:0] sol_storeData
);
  wire fork0_outs_0_valid;
  wire fork0_outs_0_ready;
  wire fork0_outs_1_valid;
  wire fork0_outs_1_ready;
  wire fork0_outs_2_valid;
  wire fork0_outs_2_ready;
  wire mem_controller0_memEnd_valid;
  wire mem_controller0_memEnd_ready;
  wire  mem_controller0_loadEn;
  wire [31:0] mem_controller0_loadAddr;
  wire  mem_controller0_storeEn;
  wire [31:0] mem_controller0_storeAddr;
  wire [31:0] mem_controller0_storeData;
  wire [31:0] mem_controller1_ldData_0;
  wire mem_controller1_ldData_0_valid;
  wire mem_controller1_ldData_0_ready;
  wire mem_controller1_memEnd_valid;
  wire mem_controller1_memEnd_ready;
  wire  mem_controller1_loadEn;
  wire [31:0] mem_controller1_loadAddr;
  wire  mem_controller1_storeEn;
  wire [31:0] mem_controller1_storeAddr;
  wire [31:0] mem_controller1_storeData;
  wire [31:0] mem_controller2_ldData_0;
  wire mem_controller2_ldData_0_valid;
  wire mem_controller2_ldData_0_ready;
  wire mem_controller2_memEnd_valid;
  wire mem_controller2_memEnd_ready;
  wire  mem_controller2_loadEn;
  wire [31:0] mem_controller2_loadAddr;
  wire  mem_controller2_storeEn;
  wire [31:0] mem_controller2_storeAddr;
  wire [31:0] mem_controller2_storeData;
  wire [0:0] constant1_outs;
  wire constant1_outs_valid;
  wire constant1_outs_ready;
  wire [5:0] extsi12_outs;
  wire extsi12_outs_valid;
  wire extsi12_outs_ready;
  wire [5:0] buffer18_outs;
  wire buffer18_outs_valid;
  wire buffer18_outs_ready;
  wire [5:0] buffer19_outs;
  wire buffer19_outs_valid;
  wire buffer19_outs_ready;
  wire [5:0] mux8_outs;
  wire mux8_outs_valid;
  wire mux8_outs_ready;
  wire buffer20_outs_valid;
  wire buffer20_outs_ready;
  wire buffer21_outs_valid;
  wire buffer21_outs_ready;
  wire control_merge0_outs_valid;
  wire control_merge0_outs_ready;
  wire [0:0] control_merge0_index;
  wire control_merge0_index_valid;
  wire control_merge0_index_ready;
  wire fork1_outs_0_valid;
  wire fork1_outs_0_ready;
  wire fork1_outs_1_valid;
  wire fork1_outs_1_ready;
  wire [0:0] constant3_outs;
  wire constant3_outs_valid;
  wire constant3_outs_ready;
  wire [0:0] fork2_outs_0;
  wire fork2_outs_0_valid;
  wire fork2_outs_0_ready;
  wire [0:0] fork2_outs_1;
  wire fork2_outs_1_valid;
  wire fork2_outs_1_ready;
  wire [2:0] extsi13_outs;
  wire extsi13_outs_valid;
  wire extsi13_outs_ready;
  wire [31:0] extsi14_outs;
  wire extsi14_outs_valid;
  wire extsi14_outs_ready;
  wire [2:0] buffer10_outs;
  wire buffer10_outs_valid;
  wire buffer10_outs_ready;
  wire [2:0] buffer11_outs;
  wire buffer11_outs_valid;
  wire buffer11_outs_ready;
  wire [2:0] mux9_outs;
  wire mux9_outs_valid;
  wire mux9_outs_ready;
  wire [31:0] buffer12_outs;
  wire buffer12_outs_valid;
  wire buffer12_outs_ready;
  wire [31:0] buffer13_outs;
  wire buffer13_outs_valid;
  wire buffer13_outs_ready;
  wire [31:0] mux2_outs;
  wire mux2_outs_valid;
  wire mux2_outs_ready;
  wire [5:0] buffer14_outs;
  wire buffer14_outs_valid;
  wire buffer14_outs_ready;
  wire [5:0] buffer15_outs;
  wire buffer15_outs_valid;
  wire buffer15_outs_ready;
  wire [5:0] mux10_outs;
  wire mux10_outs_valid;
  wire mux10_outs_ready;
  wire buffer16_outs_valid;
  wire buffer16_outs_ready;
  wire buffer17_outs_valid;
  wire buffer17_outs_ready;
  wire control_merge1_outs_valid;
  wire control_merge1_outs_ready;
  wire [0:0] control_merge1_index;
  wire control_merge1_index_valid;
  wire control_merge1_index_ready;
  wire [0:0] fork3_outs_0;
  wire fork3_outs_0_valid;
  wire fork3_outs_0_ready;
  wire [0:0] fork3_outs_1;
  wire fork3_outs_1_valid;
  wire fork3_outs_1_ready;
  wire [0:0] fork3_outs_2;
  wire fork3_outs_2_valid;
  wire fork3_outs_2_ready;
  wire fork4_outs_0_valid;
  wire fork4_outs_0_ready;
  wire fork4_outs_1_valid;
  wire fork4_outs_1_ready;
  wire [0:0] constant4_outs;
  wire constant4_outs_valid;
  wire constant4_outs_ready;
  wire [2:0] extsi15_outs;
  wire extsi15_outs_valid;
  wire extsi15_outs_ready;
  wire [2:0] buffer0_outs;
  wire buffer0_outs_valid;
  wire buffer0_outs_ready;
  wire [2:0] buffer1_outs;
  wire buffer1_outs_valid;
  wire buffer1_outs_ready;
  wire [2:0] mux11_outs;
  wire mux11_outs_valid;
  wire mux11_outs_ready;
  wire [2:0] fork5_outs_0;
  wire fork5_outs_0_valid;
  wire fork5_outs_0_ready;
  wire [2:0] fork5_outs_1;
  wire fork5_outs_1_valid;
  wire fork5_outs_1_ready;
  wire [2:0] fork5_outs_2;
  wire fork5_outs_2_valid;
  wire fork5_outs_2_ready;
  wire [6:0] extsi16_outs;
  wire extsi16_outs_valid;
  wire extsi16_outs_ready;
  wire [5:0] extsi17_outs;
  wire extsi17_outs_valid;
  wire extsi17_outs_ready;
  wire [3:0] extsi18_outs;
  wire extsi18_outs_valid;
  wire extsi18_outs_ready;
  wire [31:0] buffer2_outs;
  wire buffer2_outs_valid;
  wire buffer2_outs_ready;
  wire [31:0] buffer3_outs;
  wire buffer3_outs_valid;
  wire buffer3_outs_ready;
  wire [31:0] mux5_outs;
  wire mux5_outs_valid;
  wire mux5_outs_ready;
  wire [5:0] buffer4_outs;
  wire buffer4_outs_valid;
  wire buffer4_outs_ready;
  wire [5:0] buffer5_outs;
  wire buffer5_outs_valid;
  wire buffer5_outs_ready;
  wire [5:0] mux12_outs;
  wire mux12_outs_valid;
  wire mux12_outs_ready;
  wire [5:0] fork6_outs_0;
  wire fork6_outs_0_valid;
  wire fork6_outs_0_ready;
  wire [5:0] fork6_outs_1;
  wire fork6_outs_1_valid;
  wire fork6_outs_1_ready;
  wire [6:0] extsi19_outs;
  wire extsi19_outs_valid;
  wire extsi19_outs_ready;
  wire [2:0] buffer6_outs;
  wire buffer6_outs_valid;
  wire buffer6_outs_ready;
  wire [2:0] buffer7_outs;
  wire buffer7_outs_valid;
  wire buffer7_outs_ready;
  wire [2:0] mux13_outs;
  wire mux13_outs_valid;
  wire mux13_outs_ready;
  wire [2:0] fork7_outs_0;
  wire fork7_outs_0_valid;
  wire fork7_outs_0_ready;
  wire [2:0] fork7_outs_1;
  wire fork7_outs_1_valid;
  wire fork7_outs_1_ready;
  wire [2:0] fork7_outs_2;
  wire fork7_outs_2_valid;
  wire fork7_outs_2_ready;
  wire [2:0] fork7_outs_3;
  wire fork7_outs_3_valid;
  wire fork7_outs_3_ready;
  wire [8:0] extsi20_outs;
  wire extsi20_outs_valid;
  wire extsi20_outs_ready;
  wire [4:0] extsi21_outs;
  wire extsi21_outs_valid;
  wire extsi21_outs_ready;
  wire [3:0] extsi22_outs;
  wire extsi22_outs_valid;
  wire extsi22_outs_ready;
  wire buffer8_outs_valid;
  wire buffer8_outs_ready;
  wire buffer9_outs_valid;
  wire buffer9_outs_ready;
  wire control_merge2_outs_valid;
  wire control_merge2_outs_ready;
  wire [0:0] control_merge2_index;
  wire control_merge2_index_valid;
  wire control_merge2_index_ready;
  wire [0:0] fork8_outs_0;
  wire fork8_outs_0_valid;
  wire fork8_outs_0_ready;
  wire [0:0] fork8_outs_1;
  wire fork8_outs_1_valid;
  wire fork8_outs_1_ready;
  wire [0:0] fork8_outs_2;
  wire fork8_outs_2_valid;
  wire fork8_outs_2_ready;
  wire [0:0] fork8_outs_3;
  wire fork8_outs_3_valid;
  wire fork8_outs_3_ready;
  wire source0_outs_valid;
  wire source0_outs_ready;
  wire [5:0] constant5_outs;
  wire constant5_outs_valid;
  wire constant5_outs_ready;
  wire [8:0] extsi23_outs;
  wire extsi23_outs_valid;
  wire extsi23_outs_ready;
  wire source1_outs_valid;
  wire source1_outs_ready;
  wire [2:0] constant16_outs;
  wire constant16_outs_valid;
  wire constant16_outs_ready;
  wire [3:0] extsi24_outs;
  wire extsi24_outs_valid;
  wire extsi24_outs_ready;
  wire source2_outs_valid;
  wire source2_outs_ready;
  wire [1:0] constant17_outs;
  wire constant17_outs_valid;
  wire constant17_outs_ready;
  wire [1:0] fork9_outs_0;
  wire fork9_outs_0_valid;
  wire fork9_outs_0_ready;
  wire [1:0] fork9_outs_1;
  wire fork9_outs_1_valid;
  wire fork9_outs_1_ready;
  wire [3:0] extui0_outs;
  wire extui0_outs_valid;
  wire extui0_outs_ready;
  wire [3:0] extsi25_outs;
  wire extsi25_outs_valid;
  wire extsi25_outs_ready;
  wire [3:0] shli1_result;
  wire shli1_result_valid;
  wire shli1_result_ready;
  wire [4:0] extsi26_outs;
  wire extsi26_outs_valid;
  wire extsi26_outs_ready;
  wire [4:0] addi8_result;
  wire addi8_result_valid;
  wire addi8_result_ready;
  wire [5:0] extsi27_outs;
  wire extsi27_outs_valid;
  wire extsi27_outs_ready;
  wire [5:0] addi9_result;
  wire addi9_result_valid;
  wire addi9_result_ready;
  wire [31:0] extsi28_outs;
  wire extsi28_outs_valid;
  wire extsi28_outs_ready;
  wire [31:0] mc_load0_addrOut;
  wire mc_load0_addrOut_valid;
  wire mc_load0_addrOut_ready;
  wire [31:0] mc_load0_dataOut;
  wire mc_load0_dataOut_valid;
  wire mc_load0_dataOut_ready;
  wire [6:0] addi10_result;
  wire addi10_result_valid;
  wire addi10_result_ready;
  wire [9:0] extsi29_outs;
  wire extsi29_outs_valid;
  wire extsi29_outs_ready;
  wire [8:0] muli1_result;
  wire muli1_result_valid;
  wire muli1_result_ready;
  wire [9:0] extsi30_outs;
  wire extsi30_outs_valid;
  wire extsi30_outs_ready;
  wire [9:0] addi11_result;
  wire addi11_result_valid;
  wire addi11_result_ready;
  wire [31:0] extsi31_outs;
  wire extsi31_outs_valid;
  wire extsi31_outs_ready;
  wire [31:0] mc_load1_addrOut;
  wire mc_load1_addrOut_valid;
  wire mc_load1_addrOut_ready;
  wire [31:0] mc_load1_dataOut;
  wire mc_load1_dataOut_valid;
  wire mc_load1_dataOut_ready;
  wire [31:0] muli0_result;
  wire muli0_result_valid;
  wire muli0_result_ready;
  wire [31:0] addi0_result;
  wire addi0_result_valid;
  wire addi0_result_ready;
  wire [3:0] addi12_result;
  wire addi12_result_valid;
  wire addi12_result_ready;
  wire [3:0] fork10_outs_0;
  wire fork10_outs_0_valid;
  wire fork10_outs_0_ready;
  wire [3:0] fork10_outs_1;
  wire fork10_outs_1_valid;
  wire fork10_outs_1_ready;
  wire [2:0] trunci0_outs;
  wire trunci0_outs_valid;
  wire trunci0_outs_ready;
  wire [0:0] cmpi3_result;
  wire cmpi3_result_valid;
  wire cmpi3_result_ready;
  wire [0:0] fork11_outs_0;
  wire fork11_outs_0_valid;
  wire fork11_outs_0_ready;
  wire [0:0] fork11_outs_1;
  wire fork11_outs_1_valid;
  wire fork11_outs_1_ready;
  wire [0:0] fork11_outs_2;
  wire fork11_outs_2_valid;
  wire fork11_outs_2_ready;
  wire [0:0] fork11_outs_3;
  wire fork11_outs_3_valid;
  wire fork11_outs_3_ready;
  wire [0:0] fork11_outs_4;
  wire fork11_outs_4_valid;
  wire fork11_outs_4_ready;
  wire [2:0] cond_br0_trueOut;
  wire cond_br0_trueOut_valid;
  wire cond_br0_trueOut_ready;
  wire [2:0] cond_br0_falseOut;
  wire cond_br0_falseOut_valid;
  wire cond_br0_falseOut_ready;
  wire [31:0] cond_br4_trueOut;
  wire cond_br4_trueOut_valid;
  wire cond_br4_trueOut_ready;
  wire [31:0] cond_br4_falseOut;
  wire cond_br4_falseOut_valid;
  wire cond_br4_falseOut_ready;
  wire [5:0] cond_br1_trueOut;
  wire cond_br1_trueOut_valid;
  wire cond_br1_trueOut_ready;
  wire [5:0] cond_br1_falseOut;
  wire cond_br1_falseOut_valid;
  wire cond_br1_falseOut_ready;
  wire [2:0] cond_br2_trueOut;
  wire cond_br2_trueOut_valid;
  wire cond_br2_trueOut_ready;
  wire [2:0] cond_br2_falseOut;
  wire cond_br2_falseOut_valid;
  wire cond_br2_falseOut_ready;
  wire cond_br7_trueOut_valid;
  wire cond_br7_trueOut_ready;
  wire cond_br7_falseOut_valid;
  wire cond_br7_falseOut_ready;
  wire [3:0] extsi32_outs;
  wire extsi32_outs_valid;
  wire extsi32_outs_ready;
  wire source3_outs_valid;
  wire source3_outs_ready;
  wire [2:0] constant18_outs;
  wire constant18_outs_valid;
  wire constant18_outs_ready;
  wire [3:0] extsi33_outs;
  wire extsi33_outs_valid;
  wire extsi33_outs_ready;
  wire source4_outs_valid;
  wire source4_outs_ready;
  wire [1:0] constant19_outs;
  wire constant19_outs_valid;
  wire constant19_outs_ready;
  wire [3:0] extsi34_outs;
  wire extsi34_outs_valid;
  wire extsi34_outs_ready;
  wire [3:0] addi13_result;
  wire addi13_result_valid;
  wire addi13_result_ready;
  wire [3:0] fork12_outs_0;
  wire fork12_outs_0_valid;
  wire fork12_outs_0_ready;
  wire [3:0] fork12_outs_1;
  wire fork12_outs_1_valid;
  wire fork12_outs_1_ready;
  wire [2:0] trunci1_outs;
  wire trunci1_outs_valid;
  wire trunci1_outs_ready;
  wire [0:0] cmpi4_result;
  wire cmpi4_result_valid;
  wire cmpi4_result_ready;
  wire [0:0] fork13_outs_0;
  wire fork13_outs_0_valid;
  wire fork13_outs_0_ready;
  wire [0:0] fork13_outs_1;
  wire fork13_outs_1_valid;
  wire fork13_outs_1_ready;
  wire [0:0] fork13_outs_2;
  wire fork13_outs_2_valid;
  wire fork13_outs_2_ready;
  wire [0:0] fork13_outs_3;
  wire fork13_outs_3_valid;
  wire fork13_outs_3_ready;
  wire [2:0] cond_br15_trueOut;
  wire cond_br15_trueOut_valid;
  wire cond_br15_trueOut_ready;
  wire [2:0] cond_br15_falseOut;
  wire cond_br15_falseOut_valid;
  wire cond_br15_falseOut_ready;
  wire [31:0] cond_br9_trueOut;
  wire cond_br9_trueOut_valid;
  wire cond_br9_trueOut_ready;
  wire [31:0] cond_br9_falseOut;
  wire cond_br9_falseOut_valid;
  wire cond_br9_falseOut_ready;
  wire [5:0] cond_br16_trueOut;
  wire cond_br16_trueOut_valid;
  wire cond_br16_trueOut_ready;
  wire [5:0] cond_br16_falseOut;
  wire cond_br16_falseOut_valid;
  wire cond_br16_falseOut_ready;
  wire cond_br11_trueOut_valid;
  wire cond_br11_trueOut_ready;
  wire cond_br11_falseOut_valid;
  wire cond_br11_falseOut_ready;
  wire [1:0] constant20_outs;
  wire constant20_outs_valid;
  wire constant20_outs_ready;
  wire [31:0] extsi9_outs;
  wire extsi9_outs_valid;
  wire extsi9_outs_ready;
  wire [5:0] fork14_outs_0;
  wire fork14_outs_0_valid;
  wire fork14_outs_0_ready;
  wire [5:0] fork14_outs_1;
  wire fork14_outs_1_valid;
  wire fork14_outs_1_ready;
  wire [6:0] extsi35_outs;
  wire extsi35_outs_valid;
  wire extsi35_outs_ready;
  wire [31:0] extsi36_outs;
  wire extsi36_outs_valid;
  wire extsi36_outs_ready;
  wire [31:0] fork15_outs_0;
  wire fork15_outs_0_valid;
  wire fork15_outs_0_ready;
  wire [31:0] fork15_outs_1;
  wire fork15_outs_1_valid;
  wire fork15_outs_1_ready;
  wire fork16_outs_0_valid;
  wire fork16_outs_0_ready;
  wire fork16_outs_1_valid;
  wire fork16_outs_1_ready;
  wire source5_outs_valid;
  wire source5_outs_ready;
  wire [5:0] constant21_outs;
  wire constant21_outs_valid;
  wire constant21_outs_ready;
  wire [6:0] extsi37_outs;
  wire extsi37_outs_valid;
  wire extsi37_outs_ready;
  wire source6_outs_valid;
  wire source6_outs_ready;
  wire [1:0] constant22_outs;
  wire constant22_outs_valid;
  wire constant22_outs_ready;
  wire [6:0] extsi38_outs;
  wire extsi38_outs_valid;
  wire extsi38_outs_ready;
  wire [31:0] mc_store0_addrOut;
  wire mc_store0_addrOut_valid;
  wire mc_store0_addrOut_ready;
  wire [31:0] mc_store0_dataToMem;
  wire mc_store0_dataToMem_valid;
  wire mc_store0_dataToMem_ready;
  wire [6:0] addi14_result;
  wire addi14_result_valid;
  wire addi14_result_ready;
  wire [6:0] fork17_outs_0;
  wire fork17_outs_0_valid;
  wire fork17_outs_0_ready;
  wire [6:0] fork17_outs_1;
  wire fork17_outs_1_valid;
  wire fork17_outs_1_ready;
  wire [5:0] trunci2_outs;
  wire trunci2_outs_valid;
  wire trunci2_outs_ready;
  wire [0:0] cmpi5_result;
  wire cmpi5_result_valid;
  wire cmpi5_result_ready;
  wire [0:0] fork18_outs_0;
  wire fork18_outs_0_valid;
  wire fork18_outs_0_ready;
  wire [0:0] fork18_outs_1;
  wire fork18_outs_1_valid;
  wire fork18_outs_1_ready;
  wire [0:0] fork18_outs_2;
  wire fork18_outs_2_valid;
  wire fork18_outs_2_ready;
  wire [5:0] cond_br17_trueOut;
  wire cond_br17_trueOut_valid;
  wire cond_br17_trueOut_ready;
  wire [5:0] cond_br17_falseOut;
  wire cond_br17_falseOut_valid;
  wire cond_br17_falseOut_ready;
  wire cond_br13_trueOut_valid;
  wire cond_br13_trueOut_ready;
  wire cond_br13_falseOut_valid;
  wire cond_br13_falseOut_ready;
  wire [31:0] cond_br14_trueOut;
  wire cond_br14_trueOut_valid;
  wire cond_br14_trueOut_ready;
  wire [31:0] cond_br14_falseOut;
  wire cond_br14_falseOut_valid;
  wire cond_br14_falseOut_ready;
  wire fork19_outs_0_valid;
  wire fork19_outs_0_ready;
  wire fork19_outs_1_valid;
  wire fork19_outs_1_ready;
  wire fork19_outs_2_valid;
  wire fork19_outs_2_ready;

  // module outputs
  assign out0 = cond_br14_falseOut;
  assign out0_valid = cond_br14_falseOut_valid;
  assign cond_br14_falseOut_ready = out0_ready;
  assign orig_end_valid = mem_controller2_memEnd_valid;
  assign mem_controller2_memEnd_ready = orig_end_ready;
  assign filter_end_valid = mem_controller1_memEnd_valid;
  assign mem_controller1_memEnd_ready = filter_end_ready;
  assign sol_end_valid = mem_controller0_memEnd_valid;
  assign mem_controller0_memEnd_ready = sol_end_ready;
  assign end_valid = fork0_outs_1_valid;
  assign fork0_outs_1_ready = end_ready;
  assign orig_loadEn = mem_controller2_loadEn;
  assign orig_loadAddr = mem_controller2_loadAddr;
  assign orig_storeEn = mem_controller2_storeEn;
  assign orig_storeAddr = mem_controller2_storeAddr;
  assign orig_storeData = mem_controller2_storeData;
  assign filter_loadEn = mem_controller1_loadEn;
  assign filter_loadAddr = mem_controller1_loadAddr;
  assign filter_storeEn = mem_controller1_storeEn;
  assign filter_storeAddr = mem_controller1_storeAddr;
  assign filter_storeData = mem_controller1_storeData;
  assign sol_loadEn = mem_controller0_loadEn;
  assign sol_loadAddr = mem_controller0_loadAddr;
  assign sol_storeEn = mem_controller0_storeEn;
  assign sol_storeAddr = mem_controller0_storeAddr;
  assign sol_storeData = mem_controller0_storeData;

  fork_dataless #(.SIZE(3)) fork0(
    .clk (clk),
    .ins_ready (start_ready),
    .ins_valid (start_valid),
    .outs_ready ({fork0_outs_2_ready, fork0_outs_1_ready, fork0_outs_0_ready}),
    .outs_valid ({fork0_outs_2_valid, fork0_outs_1_valid, fork0_outs_0_valid}),
    .rst (rst)
  );

  mem_controller_loadless #(.NUM_CONTROLS(1), .NUM_STORES(1), .DATA_TYPE(32), .ADDR_TYPE(32)) mem_controller0(
    .clk (clk),
    .ctrl ({extsi9_outs}),
    .ctrlEnd_ready (fork19_outs_0_ready),
    .ctrlEnd_valid (fork19_outs_0_valid),
    .ctrl_ready ({extsi9_outs_ready}),
    .ctrl_valid ({extsi9_outs_valid}),
    .loadAddr (mem_controller0_loadAddr),
    .loadData (sol_loadData),
    .loadEn (mem_controller0_loadEn),
    .memEnd_ready (mem_controller0_memEnd_ready),
    .memEnd_valid (mem_controller0_memEnd_valid),
    .memStart_ready (sol_start_ready),
    .memStart_valid (sol_start_valid),
    .rst (rst),
    .stAddr ({mc_store0_addrOut}),
    .stAddr_ready ({mc_store0_addrOut_ready}),
    .stAddr_valid ({mc_store0_addrOut_valid}),
    .stData ({mc_store0_dataToMem}),
    .stData_ready ({mc_store0_dataToMem_ready}),
    .stData_valid ({mc_store0_dataToMem_valid}),
    .storeAddr (mem_controller0_storeAddr),
    .storeData (mem_controller0_storeData),
    .storeEn (mem_controller0_storeEn)
  );

  mem_controller_storeless #(.NUM_LOADS(1), .DATA_TYPE(32), .ADDR_TYPE(32)) mem_controller1(
    .clk (clk),
    .ctrlEnd_ready (fork19_outs_1_ready),
    .ctrlEnd_valid (fork19_outs_1_valid),
    .ldAddr ({mc_load0_addrOut}),
    .ldAddr_ready ({mc_load0_addrOut_ready}),
    .ldAddr_valid ({mc_load0_addrOut_valid}),
    .ldData ({mem_controller1_ldData_0}),
    .ldData_ready ({mem_controller1_ldData_0_ready}),
    .ldData_valid ({mem_controller1_ldData_0_valid}),
    .loadAddr (mem_controller1_loadAddr),
    .loadData (filter_loadData),
    .loadEn (mem_controller1_loadEn),
    .memEnd_ready (mem_controller1_memEnd_ready),
    .memEnd_valid (mem_controller1_memEnd_valid),
    .memStart_ready (filter_start_ready),
    .memStart_valid (filter_start_valid),
    .rst (rst),
    .storeAddr (mem_controller1_storeAddr),
    .storeData (mem_controller1_storeData),
    .storeEn (mem_controller1_storeEn)
  );

  mem_controller_storeless #(.NUM_LOADS(1), .DATA_TYPE(32), .ADDR_TYPE(32)) mem_controller2(
    .clk (clk),
    .ctrlEnd_ready (fork19_outs_2_ready),
    .ctrlEnd_valid (fork19_outs_2_valid),
    .ldAddr ({mc_load1_addrOut}),
    .ldAddr_ready ({mc_load1_addrOut_ready}),
    .ldAddr_valid ({mc_load1_addrOut_valid}),
    .ldData ({mem_controller2_ldData_0}),
    .ldData_ready ({mem_controller2_ldData_0_ready}),
    .ldData_valid ({mem_controller2_ldData_0_valid}),
    .loadAddr (mem_controller2_loadAddr),
    .loadData (orig_loadData),
    .loadEn (mem_controller2_loadEn),
    .memEnd_ready (mem_controller2_memEnd_ready),
    .memEnd_valid (mem_controller2_memEnd_valid),
    .memStart_ready (orig_start_ready),
    .memStart_valid (orig_start_valid),
    .rst (rst),
    .storeAddr (mem_controller2_storeAddr),
    .storeData (mem_controller2_storeData),
    .storeEn (mem_controller2_storeEn)
  );

  handshake_constant_0 #(.DATA_WIDTH(1)) constant1(
    .clk (clk),
    .ctrl_ready (fork0_outs_0_ready),
    .ctrl_valid (fork0_outs_0_valid),
    .outs (constant1_outs),
    .outs_ready (constant1_outs_ready),
    .outs_valid (constant1_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(1), .OUTPUT_TYPE(6)) extsi12(
    .clk (clk),
    .ins (constant1_outs),
    .ins_ready (constant1_outs_ready),
    .ins_valid (constant1_outs_valid),
    .outs (extsi12_outs),
    .outs_ready (extsi12_outs_ready),
    .outs_valid (extsi12_outs_valid),
    .rst (rst)
  );

  oehb #(.DATA_TYPE(6)) buffer18(
    .clk (clk),
    .ins (cond_br17_trueOut),
    .ins_ready (cond_br17_trueOut_ready),
    .ins_valid (cond_br17_trueOut_valid),
    .outs (buffer18_outs),
    .outs_ready (buffer18_outs_ready),
    .outs_valid (buffer18_outs_valid),
    .rst (rst)
  );

  tehb #(.DATA_TYPE(6)) buffer19(
    .clk (clk),
    .ins (buffer18_outs),
    .ins_ready (buffer18_outs_ready),
    .ins_valid (buffer18_outs_valid),
    .outs (buffer19_outs),
    .outs_ready (buffer19_outs_ready),
    .outs_valid (buffer19_outs_valid),
    .rst (rst)
  );

  mux #(.SIZE(2), .DATA_TYPE(6), .SELECT_TYPE(1)) mux8(
    .clk (clk),
    .index (control_merge0_index),
    .index_ready (control_merge0_index_ready),
    .index_valid (control_merge0_index_valid),
    .ins ({buffer19_outs, extsi12_outs}),
    .ins_ready ({buffer19_outs_ready, extsi12_outs_ready}),
    .ins_valid ({buffer19_outs_valid, extsi12_outs_valid}),
    .outs (mux8_outs),
    .outs_ready (mux8_outs_ready),
    .outs_valid (mux8_outs_valid),
    .rst (rst)
  );

  oehb_dataless buffer20(
    .clk (clk),
    .ins_ready (cond_br13_trueOut_ready),
    .ins_valid (cond_br13_trueOut_valid),
    .outs_ready (buffer20_outs_ready),
    .outs_valid (buffer20_outs_valid),
    .rst (rst)
  );

  tehb_dataless buffer21(
    .clk (clk),
    .ins_ready (buffer20_outs_ready),
    .ins_valid (buffer20_outs_valid),
    .outs_ready (buffer21_outs_ready),
    .outs_valid (buffer21_outs_valid),
    .rst (rst)
  );

  control_merge_dataless #(.SIZE(2), .INDEX_TYPE(1)) control_merge0(
    .clk (clk),
    .index (control_merge0_index),
    .index_ready (control_merge0_index_ready),
    .index_valid (control_merge0_index_valid),
    .ins_ready ({buffer21_outs_ready, fork0_outs_2_ready}),
    .ins_valid ({buffer21_outs_valid, fork0_outs_2_valid}),
    .outs_ready (control_merge0_outs_ready),
    .outs_valid (control_merge0_outs_valid),
    .rst (rst)
  );

  fork_dataless #(.SIZE(2)) fork1(
    .clk (clk),
    .ins_ready (control_merge0_outs_ready),
    .ins_valid (control_merge0_outs_valid),
    .outs_ready ({fork1_outs_1_ready, fork1_outs_0_ready}),
    .outs_valid ({fork1_outs_1_valid, fork1_outs_0_valid}),
    .rst (rst)
  );

  handshake_constant_0 #(.DATA_WIDTH(1)) constant3(
    .clk (clk),
    .ctrl_ready (fork1_outs_0_ready),
    .ctrl_valid (fork1_outs_0_valid),
    .outs (constant3_outs),
    .outs_ready (constant3_outs_ready),
    .outs_valid (constant3_outs_valid),
    .rst (rst)
  );

  fork_type #(.SIZE(2), .DATA_TYPE(1)) fork2(
    .clk (clk),
    .ins (constant3_outs),
    .ins_ready (constant3_outs_ready),
    .ins_valid (constant3_outs_valid),
    .outs ({fork2_outs_1, fork2_outs_0}),
    .outs_ready ({fork2_outs_1_ready, fork2_outs_0_ready}),
    .outs_valid ({fork2_outs_1_valid, fork2_outs_0_valid}),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(1), .OUTPUT_TYPE(3)) extsi13(
    .clk (clk),
    .ins (fork2_outs_0),
    .ins_ready (fork2_outs_0_ready),
    .ins_valid (fork2_outs_0_valid),
    .outs (extsi13_outs),
    .outs_ready (extsi13_outs_ready),
    .outs_valid (extsi13_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(1), .OUTPUT_TYPE(32)) extsi14(
    .clk (clk),
    .ins (fork2_outs_1),
    .ins_ready (fork2_outs_1_ready),
    .ins_valid (fork2_outs_1_valid),
    .outs (extsi14_outs),
    .outs_ready (extsi14_outs_ready),
    .outs_valid (extsi14_outs_valid),
    .rst (rst)
  );

  oehb #(.DATA_TYPE(3)) buffer10(
    .clk (clk),
    .ins (cond_br15_trueOut),
    .ins_ready (cond_br15_trueOut_ready),
    .ins_valid (cond_br15_trueOut_valid),
    .outs (buffer10_outs),
    .outs_ready (buffer10_outs_ready),
    .outs_valid (buffer10_outs_valid),
    .rst (rst)
  );

  tehb #(.DATA_TYPE(3)) buffer11(
    .clk (clk),
    .ins (buffer10_outs),
    .ins_ready (buffer10_outs_ready),
    .ins_valid (buffer10_outs_valid),
    .outs (buffer11_outs),
    .outs_ready (buffer11_outs_ready),
    .outs_valid (buffer11_outs_valid),
    .rst (rst)
  );

  mux #(.SIZE(2), .DATA_TYPE(3), .SELECT_TYPE(1)) mux9(
    .clk (clk),
    .index (fork3_outs_1),
    .index_ready (fork3_outs_1_ready),
    .index_valid (fork3_outs_1_valid),
    .ins ({buffer11_outs, extsi13_outs}),
    .ins_ready ({buffer11_outs_ready, extsi13_outs_ready}),
    .ins_valid ({buffer11_outs_valid, extsi13_outs_valid}),
    .outs (mux9_outs),
    .outs_ready (mux9_outs_ready),
    .outs_valid (mux9_outs_valid),
    .rst (rst)
  );

  oehb #(.DATA_TYPE(32)) buffer12(
    .clk (clk),
    .ins (cond_br9_trueOut),
    .ins_ready (cond_br9_trueOut_ready),
    .ins_valid (cond_br9_trueOut_valid),
    .outs (buffer12_outs),
    .outs_ready (buffer12_outs_ready),
    .outs_valid (buffer12_outs_valid),
    .rst (rst)
  );

  tehb #(.DATA_TYPE(32)) buffer13(
    .clk (clk),
    .ins (buffer12_outs),
    .ins_ready (buffer12_outs_ready),
    .ins_valid (buffer12_outs_valid),
    .outs (buffer13_outs),
    .outs_ready (buffer13_outs_ready),
    .outs_valid (buffer13_outs_valid),
    .rst (rst)
  );

  mux #(.SIZE(2), .DATA_TYPE(32), .SELECT_TYPE(1)) mux2(
    .clk (clk),
    .index (fork3_outs_2),
    .index_ready (fork3_outs_2_ready),
    .index_valid (fork3_outs_2_valid),
    .ins ({buffer13_outs, extsi14_outs}),
    .ins_ready ({buffer13_outs_ready, extsi14_outs_ready}),
    .ins_valid ({buffer13_outs_valid, extsi14_outs_valid}),
    .outs (mux2_outs),
    .outs_ready (mux2_outs_ready),
    .outs_valid (mux2_outs_valid),
    .rst (rst)
  );

  oehb #(.DATA_TYPE(6)) buffer14(
    .clk (clk),
    .ins (cond_br16_trueOut),
    .ins_ready (cond_br16_trueOut_ready),
    .ins_valid (cond_br16_trueOut_valid),
    .outs (buffer14_outs),
    .outs_ready (buffer14_outs_ready),
    .outs_valid (buffer14_outs_valid),
    .rst (rst)
  );

  tehb #(.DATA_TYPE(6)) buffer15(
    .clk (clk),
    .ins (buffer14_outs),
    .ins_ready (buffer14_outs_ready),
    .ins_valid (buffer14_outs_valid),
    .outs (buffer15_outs),
    .outs_ready (buffer15_outs_ready),
    .outs_valid (buffer15_outs_valid),
    .rst (rst)
  );

  mux #(.SIZE(2), .DATA_TYPE(6), .SELECT_TYPE(1)) mux10(
    .clk (clk),
    .index (fork3_outs_0),
    .index_ready (fork3_outs_0_ready),
    .index_valid (fork3_outs_0_valid),
    .ins ({buffer15_outs, mux8_outs}),
    .ins_ready ({buffer15_outs_ready, mux8_outs_ready}),
    .ins_valid ({buffer15_outs_valid, mux8_outs_valid}),
    .outs (mux10_outs),
    .outs_ready (mux10_outs_ready),
    .outs_valid (mux10_outs_valid),
    .rst (rst)
  );

  oehb_dataless buffer16(
    .clk (clk),
    .ins_ready (cond_br11_trueOut_ready),
    .ins_valid (cond_br11_trueOut_valid),
    .outs_ready (buffer16_outs_ready),
    .outs_valid (buffer16_outs_valid),
    .rst (rst)
  );

  tehb_dataless buffer17(
    .clk (clk),
    .ins_ready (buffer16_outs_ready),
    .ins_valid (buffer16_outs_valid),
    .outs_ready (buffer17_outs_ready),
    .outs_valid (buffer17_outs_valid),
    .rst (rst)
  );

  control_merge_dataless #(.SIZE(2), .INDEX_TYPE(1)) control_merge1(
    .clk (clk),
    .index (control_merge1_index),
    .index_ready (control_merge1_index_ready),
    .index_valid (control_merge1_index_valid),
    .ins_ready ({buffer17_outs_ready, fork1_outs_1_ready}),
    .ins_valid ({buffer17_outs_valid, fork1_outs_1_valid}),
    .outs_ready (control_merge1_outs_ready),
    .outs_valid (control_merge1_outs_valid),
    .rst (rst)
  );

  fork_type #(.SIZE(3), .DATA_TYPE(1)) fork3(
    .clk (clk),
    .ins (control_merge1_index),
    .ins_ready (control_merge1_index_ready),
    .ins_valid (control_merge1_index_valid),
    .outs ({fork3_outs_2, fork3_outs_1, fork3_outs_0}),
    .outs_ready ({fork3_outs_2_ready, fork3_outs_1_ready, fork3_outs_0_ready}),
    .outs_valid ({fork3_outs_2_valid, fork3_outs_1_valid, fork3_outs_0_valid}),
    .rst (rst)
  );

  fork_dataless #(.SIZE(2)) fork4(
    .clk (clk),
    .ins_ready (control_merge1_outs_ready),
    .ins_valid (control_merge1_outs_valid),
    .outs_ready ({fork4_outs_1_ready, fork4_outs_0_ready}),
    .outs_valid ({fork4_outs_1_valid, fork4_outs_0_valid}),
    .rst (rst)
  );

  handshake_constant_0 #(.DATA_WIDTH(1)) constant4(
    .clk (clk),
    .ctrl_ready (fork4_outs_0_ready),
    .ctrl_valid (fork4_outs_0_valid),
    .outs (constant4_outs),
    .outs_ready (constant4_outs_ready),
    .outs_valid (constant4_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(1), .OUTPUT_TYPE(3)) extsi15(
    .clk (clk),
    .ins (constant4_outs),
    .ins_ready (constant4_outs_ready),
    .ins_valid (constant4_outs_valid),
    .outs (extsi15_outs),
    .outs_ready (extsi15_outs_ready),
    .outs_valid (extsi15_outs_valid),
    .rst (rst)
  );

  oehb #(.DATA_TYPE(3)) buffer0(
    .clk (clk),
    .ins (cond_br0_trueOut),
    .ins_ready (cond_br0_trueOut_ready),
    .ins_valid (cond_br0_trueOut_valid),
    .outs (buffer0_outs),
    .outs_ready (buffer0_outs_ready),
    .outs_valid (buffer0_outs_valid),
    .rst (rst)
  );

  tehb #(.DATA_TYPE(3)) buffer1(
    .clk (clk),
    .ins (buffer0_outs),
    .ins_ready (buffer0_outs_ready),
    .ins_valid (buffer0_outs_valid),
    .outs (buffer1_outs),
    .outs_ready (buffer1_outs_ready),
    .outs_valid (buffer1_outs_valid),
    .rst (rst)
  );

  mux #(.SIZE(2), .DATA_TYPE(3), .SELECT_TYPE(1)) mux11(
    .clk (clk),
    .index (fork8_outs_2),
    .index_ready (fork8_outs_2_ready),
    .index_valid (fork8_outs_2_valid),
    .ins ({buffer1_outs, extsi15_outs}),
    .ins_ready ({buffer1_outs_ready, extsi15_outs_ready}),
    .ins_valid ({buffer1_outs_valid, extsi15_outs_valid}),
    .outs (mux11_outs),
    .outs_ready (mux11_outs_ready),
    .outs_valid (mux11_outs_valid),
    .rst (rst)
  );

  fork_type #(.SIZE(3), .DATA_TYPE(3)) fork5(
    .clk (clk),
    .ins (mux11_outs),
    .ins_ready (mux11_outs_ready),
    .ins_valid (mux11_outs_valid),
    .outs ({fork5_outs_2, fork5_outs_1, fork5_outs_0}),
    .outs_ready ({fork5_outs_2_ready, fork5_outs_1_ready, fork5_outs_0_ready}),
    .outs_valid ({fork5_outs_2_valid, fork5_outs_1_valid, fork5_outs_0_valid}),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(3), .OUTPUT_TYPE(7)) extsi16(
    .clk (clk),
    .ins (fork5_outs_0),
    .ins_ready (fork5_outs_0_ready),
    .ins_valid (fork5_outs_0_valid),
    .outs (extsi16_outs),
    .outs_ready (extsi16_outs_ready),
    .outs_valid (extsi16_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(3), .OUTPUT_TYPE(6)) extsi17(
    .clk (clk),
    .ins (fork5_outs_1),
    .ins_ready (fork5_outs_1_ready),
    .ins_valid (fork5_outs_1_valid),
    .outs (extsi17_outs),
    .outs_ready (extsi17_outs_ready),
    .outs_valid (extsi17_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(3), .OUTPUT_TYPE(4)) extsi18(
    .clk (clk),
    .ins (fork5_outs_2),
    .ins_ready (fork5_outs_2_ready),
    .ins_valid (fork5_outs_2_valid),
    .outs (extsi18_outs),
    .outs_ready (extsi18_outs_ready),
    .outs_valid (extsi18_outs_valid),
    .rst (rst)
  );

  oehb #(.DATA_TYPE(32)) buffer2(
    .clk (clk),
    .ins (cond_br4_trueOut),
    .ins_ready (cond_br4_trueOut_ready),
    .ins_valid (cond_br4_trueOut_valid),
    .outs (buffer2_outs),
    .outs_ready (buffer2_outs_ready),
    .outs_valid (buffer2_outs_valid),
    .rst (rst)
  );

  tehb #(.DATA_TYPE(32)) buffer3(
    .clk (clk),
    .ins (buffer2_outs),
    .ins_ready (buffer2_outs_ready),
    .ins_valid (buffer2_outs_valid),
    .outs (buffer3_outs),
    .outs_ready (buffer3_outs_ready),
    .outs_valid (buffer3_outs_valid),
    .rst (rst)
  );

  mux #(.SIZE(2), .DATA_TYPE(32), .SELECT_TYPE(1)) mux5(
    .clk (clk),
    .index (fork8_outs_3),
    .index_ready (fork8_outs_3_ready),
    .index_valid (fork8_outs_3_valid),
    .ins ({buffer3_outs, mux2_outs}),
    .ins_ready ({buffer3_outs_ready, mux2_outs_ready}),
    .ins_valid ({buffer3_outs_valid, mux2_outs_valid}),
    .outs (mux5_outs),
    .outs_ready (mux5_outs_ready),
    .outs_valid (mux5_outs_valid),
    .rst (rst)
  );

  oehb #(.DATA_TYPE(6)) buffer4(
    .clk (clk),
    .ins (cond_br1_trueOut),
    .ins_ready (cond_br1_trueOut_ready),
    .ins_valid (cond_br1_trueOut_valid),
    .outs (buffer4_outs),
    .outs_ready (buffer4_outs_ready),
    .outs_valid (buffer4_outs_valid),
    .rst (rst)
  );

  tehb #(.DATA_TYPE(6)) buffer5(
    .clk (clk),
    .ins (buffer4_outs),
    .ins_ready (buffer4_outs_ready),
    .ins_valid (buffer4_outs_valid),
    .outs (buffer5_outs),
    .outs_ready (buffer5_outs_ready),
    .outs_valid (buffer5_outs_valid),
    .rst (rst)
  );

  mux #(.SIZE(2), .DATA_TYPE(6), .SELECT_TYPE(1)) mux12(
    .clk (clk),
    .index (fork8_outs_0),
    .index_ready (fork8_outs_0_ready),
    .index_valid (fork8_outs_0_valid),
    .ins ({buffer5_outs, mux10_outs}),
    .ins_ready ({buffer5_outs_ready, mux10_outs_ready}),
    .ins_valid ({buffer5_outs_valid, mux10_outs_valid}),
    .outs (mux12_outs),
    .outs_ready (mux12_outs_ready),
    .outs_valid (mux12_outs_valid),
    .rst (rst)
  );

  fork_type #(.SIZE(2), .DATA_TYPE(6)) fork6(
    .clk (clk),
    .ins (mux12_outs),
    .ins_ready (mux12_outs_ready),
    .ins_valid (mux12_outs_valid),
    .outs ({fork6_outs_1, fork6_outs_0}),
    .outs_ready ({fork6_outs_1_ready, fork6_outs_0_ready}),
    .outs_valid ({fork6_outs_1_valid, fork6_outs_0_valid}),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(6), .OUTPUT_TYPE(7)) extsi19(
    .clk (clk),
    .ins (fork6_outs_1),
    .ins_ready (fork6_outs_1_ready),
    .ins_valid (fork6_outs_1_valid),
    .outs (extsi19_outs),
    .outs_ready (extsi19_outs_ready),
    .outs_valid (extsi19_outs_valid),
    .rst (rst)
  );

  oehb #(.DATA_TYPE(3)) buffer6(
    .clk (clk),
    .ins (cond_br2_trueOut),
    .ins_ready (cond_br2_trueOut_ready),
    .ins_valid (cond_br2_trueOut_valid),
    .outs (buffer6_outs),
    .outs_ready (buffer6_outs_ready),
    .outs_valid (buffer6_outs_valid),
    .rst (rst)
  );

  tehb #(.DATA_TYPE(3)) buffer7(
    .clk (clk),
    .ins (buffer6_outs),
    .ins_ready (buffer6_outs_ready),
    .ins_valid (buffer6_outs_valid),
    .outs (buffer7_outs),
    .outs_ready (buffer7_outs_ready),
    .outs_valid (buffer7_outs_valid),
    .rst (rst)
  );

  mux #(.SIZE(2), .DATA_TYPE(3), .SELECT_TYPE(1)) mux13(
    .clk (clk),
    .index (fork8_outs_1),
    .index_ready (fork8_outs_1_ready),
    .index_valid (fork8_outs_1_valid),
    .ins ({buffer7_outs, mux9_outs}),
    .ins_ready ({buffer7_outs_ready, mux9_outs_ready}),
    .ins_valid ({buffer7_outs_valid, mux9_outs_valid}),
    .outs (mux13_outs),
    .outs_ready (mux13_outs_ready),
    .outs_valid (mux13_outs_valid),
    .rst (rst)
  );

  fork_type #(.SIZE(4), .DATA_TYPE(3)) fork7(
    .clk (clk),
    .ins (mux13_outs),
    .ins_ready (mux13_outs_ready),
    .ins_valid (mux13_outs_valid),
    .outs ({fork7_outs_3, fork7_outs_2, fork7_outs_1, fork7_outs_0}),
    .outs_ready ({fork7_outs_3_ready, fork7_outs_2_ready, fork7_outs_1_ready, fork7_outs_0_ready}),
    .outs_valid ({fork7_outs_3_valid, fork7_outs_2_valid, fork7_outs_1_valid, fork7_outs_0_valid}),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(3), .OUTPUT_TYPE(9)) extsi20(
    .clk (clk),
    .ins (fork7_outs_1),
    .ins_ready (fork7_outs_1_ready),
    .ins_valid (fork7_outs_1_valid),
    .outs (extsi20_outs),
    .outs_ready (extsi20_outs_ready),
    .outs_valid (extsi20_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(3), .OUTPUT_TYPE(5)) extsi21(
    .clk (clk),
    .ins (fork7_outs_2),
    .ins_ready (fork7_outs_2_ready),
    .ins_valid (fork7_outs_2_valid),
    .outs (extsi21_outs),
    .outs_ready (extsi21_outs_ready),
    .outs_valid (extsi21_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(3), .OUTPUT_TYPE(4)) extsi22(
    .clk (clk),
    .ins (fork7_outs_3),
    .ins_ready (fork7_outs_3_ready),
    .ins_valid (fork7_outs_3_valid),
    .outs (extsi22_outs),
    .outs_ready (extsi22_outs_ready),
    .outs_valid (extsi22_outs_valid),
    .rst (rst)
  );

  oehb_dataless buffer8(
    .clk (clk),
    .ins_ready (cond_br7_trueOut_ready),
    .ins_valid (cond_br7_trueOut_valid),
    .outs_ready (buffer8_outs_ready),
    .outs_valid (buffer8_outs_valid),
    .rst (rst)
  );

  tehb_dataless buffer9(
    .clk (clk),
    .ins_ready (buffer8_outs_ready),
    .ins_valid (buffer8_outs_valid),
    .outs_ready (buffer9_outs_ready),
    .outs_valid (buffer9_outs_valid),
    .rst (rst)
  );

  control_merge_dataless #(.SIZE(2), .INDEX_TYPE(1)) control_merge2(
    .clk (clk),
    .index (control_merge2_index),
    .index_ready (control_merge2_index_ready),
    .index_valid (control_merge2_index_valid),
    .ins_ready ({buffer9_outs_ready, fork4_outs_1_ready}),
    .ins_valid ({buffer9_outs_valid, fork4_outs_1_valid}),
    .outs_ready (control_merge2_outs_ready),
    .outs_valid (control_merge2_outs_valid),
    .rst (rst)
  );

  fork_type #(.SIZE(4), .DATA_TYPE(1)) fork8(
    .clk (clk),
    .ins (control_merge2_index),
    .ins_ready (control_merge2_index_ready),
    .ins_valid (control_merge2_index_valid),
    .outs ({fork8_outs_3, fork8_outs_2, fork8_outs_1, fork8_outs_0}),
    .outs_ready ({fork8_outs_3_ready, fork8_outs_2_ready, fork8_outs_1_ready, fork8_outs_0_ready}),
    .outs_valid ({fork8_outs_3_valid, fork8_outs_2_valid, fork8_outs_1_valid, fork8_outs_0_valid}),
    .rst (rst)
  );

  source source0(
    .clk (clk),
    .outs_ready (source0_outs_ready),
    .outs_valid (source0_outs_valid),
    .rst (rst)
  );

  handshake_constant_1 #(.DATA_WIDTH(6)) constant5(
    .clk (clk),
    .ctrl_ready (source0_outs_ready),
    .ctrl_valid (source0_outs_valid),
    .outs (constant5_outs),
    .outs_ready (constant5_outs_ready),
    .outs_valid (constant5_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(6), .OUTPUT_TYPE(9)) extsi23(
    .clk (clk),
    .ins (constant5_outs),
    .ins_ready (constant5_outs_ready),
    .ins_valid (constant5_outs_valid),
    .outs (extsi23_outs),
    .outs_ready (extsi23_outs_ready),
    .outs_valid (extsi23_outs_valid),
    .rst (rst)
  );

  source source1(
    .clk (clk),
    .outs_ready (source1_outs_ready),
    .outs_valid (source1_outs_valid),
    .rst (rst)
  );

  handshake_constant_2 #(.DATA_WIDTH(3)) constant16(
    .clk (clk),
    .ctrl_ready (source1_outs_ready),
    .ctrl_valid (source1_outs_valid),
    .outs (constant16_outs),
    .outs_ready (constant16_outs_ready),
    .outs_valid (constant16_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(3), .OUTPUT_TYPE(4)) extsi24(
    .clk (clk),
    .ins (constant16_outs),
    .ins_ready (constant16_outs_ready),
    .ins_valid (constant16_outs_valid),
    .outs (extsi24_outs),
    .outs_ready (extsi24_outs_ready),
    .outs_valid (extsi24_outs_valid),
    .rst (rst)
  );

  source source2(
    .clk (clk),
    .outs_ready (source2_outs_ready),
    .outs_valid (source2_outs_valid),
    .rst (rst)
  );

  handshake_constant_3 #(.DATA_WIDTH(2)) constant17(
    .clk (clk),
    .ctrl_ready (source2_outs_ready),
    .ctrl_valid (source2_outs_valid),
    .outs (constant17_outs),
    .outs_ready (constant17_outs_ready),
    .outs_valid (constant17_outs_valid),
    .rst (rst)
  );

  fork_type #(.SIZE(2), .DATA_TYPE(2)) fork9(
    .clk (clk),
    .ins (constant17_outs),
    .ins_ready (constant17_outs_ready),
    .ins_valid (constant17_outs_valid),
    .outs ({fork9_outs_1, fork9_outs_0}),
    .outs_ready ({fork9_outs_1_ready, fork9_outs_0_ready}),
    .outs_valid ({fork9_outs_1_valid, fork9_outs_0_valid}),
    .rst (rst)
  );

  extui #(.INPUT_TYPE(2), .OUTPUT_TYPE(4)) extui0(
    .clk (clk),
    .ins (fork9_outs_0),
    .ins_ready (fork9_outs_0_ready),
    .ins_valid (fork9_outs_0_valid),
    .outs (extui0_outs),
    .outs_ready (extui0_outs_ready),
    .outs_valid (extui0_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(2), .OUTPUT_TYPE(4)) extsi25(
    .clk (clk),
    .ins (fork9_outs_1),
    .ins_ready (fork9_outs_1_ready),
    .ins_valid (fork9_outs_1_valid),
    .outs (extsi25_outs),
    .outs_ready (extsi25_outs_ready),
    .outs_valid (extsi25_outs_valid),
    .rst (rst)
  );

  shli #(.DATA_TYPE(4)) shli1(
    .clk (clk),
    .lhs (extsi22_outs),
    .lhs_ready (extsi22_outs_ready),
    .lhs_valid (extsi22_outs_valid),
    .result (shli1_result),
    .result_ready (shli1_result_ready),
    .result_valid (shli1_result_valid),
    .rhs (extui0_outs),
    .rhs_ready (extui0_outs_ready),
    .rhs_valid (extui0_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(4), .OUTPUT_TYPE(5)) extsi26(
    .clk (clk),
    .ins (shli1_result),
    .ins_ready (shli1_result_ready),
    .ins_valid (shli1_result_valid),
    .outs (extsi26_outs),
    .outs_ready (extsi26_outs_ready),
    .outs_valid (extsi26_outs_valid),
    .rst (rst)
  );

  addi #(.DATA_TYPE(5)) addi8(
    .clk (clk),
    .lhs (extsi21_outs),
    .lhs_ready (extsi21_outs_ready),
    .lhs_valid (extsi21_outs_valid),
    .result (addi8_result),
    .result_ready (addi8_result_ready),
    .result_valid (addi8_result_valid),
    .rhs (extsi26_outs),
    .rhs_ready (extsi26_outs_ready),
    .rhs_valid (extsi26_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(5), .OUTPUT_TYPE(6)) extsi27(
    .clk (clk),
    .ins (addi8_result),
    .ins_ready (addi8_result_ready),
    .ins_valid (addi8_result_valid),
    .outs (extsi27_outs),
    .outs_ready (extsi27_outs_ready),
    .outs_valid (extsi27_outs_valid),
    .rst (rst)
  );

  addi #(.DATA_TYPE(6)) addi9(
    .clk (clk),
    .lhs (extsi17_outs),
    .lhs_ready (extsi17_outs_ready),
    .lhs_valid (extsi17_outs_valid),
    .result (addi9_result),
    .result_ready (addi9_result_ready),
    .result_valid (addi9_result_valid),
    .rhs (extsi27_outs),
    .rhs_ready (extsi27_outs_ready),
    .rhs_valid (extsi27_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(6), .OUTPUT_TYPE(32)) extsi28(
    .clk (clk),
    .ins (addi9_result),
    .ins_ready (addi9_result_ready),
    .ins_valid (addi9_result_valid),
    .outs (extsi28_outs),
    .outs_ready (extsi28_outs_ready),
    .outs_valid (extsi28_outs_valid),
    .rst (rst)
  );

  mc_load #(.DATA_TYPE(32), .ADDR_TYPE(32)) mc_load0(
    .addrIn (extsi28_outs),
    .addrIn_ready (extsi28_outs_ready),
    .addrIn_valid (extsi28_outs_valid),
    .addrOut (mc_load0_addrOut),
    .addrOut_ready (mc_load0_addrOut_ready),
    .addrOut_valid (mc_load0_addrOut_valid),
    .clk (clk),
    .dataFromMem (mem_controller1_ldData_0),
    .dataFromMem_ready (mem_controller1_ldData_0_ready),
    .dataFromMem_valid (mem_controller1_ldData_0_valid),
    .dataOut (mc_load0_dataOut),
    .dataOut_ready (mc_load0_dataOut_ready),
    .dataOut_valid (mc_load0_dataOut_valid),
    .rst (rst)
  );

  addi #(.DATA_TYPE(7)) addi10(
    .clk (clk),
    .lhs (extsi16_outs),
    .lhs_ready (extsi16_outs_ready),
    .lhs_valid (extsi16_outs_valid),
    .result (addi10_result),
    .result_ready (addi10_result_ready),
    .result_valid (addi10_result_valid),
    .rhs (extsi19_outs),
    .rhs_ready (extsi19_outs_ready),
    .rhs_valid (extsi19_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(7), .OUTPUT_TYPE(10)) extsi29(
    .clk (clk),
    .ins (addi10_result),
    .ins_ready (addi10_result_ready),
    .ins_valid (addi10_result_valid),
    .outs (extsi29_outs),
    .outs_ready (extsi29_outs_ready),
    .outs_valid (extsi29_outs_valid),
    .rst (rst)
  );

  muli #(.DATA_TYPE(9)) muli1(
    .clk (clk),
    .lhs (extsi20_outs),
    .lhs_ready (extsi20_outs_ready),
    .lhs_valid (extsi20_outs_valid),
    .result (muli1_result),
    .result_ready (muli1_result_ready),
    .result_valid (muli1_result_valid),
    .rhs (extsi23_outs),
    .rhs_ready (extsi23_outs_ready),
    .rhs_valid (extsi23_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(9), .OUTPUT_TYPE(10)) extsi30(
    .clk (clk),
    .ins (muli1_result),
    .ins_ready (muli1_result_ready),
    .ins_valid (muli1_result_valid),
    .outs (extsi30_outs),
    .outs_ready (extsi30_outs_ready),
    .outs_valid (extsi30_outs_valid),
    .rst (rst)
  );

  addi #(.DATA_TYPE(10)) addi11(
    .clk (clk),
    .lhs (extsi29_outs),
    .lhs_ready (extsi29_outs_ready),
    .lhs_valid (extsi29_outs_valid),
    .result (addi11_result),
    .result_ready (addi11_result_ready),
    .result_valid (addi11_result_valid),
    .rhs (extsi30_outs),
    .rhs_ready (extsi30_outs_ready),
    .rhs_valid (extsi30_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(10), .OUTPUT_TYPE(32)) extsi31(
    .clk (clk),
    .ins (addi11_result),
    .ins_ready (addi11_result_ready),
    .ins_valid (addi11_result_valid),
    .outs (extsi31_outs),
    .outs_ready (extsi31_outs_ready),
    .outs_valid (extsi31_outs_valid),
    .rst (rst)
  );

  mc_load #(.DATA_TYPE(32), .ADDR_TYPE(32)) mc_load1(
    .addrIn (extsi31_outs),
    .addrIn_ready (extsi31_outs_ready),
    .addrIn_valid (extsi31_outs_valid),
    .addrOut (mc_load1_addrOut),
    .addrOut_ready (mc_load1_addrOut_ready),
    .addrOut_valid (mc_load1_addrOut_valid),
    .clk (clk),
    .dataFromMem (mem_controller2_ldData_0),
    .dataFromMem_ready (mem_controller2_ldData_0_ready),
    .dataFromMem_valid (mem_controller2_ldData_0_valid),
    .dataOut (mc_load1_dataOut),
    .dataOut_ready (mc_load1_dataOut_ready),
    .dataOut_valid (mc_load1_dataOut_valid),
    .rst (rst)
  );

  muli #(.DATA_TYPE(32)) muli0(
    .clk (clk),
    .lhs (mc_load0_dataOut),
    .lhs_ready (mc_load0_dataOut_ready),
    .lhs_valid (mc_load0_dataOut_valid),
    .result (muli0_result),
    .result_ready (muli0_result_ready),
    .result_valid (muli0_result_valid),
    .rhs (mc_load1_dataOut),
    .rhs_ready (mc_load1_dataOut_ready),
    .rhs_valid (mc_load1_dataOut_valid),
    .rst (rst)
  );

  addi #(.DATA_TYPE(32)) addi0(
    .clk (clk),
    .lhs (mux5_outs),
    .lhs_ready (mux5_outs_ready),
    .lhs_valid (mux5_outs_valid),
    .result (addi0_result),
    .result_ready (addi0_result_ready),
    .result_valid (addi0_result_valid),
    .rhs (muli0_result),
    .rhs_ready (muli0_result_ready),
    .rhs_valid (muli0_result_valid),
    .rst (rst)
  );

  addi #(.DATA_TYPE(4)) addi12(
    .clk (clk),
    .lhs (extsi18_outs),
    .lhs_ready (extsi18_outs_ready),
    .lhs_valid (extsi18_outs_valid),
    .result (addi12_result),
    .result_ready (addi12_result_ready),
    .result_valid (addi12_result_valid),
    .rhs (extsi25_outs),
    .rhs_ready (extsi25_outs_ready),
    .rhs_valid (extsi25_outs_valid),
    .rst (rst)
  );

  fork_type #(.SIZE(2), .DATA_TYPE(4)) fork10(
    .clk (clk),
    .ins (addi12_result),
    .ins_ready (addi12_result_ready),
    .ins_valid (addi12_result_valid),
    .outs ({fork10_outs_1, fork10_outs_0}),
    .outs_ready ({fork10_outs_1_ready, fork10_outs_0_ready}),
    .outs_valid ({fork10_outs_1_valid, fork10_outs_0_valid}),
    .rst (rst)
  );

  trunci #(.INPUT_TYPE(4), .OUTPUT_TYPE(3)) trunci0(
    .clk (clk),
    .ins (fork10_outs_0),
    .ins_ready (fork10_outs_0_ready),
    .ins_valid (fork10_outs_0_valid),
    .outs (trunci0_outs),
    .outs_ready (trunci0_outs_ready),
    .outs_valid (trunci0_outs_valid),
    .rst (rst)
  );

  handshake_cmpi_0 #(.DATA_TYPE(4)) cmpi3(
    .clk (clk),
    .lhs (fork10_outs_1),
    .lhs_ready (fork10_outs_1_ready),
    .lhs_valid (fork10_outs_1_valid),
    .result (cmpi3_result),
    .result_ready (cmpi3_result_ready),
    .result_valid (cmpi3_result_valid),
    .rhs (extsi24_outs),
    .rhs_ready (extsi24_outs_ready),
    .rhs_valid (extsi24_outs_valid),
    .rst (rst)
  );

  fork_type #(.SIZE(5), .DATA_TYPE(1)) fork11(
    .clk (clk),
    .ins (cmpi3_result),
    .ins_ready (cmpi3_result_ready),
    .ins_valid (cmpi3_result_valid),
    .outs ({fork11_outs_4, fork11_outs_3, fork11_outs_2, fork11_outs_1, fork11_outs_0}),
    .outs_ready ({fork11_outs_4_ready, fork11_outs_3_ready, fork11_outs_2_ready, fork11_outs_1_ready, fork11_outs_0_ready}),
    .outs_valid ({fork11_outs_4_valid, fork11_outs_3_valid, fork11_outs_2_valid, fork11_outs_1_valid, fork11_outs_0_valid}),
    .rst (rst)
  );

  cond_br #(.DATA_TYPE(3)) cond_br0(
    .clk (clk),
    .condition (fork11_outs_0),
    .condition_ready (fork11_outs_0_ready),
    .condition_valid (fork11_outs_0_valid),
    .data (trunci0_outs),
    .data_ready (trunci0_outs_ready),
    .data_valid (trunci0_outs_valid),
    .falseOut (cond_br0_falseOut),
    .falseOut_ready (cond_br0_falseOut_ready),
    .falseOut_valid (cond_br0_falseOut_valid),
    .rst (rst),
    .trueOut (cond_br0_trueOut),
    .trueOut_ready (cond_br0_trueOut_ready),
    .trueOut_valid (cond_br0_trueOut_valid)
  );

  sink #(.DATA_TYPE(3)) sink0(
    .clk (clk),
    .ins (cond_br0_falseOut),
    .ins_ready (cond_br0_falseOut_ready),
    .ins_valid (cond_br0_falseOut_valid),
    .rst (rst)
  );

  cond_br #(.DATA_TYPE(32)) cond_br4(
    .clk (clk),
    .condition (fork11_outs_3),
    .condition_ready (fork11_outs_3_ready),
    .condition_valid (fork11_outs_3_valid),
    .data (addi0_result),
    .data_ready (addi0_result_ready),
    .data_valid (addi0_result_valid),
    .falseOut (cond_br4_falseOut),
    .falseOut_ready (cond_br4_falseOut_ready),
    .falseOut_valid (cond_br4_falseOut_valid),
    .rst (rst),
    .trueOut (cond_br4_trueOut),
    .trueOut_ready (cond_br4_trueOut_ready),
    .trueOut_valid (cond_br4_trueOut_valid)
  );

  cond_br #(.DATA_TYPE(6)) cond_br1(
    .clk (clk),
    .condition (fork11_outs_1),
    .condition_ready (fork11_outs_1_ready),
    .condition_valid (fork11_outs_1_valid),
    .data (fork6_outs_0),
    .data_ready (fork6_outs_0_ready),
    .data_valid (fork6_outs_0_valid),
    .falseOut (cond_br1_falseOut),
    .falseOut_ready (cond_br1_falseOut_ready),
    .falseOut_valid (cond_br1_falseOut_valid),
    .rst (rst),
    .trueOut (cond_br1_trueOut),
    .trueOut_ready (cond_br1_trueOut_ready),
    .trueOut_valid (cond_br1_trueOut_valid)
  );

  cond_br #(.DATA_TYPE(3)) cond_br2(
    .clk (clk),
    .condition (fork11_outs_2),
    .condition_ready (fork11_outs_2_ready),
    .condition_valid (fork11_outs_2_valid),
    .data (fork7_outs_0),
    .data_ready (fork7_outs_0_ready),
    .data_valid (fork7_outs_0_valid),
    .falseOut (cond_br2_falseOut),
    .falseOut_ready (cond_br2_falseOut_ready),
    .falseOut_valid (cond_br2_falseOut_valid),
    .rst (rst),
    .trueOut (cond_br2_trueOut),
    .trueOut_ready (cond_br2_trueOut_ready),
    .trueOut_valid (cond_br2_trueOut_valid)
  );

  cond_br_dataless cond_br7(
    .clk (clk),
    .condition (fork11_outs_4),
    .condition_ready (fork11_outs_4_ready),
    .condition_valid (fork11_outs_4_valid),
    .data_ready (control_merge2_outs_ready),
    .data_valid (control_merge2_outs_valid),
    .falseOut_ready (cond_br7_falseOut_ready),
    .falseOut_valid (cond_br7_falseOut_valid),
    .rst (rst),
    .trueOut_ready (cond_br7_trueOut_ready),
    .trueOut_valid (cond_br7_trueOut_valid)
  );

  extsi #(.INPUT_TYPE(3), .OUTPUT_TYPE(4)) extsi32(
    .clk (clk),
    .ins (cond_br2_falseOut),
    .ins_ready (cond_br2_falseOut_ready),
    .ins_valid (cond_br2_falseOut_valid),
    .outs (extsi32_outs),
    .outs_ready (extsi32_outs_ready),
    .outs_valid (extsi32_outs_valid),
    .rst (rst)
  );

  source source3(
    .clk (clk),
    .outs_ready (source3_outs_ready),
    .outs_valid (source3_outs_valid),
    .rst (rst)
  );

  handshake_constant_2 #(.DATA_WIDTH(3)) constant18(
    .clk (clk),
    .ctrl_ready (source3_outs_ready),
    .ctrl_valid (source3_outs_valid),
    .outs (constant18_outs),
    .outs_ready (constant18_outs_ready),
    .outs_valid (constant18_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(3), .OUTPUT_TYPE(4)) extsi33(
    .clk (clk),
    .ins (constant18_outs),
    .ins_ready (constant18_outs_ready),
    .ins_valid (constant18_outs_valid),
    .outs (extsi33_outs),
    .outs_ready (extsi33_outs_ready),
    .outs_valid (extsi33_outs_valid),
    .rst (rst)
  );

  source source4(
    .clk (clk),
    .outs_ready (source4_outs_ready),
    .outs_valid (source4_outs_valid),
    .rst (rst)
  );

  handshake_constant_3 #(.DATA_WIDTH(2)) constant19(
    .clk (clk),
    .ctrl_ready (source4_outs_ready),
    .ctrl_valid (source4_outs_valid),
    .outs (constant19_outs),
    .outs_ready (constant19_outs_ready),
    .outs_valid (constant19_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(2), .OUTPUT_TYPE(4)) extsi34(
    .clk (clk),
    .ins (constant19_outs),
    .ins_ready (constant19_outs_ready),
    .ins_valid (constant19_outs_valid),
    .outs (extsi34_outs),
    .outs_ready (extsi34_outs_ready),
    .outs_valid (extsi34_outs_valid),
    .rst (rst)
  );

  addi #(.DATA_TYPE(4)) addi13(
    .clk (clk),
    .lhs (extsi32_outs),
    .lhs_ready (extsi32_outs_ready),
    .lhs_valid (extsi32_outs_valid),
    .result (addi13_result),
    .result_ready (addi13_result_ready),
    .result_valid (addi13_result_valid),
    .rhs (extsi34_outs),
    .rhs_ready (extsi34_outs_ready),
    .rhs_valid (extsi34_outs_valid),
    .rst (rst)
  );

  fork_type #(.SIZE(2), .DATA_TYPE(4)) fork12(
    .clk (clk),
    .ins (addi13_result),
    .ins_ready (addi13_result_ready),
    .ins_valid (addi13_result_valid),
    .outs ({fork12_outs_1, fork12_outs_0}),
    .outs_ready ({fork12_outs_1_ready, fork12_outs_0_ready}),
    .outs_valid ({fork12_outs_1_valid, fork12_outs_0_valid}),
    .rst (rst)
  );

  trunci #(.INPUT_TYPE(4), .OUTPUT_TYPE(3)) trunci1(
    .clk (clk),
    .ins (fork12_outs_0),
    .ins_ready (fork12_outs_0_ready),
    .ins_valid (fork12_outs_0_valid),
    .outs (trunci1_outs),
    .outs_ready (trunci1_outs_ready),
    .outs_valid (trunci1_outs_valid),
    .rst (rst)
  );

  handshake_cmpi_0 #(.DATA_TYPE(4)) cmpi4(
    .clk (clk),
    .lhs (fork12_outs_1),
    .lhs_ready (fork12_outs_1_ready),
    .lhs_valid (fork12_outs_1_valid),
    .result (cmpi4_result),
    .result_ready (cmpi4_result_ready),
    .result_valid (cmpi4_result_valid),
    .rhs (extsi33_outs),
    .rhs_ready (extsi33_outs_ready),
    .rhs_valid (extsi33_outs_valid),
    .rst (rst)
  );

  fork_type #(.SIZE(4), .DATA_TYPE(1)) fork13(
    .clk (clk),
    .ins (cmpi4_result),
    .ins_ready (cmpi4_result_ready),
    .ins_valid (cmpi4_result_valid),
    .outs ({fork13_outs_3, fork13_outs_2, fork13_outs_1, fork13_outs_0}),
    .outs_ready ({fork13_outs_3_ready, fork13_outs_2_ready, fork13_outs_1_ready, fork13_outs_0_ready}),
    .outs_valid ({fork13_outs_3_valid, fork13_outs_2_valid, fork13_outs_1_valid, fork13_outs_0_valid}),
    .rst (rst)
  );

  cond_br #(.DATA_TYPE(3)) cond_br15(
    .clk (clk),
    .condition (fork13_outs_0),
    .condition_ready (fork13_outs_0_ready),
    .condition_valid (fork13_outs_0_valid),
    .data (trunci1_outs),
    .data_ready (trunci1_outs_ready),
    .data_valid (trunci1_outs_valid),
    .falseOut (cond_br15_falseOut),
    .falseOut_ready (cond_br15_falseOut_ready),
    .falseOut_valid (cond_br15_falseOut_valid),
    .rst (rst),
    .trueOut (cond_br15_trueOut),
    .trueOut_ready (cond_br15_trueOut_ready),
    .trueOut_valid (cond_br15_trueOut_valid)
  );

  sink #(.DATA_TYPE(3)) sink2(
    .clk (clk),
    .ins (cond_br15_falseOut),
    .ins_ready (cond_br15_falseOut_ready),
    .ins_valid (cond_br15_falseOut_valid),
    .rst (rst)
  );

  cond_br #(.DATA_TYPE(32)) cond_br9(
    .clk (clk),
    .condition (fork13_outs_2),
    .condition_ready (fork13_outs_2_ready),
    .condition_valid (fork13_outs_2_valid),
    .data (cond_br4_falseOut),
    .data_ready (cond_br4_falseOut_ready),
    .data_valid (cond_br4_falseOut_valid),
    .falseOut (cond_br9_falseOut),
    .falseOut_ready (cond_br9_falseOut_ready),
    .falseOut_valid (cond_br9_falseOut_valid),
    .rst (rst),
    .trueOut (cond_br9_trueOut),
    .trueOut_ready (cond_br9_trueOut_ready),
    .trueOut_valid (cond_br9_trueOut_valid)
  );

  cond_br #(.DATA_TYPE(6)) cond_br16(
    .clk (clk),
    .condition (fork13_outs_1),
    .condition_ready (fork13_outs_1_ready),
    .condition_valid (fork13_outs_1_valid),
    .data (cond_br1_falseOut),
    .data_ready (cond_br1_falseOut_ready),
    .data_valid (cond_br1_falseOut_valid),
    .falseOut (cond_br16_falseOut),
    .falseOut_ready (cond_br16_falseOut_ready),
    .falseOut_valid (cond_br16_falseOut_valid),
    .rst (rst),
    .trueOut (cond_br16_trueOut),
    .trueOut_ready (cond_br16_trueOut_ready),
    .trueOut_valid (cond_br16_trueOut_valid)
  );

  cond_br_dataless cond_br11(
    .clk (clk),
    .condition (fork13_outs_3),
    .condition_ready (fork13_outs_3_ready),
    .condition_valid (fork13_outs_3_valid),
    .data_ready (cond_br7_falseOut_ready),
    .data_valid (cond_br7_falseOut_valid),
    .falseOut_ready (cond_br11_falseOut_ready),
    .falseOut_valid (cond_br11_falseOut_valid),
    .rst (rst),
    .trueOut_ready (cond_br11_trueOut_ready),
    .trueOut_valid (cond_br11_trueOut_valid)
  );

  handshake_constant_3 #(.DATA_WIDTH(2)) constant20(
    .clk (clk),
    .ctrl_ready (fork16_outs_0_ready),
    .ctrl_valid (fork16_outs_0_valid),
    .outs (constant20_outs),
    .outs_ready (constant20_outs_ready),
    .outs_valid (constant20_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(2), .OUTPUT_TYPE(32)) extsi9(
    .clk (clk),
    .ins (constant20_outs),
    .ins_ready (constant20_outs_ready),
    .ins_valid (constant20_outs_valid),
    .outs (extsi9_outs),
    .outs_ready (extsi9_outs_ready),
    .outs_valid (extsi9_outs_valid),
    .rst (rst)
  );

  fork_type #(.SIZE(2), .DATA_TYPE(6)) fork14(
    .clk (clk),
    .ins (cond_br16_falseOut),
    .ins_ready (cond_br16_falseOut_ready),
    .ins_valid (cond_br16_falseOut_valid),
    .outs ({fork14_outs_1, fork14_outs_0}),
    .outs_ready ({fork14_outs_1_ready, fork14_outs_0_ready}),
    .outs_valid ({fork14_outs_1_valid, fork14_outs_0_valid}),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(6), .OUTPUT_TYPE(7)) extsi35(
    .clk (clk),
    .ins (fork14_outs_0),
    .ins_ready (fork14_outs_0_ready),
    .ins_valid (fork14_outs_0_valid),
    .outs (extsi35_outs),
    .outs_ready (extsi35_outs_ready),
    .outs_valid (extsi35_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(6), .OUTPUT_TYPE(32)) extsi36(
    .clk (clk),
    .ins (fork14_outs_1),
    .ins_ready (fork14_outs_1_ready),
    .ins_valid (fork14_outs_1_valid),
    .outs (extsi36_outs),
    .outs_ready (extsi36_outs_ready),
    .outs_valid (extsi36_outs_valid),
    .rst (rst)
  );

  fork_type #(.SIZE(2), .DATA_TYPE(32)) fork15(
    .clk (clk),
    .ins (cond_br9_falseOut),
    .ins_ready (cond_br9_falseOut_ready),
    .ins_valid (cond_br9_falseOut_valid),
    .outs ({fork15_outs_1, fork15_outs_0}),
    .outs_ready ({fork15_outs_1_ready, fork15_outs_0_ready}),
    .outs_valid ({fork15_outs_1_valid, fork15_outs_0_valid}),
    .rst (rst)
  );

  fork_dataless #(.SIZE(2)) fork16(
    .clk (clk),
    .ins_ready (cond_br11_falseOut_ready),
    .ins_valid (cond_br11_falseOut_valid),
    .outs_ready ({fork16_outs_1_ready, fork16_outs_0_ready}),
    .outs_valid ({fork16_outs_1_valid, fork16_outs_0_valid}),
    .rst (rst)
  );

  source source5(
    .clk (clk),
    .outs_ready (source5_outs_ready),
    .outs_valid (source5_outs_valid),
    .rst (rst)
  );

  handshake_constant_4 #(.DATA_WIDTH(6)) constant21(
    .clk (clk),
    .ctrl_ready (source5_outs_ready),
    .ctrl_valid (source5_outs_valid),
    .outs (constant21_outs),
    .outs_ready (constant21_outs_ready),
    .outs_valid (constant21_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(6), .OUTPUT_TYPE(7)) extsi37(
    .clk (clk),
    .ins (constant21_outs),
    .ins_ready (constant21_outs_ready),
    .ins_valid (constant21_outs_valid),
    .outs (extsi37_outs),
    .outs_ready (extsi37_outs_ready),
    .outs_valid (extsi37_outs_valid),
    .rst (rst)
  );

  source source6(
    .clk (clk),
    .outs_ready (source6_outs_ready),
    .outs_valid (source6_outs_valid),
    .rst (rst)
  );

  handshake_constant_3 #(.DATA_WIDTH(2)) constant22(
    .clk (clk),
    .ctrl_ready (source6_outs_ready),
    .ctrl_valid (source6_outs_valid),
    .outs (constant22_outs),
    .outs_ready (constant22_outs_ready),
    .outs_valid (constant22_outs_valid),
    .rst (rst)
  );

  extsi #(.INPUT_TYPE(2), .OUTPUT_TYPE(7)) extsi38(
    .clk (clk),
    .ins (constant22_outs),
    .ins_ready (constant22_outs_ready),
    .ins_valid (constant22_outs_valid),
    .outs (extsi38_outs),
    .outs_ready (extsi38_outs_ready),
    .outs_valid (extsi38_outs_valid),
    .rst (rst)
  );

  mc_store #(.DATA_TYPE(32), .ADDR_TYPE(32)) mc_store0(
    .addrIn (extsi36_outs),
    .addrIn_ready (extsi36_outs_ready),
    .addrIn_valid (extsi36_outs_valid),
    .addrOut (mc_store0_addrOut),
    .addrOut_ready (mc_store0_addrOut_ready),
    .addrOut_valid (mc_store0_addrOut_valid),
    .clk (clk),
    .dataIn (fork15_outs_1),
    .dataIn_ready (fork15_outs_1_ready),
    .dataIn_valid (fork15_outs_1_valid),
    .dataToMem (mc_store0_dataToMem),
    .dataToMem_ready (mc_store0_dataToMem_ready),
    .dataToMem_valid (mc_store0_dataToMem_valid),
    .rst (rst)
  );

  addi #(.DATA_TYPE(7)) addi14(
    .clk (clk),
    .lhs (extsi35_outs),
    .lhs_ready (extsi35_outs_ready),
    .lhs_valid (extsi35_outs_valid),
    .result (addi14_result),
    .result_ready (addi14_result_ready),
    .result_valid (addi14_result_valid),
    .rhs (extsi38_outs),
    .rhs_ready (extsi38_outs_ready),
    .rhs_valid (extsi38_outs_valid),
    .rst (rst)
  );

  fork_type #(.SIZE(2), .DATA_TYPE(7)) fork17(
    .clk (clk),
    .ins (addi14_result),
    .ins_ready (addi14_result_ready),
    .ins_valid (addi14_result_valid),
    .outs ({fork17_outs_1, fork17_outs_0}),
    .outs_ready ({fork17_outs_1_ready, fork17_outs_0_ready}),
    .outs_valid ({fork17_outs_1_valid, fork17_outs_0_valid}),
    .rst (rst)
  );

  trunci #(.INPUT_TYPE(7), .OUTPUT_TYPE(6)) trunci2(
    .clk (clk),
    .ins (fork17_outs_0),
    .ins_ready (fork17_outs_0_ready),
    .ins_valid (fork17_outs_0_valid),
    .outs (trunci2_outs),
    .outs_ready (trunci2_outs_ready),
    .outs_valid (trunci2_outs_valid),
    .rst (rst)
  );

  handshake_cmpi_1 #(.DATA_TYPE(7)) cmpi5(
    .clk (clk),
    .lhs (fork17_outs_1),
    .lhs_ready (fork17_outs_1_ready),
    .lhs_valid (fork17_outs_1_valid),
    .result (cmpi5_result),
    .result_ready (cmpi5_result_ready),
    .result_valid (cmpi5_result_valid),
    .rhs (extsi37_outs),
    .rhs_ready (extsi37_outs_ready),
    .rhs_valid (extsi37_outs_valid),
    .rst (rst)
  );

  fork_type #(.SIZE(3), .DATA_TYPE(1)) fork18(
    .clk (clk),
    .ins (cmpi5_result),
    .ins_ready (cmpi5_result_ready),
    .ins_valid (cmpi5_result_valid),
    .outs ({fork18_outs_2, fork18_outs_1, fork18_outs_0}),
    .outs_ready ({fork18_outs_2_ready, fork18_outs_1_ready, fork18_outs_0_ready}),
    .outs_valid ({fork18_outs_2_valid, fork18_outs_1_valid, fork18_outs_0_valid}),
    .rst (rst)
  );

  cond_br #(.DATA_TYPE(6)) cond_br17(
    .clk (clk),
    .condition (fork18_outs_0),
    .condition_ready (fork18_outs_0_ready),
    .condition_valid (fork18_outs_0_valid),
    .data (trunci2_outs),
    .data_ready (trunci2_outs_ready),
    .data_valid (trunci2_outs_valid),
    .falseOut (cond_br17_falseOut),
    .falseOut_ready (cond_br17_falseOut_ready),
    .falseOut_valid (cond_br17_falseOut_valid),
    .rst (rst),
    .trueOut (cond_br17_trueOut),
    .trueOut_ready (cond_br17_trueOut_ready),
    .trueOut_valid (cond_br17_trueOut_valid)
  );

  sink #(.DATA_TYPE(6)) sink4(
    .clk (clk),
    .ins (cond_br17_falseOut),
    .ins_ready (cond_br17_falseOut_ready),
    .ins_valid (cond_br17_falseOut_valid),
    .rst (rst)
  );

  cond_br_dataless cond_br13(
    .clk (clk),
    .condition (fork18_outs_1),
    .condition_ready (fork18_outs_1_ready),
    .condition_valid (fork18_outs_1_valid),
    .data_ready (fork16_outs_1_ready),
    .data_valid (fork16_outs_1_valid),
    .falseOut_ready (cond_br13_falseOut_ready),
    .falseOut_valid (cond_br13_falseOut_valid),
    .rst (rst),
    .trueOut_ready (cond_br13_trueOut_ready),
    .trueOut_valid (cond_br13_trueOut_valid)
  );

  cond_br #(.DATA_TYPE(32)) cond_br14(
    .clk (clk),
    .condition (fork18_outs_2),
    .condition_ready (fork18_outs_2_ready),
    .condition_valid (fork18_outs_2_valid),
    .data (fork15_outs_0),
    .data_ready (fork15_outs_0_ready),
    .data_valid (fork15_outs_0_valid),
    .falseOut (cond_br14_falseOut),
    .falseOut_ready (cond_br14_falseOut_ready),
    .falseOut_valid (cond_br14_falseOut_valid),
    .rst (rst),
    .trueOut (cond_br14_trueOut),
    .trueOut_ready (cond_br14_trueOut_ready),
    .trueOut_valid (cond_br14_trueOut_valid)
  );

  sink #(.DATA_TYPE(32)) sink5(
    .clk (clk),
    .ins (cond_br14_trueOut),
    .ins_ready (cond_br14_trueOut_ready),
    .ins_valid (cond_br14_trueOut_valid),
    .rst (rst)
  );

  fork_dataless #(.SIZE(3)) fork19(
    .clk (clk),
    .ins_ready (cond_br13_falseOut_ready),
    .ins_valid (cond_br13_falseOut_valid),
    .outs_ready ({fork19_outs_2_ready, fork19_outs_1_ready, fork19_outs_0_ready}),
    .outs_valid ({fork19_outs_2_valid, fork19_outs_1_valid, fork19_outs_0_valid}),
    .rst (rst)
  );

endmodule
