from typing import Any, Dict
import tqdm

import imageio
from io import BytesIO

from frontend.algorithms.cfg import Any, Dict
from frontend.algorithms.simulator.simulateFSM import Any, Dict

from .simulateLoop import *


class Simulator(LoopSimulator):

    def __init__(self, fsm: FSM) -> None:
        super().__init__(fsm)
        self.images: List[BytesIO] = []
        self._cycle = 0

    def run(self, numCycles: int = None, verbose: bool = True) -> None:
        maxCycles = numCycles or 100

        self.images.clear()
        for cycle in tqdm.tqdm(range(maxCycles)):
            self._cycle = cycle
            self.images.append(self._renderFSM())
            done = self.step()
            self.leave()
            if verbose:
                self.printStats()

            if done:
                break

    def dumpGIF(self, filename: str) -> None:
        images = [imageio.imread(img) for img in self.images]
        imageio.mimsave(filename, images, duration=len(images) * 1)

    def printStats(self) -> Dict[str, Any]:
        print("-" * 80)
        print("Cycle", self._cycle)
        return super().printStats()
