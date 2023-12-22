LOW = True
HIGH = False

def main():
    lines = readLines("input.txt")
    components = {}
    for line in lines:
        name = line.split(" -> ")[0]
        if name == "broadcaster":
            components[name] = Broadcast(name)
        elif name[0] == "%":
            components[name[1:]] = FlipFlop(name[1:])
        elif name[0] == "&":
            components[name[1:]] = Conjunction(name[1:])
        else:
            raise "err"

    for line in lines:
        pieces = line.split(" -> ")
        name = pieces[0]
        if name[0] == "%" or name[0] == "&":
            name = name[1:]
        deps = pieces[1].split(", ")
        for dep in deps:
            if dep in components:
                components[name].addOutput(components[dep])
            else:
                components[name].addOutput(Broadcast(dep))

    pulses = {LOW: 0, HIGH: 0}

    for _ in range(1000):
        pending = [(components["broadcaster"], Broadcast("button"), LOW)]

        while len(pending) != 0:
            comp, source, signal = pending.pop(0)
            # print(source.name + " " + str(signal) + " " + comp.name)
            pulses[signal] = pulses[signal] + 1
            comp.receive(source, signal, pending)

    res = pulses[LOW] * pulses[HIGH]
    print(res)

class Broadcast:
    def __init__(self, name):
        self.name = name
        self.outputs = []

    def addOutput(self, output):
        self.outputs.append(output)
        output.registerInput(self)

    def registerInput(self, input):
        pass

    def receive(self, source, signal, pending):
        for output in self.outputs:
            pending.append((output, self, signal))

class FlipFlop:
    def __init__(self, name):
        self.on = False
        self.name = name
        self.outputs = []

    def addOutput(self, output):
        self.outputs.append(output)
        output.registerInput(self)

    def registerInput(self, input):
        pass

    def receive(self, source, signal, pending):
        if signal:
            self.on = not self.on
            for output in self.outputs:
                pending.append((output, self, not self.on))

class Conjunction:
    def __init__(self, name):
        self.inputs = {}
        self.name = name
        self.outputs = []

    def addOutput(self, output):
        self.outputs.append(output)
        output.registerInput(self)

    def registerInput(self, input):
        self.inputs[input] = LOW

    def receive(self, source, signal, pending):
        self.inputs[source] = signal
        pulse = LOW
        for _, inp in self.inputs.items():
            if inp == LOW:
                pulse = HIGH
        for output in self.outputs:
            pending.append((output, self, pulse))


def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()