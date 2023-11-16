from output import UNI
from tqdm import tqdm
import time
import os

class HUB:
    def __init__(self) -> None:
        pass
    
    def initialize() -> None:
        UNI.Success("#   [Initializing HUB]")
        for tqdmLoadingBar in tqdm(range(100)):
            CPUCOUNTFORLOADING = os.cpu_count()
            CPUCOUNTFORLOADING /= 100
            time.sleep(CPUCOUNTFORLOADING - .119)
        UNI.Success("#   [HUB has been Initialized]")
        try:
            from Application import HUB_APP
            HUB_APP.Application()
        except ImportError as IError:
            UNI.Error(f"Error while importing - {IError}")
