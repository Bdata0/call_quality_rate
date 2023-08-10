"""The module performs Exports data to Google Sheets."""

import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetsExporter:
    """
    Exports data to Google Sheets using the Google Sheets API.

    Args:
        credentials_path (str): Path to the Google Sheets API credentials JSON file.

    Attributes:
        client (gspread.Client): Google Sheets API client.

    Methods:
        export_to_sheets(data): Exports data to a Google Sheets worksheet.
    """

    def __init__(self, credentials_path):
        """
        Initialize the GoogleSheetsExporter with Google Sheets API credentials.

        Args:
            credentials_path (str): Path to the Google Sheets API credentials JSON file.
        """

    def _get_credentials(self):
        """
        Get the credentials required to access Google Sheets API.

        Returns:
            gspread.Client: An authorized client for Google Sheets API.
        """
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.credentials_path, scope)
        return gspread.authorize(credentials)

    def export_to_sheets(self, data):
        """
        Export data to a Google Sheets worksheet.

        Args:
            data (List[List]): List of lists representing data to be exported.
        """
        client = self._get_credentials()
        spreadsheet = client.open("Call Quality Rate")
        worksheet = spreadsheet.get_worksheet(0)
        for row in data:
            worksheet.insert_row(row)
