import pandas as pd
import asyncio
from project_data_gathering import constant_data_pull
from textual.app import App, ComposeResult
from textual.widgets import DataTable, ListView, ListItem, Static, Label
from textual.containers import Horizontal, Vertical

from time import time
from textual.reactive import reactive
from textual.widget import Widget

class Timer(Widget):

    start_time = reactive(time)

# Textual app to display the three items from data_dict
class TfLDisplayApp(App):
    """Display three widgets: 
    - left: DataTable for `next_tube_and_bus_df`
    - top-right: vertical df from `tube_line_status` (one item per row)
    - bottom-right: DataTable for `borris_bike_df`

    Pass `data_dict` into the constructor.
    """

    CSS_PATH = "horizontal_layout.tcss"

    def __init__(self, data_dict: dict, **kwargs):
        super().__init__(**kwargs)
        self.data_dict = data_dict

    def _df_to_datatable(self, df) -> DataTable:
        """Convert a pandas DataFrame to a Textual DataTable widget.

        If `df` is not a DataFrame, returns a Static widget with stringified content.
        """
        try:
            if not hasattr(df, "columns"):
                raise TypeError
            table = DataTable(zebra_stripes=True)
            # add columns
            for col in df.columns:
                table.add_column(str(col))
            # add rows
            for _, row in df.iterrows():
                table.add_row(*[str(x) for x in row.tolist()])
            return table
        except Exception as e:
            return Static(f"Error: {str(e)}\n\n{str(df)[:500]}")

    def compose(self) -> ComposeResult:
        """Compose the layout: left list + right container with two tables."""
        # Left side: DataFrame rendered as DataTable
        
        left_table = self._df_to_datatable(self.data_dict.get("next_tube_and_bus_df", pd.DataFrame()))
        left_table.id = "next_tube_and_bus_df"

        # Right side: top and bottom DataTables
        top_table = self._df_to_datatable(self.data_dict.get("tube_line_status", pd.DataFrame()))
        top_table.id = "status_df"
        
        bottom_table = self._df_to_datatable(self.data_dict.get("borris_bike_df", pd.DataFrame()))
        bottom_table.id = "borris_bike_df"

        # Right container: vertical stack of two tables
        right_container = Vertical(
            top_table,
            bottom_table,
            id="right_container"
        )

        # Main horizontal layout: left DataFrame table + right container
        yield Horizontal(
            left_table,
            right_container,
            id="main_container"
        )


if __name__ == "__main__":
    # gather data and run the textual app. `constant_data_pull` should return a dict
    data_dict = asyncio.run(constant_data_pull())

    app = TfLDisplayApp(data_dict)
    # run the TUI
    app.run()
