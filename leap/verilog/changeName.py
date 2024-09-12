"""
Copyright (c) 2024 Hanyu Wang <https://github.com/Nozidoali>

Created Date: Friday, August 16th 2024, 8:01:50 am
Author: Hanyu Wang

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1. Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
contributors may be used to endorse or promote products derived from this
software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS AS
IS AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR 
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
THE POSSIBILITY OF SUCH DAMAGE.

HISTORY:
Date      	By	Comments
----------	---	----------------------------------------------------------
"""


def changeNameInLines(inputLines: list[str], renameClk: bool = True) -> list[str]:
    data = "\n".join(inputLines)
    newData = changeNameInData(data, renameClk)
    return [x + "\n" for x in newData.split("\n")]


def changeName(inputFile: str, outputFile: str, renameClk: bool = True):
    with open(inputFile, "r") as f:
        data = f.read()
        if not data:
            raise ValueError("Empty file")

    newData = changeNameInData(data, renameClk)
    with open(outputFile, "w") as f:
        f.write(newData)


def changeNameInData(data: str, renameClk: bool = True) -> str:
    import re

    old2new = {}

    # remove comments
    data = re.sub(r"//.*", "", data)
    data = re.sub(r"/\*.*\*/", "", data)

    # remove line breaks
    data = re.sub(r"\n", " ", data)

    # search for wire ...; and reg ...;
    wireDefs = re.findall(r"wire\s+(.*?);", data)
    regDefs = re.findall(r"reg\s+(.*?);", data)
    inputDefs = re.findall(r"input\s+(.*?);", data)
    outputDefs = re.findall(r"output\s+(.*?);", data)

    signals = []
    for definitions in wireDefs + regDefs + inputDefs + outputDefs:
        for x in definitions.split(","):
            x = x.strip()
            if " " in x:
                # this means the definition is like [7:0] signal and has to be split
                x = x.split()[1]
            signals.append(x)

    # search for special characters
    for signal in signals:
        newName = signal
        # check for \\ and replace it with _
        newName = re.sub(r"\\", "", newName)
        # check for | and replace it with __
        newName = re.sub(r"\|", "_", newName)
        if newName != signal:
            old2new[signal] = newName

    # search for the clock signal
    if renameClk:
        old2new["clock"] = "clk"

    # check for the module port list
    modulePortList = re.findall(r"module\s+(.*?)\s*\((.*?)\);", data)
    for modulePort in modulePortList:
        data = getNewDefStr(modulePort[1], data, defStr=None, showRange=False)

    # check the input and output definitions
    for defStr in ["input", "output", "reg", "wire"]:
        defs = re.findall(rf"\s{defStr}\s+(.*?);", data)
        for definition in defs:
            data = getNewDefStr(definition, data, defStr=defStr, showRange=True)

    for old, new in old2new.items():
        try:
            data = data.replace(old, new)
        except Exception as e:
            print(f"Error: {e}")
            print(f"Old: {old}")
            print(f"New: {new}")
            # print(f"Data: {data}")
            exit(1)

    # search for the initial begin block and change it to reset
    # we first match the string between initial begin and end
    m = re.search(r"initial begin(.*?)end", data, re.DOTALL)
    if m:
        content = m.group(1)
        newContents = []
        statements = content.split(";")
        for statement in statements:
            # we wrap it with reset begin and end
            if statement.strip() == "":
                continue
            statement = statement.strip()
            # newContent = f"if (reset) begin\n{statement};\nend "
            newContent = f"{statement}; "
            newContents.append(newContent)
        data = data.replace(content, "\n".join(newContents))

        # finally we replace the initial begin with always @(*)
        data = data.replace("initial begin", "always @(reset) begin ")

    # pretty
    # replace more than one space with one space
    data = re.sub(r"\s+", " ", data)
    data = data.replace(";", ";\n")
    data = data.replace("{", "{\n")
    data = data.replace("}", "}\n")
    data = data.replace("endmodule", "endmodule\n")
    data = data.replace("end ", "end\n")
    data = data.replace("\t", " ")

    return data


def getNewDefStr(
    oldDef: str,
    dataStr: str,
    defStr: str = None,
    showRange: bool = True,
    renameClk: bool = True,
):
    import re

    signalWidth = {}
    ports = []
    for x in oldDef.split(","):
        x = x.strip()

        if " " in x:
            # this means the definition is like [7:0] signal and has to be split
            x = x.split(" ")[1]
        ports.append(x)

    newPortDefs = []
    for port in ports:
        port = port.strip()
        port = re.sub(r"\\", "", port)
        port = re.sub(r"\|", "_", port)

        if renameClk:
            if port == "clock":
                port = "clk"

        if port.endswith("]") and "[" in port:
            portName = port.split("[")[0]
            m = re.search(r"\[(\d+)\]", port)
            if m:
                width = int(m.group(1))
                if portName in signalWidth:
                    signalWidth[portName] = max(signalWidth[portName], width)
                else:
                    signalWidth[portName] = width
            port = portName
        newPortDefs.append(port)

    newPortDefs = list(set(newPortDefs))
    newPortDefsStr = []
    for port in newPortDefs:
        if port in signalWidth and showRange:
            newPortDefsStr.append(f"[{signalWidth[port]}:0] {port}")
        else:
            newPortDefsStr.append(port)

    if defStr is None:
        return dataStr.replace(oldDef, ",\n\t".join(newPortDefsStr))
    else:
        return dataStr.replace(oldDef, f";\n{defStr} ".join(newPortDefsStr))
