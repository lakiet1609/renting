import pandas as pd

from configs.cfg import SysConfig as sc
from schema.system_schema import (InputModel,
                                  OutputModel,
                                  ResultModel,
                                  StatusEnum,
                                  StatusModel) 


class RoommateMatching:
    def __init__(self, inp: InputModel):
        self.input_model = inp.input_model
        self.data = pd.read_csv(sc.data_file)
    
    def run(self) -> OutputModel:
        dummy_data = 'This is dummy data'
        status = StatusModel(status=StatusEnum.failure, message='Fail to process')
        result = ResultModel(output_model=dummy_data)
        return OutputModel(
            result=result,
            status=status
        )



