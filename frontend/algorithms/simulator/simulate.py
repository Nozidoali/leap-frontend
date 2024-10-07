import tqdm

import imageio
from io import BytesIO

from .simulateLoop import *

class Simulator(LoopSimulator):

    def __init__(self, fsm: FSM) -> None:
        super().__init__(fsm)
        self.images: List[BytesIO] = []

    def run(self, numCycles: int = None) -> None:
        maxCycles = numCycles or 100

        self.images.clear()
        for cycle in tqdm.tqdm(range(maxCycles)):
            self.images.append(self._renderFSM())
            done = self.step()
            self.leave()
            if done:
                break

    def dumpGIF(self, filename: str) -> None:
        images = [imageio.imread(img) for img in self.images]
        imageio.mimsave(filename, images, duration=len(images) * 1)
