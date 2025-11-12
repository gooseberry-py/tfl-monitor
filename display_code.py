import pandas as pd
import asyncio
from datetime import datetime
from project_data_gathering import constant_data_pull
from textual.app import App, ComposeResult
from textual.widgets import DataTable, Button, Static, Label
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive

# Textual app to display the three items from data_dict
class TfLDisplayApp(App):
    """Display three widgets with header and auto-refresh:
    - header: current time and exit button
    - left: DataTable for `next_tube_and_bus_df`
    - top-right: DataTable from `tube_line_status`
    - bottom-right: DataTable for `borris_bike_df`
    
    Data refreshes every 5 seconds.
    """

    CSS_PATH = "horizontal_layout.tcss"
    BINDINGS = [("q", "quit", "Quit")]
    
    # Reactive attribute to trigger data refresh
    current_time = reactive(str)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_dict = {}

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

    async def _refresh_data(self) -> None:
        """Refresh data every 5 seconds and update display."""
        while True:
            try:
                # Fetch fresh data
                self.data_dict = await constant_data_pull()
                
                # Update time
                self.current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Update DataTables
                await self._update_tables()
                
            except Exception as e:
                self.notify(f"Error refreshing data: {e}", severity="error")
            
            # Wait 5 seconds before next refresh
            await asyncio.sleep(5)

    async def _update_tables(self) -> None:
        """Update the DataTable widgets with new data."""
        try:
            # Update left table
            left_table = self.query_one("#next_tube_and_bus_df", DataTable)
            left_df = self.data_dict.get("next_tube_and_bus_df", pd.DataFrame())
            await self._refresh_datatable(left_table, left_df)
            
            # Update top-right table
            top_table = self.query_one("#status_df", DataTable)
            top_df = self.data_dict.get("tube_line_status", pd.DataFrame())
            await self._refresh_datatable(top_table, top_df)
            
            # Update bottom-right table
            bottom_table = self.query_one("#borris_bike_df", DataTable)
            bottom_df = self.data_dict.get("borris_bike_df", pd.DataFrame())
            await self._refresh_datatable(bottom_table, bottom_df)
            
        except Exception as e:
            pass  # Silently fail if tables not yet rendered

    async def _refresh_datatable(self, table: DataTable, df: pd.DataFrame) -> None:
        """Clear and repopulate a DataTable with new data."""
        try:
            # Clear existing data
            table.clear()
            
            # Add columns
            # for col in df.columns:
            #     table.add_column(str(col))
            
            # Add rows
            for _, row in df.iterrows():
                table.add_row(*[str(x) for x in row.tolist()])
        except Exception:
            pass  # Skip if data invalid

    def compose(self) -> ComposeResult:
        """Compose the layout with header, main content, and exit button."""
        # Create tables with IDs
        left_table = self._df_to_datatable(self.data_dict.get("next_tube_and_bus_df", pd.DataFrame()))
        left_table.id = "next_tube_and_bus_df"
        
        top_table = self._df_to_datatable(self.data_dict.get("tube_line_status", pd.DataFrame()))
        top_table.id = "status_df"
        
        bottom_table = self._df_to_datatable(self.data_dict.get("borris_bike_df", pd.DataFrame()))
        bottom_table.id = "borris_bike_df"
        
        # Header with time and exit button
        yield Vertical(
            Horizontal(
                Label("TfL Monitor      ", id="header_title"),
                Static(self.current_time, id="header_time"),
                Button("Exit", id="exit_btn", variant="error"),
                id="header"
            ),
            # Main content: left table + right container
            Horizontal(
                left_table,
                Vertical(
                    top_table,
                    bottom_table,
                    id="right_container"
                ),
                id="main_container"
            ),
            id="main_layout"
        )

    def on_mount(self) -> None:
        """Initialize the app and start data refresh task."""
        # Set initial time
        self.current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Start background data refresh task
        self.app.call_later(self._start_refresh)

    def _start_refresh(self) -> None:
        """Start the async data refresh task."""
        asyncio.create_task(self._refresh_data())

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "exit_btn":
            self.exit()

    def watch_current_time(self, new_time: str) -> None:
        """Update time display when current_time changes."""
        try:
            header_time = self.query_one("#header_time", Static)
            header_time.update(new_time)
        except Exception:
            pass  # Widget may not be mounted yet


if __name__ == "__main__":
    # Gather initial data and run the textual app
    initial_data = asyncio.run(constant_data_pull())

    app = TfLDisplayApp()
    app.data_dict = initial_data
    # run the TUI
    app.run()
