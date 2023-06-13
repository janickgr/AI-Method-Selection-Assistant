import pandas as pd

from models.model_class import LGBModel


class Result:

    def __init__(self, input_data, count_methods_output) -> None:
        self.output_df = None
        self.plot_output_df = pd.DataFrame()

        self.lgb_model = LGBModel()

        self.input_data = input_data
        self.count_methods_output = count_methods_output
        pass

    def create_result_df(self) -> None:
        result = self.lgb_model.get_predict_result_raw(input_data=self.input_data)
        self.output_df = result[:self.count_methods_output]
        return 
    
    def create_result_plot(self) -> None:
        self.plot_output_df = self.lgb_model.get_predict_result_plot(input_data=self.input_data)
        self.plot_output_df = self.plot_output_df[:self.count_methods_output]
        return


