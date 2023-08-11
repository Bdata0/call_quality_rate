"""Module for testing the functionality of the GoogleSheetsExporter class."""

import unittest
from unittest.mock import Mock
from domain.google_sheets.google_sheets import GoogleSheetsExporter

class GoogleSheetsExportService:
    """
    A service class that abstracts the Google Sheets export functionality.

    This class provides a high-level interface for exporting data to Google Sheets
    using the GoogleSheetsExporter class.

    Attributes:
        None

    Methods:
        export_to_sheets(self, data): Export data to Google Sheets.

    """
    def __init__(self, credentials_path):
        self.exporter = GoogleSheetsExporter(credentials_path)

    def test_export_to_sheets(self):
        """
        Test the `export_to_sheets` method of the GoogleSheetsExportService class.

        This test method exports data to Google Sheets and then makes specific
        assertions to verify that the data is correctly exported.

        Args:
            self: The instance of the class.

        Returns:
            None
        """
        data = [[1, "Speaker A", "Transcript 1", 0.9],
                [2, "Speaker B", "Transcript 2", 0.6]]
        self.export_service.export_to_sheets(data)

        # TODO: Add assertions to verify data is correctly exported to Google Sheets


        # Mock the Google Sheets API to verify the export behavior
        mock_exporter = Mock(spec=GoogleSheetsExporter)
        self.export_service.exporter = mock_exporter

        # Assuming the exporter returns a successful export status
        mock_exporter.export_to_sheets.return_value = True

        # Perform the export
        exported = self.export_service.export_to_sheets(data)

        # Verify that the exporter was called with the correct data
        mock_exporter.export_to_sheets.assert_called_once_with(data)

        # Verify that the export was successful
        self.assertTrue(exported)

if __name__ == "__main__":
    unittest.main()
