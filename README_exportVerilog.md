The following README explains the important information related to the output produced. 
First, it talks about the naming conventions used in this README. Then, it talks about the naming format of the variables inside the output files. Finally, it talks about the ouput files.


# NAMING CONVENTIONS

Everything mentioned between "`" is a variable name or BB id that depends on the node and the BB it belongs to.

The following it's important terminology for the rest of the README

nodeName: the name of a generic node
PhiNodeName: name of the phi node
IdBB: id of the BB where this node belongs to
IdSrcBB: id of the BB src of the edge across BBs
IdDstBB: id of the BB dst of the edge across BBs

# NAMING FORMAT

Firstly, we have to mention name formats:

	(i) input control for the phi node (which is an output of the FSM): `PhiNodeName`_BB_`IdBB`

	(ii) input control of the branch node (which is the input of a branch node): n`ConditionNode`_ctrlOut_BB_`IdBB`

	(iii) memory ports for load: loaddd_`memoryName`_fromMem (data from memory) and loaddd_`memoryName`_addr (address to memory)

	(iv) memory ports for store: storeee_`memoryName`_toMem (data to memory) and storeee_`memoryName`_addr (address to memory)

	(v) multiplier ports: legup_mult_`multName`_result (output from memory unit), legup_mult_`multName`_in1 (input1 to memory unit) and legup_mult_`multName`_in2 (input2 to memory unit)

	(vi) loops ports (ports created to break combinational loops whose destination are phi nodes): n`nodeName`_po_BB_`IdBB` (PO of the loop) and n`PhiNodeName`_pi_BB_`IdBB` (PI of the loop)

	(vii) anchor ports (ports created to identify the edges connecting different BBs. It is only create one PO of the anchor which represents the output of the src node of the edge across BBs. Only this port is necessary to identify such an edge.): `nodeName`_anchorPo_BB_`IdSrcBB`_BB_`IdDstBB`


# OUTPUT

The leap-frontend produces three important files that can be used for the scheduling of the datapath:
  
        (1) JSON FILE

        (2) VERILOG FILE

        (3) CFG FILE


## JSON FILE
         The json file is organized in three parts:
		- dip
		- cip
		- BB_info

	dip : Contains information related to dip dependencies. It is organized as a dictionary where the keys are PIs or POs variable names and the values are the bits of this variable

	cip : Describes the cip constraints to add in the scheduling formulation. There are  types of constraints: 
		
		(i) enable_ctrl constraints: connect the input control signal of the branch node (input of the FSM) to the input control signal of the phi node (output of the FSM). If this edge is a loopback edge, the constraint includes the II variable.
					
		(ii) memory constraints: connects the memory ports to preserve memory control constraints. If this edge is a loopback edge, it includes the II constraint.

		(iii) multi-latency constraints: it describes the multi-latency caused by the multi-latency operations. For example, it describes the delays between the memory ports 

	BB_info : Describes the BB in which each nodes belongs to. The keys are BB ids following the format BB_`IdBB`. The values are lists containing all the nodes belonging to this BB.


## VERILOG FILE
	

	Verilog file containts the datapath of the initial circuit. Also contains additional PIs/POs which are the following:


		(i) input control of the branch node which become PO since they govern the FSM

		(ii) input control of the phi nodes which are PI of the datapath since they are controlled by the FSM

		(iii) memory ports

		(iv) multi-latency operations ports

		(v) anchors PO which are used only to identify an edge across BBs

		(vi) end circuit PI which is the input of the end signal value endCircuit_endCircuitPI. The endCircuit PO which represents the end signal sent by the datapath. In the majority of the cases in the datapath endCircuit = endCircuit_endCircuitPI. However, there could be more complicated cases where multiple conditions are needed to end a circuit


## CFG FILE


	It is a dot file describing the CFG of the datapath. The ids used in the CFG match the BB ids in the JSON and VERILOG FILE.

